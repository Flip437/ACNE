---
name: nouvelle-seance
description: Ajouter une ou plusieurs séances (films de la semaine) à la programmation en cours du site ACNE, avec leurs affiches et les courts métrages associés.
---

# Ajouter une séance

1. `git pull`.
2. Rassemble les informations, en les demandant si elles manquent :
   - les dates de la semaine (ex. « Jeudi 5, dimanche 8, lundi 9 et mardi 10 novembre ») ;
   - pour chaque long métrage : titre, réalisateur·rice, horaires
     (format `Jeu 13h30, Dim 19h45, Lun 13h30, Mar 19h45`), ligne
     `(Pays - année - durée avec Acteurs)`, affiche ;
   - le court métrage de la semaine s'il y en a un : titre, réalisateur·rice,
     `Pays – Genre – année – durée`, résumé, image.
   Les infos peuvent venir d'un PDF ou d'un document fourni : lis-le et
   récapitule ce que tu as compris avant d'écrire.
3. Affiches : copie-les dans `img_originals/bg-img/films/` avec un nom en
   minuscules sans accents ni espaces, puis `python outils/reduire-images.py`.
4. Dans `programmation_en_cours.html`, ajoute un bloc
   `<div class="single-post-area style-2">` **en haut de la liste** (juste après
   le titre « Programme »), en copiant un bloc existant. `mb-30` sur chaque
   film sauf le dernier du bloc.
5. Court métrage : même chose dans la **première carte** de l'accordéon de
   `programmation_courts_métrages.html` (en haut).
6. Termine avec la commande `/publier`.
