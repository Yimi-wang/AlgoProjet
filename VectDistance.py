import math
import numpy as np
"""
API pour la classe VectDistance :

1. sim_cosinus(vec1: dict, vec2: dict) -> float:
    Calcule la similarité cosinus entre deux vecteurs représentés par des dictionnaires.
    Paramètres :
        vec1 (dict) : Premier vecteur sous forme de dictionnaire.
        vec2 (dict) : Deuxième vecteur sous forme de dictionnaire.
    Retour :
        float : La similarité cosinus entre les deux vecteurs.

2. euclidean_distance(vec1: dict, vec2: dict) -> float:
    Calcule la distance euclidienne entre deux vecteurs représentés par des dictionnaires.
    Paramètres :
        vec1 (dict) : Premier vecteur sous forme de dictionnaire.
        vec2 (dict) : Deuxième vecteur sous forme de dictionnaire.
    Retour :
        float : La distance euclidienne entre les deux vecteurs.

3. manhattan_distance(vec1: dict, vec2: dict) -> float:
    Calcule la distance de Manhattan entre deux vecteurs représentés par des dictionnaires.
    Paramètres :
        vec1 (dict) : Premier vecteur sous forme de dictionnaire.
        vec2 (dict) : Deuxième vecteur sous forme de dictionnaire.
    Retour :
        float : La distance de Manhattan entre les deux vecteurs.

4. pearson_correlation_coefficient(vect1: dict, vect2: dict) -> float:
    Calcule le coefficient de corrélation de Pearson entre deux vecteurs représentés par des dictionnaires.
    Paramètres :
        vec1 (dict) : Premier vecteur sous forme de dictionnaire.
        vec2 (dict) : Deuxième vecteur sous forme de dictionnaire.
    Retour :
        float : Le coefficient de corrélation de Pearson entre les deux vecteurs.
"""

class VectDistance:    
    @staticmethod
    def is_valid_vector(dist):
        if not isinstance(dist, dict):
            return False
        for key, value in dist.items():
            if not isinstance(key, str):
                return False
            if not isinstance(value, (int, float)):
                return False
        return True
    # Définition de la fonction sim_cosinus pour calculer la similarité cosinus entre deux vecteurs 
    @staticmethod
    def sim_cosinus(vec1: dict, vec2: dict) -> float:
        # Determiner le vec1 et vec2 est une vector ou pas
        if not (VectDistance.is_valid_vector(vec1) and VectDistance.is_valid_vector(vec2) ):
            raise ValueError("vec1 et vec2 doit etre un forme de str:int ou str:float")
        
        # Obtenir les clés communes entre les deux vecteurs
        keys = set(vec1.keys()) & set(vec2.keys())

        # Si les vecteurs n'ont pas de clés communes, retourner 0.0
        if not keys:
            return 0.0
        # Créer des tableaux numpy avec les valeurs des clés communes
        vec1_values = np.array([vec1[key] for key in keys])
        vec2_values = np.array([vec2[key] for key in keys])

        # Calculer le produit scalaire des deux tableaux
        dot_product = np.dot(vec1_values, vec2_values)
        # Calculer la magnitude de chaque vecteur
        vec1_values_tous_vector=np.array(list(vec1.values()))
        vec2_values_tous_vector=np.array(list(vec2.values()))
        magnitude_vec1 = np.linalg.norm(vec1_values_tous_vector)
        magnitude_vec2 = np.linalg.norm(vec2_values_tous_vector)

        # Si l'une des magnitudes est égale à 0, retourner 0.0
        if magnitude_vec1 == 0 or magnitude_vec2 == 0:
            return 0.0

        # Calculer la similarité cosinus en divisant le produit scalaire par le produit des magnitudes
        cosine_sim = dot_product / (magnitude_vec1 * magnitude_vec2)
        return cosine_sim

    # Définition de la fonction euclidean_distance pour calculer la distance euclidienne entre deux vecteurs
    @staticmethod
    def euclidean_distance(vec1: dict, vec2: dict) -> float:
        # Determiner le vec1 et vec2 est une vector ou pas
        if not (VectDistance.is_valid_vector(vec1) and VectDistance.is_valid_vector(vec2) ):
            raise ValueError("vec1 et vec2 doit etre un forme de str:int ou str:float")
        
        distance = 0

        # Parcourir toutes les clés des deux dictionnaires
        for key in set(vec1.keys()).union(vec2.keys()):
            # Récupérer la valeur de la clé dans dict1, sinon retourner 0
            value1 = vec1.get(key, 0)
            # Récupérer la valeur de la clé dans dict2, sinon retourner 0
            value2 = vec2.get(key, 0)
            # Calculer la somme des différences au carré
            distance += (value1 - value2) ** 2
        if distance < 0:
            # Si la distance est négative, lever une exception ValueError avec un message d'erreur correspondant
            raise ValueError("La distance euclidienne ne peut pas être négative.")
        # Retourner la racine carrée de la distance
        return math.sqrt(distance)

    # Définition de la fonction manhattan_distance pour calculer la distance de Manhattan entre deux vecteurs
    @staticmethod
    def manhattan_distance(vec1: dict, vec2: dict) -> float:
        # Determiner le vec1 et vec2 est une vector ou pas
        if not (VectDistance.is_valid_vector(vec1) and VectDistance.is_valid_vector(vec2) ):
            raise ValueError("vec1 et vec2 doit etre un forme de str:int ou str:float")
        
        distance = 0

        # Parcourir toutes les clés des deux dictionnaires
        for key in set(vec1.keys()).union(vec2.keys()):
            # Récupérer la valeur de la clé dans dict1, sinon retourner 0
            value1 = vec1.get(key, 0)
            # Récupérer la valeur de la clé dans dict2, sinon retourner 0
            value2 = vec2.get(key, 0)

            # Calculer la somme des différences absolues
            distance += abs(value1 - value2)
        return distance
    @staticmethod
    def pearson_correlation_coefficient(vect1, vect2):
        # Determiner le vec1 et vec2 est une vector ou pas
        if not (VectDistance.is_valid_vector(vect1) and VectDistance.is_valid_vector(vect2) ):
            raise ValueError("vec1 et vec2 doit etre un forme de str:int ou str:float")
                
        # Intersection des clés des deux dictionnaires
        keys = set(vect1.keys()) & set(vect2.keys())
        
        # Extraction des valeurs des deux dictionnaires en utilisant les clés communes
        values1 = [vect1[key] for key in keys]
        values2 = [vect2[key] for key in keys]
        
        # Vérification que les listes de valeurs ne sont pas vides
        if len(values1) == 0 or len(values2) == 0:
            raise ValueError("Pas de key commun.")
        
        # Calcul du nombre de valeurs communes
        n = len(values1)
        
        # Calcul des sommes des valeurs de chaque vecteur
        sum1 = sum(values1)
        sum2 = sum(values2)
        
        # Calcul des sommes des carrés des valeurs de chaque vecteur
        sum1_sq = sum([pow(v, 2) for v in values1])
        sum2_sq = sum([pow(v, 2) for v in values2])
        
        # Calcul de la somme des produits des valeurs correspondantes des deux vecteurs
        prod_sum = sum([values1[i] * values2[i] for i in range(n)])
        
        # Calcul du numérateur de la formule de la corrélation de Pearson
        num = prod_sum - (sum1 * sum2 / n)
        
        # Calcul du dénominateur de la formule de la corrélation de Pearson
        den = ((sum1_sq - pow(sum1, 2) / n) * (sum2_sq - pow(sum2, 2) / n)) ** 0.5
        
        # Vérification que le dénominateur n'est pas égal à zéro
        if den == 0:
            return 0
        
        # Calcul et retour du coefficient de corrélation de Pearson
        return num / den
    