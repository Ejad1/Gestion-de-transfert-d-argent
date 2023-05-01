# -*-coding:Utf-8 -*
import os
from functions import *

reponse = 1
while reponse == 1:
    print("\nBienvenue sur notre système de transfert et de dépôt d'argent. \n")

    user = dict()

    nom = name()

    print("Merci", nom, "de nous faire confiance. \n")

    print("Veuillez définir un mot de passe")
    mot_de_passe = password()

    user[nom] = mot_de_passe

    nom_utilisateur = ""
    mdp_utilisateur = 0
    for cle in user.keys():
        nom_utilisateur = cle

    for valeur in user.values():
        mdp_utilisateur = valeur

    print('\nEntrez la somme présente sur votre compte')
    montant = montant_compte(nom)

    print("Que voulez-vous faire : un dépôt ou un transfert (d/t) ?")
    choix = operation_choice(mot_de_passe, montant)

    print("Voulez-vous continuer ?\nTaper 1 pour oui\nTaper tout autre lettre ou chiffre pour non\n")
    reponse = input("Voulez-vous continuer : ")
    if not reponse.isalpha():
        reponse = int(reponse)

os.system("pause")
