import time  #Cette librairie c'est pour la fin du programme

file= open('Processeur.txt', 'w')
  




  
def menu():
  print("Bienvenue dans le programme\n 1.Saisir nouvel équipement.\n 2.Mettre à jour ou supprimer un équippement.\n 3.Voir la liste des équipements.\n 4.Quitter application")
  choix = int(input("Entrer votre choix :"))

  if choix == "1":
    print("Quel équipement souaitez-vous saisir ?,\n Voici la liste des équipements:") # ici faut mettre le fichier texte avec tout les composants
  
  if choix == "2":
    print("1.Mettre à jours?,\n 2.Supprimer?") # je donne a l'utilisateur la posibilité de choissir entre mettre a jour ou supprimer dans un autre sous menu
    Second_choix = int(input("Entrer votre choix :"))
    
    if Second_choix == 1 :
        print("Quel équipement souhaitez-vous mettre à jour ?,\n Voici la liste des équipements:") # ici faut mettre le fichier texte avec tout les composants
    
    if Second_choix == 2 :
        print("Quel équipements souhaitez-vous supprimer ?,\n Voici la liste des équipements:") # ici faut mettre le fichier texte avec tout les composants
  
  if choix == "3":
    print("Voici la liste des équipements:") # ici faut mettre le fichier texte avec tout les composants
  
  if choix == "4":
    print("A plus tard !")
    time.sleep(5)
    print("Le programme se ferme dans 5 secondes")
    break


menu()
    
