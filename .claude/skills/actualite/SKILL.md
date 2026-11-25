---
name: actualite
description: Ajouter, modifier ou retirer une actualité ou un évènement sur la page d'accueil du site ACNE (annonce, soirée, débat, ciné-philo, bande-annonce YouTube).
---

# Actualités de l'accueil

Les actualités sont dans `index.html`, sous le titre « Actualités », les plus
récentes en haut. Deux formats, à copier depuis un bloc existant :

- **Annonce courte** : `<div class="single-widget share-post-widget news-widget mb-50">`
  avec un `<p>` et éventuellement un bouton
  `<a href="..." target="_blank">Cliquer ici</a>`.
- **Évènement** (film + débat…) : bloc `single-post-area style-2` avec une
  bande-annonce YouTube à gauche (`https://www.youtube.com/embed/<identifiant>`)
  et à droite catégorie « Évènement », titre, réalisateur·rice, date/heure/lieu
  et une ligne de description. Pour l'identifiant YouTube : c'est la partie
  après `v=` ou `youtu.be/` du lien fourni.

1. `git pull`, puis demande le texte, la date, le lieu et le lien de la
   bande-annonce si c'est un évènement.
2. Propose de retirer les actualités dont la date est passée.
3. Aperçu, puis `/publier`.
