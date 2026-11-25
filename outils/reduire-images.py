"""Prépare les images du site : réduit les originaux pour le web.

- img_originals/  : images en taille originale (non versionnées, restent sur le PC)
- img/            : copies réduites utilisées par le site (versionnées et publiées)

Le script parcourt img_originals/ et écrit dans img/ (même chemin relatif) une
version réduite de chaque image nouvelle ou modifiée :
  - photos de la galerie (img/bg-img/annee_XXXX/) : 1600 px maximum
  - toutes les autres images (affiches...)       : 1200 px maximum
  - JPEG qualité 80 ; l'orientation des photos de téléphone est corrigée.
Une image déjà assez petite est copiée telle quelle.

Utilisation (depuis le dossier du site) :
    python outils/reduire-images.py
Prérequis : Pillow  ->  python -m pip install pillow
"""
import shutil
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow manque. Installez-le avec :  python -m pip install pillow")

SITE = Path(__file__).resolve().parent.parent
ORIG = SITE / "img_originals"
WEB = SITE / "img"
RESIZABLE = {".jpg", ".jpeg", ".png"}


def limit_for(rel: Path) -> int:
    return 1600 if any(part.startswith("annee_") for part in rel.parts) else 1200


def is_up_to_date(orig: Path, dest: Path) -> bool:
    return dest.exists() and dest.stat().st_mtime >= orig.stat().st_mtime


def reduce(orig: Path, dest: Path, limit: int) -> bool:
    """Écrit la version réduite ; renvoie False si l'original est déjà assez petit."""
    with Image.open(orig) as im:
        im = ImageOps.exif_transpose(im)
        if max(im.size) <= limit:
            return False
        im.thumbnail((limit, limit), Image.LANCZOS)
        if orig.suffix.lower() in {".jpg", ".jpeg"}:
            im.convert("RGB").save(dest, quality=80, optimize=True, progressive=True)
        else:
            im.save(dest, optimize=True)
    return True


if not ORIG.exists():
    sys.exit(f"Dossier introuvable : {ORIG}")

resized = copied = skipped = 0
for orig in sorted(p for p in ORIG.rglob("*") if p.is_file() and not p.name.startswith(".")):
    rel = orig.relative_to(ORIG)
    dest = WEB / rel
    if is_up_to_date(orig, dest):
        skipped += 1
        continue
    dest.parent.mkdir(parents=True, exist_ok=True)
    done = orig.suffix.lower() in RESIZABLE and reduce(orig, dest, limit_for(rel))
    if done and dest.stat().st_size < orig.stat().st_size:
        resized += 1
        print(f"réduite : img/{rel.as_posix()}  ({orig.stat().st_size // 1024} Ko -> {dest.stat().st_size // 1024} Ko)")
    else:
        shutil.copy2(orig, dest)  # déjà petite, ou la réduction serait plus lourde
        copied += 1
        print(f"copiée  : img/{rel.as_posix()}")

print(f"\n{resized} réduite(s), {copied} copiée(s), {skipped} déjà à jour.")
