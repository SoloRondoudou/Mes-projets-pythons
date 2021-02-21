"""
cote main.py :


import test    // importer le fichier module

test.lol()     // utiliser la fontion


cote modules.py

def lol():
  print("c'est tros drole 🤣")

"""

"""
    database
db["yann"] = "13"   cree une cle dans la base de donne yann -> 13
  print(db["yann"])   afficher la valeur de la cle yann
  matches = db.prefix("yann")  lister une cle
  print(matches)
  del db["yann"]      supprimer la cle yann
"""
from tkinter import *
import time
import sys
import random


def vitesse(km, h):
    result = km / h
    print("Vous allez a " + str(result) + "km/h")


def algorithm():
    i = 0
    sys.stdout.write('Chargement de l algorithm : 0%|')
    while (i < 15):
        sys.stdout.write('-')
        i = i + 1
        sys.stdout.flush()
        time.sleep(0.2)

    sys.stdout.write('|100%\n')
    sys.stdout.flush()

    while (True):
        database_insert_cle_nom = input("merci d'entrer le nom de votre cle : ")
        database_insert_cle_val = int(input("merci d'entrer la valeur de votre cle : "))
        db[database_insert_cle_nom] = database_insert_cle_val
        print("votre cle se nomme : " + database_insert_cle_nom)
        print("votre cle a comme valeur : " + str(db[database_insert_cle_nom]))
        print(db.prefix(database_insert_cle_nom))
        print("")


def tkinter(titre, taill, min_x, min_y, color, logo):
    """
    :param titre: l'element titre vous servira a donner un titre a votre page (cette element doit etre ecrit entre "" ex: "titre")
    :param taill: l'element taill vous servira a definir une taill (cette element doit etre ecri entre "" ex: "360x360")
    :param min_x: l'element  vous servira a definir la plus petite tail en x (cette element doit etre ecri sans "" ex: 360)
    :param min_y: l'element  vous servira a definir la plus petite tail en y (cette element doit etre ecri sans "" ex: 360)
    :param color: l'element  vous servira a definir la couleur de font (cette element doit etre ecri entre "" ex: black ou #FF0000)
    :param logo: l'element  vous servira a definir  un petit logo en haut a gauche (cette element doit etre ecri entre "" ex: "logo.ico")
    """
    windows = Tk()
    windows.title(titre)
    windows.geometry(taill)
    windows.minsize(min_x, min_y)
    windows.config(background=color)
    windows.iconbitmap(logo)
    windows.mainloop()


def code(code):
    """
    :param code: l'element code sera le code que vou aller choisir (cette element doit etre ecri entre "" ex : "200ET"
    """
    code_v = input("code : ")
    code_valide = len(code_v)
    if code_v == code:
        print("code bon")
        code_validation = input("confirmer votre code : ")
        if code_validation == code:
            print("vous etes inscris")


        else:
            print("recomencer mauvais code")
            recommencer = input("je ne connais pas le mot de passe (appuis sur une touche) : ")
            if recommencer != 1:
                nom = input("quel est votre nom : ")
                if nom == "yann":
                    print("ok")
                    nomf = input("quel est votre nom de famille : ")
                    if nomf == "guszkiewicz":
                        print("vous etes inscris")

    else:
        recommencer = input("je ne connais pas le mot de passe (appuis sur entrer) : ")
        if recommencer != 1:
            nom = input("quel est votre nom : ")
            if nom == "yann":
                print("ok")
                nomf = input("quel est votre nom de famille : ")
                if nomf == "guszkiewicz":
                    print("vous etes inscris")


def affiche(x):
    """
    :param x: l'elemen x serre a ecrire quelque chose sur la console
    """
    print(x)


def delay(x):
    """
    :param x: l'elemen x serre a attendre "x" seconde(s)
    """
    time.sleep(x)


def gramme_en_ml(gramme):
    """
    :param gramme: l'element gramme pourra convertire les grammes en ml de lait
    """
    result = gramme * 1.03
    print(result, "ml de lait")


def ml_en_gramme(ml):
    """
     :param ml_en_gramme: merci de vous rendre a la fontion gramme_en_ml
    """
    result = ml / 1.03
    print(result, "gramme")


def loto(x, y):
    """
    :param x: la valeur de x est un chois entre x et y
    :param y: la valeur de y est un chois entre x et y
    """
    print("le loto")
    choices = random.randint(x, y)
    val = input("donnee votre chiffre: ")

    print(choices)

    if choices == val:
        print("vous avez gagnée 1 000 000$")



    else:
        print("perdue")


def aleatoir(x, y):
    """
    :param x: la valeur de x est un chois entre x et y
    :param y: la valeur de x est un chois entre x et y
    """
    choices = random.randint(x, y)
    print(choices)


def timer():
    """
    :return: cette fontion serre a cree un timmer
    """
    for u in range(100):
        y = input("timmer : ")
        y = int(y)
        y = y + 1
        for x in range(0, y):
            print(x, "seconde")
            time.sleep(1)

        print("temps termine")
        print("")
        print("")
        print("")
        print("")
        print("")

    print("appuyer sur run")


def addition(x, y):
    result = x + y
    print(result)


def soustration(x, y):
    result = x - y
    print(result)


def division(x, y):
    result = x / y
    print(result)


def multiplication(x, y):
    result = x * y
    print(result)


def vetement():
    print("voici le chois de vetement de cette journer\n")
    habit_tete = ["un collier", "des boucles d'oreilles", "une casquette", "des lunettes", "bracelet"]
    habit_haut = ["un T-shirt manche longue", "un T-shirt manche courte", "un pulle"]
    habit_bas = ["un pantalons", "une jupe", "une salopette", "un shirt"]
    couleur = ["blanc(he)", "noir", "rose", "bleu", "gris(e)", "jaune"]

    print(random.choice(habit_tete), random.choice(couleur))
    print(random.choice(habit_haut), random.choice(couleur))
    print(random.choice(habit_bas), random.choice(couleur))


def timer_minute(x):
    for i in range(0, x):
        print(i, "minute")
        time.sleep(15)
        print(i, ". 25 minute")
        time.sleep(15)
        print(i, ". 50 minute")
        time.sleep(15)
        print(i, ". 75 minute")
        time.sleep(15)


def fichier():
    read_or_write = input("lire(r) ecrire(w) : ")

    fichier = input("nom du fichier : ")

    if (read_or_write == "w"):
        x = input()

        with open(fichier, "w") as fichier:
            fichier.write(x)

        fichier.close()
        print("fichier cree")


    elif (read_or_write == "r"):
        with open(fichier, "r") as fichier:
            i = fichier.read()
            print("voici la lecture : ")
            print("")
            print(i)


def Tableau():
    liste = []
    print("ajouter 1 element")
    print("ajouter plusieurs elements")
    print("supprimer")
    print("afficher")
    print("tout supprimer")
    print("nombre d'article")
    print("quitter")
    while (1 == 1):
        print("")
        action = input("ation : ")

        if (action == "ajouter 1 element"):
            aj = input("que voulez vous ajouttez : ")
            liste.append(aj)
            print(aj, " a ete ajouter a : ", liste)
            print("")



        elif (action == "ajouter plusieurs elements"):
            article = input("merci de separer les element par une virgule ex : oeufs,eau,... : ").split(",")
            liste.extend(article)
            print(article, "ont ete ajouter a la liste")
            print("voici la liste : ", liste)
            print("")




        elif (action == "nombre d'article"):
            compte = len(liste)
            print("il y a : ", compte, " element(s)")
            print("")



        elif (action == "afficher"):
            print("voici votre list : ", liste)
            print("")


        elif (action == "supprimer"):
            personage = input("le quel voulez vous supprimer : ")
            liste.remove(personage)
            print(personage, "a ete supprimmer")
            print("list : ", liste)
            print("")




        elif (action == "tout supprimer"):
            liste.clear()
            print("tout a ete effacer : ", liste)
            print("")



        elif (action == "quitter"):
            print("au revoir")
            quit()


        else:
            print("action non valide")
