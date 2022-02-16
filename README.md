# Ensemble de scripts réalisés au sein du projet BaOIA

Lien vers le site du projet : https://baoia.huma-num.fr/ où des tutoriels détaillés sont disponibles pour certains scripts.


## Structure du dépôt

Le dépôt est divisé en dossiers relatifs aux corpus de sources étudiées. Chaque dossier contient les scripts notebooks utilisables à travers Google Colab. Une aide technique sur le site du projet permet la prise en main des outils (cf [aide technique](https://baoia.huma-num.fr/aide-technique/)).

### Les guides de voyage (Gallica)
#### Téléchargement et récupération des données
- ```BaOIA_gallica_txt.ipynb``` : télécharge les fichiers issus de Gallica en fichiers de texte brut.
- ```BaOIA_gallica_jpg.ipynb``` : télécharge les fichiers issus de Gallica en format image.
- ```BaOIA_scraper_gallica_iiif.ipynb``` : télécharge les images en format IIIF (utilisation pour la récupération des cartes).
- ```BaOIA_ocerisation_tesseract.ipynb``` : océrisation de fichiers images

#### Étude de contenu
- ```BaOIA_reconnaisance_extraction_entites.ipynb``` : outil de Reconnaissance automatique des entités nommées. 
- ```BAOIA_alignement_statistiques_personnages.ipynb``` : outil d'alignement des données avec Wikidata de récupération des informations sur les personnages identifiés et des études statistiques.

#### Visualisation
- ```BaOIA_cartographie-complete.ipynb``` : outil de création automatique d'une carte avec tous les lieux référencés.
- ```BaOIA_cartographie_categorisee.ipynb``` : outil de création d'une carte intéractive de sélection avec tri des lieux par "types".
- ```BaOIA_cartographie_parcours.ipynb``` : outil de création d'un parcours automatique sur une carte.
- ```BaOIA_cartographie_comparaison_parcours.ipynb``` : outil de création de deux parcoure sur une carte intéractive.

### Projet MonumenTAL
- ```BaOIA_alignement_artistes_monumenTAL.ipynb``` : outil d'alignement des artistes repérés avec Wikidata et récupération des informations biographiques.
- ```BaOIA_API_bases_de_donnees.ipynb``` : outil d'alignement des données avec la base Joconde et de récupération des métadonnées, téléchargement des images correspondantes, création de cartographie des lieux de conservation (base joconde) et comparaison des bases de données.

### Presse illustrée et estampes satiriques
- ```BaOIA_scraper_heidelberg.ipynb``` : téléchargement des documents issus de la bibliothèque numérique d'Heidelberg dans tous les formats disponibles (xml-alto, IIIF, texte brut océrisé, extraction des illustrations, jpg).
