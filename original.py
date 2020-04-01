import time  #Cette librairie c'est pour la fin du programme

  

def ajouterEquippement():
    
    processeur=input("Entrer le modele et la vitesse du processeur :")
    ram=input("Entrer la taille de la RAM :")
    bus=input("Enter le type de bus (PCI, SATA...) :")
    carteGraphique=input("Enter le modele de la carte graphique :")
    portVideo=input("Entrer les ports présents sur l'appareil (VGA, HDMI, Thunderbolt,...):")
    resolutionEcran=input("Entrer la résoution de l'écran :")
    tailleEcran=input("Entrer la taille de l'ecran :")
    nombreDePortsUSB=input("Entrer le nombre de ports USB :")
    tailleDisqueSSD=input("Indique la capacité du disque du ou du SSD")
    graveurCD=input("INdiquez si l'appareil possede un graveur/lecteur CD")
    carteReseau=input("Indiquez le constructeur et le débit de la carte reseau :")
    wifi=input("Entrer le type et la bande frequence du wifi :")
    bluetooth=input("Indiquez le type de bleutooth :")
    fabricant=input("Entrer le fabriquant du PC :")
    fournisseur=input("Entrer le fournisseur du PC :")
    dateAchat=input("Entrer la date de l'achat:")
    localisation=input("Entrer la localisation de l'appereil dans l'établissement :")
    utilisateur=input("Entrer les utilisateurs ou le nombre d'utilisateur pouvant acceder au PC :")
    nomDuLogiciel=input("Indiquez le nom du system d'exploitation :")
    editeur=input("Entrer l'editeur du system d'exloitation :")
    version=input("Entrer la version du system d'exploitation :")
    dateExpiration=input("Entrer la date d'expiration de la liscence du system d'exploitation :")

    
    
    sauvegarde= (input("Voules vous sauvegarder les données saisies ? tapez 'o' ou 'n' "))

    
    
    if sauvegarde == "o":
        file= open('data.txt', 'a')
        file.write(processeur+ "#" +ram+ "#" +bus+ "#" +carteGraphique+ "#" +portVideo+ "#" +resolutionEcran+ "#" +tailleEcran+ "#" +nombreDePortsUSB+ "#" +tailleDisqueSSD+ "#" +graveurCD+ "#" +carteReseau+ "#" +wifi+ "#" +bluetooth+ "#" +fabricant+ "#" +fournisseur+ "#" +dateAchat+ "#" +localisation+ "#" +utilisateur+ "#" +nomDuLogiciel+ "#" +editeur+ "#" +version+ "#" +dateExpiration+ "\n")
        file.close()




def menu():
 
    print("Bienvenue dans le programme\n 1.Saisir nouvel équipement.\n 2.Mettre à jour ou supprimer un équippement.\n 3.Voir la liste des équipements.\n 4.Quitter application")
    choix = int(input("Entrer votre choix :"))

    if choix == 1:
        print("Vous avez choisi : Saisir un equipement.")
        ajouterEquippement()
  
    if choix == 2:
        print("1.Mettre à jour?,\n 2.Supprimer?") # je donne a l'utilisateur la posibilité de choissir entre mettre a jour ou supprimer dans un autre sous menu
        second_choix = int(input("Entrer votre choix :"))
    
        if second_choix == 1 :
            print("Quel équipement souhaitez-vous mettre à jour ?,\n Voici la liste des équipements:") # ici faut mettre le fichier texte avec tout les composants
    
        if second_choix == 2 :
            print("Quel équipements souhaitez-vous supprimer ?,\n Voici la liste des équipements:") # ici faut mettre le fichier texte avec tout les composants
  
    if choix == 3:
        print("Voici la liste des équipements:") # ici faut mettre le fichier texte avec tout les composants
  
    if choix == 4:
        print("A plus tard !")
        time.sleep(5)
        print("Le programme se ferme dans 5 secondes")
        exit()
    
    
    else:
        print("Le parametre entré n'est pas un entier de la liste, recommencer s'il vous plait.\n")
        menu()


menu()
file= open('data.txt', 'r')
print(file.read())