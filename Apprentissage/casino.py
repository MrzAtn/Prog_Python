import random
from math import *


def r_roulette(nb_D, nb_F):
    result = random.randrange(nb_D, nb_F)
    return result


def arrondi(gain):
    gain = ceil(gain)
    return gain


if __name__ == "__main__":

    continuer_Partie = True
    mise = 0

    nb_D = 0
    nb_F = 49

    argent = 100
    print("==Le jeu de la roulette==")
    print("Vous commencez avec :", argent, "$")
    while (argent > 0 and continuer_Partie == True):
        num_choix = int(input("Quel est le numero sur lequel vous voulez miser ? : Choisir entre 0 et 49\n"))
        while (num_choix > nb_F or num_choix < nb_D):
            print("Error : vous devez choisir un nombre entre 0 et 49 petit(e) Malin(e)")
            num_choix = int(input("Quel est le numero sur lequel vous voulez miser ? : Choisir entre 0 et 49\n"))
        mise = int(input("Combien voulez vous miser ? :"))
        if mise > argent:
            while mise > argent:
                print("Error vous n'avez pas assez d'argent pour miser cette somme !")
                print("Veuillez saisir une somme dans vos moyens svp !\n")
                mise = int(input("Combien voulez vous miser ? :"))
        result = r_roulette(nb_D, nb_F)
        print("\nLe numero tire est le : ", result)
        if result == num_choix:
            gain = arrondi(3 * mise)
            print("Vous avez gagné avec le numero ! \n Votre gain est de : ", gain)
            argent = argent + gain
            print("Votre portefeuil vaut maintenant : ", argent, "$")
            answer = input("Voulez-vous rejouer ? (Appuyer Y pour oui et N pour non) :\t")
            if answer == "Y":
                continuer_Partie = True
            elif answer == "N":
                continuer_Partie = False
                break
            else:
                print("Erreur : Vous n'avez pas sélectionner la commande correctement ")
                continuer_Partie = False
                break

        elif (num_choix % 2 == result % 2):
            gain = arrondi(0.5 * mise)
            print("Vous avez gangé avec la couleur ! \nVotre gain est de :", gain)
            argent = argent - gain
            print("Votre portefeuil vaut maintenant : ", argent, "$")

            answer = input("Voulez-vous rejouer ? (Appuyer Y pour oui et N pour non) :\t")
            if answer == "Y":
                continuer_Partie = True
            elif answer == "N":
                continuer_Partie = False
                break
            else:
                print("Erreur : Vous n'avez pas sélectionner la commande correctement ")
                continuer_Partie = False
                break
        else:
            print("Desole, vous avez perdu...")
            argent = argent - mise
            print("Votre portefeuil vaut maintenant : ", argent, "$")
            answer = input("Voulez-vous rejouer ? (Appuyer Y pour oui et N pour non) :\t")
            if answer == "Y":
                continuer_Partie = True
            elif answer == "N":
                continuer_Partie = False
                break
            else:
                print("Erreur : Vous n'avez pas sélectionner la commande correctement ")
                continuer_Partie = False
                break
    print("Vous allez être expulsé du casino... Desole et à la prochaine fois !")
