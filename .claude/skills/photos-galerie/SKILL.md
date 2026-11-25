---
name: photos-galerie
description: Ajouter des photos à la galerie du site ACNE (gallery.html), dans l'année existante ou dans une nouvelle année.
---

# Ajouter des photos à la galerie

1. `git pull`. Demande où sont les photos (un dossier du PC) et l'année.
2. Copie-les dans `img_originals/bg-img/annee_AAAA/` (crée le dossier si besoin),
   en gardant des noms sans espaces ni accents, puis
   `python outils/reduire-images.py`.
3. Dans `gallery.html` :
   - année déjà présente : ajoute un bloc `<div class="col-6 col-md-3 ftco-animate">`
     par photo au début de sa `row gallery`, en copiant un bloc existant
     (le chemin apparaît deux fois : `background-image` et `href`) ;
   - nouvelle année : ajoute une carte **en haut** de l'accordéon `#accordion`,
     titre « Année AAAA », identifiants jamais utilisés,
     `data-parent="#accordion"`, ouverte (`collapse show`) ; ferme l'ancienne
     première carte.
4. Vérifie dans l'aperçu que les vignettes s'affichent et que le clic ouvre
   la photo en grand, puis `/publier`.
