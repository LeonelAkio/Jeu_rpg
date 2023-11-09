#créé par leonel akio briones

import random
from colorama import Fore, Style, init

init(autoreset=True)  # Initialise colorama

def lancer_des():
    return random.randint(1, 6), random.randint(1, 6)

def main():
    niveau_vie = 20
    nombre_victoires = 0
    nombre_defaites = 0
    victoires_consecutives = 0  # Compteur de victoires consécutives

    while niveau_vie > 0:
        if victoires_consecutives < 3:
            force_adversaire = random.randint(1, 5)
        else:
            force_adversaire = random.randint(6, 12)  # Difficulté pour le boss
            print(Fore.RED + "Félicitations ! Vous affrontez maintenant le boss avec une difficulté de :", force_adversaire)

        print("Vous tombez face à face avec un adversaire de difficulté :", force_adversaire)
        print("Que voulez-vous faire?")
        print("1- " + Fore.GREEN + "Combattre cet adversaire" + Style.RESET_ALL)
        print("2- " + Fore.YELLOW + "Contourner cet adversaire et aller ouvrir une autre porte" + Style.RESET_ALL)
        print("3- " + Fore.BLUE + "Afficher les règles du jeu" + Style.RESET_ALL)
        print("4- " + Fore.MAGENTA + "Quitter la partie" + Style.RESET_ALL)

        choix = input("Entrez votre choix : ")

        if choix == "1":
            votre_de_1, votre_de_2 = lancer_des()
            monstre_de_1, monstre_de_2 = lancer_des()
            somme_votre_de = votre_de_1 + votre_de_2
            somme_monstre_de = monstre_de_1 + monstre_de_2

            print("Vos dés :", votre_de_1, ",", votre_de_2)
            print("Dés du monstre :", monstre_de_1, ",", monstre_de_2)

            if somme_votre_de > somme_monstre_de:
                print(Fore.GREEN + "Victoire!")
                niveau_vie += force_adversaire
                nombre_victoires += 1
                victoires_consecutives += 1
            else:
                print(Fore.RED + "Défaite!")
                niveau_vie -= force_adversaire
                nombre_defaites += force_adversaire  # Le joueur perd autant de points de vie que la force du monstre
                victoires_consecutives = 0  # Réinitialisation du compteur de victoires consécutives en cas de défaite

            print("Niveau de vie :", niveau_vie)

        elif choix == "2":
            niveau_vie -= 1  # Pénalité de 1 point de vie
            print(Fore.YELLOW + "Vous contournez l'adversaire et allez ouvrir une autre porte.")
            print("Niveau de vie :", niveau_vie)

        elif choix == "3":
            print(Fore.BLUE + "Règles du jeu :")
            print("Pour réussir un combat, la somme des dés lancés doit être supérieure à la force de l’adversaire.")
            print("Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.")
            print("Une défaite a lieu lorsque la somme des dés lancés par l’usager est inférieure ou égale à la force de l’adversaire.")
            print("Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
            print("La partie se termine lorsque les points de vie de l’usager tombent sous 0.")
            print("L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

        elif choix == "4":
            print(Fore.MAGENTA + "Merci et au revoir...")
            break

    if niveau_vie <= 0:
        print("La partie est terminée. Vous avez vaincu", nombre_victoires, "monstres.")

if __name__ == "__main__":
    main()
