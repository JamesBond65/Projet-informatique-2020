

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
    dateExpiration=input("Entrer la date d'expiration de la liscence du system d'exploitation :")       #J'ajoute tt les éléments

    
    
    sauvegarde= (input("Voules vous sauvegarder les données saisies ? tapez 'o' ou 'n' "))  

    
    
    if sauvegarde == "o":
        file= open('data.txt', 'a')
        file.write(processeur+ "#" +ram+ "#" +bus+ "#" +carteGraphique+ "#" +portVideo+ "#" +resolutionEcran+ "#" +tailleEcran+ "#" +nombreDePortsUSB+ "#" +tailleDisqueSSD+ "#" +graveurCD+ "#" +carteReseau+ "#" +wifi+ "#" +bluetooth+ "#" +fabricant+ "#" +fournisseur+ "#" +dateAchat+ "#" +localisation+ "#" +utilisateur+ "#" +nomDuLogiciel+ "#" +editeur+ "#" +version+ "#" +dateExpiration+ "\n")
        file.close()    #J'enregistre ci dessus les nouveaux parametres dans le fichier


def mettre_a_jour():
    
    with open("data.txt", "r" ) as file : 
        numérotation=1
        
        for ligne in file:   
            chaine= ligne.split("#")
            print(numérotation, ")  ", end="")
            numérotation=numérotation+1
                
            for valeur in range(len(chaine)):
                print(valeur ,end=" ")            #Tout ca permet d'ouvrir le fichier et d'afficher ce qu'y a dedans
                
            print("")

    mise_a_jour= int(input("\nQuelle ligne souhaitez vous mettre à jour ?"))        
    print("Vous avez choisi la ligne numéro :", mise_a_jour)
    
    chaine_recherchée=0
    
    with open("data.txt", "r" ) as file :
        for i in range(mise_a_jour) :
            
            chaine_recherchée= file.readline()
   
    print("\nVoici l'equippement selectionne:", end="")
    for valeurs in range(len(chaine_recherchée)):
                print(valeurs ,end=" ")        #La y'a un problrme mais j'ai pas encore trouvé
    
    


def supprimer_equipement():

    with open("data.txt", "r" ) as file : 
        numérotation=1

        for ligne in file:   
            chaine= ligne.split("#")
            print(numérotation, ")  ", end="")
            numérotation=numérotation+1
                
            for valeur in range(len(chaine)):
                print(valeur ,end=" ")
                
            print("")

    ligne_supression=int(input("Sur quelle ligne se situe l'équippement que vous voulez supprimer ?"))
    f = open ("data.txt", "r" )
    lines = f.readlines()
    del(lines[ligne_supression - 1])
    f.close()
    f= open("data.txt", "w")
    f.writelines(lines)
    f.close()


def menu():
 
    print("Bienvenue dans le programme\n 1.Saisir nouvel équipement.\n 2.Mettre à jour ou supprimer un équippement.\n 3.Voir la liste des équipements.\n 4.Quitter application")
    choix = int(input("Entrer votre choix :"))

    if choix == 1:
        print("Vous avez choisi : Ajouter un equipement.")
        ajouterEquippement()  #renvoie à la fonction définie ci-dessus
  
    if choix == 2:
        print("1.Mettre à jour?,\n 2.Supprimer?") # je donne a l'utilisateur la posibilité de choissir entre mettre a jour ou supprimer dans un autre sous menu
        second_choix = int(input("Entrer votre choix (1 ou 2):"))
        
    
        if second_choix == 1 :
            print("Quel équipement souhaitez-vous mettre à jour ?,\n Voici la liste des équipements:\n") # ici faut mettre le fichier texte avec tout les composants
            mettre_a_jour()
                


        if second_choix == 2 :
            print("Quel équipements souhaitez-vous supprimer ?,\n Voici la liste des équipements:") # ici faut mettre le fichier texte avec tout les composants
            supprimer_equipement()
  
    if choix == 3:
        print("Voici la liste des équipements:\n") # ici faut mettre le fichier texte avec tout les composants
        with open("data.txt", "r" ) as file : 
            numérotation=1
            for ligne in file:   
                chaine= ligne.split("#")
                print(numérotation, ")  ", end="")
                numérotation=numérotation+1
                
                for valeur in range(len(chaine)):
                    print(valeur ,end=" ")
                
                print("")
                    
        
        input("\nAppuyez sur entrer pour continuer\n")
        menu()

    if choix == 4:
        print("A plus tard !")
        print("Le programme se ferme dans  secondes")
        exit(0)
    
    
    else:
        print("Le parametre entré n'est pas un entier de la liste, recommencer s'il vous plait.\n")
        menu()



while 1:
    menu()


