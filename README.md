### ---------------------------------------------------------------------------------- ###
##       CAHIER DES CHARGES DU PROGRAMME HUGSBOX -- HUGSBOX MELANGEUR DE BINOMES        ##
##                 by T0my  (02 oct. 2019)                                              ##
### ---------------------------------------------------------------------------------- ###

		 _   _                 ____            
		| | | |_   _  __ _ ___| __ )  _____  __
		| |_| | | | |/ _` / __|  _ \ / _ \ \/ /
		|  _  | |_| | (_| \__ \ |_) | (_) >  < 
		|_| |_|\__,_|\__, |___/____/ \___/_/\_\
			     |___/                     

Phase de tests : le fichier à éxécuter est classhugs.py ;

	1 ) PRESENTATION

Le programme HugsBox est un exécutable python multi-platformes permettant de former des binômes
en fonctions de leur résultats pour les aider à trouver un partenaire de TP idéal.

Au début, le programme forme des groupe de manière aléatoire et enregistre des statistiques
sur la capacité des élèves à raisonner ensemble, à s'entendre mais aussi en fonction de leur
rigueur scientifique et de leur goût pour la matière. En fonction des résultats recceuillis,
il sera en mesure de former des binômes qui ont une performance optimale.

Bien que ce programme ne soit qu'un gadget, il bénéficiera de nombreuses fonctionnalités
statistiques.


	2 ) FONCTIONALITES PRINCIPALES

Le programme HugsBox se doit d'anticiper les besoins de l'enseignant en matière de pédagogie.
Pour répondre à ces besoins, le programme doit avoir :
	- un lieu de receuil statistique sur les groupes expérimentés;
	- un bouton de tirage rapide et simple à lancer. Les binômes choisis doivent être crédibles;
	- un code source portable et multi-platformes;
	- une interface graphique simple et intuitive.

Les fonctionalités associées à la HugsBox sont donc :
	- tirage aléatoire et unique (personne ne doit retomber avec le même partenaire);

	- après exécution et saisie d'informations diverses (notes, difficultée du TP, capacité
	  d'entente,..), le programme doit fournir des stats sur la probabilité qu'un individu soit
	  associé à un autre, sur les groupes déja passés, sur la note du TP et les affinités;

	- enfin, il peut également se comporter de manière bête et stupide en effectuant des tirages
	  très proches de l'aléatoire mais toujours uniques (car rien n'est réellement aléatoire en
	  informatique).


	4 ) CREATION DE CLASSES

Pour créer un classe, il suffit de créer un fichier texte dans le dossier classes/ avec les noms des
élèves à l'intérieur. Les statistiques seront déposées dans le même répertoire que ce fichier. Il est
tout à fait viable de vouloir organiser ces classes en créant des répertoires portant le nom de la classe
concernée, et d'y déposer le fichier .txt en question. Le nom du répertoire comme celui du fichier .txt ne
doit pas comporter d'espaces.


	5) EN CAS DE BUGS..

En cas de plantage répétés du programme, supprimer tout les fichier de configuration se trouvant dans variables/
et ré-exécutez le programme. Attention : cette action supprimera toutes les statistiques déjà générées !
Ces gestes sont des connaissances utiles en cas de problèmes mais en aucun cas une habitude à prendre et
n'entachent en rien la crédibilité du programme fourni.
