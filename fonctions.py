#-*-coding:Utf-8-*
#!/usr/bin/python3.7

""" Fichier secondant <classhug.py> et contient toutes les fonctions
utiles au bon fonctionnement de celui-ci """

# On importe les modules;
import pickle
import os
import tkinter

def enregistrer(objet):
	''' Fonction qui permet d'enregistrer des objets '''

	with open('fichiers/elements_graphiques.txt', 'wb') as fichier:
		pickler = pickle.Pickler(fichier)
		pickler.dump(objet)


def recuperer(element, liste=None):
	''' Fonction permettant de récupérer un objet '''

	if os.path.exists(element):
		with open(element, 'rb') as fichier:
			unpickler = pickle.Unpickler(fichier)
			objet = unpickler.load()
			return objet
	else:
		dictionnaire = dict()
		return dictionnaire

def wait(widget, temps_restant):
	''' Fonction permettant d'afficher les noms au fur et à mesure '''

	widget.after(1000, temps_restant)

def lire_noms():
	''' Fonction permettant de lire les noms des classes. '''

	classes = list()
	classes_dico = dict()

	for nom in os.listdir('fichiers'):
		if nom.endswith('.txt'):
			nom_fichier = nom[:-4].capitalize()
			classes.append(nom_fichier)
			classes_dico[nom_fichier] = os.path.join('fichiers', nom)
		else:
			for noms in os.listdir(nom):
				if nom.endswith('.txt'):
					nom_fichier = nom[:-4].capitalize()
					classes.append(nom_fichier)
					classes_dico[nom_fichier] = os.path.join('fichiers', nom)
		return classes, classes_dico

def enregistrer_tirages(dictionnaire):
	''' Fonction permettant d'affirmer ou de réfuter la présence de la loi binomiale
	pour des tirages aléatoires '''

	# On enregistre le dictionnaire;
	with open("variables/dictionnaire.txt", 'wb') as fichier:
		pickler = pickle.Pickler(fichier)
		pickler.dump(dictionnaire)	

	# On enregistre le compteur;
	if os.path.exists('variables/compteur.txt'):
		counter = recuperer("variables/compteur.txt")
		counter += 1
	else:
		counter = 1
	with open("variables/compteur.txt", 'wb') as fichier:
		pickler = pickle.Pickler(fichier)
		pickler.dump(counter)

def verify():
	''' Fonction permettant de vérifier combien de fois un nom à été associé à
	un autre '''

	dictionnaire = recuperer('variables/dictionnaire.txt')
	counter = recuperer('variables/compteur.txt')

	for i,clé in dictionnaire.keys():
		i = len(dictionnaire[clé])
		print('{} -- {} -- {}'.format(clé, i, counter))