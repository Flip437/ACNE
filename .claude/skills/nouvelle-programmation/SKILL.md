---
name: nouvelle-programmation
description: Passer à une nouvelle programmation du site ACNE (ex. « 2e programmation 2026-2027 ») - archiver la programmation en cours dans les archives et repartir d'une page vide, avec le nouveau PDF du programme.
---

# Nouvelle programmation

1. `git pull`. Demande le nom exact de la nouvelle programmation
   (ex. « 2e programmation 2026 - 2027 ») et le PDF du programme s'il existe.
2. **Archiver l'actuelle** dans `programmation_passee.html` : ajoute une carte
   **en haut** de l'accordéon `#passee`, avec pour titre le nom de la
   programmation qui se termine (celui du `post-title` de
   `programmation_en_cours.html`) et pour contenu tous ses blocs
   `single-post-area`. Nouvelle carte ouverte (`collapse show`,
   `aria-expanded="true"`), l'ancienne première carte fermée (`collapse`,
   bouton `collapsed`, `aria-expanded="false"`). Identifiants jamais utilisés.
3. **Vider la programmation en cours** : change le titre (`post-title`) et
   supprime les anciens blocs de séances. Ajoute les nouvelles séances si on
   te les donne (voir `/nouvelle-seance`).
4. **Courts métrages** : dans `programmation_courts_métrages.html`, ajoute une
   nouvelle carte en haut de l'accordéon `#courts` pour la nouvelle
   programmation (même règle d'ouverture/fermeture).
5. **PDF** : copie-le dans `programmes/` (nom sans espaces ni accents) et mets à
   jour le lien « Retrouvez la … programmation en version téléchargeable » dans
   les actualités de `index.html`.
6. Vérifie avec l'aperçu que les accordéons s'ouvrent et se ferment, puis `/publier`.
