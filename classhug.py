#-*-coding:Utf-8-*
#!/usr/bin/python3.7

""" Fichier classes de notre programme. Il définie la classe <Graphique>, <Alea> et <ZeroDay> """
""" Méthodes à créer :
		- verify(self)		vérifie si les binômes sont réellement uniques

"""


# importation des modules;
import tkinter.font as tkFont
from fonctions import *
from random import choice
from tkinter import *
import time
import pickle
import os

class Alea():
	""" Classe permettant de faire des tirages aléatoires, des relevés statistiques et autre. """

	def __init__(self, fichier_classe):
		''' Constructeur de notre classe '''

		# récupération des noms;
		with open(fichier_classe, 'r') as fichier:
			classe = fichier.read()

		liste = list()
		mot = list()
		for elem in classe:
			if elem != '\n':
				mot.append(elem)
			else:
				liste.append(str(''.join(mot)))
				mot = list()

		self.classe = list(liste)
		self.interface = None
		self.relancer = 0


	def tirage(self):
		''' méthode <tirage> permettant de faire un tirage aléatoire simple d'une liste de noms '''

		# fonction gérant le tirage aléatoire;
		restes = list(self.classe)
		passes = recuperer('variables/dictionnaire.txt')
		i = 0 # <i> représente le numéro du groupe (Cf dictionnaire passes);

		while restes:
			if len(restes) == 1:
#				 print(restes[0])
				passes[i] = [restes[0]]
				restes.remove(restes[0])
				break
			else:
				mot1 = str(choice(restes))
				restes.remove(mot1)
				mot2 = str(choice(restes))
				restes.remove(mot2)

			passes[i] = [mot1, mot2]
			i += 1

		self.groupes = dict(passes)
		enregistrer_tirages(passes)


	def afficher_base(self):
		''' méthode permettant d'afficher le menu '''

		# On lance un tirage;
		self.tirage()

		# On nettoye l'écran;
		if self.interface != None:
			for elem in self.graphique:
				elem.destroy()

		# On définie les variables;
		# <graphique> permet de stocker les objets affichés à l'écran pour pouvoir les supprimer
		# plus facilement ensuite;
		graphique = list()
		
		# On crée notre objet Tk().. ;
		print(self.interface)
		if self.interface != None:
			interface = self.interface
			pass
		else:
			interface = Tk()
			interface.title('HugsBox 1.0')
			interface.minsize(height=350, width=500)
			self.interface = interface

		# On rajoute une barre de menus;
		def alert():
			message = Tk()
			Label(message, text="Oops !\nCette fonctionnalité n'a pas encore été crée ! Revenez plus tard ;)").pack()
			message.title("Oops !!")
			Button(message, text="Ok !", command=message.destroy).pack(side=BOTTOM)
			message.mainloop()

		menubar = Menu(interface)

		menu1 = Menu(menubar, tearoff=0)
		menu1.add_command(label="Importer..", command=alert)
		menu1.add_command(label="Editer..", command=alert)
		menu1.add_separator()
		menu1.add_command(label='Retour au Menu', command=self.afficher_base)
		menu1.add_command(label="Quitter", command=interface.quit)
		menubar.add_cascade(label="Fichier", menu=menu1)

		menu2 = Menu(menubar, tearoff=0)
		menu2.add_command(label="Copier comme PDF..", command=alert)
		menu2.add_command(label="Ecrire un mot..", command=alert)
		menubar.add_cascade(label="Edition", menu=menu2)

		menu3 = Menu(menubar, tearoff=0)
		menu3.add_command(label="Documentation", command=self.documentation)
		menu3.add_command(label="A propos", command=alert)
		menubar.add_cascade(label="Aide", menu=menu3)

		interface.config(menu=menubar)

		# On affiche une image;
#		image = PhotoImage(file='fichiers/plume-mini.gif')
#		canvas = Canvas(interface)
#		graphique.append(canvas)
#		canvas.pack()
#		canvas.create_image(-5, 0, image=image)

		# On affiche un bouton <lancer tirage>:
		_tirage_simple = Button(interface, text='Lancer le tirage', command=self.afficher_tirage)
		graphique.append(_tirage_simple)
		_tirage_simple.pack(side=BOTTOM, expand=True)

		_message = Label(interface, text="Avec quelle classe\ntravaillons-nous aujourd'hui ?\n\n\n")
		graphique.append(_message)
		_message.pack(side=BOTTOM)

		helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
		titre = Label(interface, text="HugsBox 1.0", font=helv36)
		graphique.append(titre)
		titre.pack()

		print("1", graphique)
		
		# On re-défini self.graphique;
		self.graphique = list(graphique)

		# On fait tourner notre interface en boucle jusqu'a fermeture;
		interface.mainloop()

	def afficher_tirage(self):
		''' méthode permettant d'afficher les résultats obtenus à l'aide de <tirage> '''

		# On récupère les labels déjà crées et on les efface;
		graphique = list(self.graphique)
		print("2", graphique)
		for elem in graphique:
			elem.destroy()

		# On défini les variables utiles;
		interface = self.interface
		graphique = list()
		if self.relancer != 0:
			self.tirage()
		groupes = dict(self.groupes)

		# On défini un cadre contenant un label;
		cadre = LabelFrame(interface, text="Résultats de la recherche de binômes :", padx=20, pady=20, borderwidth=2)
		graphique.append(cadre)
		cadre.pack(fill="both", side=LEFT)

		# On crée deux boutons <Relancer> et <Stats>;
		bouton1 = Button(interface, text='Relancer', command=self.afficher_tirage)
		self.relancer = 1
		graphique.append(bouton1)
		bouton1.pack(side=TOP, padx=5, pady=5)

		bouton2 = Button(interface, text='Stats')
		graphique.append(bouton2)
		bouton2.pack(side=TOP, padx=5, pady=5)

		signature = Label(interface, text="*- by T0my")
		graphique.append(signature)
		signature.pack(side=BOTTOM)

		# Dans notre label on affiche nos noms;
		i = 0
		num_group = 0
		for ligne in range(len(groupes.keys())):
			for colonne in range(len(groupes[ligne])):
				Label(cadre, text="  {}  ".format(groupes[ligne][colonne]), borderwidth=1).grid(row=ligne, column=colonne)

		# Une fois l'interface affichée, on enregistre nos label;
		self.graphique = list(graphique)

	def documentation(self):
		''' Méthode permettant d'afficher la documentation '''

		# On importe la documentation;
		with open('brainhug.txt', 'r') as fichier:
			docu = fichier.read()

		# On crée la fenetre;
		doc = Tk()
		espace = LabelFrame(doc, text='Cahier des charges :').pack()
		Label(espace, text=docu).pack()
		Button(doc, text='Fermer', command=doc.destroy).pack(side=SW)
		doc.mainloop()

		# On crée une scrollbar;
		scrollbar = Scrollbar(doc)
		scrollbar.pack(side=RIGHT)


var = Alea('fichiers/Terminales.txt')
var.afficher_base()
