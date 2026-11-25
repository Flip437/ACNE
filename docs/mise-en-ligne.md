# Mise en ligne sur GitHub Pages (à faire une seule fois)

Le site est publié par GitHub Pages directement depuis la branche `main` :
pas de serveur FTP ni d'étape de construction. Chaque modification poussée sur
`main` est en ligne 1 à 2 minutes plus tard.

L'ordre conseillé : **transférer le dépôt → activer Pages → vérifier → brancher le domaine**.

## 1. Donner le dépôt à l'association

1. Créer un compte GitHub pour l'association, idéalement une **organisation**
   (gratuite) : https://github.com/organizations/plan → « Free ».
   Chaque bénévole qui modifiera le site y est invité avec son propre compte
   GitHub (on voit ainsi qui a fait quoi, et on peut retirer un accès).
2. Dans le dépôt actuel : *Settings → General → Danger Zone → Transfer ownership*,
   choisir l'organisation. GitHub redirige l'ancienne adresse vers la nouvelle.
3. Sur ton poste, mettre à jour l'adresse du dépôt :
   `git remote set-url origin git@github.com:<organisation>/ACNE.git`

Le dépôt doit rester **public** : GitHub Pages est gratuit pour les dépôts publics.
Rien de confidentiel n'y est stocké (les originaux des images restent hors du dépôt).

## 2. Activer GitHub Pages

*Settings → Pages* :
- **Source** : *Deploy from a branch*
- **Branch** : `main`, dossier `/ (root)` → *Save*

Après 1 à 2 minutes, le site est visible à
`https://<organisation>.github.io/ACNE/`. Vérifier en particulier :
- les pages dont le nom a un accent (Courts métrages, Adhésions) ;
- la galerie (ouverture des photos en grand) ;
- le PDF du programme sur l'accueil.

Le fichier `.nojekyll` à la racine indique à GitHub de publier les fichiers tels
quels (sans le moteur Jekyll) : il ne faut pas le supprimer.

## 3. Brancher le domaine acne-cine.com

Le domaine et l'adresse `contact@acne-cine.com` restent chez **OVH** : on ne
change que l'adresse vers laquelle pointe le site.

1. *Settings → Pages → Custom domain* : saisir `acne-cine.com` → *Save*.
   GitHub ajoute un fichier `CNAME` dans le dépôt (faire un `git pull` ensuite).
2. Dans l'espace client OVH, *Domaines → acne-cine.com → Zone DNS* :
   - remplacer les enregistrements **A** de `acne-cine.com` par ces quatre :
     `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - remplacer les enregistrements **AAAA** de `acne-cine.com` (s'il y en a) par :
     `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
   - `www` : un enregistrement **CNAME** vers `<organisation>.github.io.`
   - **ne pas toucher** aux enregistrements **MX**, SPF/TXT et autres liés aux e-mails.
3. Attendre la propagation (de quelques minutes à 24 h), puis cocher
   *Enforce HTTPS* dans *Settings → Pages* quand GitHub le propose.
4. Recommandé : *Settings (du compte ou de l'organisation) → Pages → Verified domains*
   pour vérifier le domaine, ce qui empêche quelqu'un d'autre de l'utiliser sur GitHub.

## 4. Après la bascule

- L'ancien hébergement OVH ne sert plus pour le site. **Avant de le résilier**,
  vérifier que la boîte `contact@acne-cine.com` n'en dépend pas (sur OVH, les
  e-mails sont souvent inclus dans l'offre d'hébergement).
- Les anciennes pages de films (`films/…html`) et les anciens PDF qui n'étaient
  que sur le serveur OVH ne seront plus accessibles. Ils n'étaient plus liés
  depuis le site, mais des liens externes ou Google peuvent encore y mener.
