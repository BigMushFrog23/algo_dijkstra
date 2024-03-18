# -*- coding: utf-8 -*-
import math

graphe_test = {"a" : {"b" : 3, "c" : 1},
               "b" : {"a" : 3, "c" : 2,"d" : 2},
               "c" : {"a" : 1,"b" : 2,"d" : 3,"e" : 5},
               "d" : {"b" : 2,"c" : 3,"e" : 1,"f" : 3},
               "e" : {"c" : 5,"d" : 1,"f" : 1},
               "f" : {"d" : 3,"e" : 1}}

graphe_villes = {"berlin"   : {"budapest" : 935, "kiev" : 1346, "milan" : 1036,
                               "paris" : 1047},
                 "budapest" : {"berlin" : 935, "kiev" : 1121, "milan" : 954},
                 "kiev"     : {"berlin" : 1346, "budapest" : 1121},
                 "madrid"   : {"milan" : 1570, "paris" : 1271},
                 "milan"    : {"berlin" : 1036, "budapest" : 954, "madrid" : 1570,
                               "paris" : 849},
                 "paris"    : {"berlin" : 1047, "madrid" : 1271, "milan" : 849}}

def sommet_distance_min(sommets_a_visiter, distance):
    ''' Prend en entrée un tableau de sommets et un dictionnaire de distances
        Renvoie le sommet à distance minimale
    '''
    # la distance affectée à chaque sommet est infinie
    distance_min = math.inf
    # Initialisation du sommet à distance minimale à None
    sommet_min = None
    # pour chaque sommet à visiter, si la distance est inférieure à la distance
    # minimale actuelle, on met à jour les données distance_min et sommet_min
    for sommet in sommets_a_visiter:
        if distance[sommet] < distance_min:
            distance_min = distance[sommet]
            sommet_min = sommet
    # on renvoie le sommet à distance minimale
    return sommet_min

def dijkstra(graphe, depart, arrivee):
    ''' Prend en entrée une liste d'adjacence (graphe), un sommet de départ et
    un sommet d'arrivée.
    Renvoie deux dictionnaires :
        - distance : la distance de chaque sommet avec le sommet de départ
        - parent : le parent du sommet dans le chemin minimal à ce sommet
    '''
    # création des dictionnaires distance et parent
    distance = {}
    parent   = {}
    # initialisation des distances à l'infini
    for sommet in graphe:
        distance[sommet] = math.inf
    # on marque le départ dans les dictionnaires distance et parent
    distance[depart] = 0
    parent[depart] = None
    # on crée un tableau de sommets non sélectionnés, qui contient tous les
    # sommets du graphe au début
    sommets_a_visiter = [sommet for sommet in graphe] 
    
    # boucle principale de l'algorithme
    while sommets_a_visiter:
        # récupération du sommet non visité à distance minimale
        sommet_min = sommet_distance_min(sommets_a_visiter, distance)
        # test de sortie de l'algorithme : si le sommet choisi est l'arrivée,
        # on renvoie les deux dictionnaires construits.
        if sommet_min == arrivee:
            return distance,parent
        # dans le cas contraire
        else:
            # on supprime le sommet choisi du tableau des sommets à visiter
            sommets_a_visiter.remove(sommet_min)
            # création du tableau des voisins du sommet choisi
            voisins = [sommet for sommet in graphe[sommet_min] if sommet in sommets_a_visiter]
            # pour chaque sommet voisin non visité
            for voisin in voisins:
                # on calcule la distance totale au voisin
                distance_total = distance[sommet_min] + graphe[sommet_min][voisin]
                # si la distance calculée est inférieure à la distance actuelle,
                # on met à jour les données distance et parent
                if distance_total < distance[voisin]:
                    distance[voisin] = distance_total
                    parent[voisin] = sommet_min 

def affiche_chemin_min(graphe, depart, arrivee):
    ''' Prend en entrée une liste d'adjacence (graphe), un sommet de départ et
    un sommet d'arrivée.
    Affiche la distance minimale entre les deux sommets, et le chemin minimal.
    '''
    # application de l'algorithme de Dijkstra sur le graphe, entre les deux sommets
    distance, parent = dijkstra(graphe, depart, arrivee)
    print(f"La distance de {depart} à {arrivee} est de longueur {distance[arrivee]}.")
    # affichage du chemin minimal entre les deux sommets
    chemin = arrivee
    sommet = arrivee
    while sommet != depart:
        chemin = parent[sommet] + ' --> ' + chemin
        sommet = parent[sommet]
    print(f"Le chemin de {depart} à {arrivee} : {chemin}.")
