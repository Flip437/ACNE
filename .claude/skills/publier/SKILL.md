---
name: publier
description: Mettre en ligne les modifications du site ACNE (aperçu, validation, enregistrement et publication sur GitHub Pages). À utiliser quand la personne veut publier, mettre en ligne ou « envoyer » ses changements.
---

# Publier le site

1. `git status` et `git diff --stat` : liste en mots simples ce qui a changé
   (« la page Programmation : 2 films ajoutés », « 12 photos dans la galerie 2026 »).
   Rien n'a changé → dis-le et arrête-toi.
2. Si des images ont été ajoutées dans `img_originals/`, lance
   `python outils/reduire-images.py` et vérifie qu'aucune image de `img/` modifiée
   ne dépasse ~1 Mo (`git diff --cached --stat` après `git add`).
3. Lance l'aperçu (configuration `site-acne` de `.claude/launch.json`), ouvre
   chaque page modifiée, vérifie : pas d'image cassée, pas d'erreur console,
   accordéons qui s'ouvrent. Montre l'aperçu à la personne.
4. Demande : « Je mets ces modifications en ligne ? » et attends un oui clair.
5. `git add -A`, `git commit -m "<description en français>"`, `git pull --rebase`,
   `git push` (sur `main`, jamais de branche).
6. Annonce que le site public sera à jour dans 1 à 2 minutes. Si possible,
   vérifie ensuite la page en ligne et confirme.

En cas d'erreur de connexion à GitHub, explique simplement le problème et
renvoie vers `docs/guide-benevoles.md` (section « Connexion à GitHub »).
