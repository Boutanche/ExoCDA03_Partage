
################################################################################
# Programme testant si une année est bissextile ou non.
# Tests if user's input is an leap year.
# by Benoit Bertrand CDA03
# 25/11/2019
################################################################################

"""Module anneeBissextile contenant :
la fonction anneeBissextile
la fonction anneeBissextile2 """

#-------------------------- Première Fonction ----------------------------------

# La fonction anneeBissextile est l'exercice demandé par Davy en cours.
# This is what the teacher wants.
def anneeBissextile() :
    """ Fonction anneeBissextile()
    Demande à l'utilisiateur de saisir une année :
    Ecrit si elle l'est ou pas. """

    annee = input("Saisissez une année : ")

    # La fonction try me permet de tester la saisie utilisateur et générer un expet.
    # Try is an fonction for trying the user's input.
    try :
        annee = int(annee)
        bissextile = False

        if annee % 400 == 0 or (annee % 100 != 0 and annee % 4 == 0) :
            bissextile = True
            print("L'année saisie est bissextile.")
        else:
            print("L'année saisie n'est pas bissextile.")

    # Thank you Mario ! But our princess is in another castle.
    except :
        print("la variable ne contient pas un chiffre entier.")
        anneeBissextile()


#---------------------------- Deuxième Fonction --------------------------------

# La fonction anneeBissextile2 fait appelle à une fonction Python *Voir Doc.
# Fonction anneeBissextile2 calls an other Python's fonction.
def anneeBissextile2() :

    """Fonction anneeBissextile2
    Demande à l'utilisiateur de saisir une année :
    Ecrit si elle l'est ou pas.
    Fonctionne avec une fonction Python."""

    import calendar
    annee = input("Saisissez une année : ")
    try :
        annee = int(annee)
        bissextile = calendar.isleap(annee)
        if bissextile == True :
            print("L'année est bissextile.")
        else :
            print("L'année n'est pas bissextile.")
    except :
        print("Vous n'avez pas saisi une année valide : Recommencez.")
        anneeBissextile2()


#------------------------- Lancement des deux fonctions ------------------------

# Test des fonctions :
if __name__ == "__main__":

    anneeBissextile()
    anneeBissextile2()

    input("Press Any Key to Close...")


#---------------------------- Thanks ! -----------------------------------------