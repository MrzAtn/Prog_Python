"""Fichier d'explications + exemple pour ce qui est des générateurs"""
# import numpy as np

# # On défini une fonction permettant de renvoyer tout les élméments
# # dans un interval donné.
# def gene(borne_start, borne_end):
#     if borne_start<borne_end: 
#         borne_start += 1
#         while borne_start<borne_end:
#             # "yield" permet de renvoyer un élément et se met en pause 
#             # jusqu'au prochain appel de la fonction.
#             yield borne_start
#             borne_start += 1
#     # Si la borne_Start est > borne_end, on compte à l'envers
#     elif borne_start>borne_end:
#         borne_start -= 1
#         while borne_end<borne_start:
#             yield borne_start
#             borne_start -= 1

# # Deuxième géné avec possibilité de modifier comportement pendant le traitement
# def gene2(borne_start, borne_end): 
#     borne_start += 1
#     while borne_start<borne_end:
#         new_value = (yield borne_start)
#         if new_value is not None:
#             borne_start = new_value
#             yield borne_start
#         borne_start += 1

# if __name__ == "__main__":

#     generateur = gene2(1,26)

#     for nb in generateur:
#         if nb == 15: # On saute à 20
#             generateur.send(20)
#         print(nb, end=" ")



### CAS PRATIQUE POUR DE LA BIG DATA ###

import numpy as np

big_data = """Le sénateur, dont il a été parlé plus haut, était un homme entendu qui 
    avait fait son chemin avec une rectitude inattentive à toutes ces rencontres qui font 
    obstacle et qu'on nomme conscience, foi jurée, justice, devoir; il avait marché droit à 
    son but et sans broncher une seule fois dans la ligne de son avancement et de son intérêt. 
    C'était un ancien procureur, attendri par le succès, pas méchant homme du tout, rendant 
    tous les petits services qu'il pouvait à ses fils, à ses gendres, à ses parents, même à 
    des amis; ayant sagement pris de la vie les bons côtés, les bonnes occasions, les bonnes 
    aubaines. Le reste lui semblait assez bête. Il était spirituel, et juste assez lettré 
    pour se croire un disciple d'Epicure en n'étant peut-être qu'un produit de Pigault-Lebrun.
    [...]
    (Les Misérables, Victor Hugo)
    """

import re

def is_part_of_a_word(character):
    return len(re.findall('\w', character, flags = re.UNICODE))  

def get_words(text):
    print("Je commence à lire le texte maintenant")
    
    current_word = ""
    for character in text:
        if not is_part_of_a_word(character):
            if current_word != "":
                yield current_word
                current_word = ""
        else:
            current_word += character

def filter_by_size(words):
    return (w for w in words if len(w) >= 6)

def filter_by_letters(words):
    return (w for w in words if "a" in w)
            
words = get_words(big_data)
words = filter_by_size(words)
words = filter_by_letters(words)
print("'words' est encore un générateur. Le texte n'a toujours pas été lu")
        
print("L'opération suivante va lancer la lecture du texte: ")
a= [w for w in words]
print(a)

