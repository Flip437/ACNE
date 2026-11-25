# Mettre à jour le site de l'ACNE avec Claude

Vous n'avez pas besoin de savoir programmer : vous dites à Claude ce que vous
voulez changer, il modifie le site, vous montre le résultat, et le met en ligne
quand vous êtes d'accord.

## Installation (une seule fois par ordinateur)

À faire de préférence avec quelqu'un qui l'a déjà fait. Compter 20 minutes.

1. **Compte GitHub** : créez un compte gratuit sur https://github.com, puis
   demandez à un responsable de l'association de vous inviter dans
   l'organisation de l'ACNE. Acceptez l'invitation reçue par e-mail.
2. **Git pour Windows** : téléchargez et installez https://git-scm.com/download/win
   (laissez toutes les options par défaut).
3. **Python** : téléchargez et installez https://www.python.org/downloads/ .
   Sur le premier écran de l'installation, **cochez « Add python.exe to PATH »**.
4. **Claude** : installez l'application Claude pour Windows
   (https://claude.ai/download) et connectez-vous avec le compte de
   l'association. L'onglet **Code** nécessite un abonnement payant.
5. **Récupérer le site** :
   - créez un dossier vide, par exemple `Documents\site-acne` ;
   - dans Claude, onglet **Code**, ouvrez ce dossier ;
   - écrivez : *« Récupère le site de l'ACNE depuis
     https://github.com/<organisation>/ACNE dans ce dossier, installe Pillow et
     configure git avec mon nom et mon e-mail. »*
6. La première mise en ligne ouvrira une fenêtre de connexion GitHub dans le
   navigateur : connectez-vous avec votre compte GitHub et autorisez l'accès.
   Ensuite, Windows s'en souvient.

## Utilisation au quotidien

Ouvrez Claude, onglet **Code**, dans le dossier `site-acne`, et demandez
simplement ce que vous voulez. Exemples :

- *« Ajoute la séance de la semaine du 5 novembre : … »* (vous pouvez aussi
  glisser le PDF du programme ou les affiches dans la conversation)
- *« On passe à la 2e programmation 2026-2027, voici le PDF. »*
- *« Ajoute les photos du dossier Images\Soirée rentrée à la galerie 2026. »*
- *« Mets une actualité : soirée ciné-philo le 12 décembre à 19h à La Maison. »*
- *« Retire l'actualité sur la rentrée. »*
- *« Le numéro de téléphone a changé sur la page contact : … »*

Raccourcis disponibles en tapant `/` : `/nouvelle-seance`,
`/nouvelle-programmation`, `/photos-galerie`, `/actualite`, `/publier`.

Claude vous montre un **aperçu** avant de publier. Rien n'est mis en ligne sans
votre accord. Une fois publié, le site est à jour en 1 à 2 minutes.

## Si quelque chose ne va pas

- **Une erreur a été mise en ligne** : dites *« Annule la dernière modification
  du site »*. Toutes les versions précédentes sont conservées : on peut toujours
  revenir en arrière.
- **Deux personnes ont modifié le site en même temps** : Claude récupère
  toujours la dernière version avant de travailler et combine les changements.
- **Claude demande une autorisation** pour lancer une commande : c'est normal,
  il s'agit de ses outils (récupérer la dernière version, réduire les images,
  publier). En cas de doute, demandez-lui ce que fait la commande.

### Connexion à GitHub

Si la mise en ligne échoue avec un message parlant d'authentification ou de
permission (« denied », « 403 ») :
- vérifiez que vous avez bien accepté l'invitation dans l'organisation ACNE sur GitHub ;
- demandez à Claude : *« Reconnecte-moi à GitHub »* (il relancera la fenêtre de connexion).
