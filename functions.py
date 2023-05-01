# Function pour le nom d'utilisateur
def name():
    nom: str = input("Entrer votre nom d'utilisateur (trois caractères au moins): ")
    if nom.isalpha():

        if len(nom) < 3:
            print("Le nom saisi est trop court")
            return name()
        else:
            nom = nom.capitalize()
            return nom

    elif not nom.isalnum():
        print("Entrez un nom valide")
        return name()
    else:
        print("Veuillez entrer un nom valide")
        return name()


# Function pour le mot de passe
def password():
    mot_de_passe = input("Entrez votre mot de passe (quatre caractères au minimum): ")

    if mot_de_passe.isalnum() and len(mot_de_passe) >= 4:
        return mot_de_passe
    else:
        print('Entrez un mot de passe valide')
        return password()


# Function pour le montant du compte
def montant_compte(n):
    montant = input('Montant sur le compte : ')
    if montant.isdigit() and int(montant) >= 0:
        print('Le montant présent sur le compte de Mr/Mlle/Mme ', n, 'est', montant, 'Fcfa\n')
        return montant
    else:
        print('Veuillez entrez une somme valide')
        return montant_compte(n)


# Function pour le choix de l'opération
def operation_choice(mdp, mt):
    choix = input("Entrez l'opération à effectuer : ")
    if choix.isalpha():

        if len(choix) == 0:
            print("Vous n'avez rien entrez")
            return operation_choice(mdp, mt)
        elif len(choix) > 1:
            print("Entrez un seul caractère")
            return operation_choice(mdp, mt)
        else:
            choix = choix.lower()

            if choix == "d":
                # On gère le dépôt
                print('\nVous voulez faire un dépôt')

                # Vérification sur la somme à déposer
                def depot():
                    somme_depot = input('\nEntrer le montant que vous voulez déposer : ')
                    if not somme_depot.isdigit():
                        print('Vous n\'avez pas entrer une somme')
                        return depot()
                    else:
                        return somme_depot

                depot_somme = depot()
                print('Vous allez déposer', depot_somme, 'Fcfa sur votre compte \n')

                def ajout():
                    j = 0
                    verification_mdp = 0
                    while (j < 3) or (verification_mdp != mdp):
                        verification_mdp = input("Entre votre mot de passe pour confirmer le dépôt: ")
                        if verification_mdp.isdigit():
                            if verification_mdp == mdp:
                                break
                            else:
                                print("Mot de passe incorrect. Veuillez réessayer")
                        else:
                            print("Mot de passe incorrect. Veuillez réessayer \n")
                        j += 1
                        if j == 3:
                            break

                    if verification_mdp == mdp:
                        print('\nEn attente de réseau... Cela peut prendre quelques instants')
                        print('Dépôt effectué avec succès. Votre nouveau solde est:', int(mt) + int(depot_somme), '\n')
                    else:
                        print("\n Vous avez atteint votre nombre maximal d'essai. L'opération est donc annulée \n")

                ajout()
            elif choix == "t":
                # On gère le transfert
                print("\nVous voulez effectuer un transfert\n")

                # Vérification sur la somme à transférer
                def transfert():
                    somme_transfert = input('Entrer le montant que vous voulez transférer: ')
                    if not somme_transfert.isdigit():
                        print('Vous n\'avez pas entrer une somme')
                        return transfert()
                    else:
                        if somme_transfert > mt:
                            print("Le montant que vous voulez transférer est supérieur à votre solde \n")
                            return transfert()
                        else:
                            return somme_transfert

                transfert_somme = transfert()

                # Numéro de compte sur lequel le transfert doit être effectué
                def compte_transfert():
                    cpte_transfert = input(
                        '\nEntrer le numéro du compte sur lequel vous voulez effectuer le transfert (huit chiffres) : ')
                    if cpte_transfert.isdigit():
                        if len(cpte_transfert) != 8:
                            print('Le numéro du compte doit être de huit(8) chiffres exactement')
                            return compte_transfert()
                        else:
                            return cpte_transfert
                    else:
                        print("Entrer un numéro de compte valide")
                        return compte_transfert()

                transfert_compte = compte_transfert()

                print('Vous voulez transférer ', transfert_somme, 'Fcfa sur le compte :', transfert_compte, '\n')

                def envoie():
                    j = 0
                    verification_mdp = 0
                    while (j < 3) or (verification_mdp != mdp):
                        verification_mdp = input("Entre votre mot de passe pour confirmer le transfert: ")
                        if verification_mdp.isdigit():
                            if verification_mdp == mdp:
                                break
                            else:
                                print("Mot de passe incorrect. Veuillez réessayer")
                        else:
                            print("Mot de passe incorrect. Veuillez réessayer \n")
                        j += 1
                        if j == 3:
                            break

                    if verification_mdp == mdp:
                        print('\nEn attente de réseau... Cela peut prendre quelques instants')
                        print('Transfert effectué avec succès. Votre nouveau solde est:', int(mt) - int(transfert_somme)
                              , 'FCFA\n')
                    else:
                        print("\n Vous avez atteint votre nombre maximal d'essai. L'opération est donc annulée \n")

                envoie()
            else:
                print("Entrez 'd' ou 't'.")
                return operation_choice(mdp, mt)
    elif choix.isalnum():
        print("Entrez une lettre")
        return operation_choice(mdp, mt)
    else:
        print("Veuillez entrer un caractère valide")
        return operation_choice(mdp, mt)
