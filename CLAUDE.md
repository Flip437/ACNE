# Site de l'ACNE (Association des cinéphages de Nevers)

Site vitrine statique : HTML + CSS (compilé depuis SCSS) + jQuery, sur le modèle
« Vizew » de Colorlib. Aucun outil de build : les fichiers du dépôt sont publiés
tels quels par **GitHub Pages** à chaque push sur `main`.

## À qui tu parles

Les personnes qui t'utilisent ici sont des **bénévoles de l'association, pas des
développeurs**, sur un **PC Windows**. Donc :

- Parle en français simple, sans jargon (pas de « commit », « push », « HTML »
  sauf si on te le demande). Dis plutôt « j'enregistre la modification »,
  « je mets le site en ligne ».
- Ne leur demande jamais de taper une commande ni d'utiliser git : tu t'en charges.
- Ils peuvent aussi avoir modifié des fichiers à la main avant de te parler :
  regarde `git status` / `git diff` et intègre ces changements.
- S'il manque une information (horaires, réalisateur, affiche…), demande-la
  plutôt que d'inventer. N'invente jamais de contenu.
- Commandes Windows : `python` (pas `python3`), chemins avec `\` possibles.

## Déroulé de chaque demande

1. **Mettre à jour la copie locale** avant toute modification : `git pull`.
   S'il y a des modifications locales non enregistrées, ne les écrase pas :
   montre-les à la personne et demande si on les garde.
2. **Faire la modification** (voir les recettes ci-dessous).
3. **Montrer un aperçu** : lance le serveur local (`.claude/launch.json`,
   configuration `site-acne` sur PC, `site-acne-mac` sur Mac, http://localhost:8080) et ouvre la page modifiée
   dans le navigateur intégré. Vérifie toi-même l'affichage avant de le montrer.
4. **Demander la validation** de la personne.
5. **Mettre en ligne**, seulement après son accord :
   `git add -A`, `git commit` avec un message en français qui décrit le
   changement (ex. « Ajout de la séance du 12 novembre »), puis `git push`.
   - Toujours directement sur `main` : **jamais de branche ni de pull request**.
   - Le site public est à jour 1 à 2 minutes après. Dis-le à la personne.
6. Si `git push` est refusé parce que quelqu'un d'autre a publié entre-temps :
   `git pull --rebase`, vérifie que rien n'a été perdu, puis `git push`.

**Annuler une modification déjà en ligne** : `git revert <commit>` puis `git push`
(ne jamais réécrire l'historique : pas de `reset --hard`, pas de `push --force`).
`git log --oneline` permet de retrouver la modification à annuler.

## Les pages

| Fichier | Contenu |
|---|---|
| `index.html` | Accueil : texte de bienvenue + **Actualités** (annonces, PDF du programme, évènements avec bande-annonce YouTube) |
| `programmation_en_cours.html` | Programmation en cours : séances de longs métrages, **la plus récente en haut** |
| `programmation_courts_métrages.html` | Courts métrages diffusés avant les films, en accordéon par programmation |
| `programmation_passee.html` | Archives des programmations passées, en accordéon (la plus récente en haut, ouverte) |
| `gallery.html` | Galerie photo, un accordéon par année |
| `lien.html` | Partenaires et liens |
| `contact.html` | Contact |
| `nous_situer.html` | Lieux / informations pratiques |
| `pour_adhérer.html` | Tarifs et adhésion |
| `festival_diversité.html`, `films/*.html` | Anciennes pages, peu modifiées |

Attention aux **noms de fichiers avec accents** (`programmation_courts_métrages.html`,
`pour_adhérer.html`, `festival_diversité.html`) : ne pas les renommer, les liens en dépendent.

**Menu et pied de page** sont recopiés dans chaque page (pas d'inclusion).
Pour les changer, modifie **toutes** les pages `*.html` et `films/*.html`,
puis vérifie avec une recherche que plus aucune page n'a l'ancienne version.

## Recettes

Avant d'écrire du HTML, **copie un bloc existant de la même page** et adapte-le :
c'est le plus sûr pour garder la mise en page. Les commandes `/nouvelle-seance`,
`/nouvelle-programmation`, `/photos-galerie`, `/actualite` et `/publier`
détaillent les cas courants.

### Une séance (programmation en cours)

Un bloc `<div class="single-post-area style-2">` par semaine de séances :
un `<h4>` avec les dates, puis une `row` par film. Toutes les `row` de films
ont `mb-30` **sauf la dernière** du bloc.

```html
<div class="row align-items-center mb-30">
  <div class="col-12 col-md-4">
    <div class="post-thumbnail">
      <img src="img/bg-img/films/nom_du_film.jpg" alt="« TITRE DU FILM »" style="width:70%" loading="lazy">
    </div>
  </div>
  <div class="col-12 col-md-8">
    <div class="post-content mt-0">
      <a class="post-cata cata-sm cata-danger text-white">Long métrage</a>
      <a class="post-title mb-2">« TITRE DU FILM »</a>
      <div class="post-meta d-flex align-items-center flex-wrap mb-2">
        <a class="post-author">Réalisateur</a>
        <i class="fa fa-circle" aria-hidden="true"></i>
        <a class="post-date">Jeu 13h30, Dim 19h45, Lun 13h30, Mar 19h45</a>
      </div>
      <p class="mb-2">(Pays - année - durée avec Acteur 1, Acteur 2)</p>
    </div>
  </div>
</div>
```

Conventions : titres de longs métrages en MAJUSCULES entre « » ; titres de
courts métrages en casse normale sans guillemets, catégorie `Court métrage`,
une ligne `Pays – Genre – année – durée` puis un résumé en `<p class="mb-2">`.

### Accordéons (courts métrages, programmations passées, galerie)

Structure Bootstrap 4 « collapse » dans un `<div class="w-100 acne-accordion" id="...">`.
Chaque carte a un `id` de titre et de contenu uniques (`passee-heading-N` /
`passee-collapse-N`, `courts-…`, `accordion-…` pour la galerie). Pour ajouter
une carte en haut : prends un identifiant jamais utilisé (pas besoin de
renuméroter), donne-lui `collapse show` + `aria-expanded="true"` et retire-les
de l'ancienne première carte (son bouton reprend la classe `collapsed`).
La galerie utilise en plus `data-parent="#accordion"` sur chaque contenu.

### Images

- Ne mets jamais une photo brute dans `img/` : les photos de téléphone font
  plusieurs Mo et rendraient le site lent.
- Copie l'original dans `img_originals/` au **même chemin** que l'image du site
  (affiches : `img_originals/bg-img/films/`, photos : `img_originals/bg-img/annee_AAAA/`),
  puis lance `python outils/reduire-images.py`, qui écrit la version réduite dans `img/`.
  Si Pillow manque : `python -m pip install pillow`.
- Noms de fichiers : minuscules, sans espaces ni accents (`les_roches_rouges.jpg`).
- `img_originals/` n'est pas versionné (`.gitignore`) : il reste sur le PC.

### Documents PDF (programmes à télécharger)

Dans `programmes/`, nom sans espaces ni accents
(ex. `programmes/ACNE_2e_programme_2026_2027.pdf`), lien relatif depuis la page :
`href="programmes/…pdf" target="_blank"`.

### Style (CSS)

Ne modifie pas `style.css` à la main : il est généré. Les personnalisations de
l'ACNE sont dans `scss/personnal.scss`. Après modification, recompile :
`npx sass@1.83.4 --quiet scss/style.scss style.css` (nécessite Node.js ; s'il
n'est pas installé, propose de l'installer avec https://nodejs.org, version LTS).

## À ne pas toucher

- `css/`, `js/`, `fonts/`, `gallery_css/`, `gallery_js/` : bibliothèques du modèle.
- `source_files/` : pages de démonstration du modèle, non liées au site.
- Le lien « Colorlib » du pied de page : la licence du modèle (CC BY 3.0) l'impose.
- `CNAME` (domaine du site) et `.nojekyll` (nécessaire à GitHub Pages).

## Vérifications avant publication

- La page s'affiche dans l'aperçu, sans image cassée ni erreur dans la console.
- Les liens ajoutés pointent vers des fichiers qui existent (attention aux accents).
- Le HTML est bien fermé (accordéons : chaque `<div>` ouvert est refermé).
- `git status` ne contient que les fichiers attendus.
