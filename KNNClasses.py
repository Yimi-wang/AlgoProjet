import json
import heapq
from TestVect import TestVect
from collections import Counter
"""
Nom de la classe: KNNClasses

Méthodes
__init__(self, description: str, data: List) -> None
    Description: Initialise une nouvelle instance de la classe KNNClasses.
    Paramètres:
    description (str): Description des données.
    data (List): Liste des classes et de leurs vecteurs.
add_class(self, label: str, vectors: List) -> None
    Description: Ajoute une nouvelle classe à l'objet KNNClasses.
    Paramètres:
    label (str): Nom de la classe.
    vectors (List): Liste des vecteurs associés à la classe.
add_vector(self, label: str, vector: Dict) -> None
    Description: Ajoute un vecteur à une classe existante.
    Paramètres:
    label (str): Nom de la classe à laquelle le vecteur doit être ajouté.
    vector (Dict): Vecteur à ajouter.
del_class(self, label: str) -> None
    Description: Supprime une classe de l'objet KNNClasses.
    Paramètres:
    label (str): Nom de la classe à supprimer.
    save_as_json(self, filename: str) -> None
Description: Sauvegarde les données dans un fichier JSON.
Paramètres:
    filename (str): Nom du fichier dans lequel sauvegarder les données.
    load_as_json(self, filename: str) -> None
Description: Charge les données à partir d'un fichier JSON.
Paramètres:
    filename (str): Nom du fichier à partir duquel charger les données.
classify(self, vector: Dict, k: int, sim_func=None) -> List[Tuple[str, float]]
    Description: Classifie un vecteur en utilisant l'algorithme KNN.
    Paramètres:
    vector (Dict): Vecteur à classifier.
    k (int): Nombre de voisins à considérer.
    sim_func (Optional[Callable]): Fonction de similarité à utiliser. Par défaut, utilise la similarité cosinus.
printjson(self) -> str
    Description: Renvoie une représentation sous forme de chaîne de caractères des données de l'objet KNNClasses.
changedata(self, new_data: List) -> None
    Description: Modifie les données de l'objet KNNClasses.
    Paramètres:
    new_data (List): Nouvelles données à utiliser.
"""
class KNNClasses:
    def __init__(self,description,data) -> None:
        # Initialise l'objet KNNClasses avec une description (chaîne) et des données (liste de dictionnaires)
        self.description =description 
        self.data=data

    def add_class(self,label:str,vectors:list) -> str: 
        # Ajoute une nouvelle classe à l'objet KNNClasses
        # label (str) : le label de la classe à ajouter
        # vectors (list) : une liste de vecteurs (dictionnaires) associés à cette classe
        add_element={"label":label,"vectors":vectors}
        self.data.append(add_element)

    def add_vector(self,label:str,vector:dict) -> str: 
        # Ajoute un vecteur à une classe existante en utilisant son label
        # label (str) : le label de la classe à laquelle ajouter le vecteur
        # vector (dict) : un dictionnaire représentant le vecteur à ajouter à la classe
        # Parcourir les éléments dans les données
        for element in self.data:
            # Vérifier si le label de l'élément correspond au label fourni
            if element['label']==label:
                #Ajouter le vecteur à la liste des vecteurs de l'élément
                element['vectors'].append(vector)
                # Retourner un message de succès pour terminer la méthode
                return "L'ajout de données a été effectué avec succès."
        # Si la méthode n'a pas été interrompue avant, imprimer un message d'échec
        return "Échec de l'ajout de données."
        
    def del_class(self, label: str) -> str:
        # Cette méthode supprime une classe en utilisant son label.
        
        # Parcourir les éléments dans les données de l'objet KNNClasses.
        for element in self.data:
            
            # Vérifier si le label de l'élément correspond au label donné.
            if element['label'] == label:
                
                # Si le label correspond, supprimer l'élément des données.
                self.data.remove(element)
                
                # Retourner un message indiquant que la suppression a réussi.
                return "La suppression de la classe a été effectuée avec succès."
        
        # Si le label n'a pas été trouvé, retourner un message d'erreur.
        return "Erreur, Label ne trouve pas."

    def save_as_json(self, filename: str) -> str:
        # Créer un dictionnaire contenant la description et les données de l'objet
        data_dict = {'description': self.description, "data": self.data}
        
        # Utiliser une instruction try-except pour gérer les erreurs d'ouverture de fichier
        try:
            # Ouvrir le fichier en mode écriture ('w')
            with open(filename, 'w') as f:
                # Écrire les données au format JSON dans le fichier
                json.dump(data_dict, f)
            
            # Retourner un message indiquant que l'enregistrement a réussi
            return "save succee"
        except IOError:
            # Retourner un message d'erreur si l'ouverture du fichier échoue
            return "Erreur de ouvrir le fichier"
    
    def load_as_json(self, filename: str) -> str:
        # Essayer d'ouvrir le fichier spécifié par "filename"
        try:
            with open(filename) as f:
                # Charger le contenu JSON du fichier dans la variable data_json
                data_json = json.load(f)
        except IOError:
            # Retourner un message d'erreur si le fichier n'a pas pu être ouvert
            return "Erreur de ouvrir le fichier"

        # Mettre à jour la description et les données à partir du contenu JSON chargé
        self.description = data_json["description"]
        self.data = data_json["data"]

        # Retourner un message indiquant que le chargement a réussi
        return "Chargement réussi"
        
    def classify(self, vector: dict, k: int, sim_func=None):
        # Si la fonction de similarité n'est pas fournie, on utilise la fonction 'sim_cosinus' par défaut.
        if sim_func is None:
            sim_func = TestVect.sim_cosinus
        # Initialisation d'un dictionnaire pour stocker les résultats de la comparaison entre le vecteur d'entrée et chaque vecteur de chaque classe.
        res_diff_vect = {}
        # On parcourt chaque classe.
        for class_data in self.data:
            # On initialise une variable 'i' pour garder la trace du nombre de vecteurs dans la classe.
            i=0
            # On parcourt chaque vecteur dans la classe.
            for vec_dans_class in class_data["vectors"]:
                # On incrémente 'i' pour garder la trace du nombre de vecteurs dans la classe.
                i+=1
                # On calcule la similarité entre le vecteur d'entrée et le vecteur actuel de la classe.
                # On stocke le résultat dans le dictionnaire 'res_diff_vect', avec une clé composée du label de la classe et de l'index du vecteur.
                # On utilise une formatage de chaine pour ajouter des zéros à gauche de l'index pour avoir un formatage uniforme.
                res_diff_vect[class_data["label"]+"{:03}".format(i)]=sim_func(vector, vec_dans_class)

        # On décide de l'ordre de tri en fonction de la fonction de similarité fournie.
        # Si la fonction est une distance, on veut le tri croissant. Sinon, on veut le tri décroissant.
        reverse_order = sim_func not in [TestVect.euclidean_distance,TestVect.manhattan_distance]

        # On utilise le module 'heapq' pour obtenir les 'k' éléments les plus similaires (ou les plus proches) du vecteur d'entrée.
        if reverse_order:
            top_k = heapq.nlargest(k, res_diff_vect.items(), key=lambda x: x[1])
        else:
            top_k = heapq.nsmallest(k, res_diff_vect.items(), key=lambda x: x[1])
        # On extrait les labels de classe à partir des clés des 'k' éléments les plus similaires.
        res_class=[]
        for top_k_class in top_k:
            res_class.append(top_k_class[0][:-3])
        
        # On utilise le module 'collections' pour compter le nombre d'occurrences de chaque classe et obtenir la classe la plus fréquente.
        counter = Counter(res_class)
        most_common = counter.most_common(1)[0]
        # On construit une chaîne de caractères pour afficher le résultat.
        res="Le type de dossier est "+str(most_common[0]) +". Et le top_"+str(k)+" est :" + str(top_k)
        return res


    def printjson(self): 
        res="description: "+self.description+"\n" # Concaténer la chaîne "description: " avec la description de l'objet
        res+="data: \n" # Ajouter la chaîne "data: \n" à la chaîne précédente
        for item in self.data: # Parcourir chaque élément dans la liste de données de l'objet
            res+=str(item)+"\n" # Ajouter la représentation chaîne de caractères de l'élément à la chaîne de résultat
        return res # Retourner la chaîne de résultat

    def changedata(self,new_data): # Fonction pour changer les données de l'objet
        self.data=new_data # Remplacer les données de l'objet par les nouvelles données fournies
        
  