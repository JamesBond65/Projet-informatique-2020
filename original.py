
def afficher_equipements():

    with open("data.txt", "r") as file:
        numérotation = 1

        for ligne in file:
            chaine = ligne.split("#")
            print(numérotation, ")  ", end="")
            numérotation = numérotation + 1

            for valeur in range(len(chaine)):
                print(chaine[valeur], end=" ")

            print("")

def ajouterEquippement():
    
    processeur= " [1] processeur : #" + input("Entrer le modele et la vitesse du processeur :")
    ram= " [2]ram : #" + input("Entrer la taille de la RAM :")
    bus= " [3]bus : #" + input("Enter le type de bus (PCI, SATA...) :")
    carteGraphique= " [4] carteGraphique : #" + input("Enter le modele de la carte graphique :")
    portVideo= " [5] portVideo : #" + input("Entrer les ports présents sur l'appareil (VGA, HDMI, Thunderbolt,...):")
    resolutionEcran= "[6] resolutionEcran : #" + input("Entrer la résoution de l'écran :")
    tailleEcran= " [7] tailleEcran : #" + input("Entrer la taille de l'ecran :")
    nombreDePortsUSB= " [8] nombreDePortsUSB : #" + input("Entrer le nombre de ports USB :")
    tailleDisqueSSD= " [9] tailleDisqueSSD : #" + input("Indique la capacité du disque du ou du SSD")
    graveurCD= " [10] graveurCD : #" + input("INdiquez si l'appareil possede un graveur/lecteur CD")
    carteReseau= " [11] carteReseau : #" + input("Indiquez le constructeur et le débit de la carte reseau :")
    wifi= " [12] wifi : #" + input("Entrer le type et la bande frequence du wifi :")
    bluetooth= " [13] bluetooth : #" + input("Indiquez le type de bleutooth :")
    fabricant= " [14] fabricant : #" + input("Entrer le fabriquant du PC :")
    fournisseur= " [15] fournisseur : #" + input("Entrer le fournisseur du PC :")
    dateAchat= " [16] dateAchat : #" + input("Entrer la date de l'achat:")
    localisation= " [17] localisation : #" + input("Entrer la localisation de l'appereil dans l'établissement :")
    utilisateur= " [18] utilisateur : #" + input("Entrer les utilisateurs ou le nombre d'utilisateur pouvant acceder au PC :")
           #J'ajoute tt les éléments

    
    
    sauvegarde= (input("Voules vous sauvegarder les données saisies ? tapez 'o' ou 'n' "))  

    
    
    if sauvegarde == "o":
        file= open('data.txt', 'a')
        file.write(processeur+ "#" +ram+ "#" +bus+ "#" +carteGraphique+ "#" +portVideo+ "#" +resolutionEcran+ "#" +tailleEcran+ "#" +nombreDePortsUSB+ "#" +tailleDisqueSSD+ "#" +graveurCD+ "#" +carteReseau+ "#" +wifi+ "#" +bluetooth+ "#" +fabricant+ "#" +fournisseur+ "#" +dateAchat+ "#" +localisation+ "#" +utilisateur)
        file.close()    #J'enregistre ci dessus les nouveaux parametres dans le fichier

    x = True
    compteur = 0
    index = 18
    while x==True :
        logiciel_supl = (input("Voulez vous rajouter des logiciels ? tapez 'o' ou 'n' "))
        if logiciel_supl == "n":
            file = open('data.txt', 'a')
            file.write("\n")
            file.close()
            x = False # le break enleve le while du menu donc fallait le faire a la mano
        else:
            compteur += 1
            index +=1
            nomDuLogiciel=  (" [%d] nom du system du logiciel  : #" % index) + input("Indiquez le nom du logiciel :")
            index += 1
            editeur = (" [%d] éditeur du logiciel : #" % index) +  input("Entrer l'editeur du logiciel :")
            index += 1
            version = (" [%d] éditeur du logiciel : #" % index) +  input("Entrer la version du logiciel :")
            index += 1
            dateExpiration = (" [%d] date d'expiration du logiciel  : #" % index) +  input("Entrer la date d'expiration de la liscence du logiciel :")
            file = open('data.txt', 'a')
            file.write("#" +nomDuLogiciel+ "#" +editeur+ "#" +version+ "#" +dateExpiration)
            file.close()



def mettre_a_jour():
    
    afficher_equipements()

    mise_a_jour= int(input("\nQuelle ligne souhaitez vous mettre à jour ?"))        
    print("Vous avez choisi la ligne numéro :", mise_a_jour)

    terme_changer = int(input("\nQuel est le numero du terme que vous voulez mettre à jour ? (numéro entre crochets)"))
    nouvelle_valeur = input("Indiquez la nouvelle valeur")
    f = open("data.txt", "r")
    lines = f.readlines()

    chaine = lines [mise_a_jour - 1]


    chaine = chaine.split("#")

    chaine[(terme_changer*2) - 1] = nouvelle_valeur
    nouvelle_chaine = ""
    for i in range (len(chaine)):
        nouvelle_chaine = nouvelle_chaine   + str(chaine[i])+ "#"
    lines[mise_a_jour - 1] = nouvelle_chaine
    f.close()
    f = open("data.txt", "w")
    f.writelines(lines)
    print("valeur changée")
    f.close()

def supprimer_equipement():

    choix_supp=int(input("\nvoulez vous supprimer un ordinateur (1) ou un logiciel d'ordinateur (2) ?"))

    if choix_supp == 1 :

        afficher_equipements()

        ligne_supression=int(input("\nSur quelle ligne se situe l'équippement que vous voulez supprimer ?"))
        f = open ("data.txt", "r" )
        lines = f.readlines()
        del(lines[ligne_supression - 1])
        f.close()
        f= open("data.txt", "w")
        f.writelines(lines)
        f.close()

    elif choix_supp == 2 :

        afficher_equipements()

        mise_a_jour = int(input("\nQuelle ligne souhaitez vous mettre à jour ?"))
        print("Vous avez choisi la ligne numéro :", mise_a_jour)

        logiciel_supp = 2* (int(input("\nQuel est le numéro du terme que vous voulez mettre à jour ? (numéro entre crochets)")))
        f = open("data.txt", "r")
        lines = f.readlines()
        chaine = lines[mise_a_jour-1]
        chaine=chaine.split("#")
        for qbc in range(8):
            del(chaine[logiciel_supp-2])
        nouvelle_chaine = ""
        for i in range(len(chaine)):
            nouvelle_chaine = nouvelle_chaine  + str(chaine[i]) + "#"
        lines[mise_a_jour - 1] = nouvelle_chaine
        f.close()
        f = open("data.txt", "w")
        f.writelines(lines)
        print("valeur changée")
        f.close()

def rechercher_par_parametre() :

    type_para = int(input("voulez vous rechercher :\n 1/Hardware\n 2/Software"))

    if type_para == 1 :
        hardware = {1: "processeur", 2: "ram", 3: "bus", 4: "carteGraphique", 5: "portVideo", 6: "resolutionEcran",
                    7: "tailleEcran", 8: "nombreDePortsUSB", 9: "tailleDisqueSSD", 10: "graveurCD", 11: "carteReseau",
                    12: "wifi", 13: "bluetooth", 14: "fabricant", 15: "fournisseur", 16: "dateAchat",
                    17: "localisation", 18: "utilisateur"}
        print(hardware.values())
        type_hardware = str()
        while type(type_hardware)== str:
            type_hardware = str(input("Quel harware souhaitez vous ?"))#je connais la caracteristique qu'il souhaite
            for abc in hardware.keys():
                if hardware[abc] == type_hardware:
                    type_hardware = abc #je la transfforme en nombre pour l'utiliser dans une liste
                    break
            if type(type_hardware)==str:
                print("valeur inconnue")

        choix_recherche = int(input("choix_recherche"))
        f = open("data.txt", "r")
        lines = f.readlines()
        numerotation = 1
        if choix_recherche == 1:
            for i in range(len(lines)):
                chaine = lines[i]
                chaine = chaine.split("#")
                print(numerotation, ")", chaine[2*type_hardware-2],chaine[2*type_hardware-1])
                numerotation += 1

        elif choix_recherche == 2:
            terme_recherche = str(input("quel est le terme recherche?"))
            for i in range(len(lines)):
                chaine = lines[i]
                chaine = chaine.split("#")
                if chaine[2*type_hardware-1] == terme_recherche:
                    print(numerotation, ")", chaine[2*type_hardware-2],chaine[2*type_hardware-1])
                numerotation += 1
        f.close()

    elif type_para == 2 :
        software = {1: "nomDuLogiciel", 2: "editeur", 3: "version", 4: "dateExpiration"}
        print(software.items())
        type_software = int(input("Quel software souhaitez vous ?"))
        type_software =2*type_software-1
        choix_recherche = int(input("choix_recherche"))
        f = open("data.txt", "r")
        lines = f.readlines()
        numerotation = 1
        if choix_recherche == 1:
            for i in range(len(lines)):
                chaine = lines[i]
                chaine = chaine.split("#")
                for abc in range(36):
                    del (chaine[0])
                for thor in range(type_software,len(chaine),8):
                    print(numerotation, ")", chaine[thor])
                numerotation += 1

        elif choix_recherche == 2:
            terme_recherche = str(input("quel est le terme recherche?"))
            for i in range(len(lines)):
                chaine = lines[i]
                chaine = chaine.split("#")
                for xyz in range(36):
                    del (chaine[0])
                for Odin in range(type_software,len(chaine),8):
                    if chaine[Odin]==terme_recherche:
                        x=int()
                        for Zeus in range(0,type_software,8):
                            x=Zeus
                            for Athena in range(8):#
                                #
                                print(numerotation, ")", chaine[x])#
                                x += 1
                numerotation += 1
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
            print("Quel équipement souhaitez-vous mettre à jour ?,\n ") # ici faut mettre le fichier texte avec tout les composants
            mettre_a_jour()
                


        if second_choix == 2 :
            print("Quel équipements souhaitez-vous supprimer ?,\n ") # ici faut mettre le fichier texte avec tout les composants
            supprimer_equipement()
  
    if choix == 3:
        print("Voici la liste des équipements:\n") # ici faut mettre le fichier texte avec tout les composants
        with open("data.txt", "r" ) as file : 
            numérotation =1
            for ligne in file:   
                chaine= ligne.split("#")
                print(numérotation, ")  ", end="")
                numérotation =numérotation+1
                
                for valeur in range(len(chaine)):
                    print(chaine[valeur] ,end=" ")
                
                print("")
                    
        
        input("\nAppuyez sur entrer pour continuer\n")
        menu()

    if choix == 4:
        print("A plus tard !")
        print("Le programme se ferme dans  secondes")
        exit(0)

    if choix == 5:
        rechercher_par_parametre()
    
    else:
        print("Le paramètre entré n'est pas un entier de la liste, recommencez s'il vous plait.\n")
        menu()


while 1:
    menu()


