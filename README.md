# Boîte à outils d'intelligence artificielle

Lien vers le site du projet : https://baoia.huma-num.fr/

Des tutoriels détaillés sont disponibles sur le site ci-dessus.

L'ensemble du répertoire est divisé en dossiers relatifs aux corpus de sources étudiées. Chaque dossier contient les scripts notebooks directement utilisables.

## Les guides de voyage (Gallica)
### Téléchargement et récupération des données:
- BaOIA_gallica-text : télécharge les fichiers issus de Gallica en fichiers de texte brut.
- BaOIA_gallica_jpg : télécharge les fichiers issus de Gallica en format images.
- BaOIA_scrapper_gallica_IIIF: télécharge les images en format IIIF (utilisation pour la récupération des cartes)
- BaOIA_océrisation_tesseract: océrisation de fichiers images

### Étude de contenu
- BaOIA_reconnaisance_extraction_entites_nommees: outil de Reconnaissance automatique des entités nommées. 
- BAOIA_alignement_statistiques_personnages: outil d'alignement des données avec Wikidata de récupération des informations sur les personnages identifiés et des études statistiques.

### Visualisation
- BaOIA_cartographie-complete : outil de création automatique d'une carte avec tous les lieux référencés.
- BaOIA_cartographie_catégorisee: outil de création d'une carte intéractive de sélection avec tri des lieux par "types".
- BaOIA_cartographie_parcours: outil de création d'un parcours automatique sur une carte.
- BaOIA_cartographie_comparaison_parcours: outil de création de deux parcoure sur une carte intéractive.


## Les romans scolaires (Gallica)
### Téléchargement et récupération des données:
- BaOIA_table_des_matieres_gallica: téléchargement des tables des matières via API
- BaOIA_metadonnees_corpus : création d'un fichier regroupant toutes les métadonnées de tous les documents du corpus à partir des fichiers json créés lors du téléchargement
- BaOIA_api_geonames: recherche d'informations géographiques avec alignement sur l'API geonames

### Étude de contenu
- BaOIA_statistiques_entites_nommees: calculs statistiques des entités extraites
- BaOIA_liste_informations_wikidata: création d'une liste d'informations disponibles pour la récupération d'informations pour un alignement "personnalisé"
- BaOIA_concordance_entités_extraits: création d'un tableur excel pour vérifier la pertinence des entités dans l'extrait dont elles sont tirées

### Visualisation
- BaOIA_statistiques_graphiques_metadonnees: calculs statistiques et création de graphiques
- BaOIA_frise_chronologique: création d'une frise chronologique avec évènements ou métadonnées
- BaOIA_carte_chaleur_regions: création d'une carte de chaleur statistique par région française
- BaOIA_carte_chaleur_departements: création d'une carte de chaleur statistique par département


## Projet MonumenTAL
- BaOIA_alignement_artistes_monumenTAL: outil d'alignement des artistes repérés avec Wikidata et récupération des informations biographiques.
- BaOIA_api_base_joconde_MonumenTAL: outil d'alignement des données avec la base Joconde et de récupération des métadonnées.
- BaOIA_MonumenTAL_alignement_bases_de_donnees : téléchargement de bases de données par recherche (base Joconde, Gallica, Europeana), téléchargement des images correspondantes, création de cartographie des lieux de conservation (base joconde) et comparaison des bases de données.


## Les affiches (La Contemporaine)
### Téléchargement et récupération des données:
- BaOIA_layout_parsing_inference_affiches_Prima: script d'inférence de layout parsing (segmentation) avec le modèle Prima sur les affiches
- BaOIA_layout_parsing_inference_affiches_NPNavigato: script d'inférence de layout parsing (segmentation) avec le modèle Newspaper Navigator sur les affiches


## Presse illustrée et estampes satiriques
### Téléchargement et récupération des données:
- BaOIA_scrapper_heidelberg: téléchargement des documents issus de la bibliothèque numérique d'Heidelberg dans tous les formats disponibles (xml-alto, IIIF, texte brut océrisé, extraction des illustrations, jpg) 
