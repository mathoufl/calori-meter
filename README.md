The goal if this project id to have a homemade calori tracker.
Here are the functionnality : 
	- Save ingredients calories
	- Save recipies and calculate the calcories of the recipe
	- Compute the calories intake over the day
	- Have a reporting module
	- Save the sport activities
	- Have a individual calori computation objective
	- Have a weigth tracker
	- Have a recipe prevision calendar 
	- Automatic shopping planning
	- Have a cooking session requiered 

Events : 
- J’entre un ingredient
    - Je peux entrer un ingerdient et ses col/kg
- Je veux verifier un ingrédient dans la liste
- Je veux entrer une nouvelle recette
    - Entrer les ingredients
    - Entrer le protocole
- Je realise une recette : je rentre les quantité réel de chaque ingredients utilisées
- Je fais une séance de sport : 
    - Je rentre quel sport fait et mes perf
    - Ça calcule mes calories dépensés
- Je fais un sport pour la premiere fois :
    - Je met les indicateur de performance
    - Je rentre les formules calculant combien de calories ont été dépensées
- Je me pese / prend des mesures sur moi / update mon profil
    - Je peux les rentrer et les données seront pris en compte 
- Je fais mon planning de repas de la semaine : 
    - Je peux rentrer les recette prévue aux bonnes date
    - Je peux sélectionner une plage de jours et demander les ingredients dont j’ai besoin
    - Je peux l’exporter dans mon presse-papier
- Je veux valider ma consommation effective de ma journée :
    - J’ai un écran qui me demande de confirmer mon sport fait
- Je veux consulter mon Dashboard 
    - Les donnée voulues s’afficent
- Je me met a cuisiner / je veux m’assurer que j’ai tout dans mon frigo : 
    - Je peux sélectionner les recette que je vais/veux réaliser et la liste des ingredient nécessaire 

Fonctionalités : (à completer)
- Entrer des ingredient et leurs cal/kg
- Entrer des recette (ingrédients + prépa)
- Calculer les cal d’une recette

Stack :
- J’ai choisi une stack en micro services avec une frontend monolithique modulaire. Et avec une couche de graphQL pour la communication entre mon front et mes services. Voici mes services
    - Workout service
    - User / health service
    - Food service
- Pour chacun de mes service je vais créer un docker avec un serveur et une bdd et un serveur
- Le but est que mes services vérifient les principes solid ainsi que des bonne pratiques de développement dans un context : event-driven, test-driven… etc
- Je voudrais travailler plusieurs technos, voici celles retenues :
    - Workout : Java + nosql
    - Food : python + bddr
    - User : GO + nosql
    - Front : react + tailwind + vite
- Chaque service tourne sur une instance de docker séparée mais toutes présente sur un meme network.

Idée : essayer de faire generer les visuels ne pixel art par IA