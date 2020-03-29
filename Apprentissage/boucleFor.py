"""Fichier d'explications + exemple pour ce qui est des générateurs et iterateur, création d'une boucle for"""

# Iterateur
def myFor(mylist):
    # La fonction iter permet d'appeler la méthode spéciale "__iter__" de 
    # l'objet passé. Celle ci renvoie un itérateur.
    ite =  iter(mylist)
    error = False
    while not error:
        # La méthode next permet d'appeler la méthode spéciale "__next__" de 
        # l'itérateur. Cele ci renvoie les contenant succesivement.
        try:
            print(next(ite)) 
        # Si on arrive à la fin de la list, "StopIteration" se raise donc on
        # stop la lecture
        except StopIteration: 
            error = True
            print("Fin de la boucle")


my_list =  [2 , 7, 878, 0]

myFor(my_list)




