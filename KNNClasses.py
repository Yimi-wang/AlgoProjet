import json
import heapq
from VectDistance import VectDistance
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
######ASD
class KNNClasses:
    def __init__(self,description,data) -> None:
        # Initialise l'objet KNNClasses avec une description (chaîne) et des données (liste de dictionnaires)
        self.description =description 
        self.data=data

    def add_class(self,label:str,vectors:list) -> str: 
        # Ajoute une nouvelle classe à l'objet KNNClasses
        # label (str) : le label de la classe à ajouter
        # vectors (list) : une liste de vecteurs (dictionnaires) associés à cette classe
        # verifier les donnees
        if not isinstance(label, str):
            return "Erreur: le paramètre 'label' doit être une chaîne de caractères."
        if not isinstance(vectors, list):
            return "Erreur: le paramètre 'vectors' doit être une liste."
        for vector in vectors:
            if not isinstance(vector, dict):
                return "Erreur: les éléments de 'vectors' doivent être des dictionnaires."
        for element in self.data:
            if element["label"] == label:
                return "Erreur: le label '{}' existe déjà.".format(label)+"Pour ajouter la vector, utilise le methode de Add_Vector."
        #main
        add_element={"label":label,"vectors":vectors}
        self.data.append(add_element)
        return "L'action add de class a été effectué avec succès."

    def add_vector(self,label:str,vector:dict) -> str: 
        # Ajoute un vecteur à une classe existante en utilisant son label
        # label (str) : le label de la classe à laquelle ajouter le vecteur
        # vector (dict) : un dictionnaire représentant le vecteur à ajouter à la classe
        # Parcourir les éléments dans les données
        if not isinstance(label, str):
            return "Erreur: le paramètre 'label' doit être une chaîne de caractères."
        
        
        if not hasattr(self, 'data'):
            return "L'objet doit avoir des attributs 'data'"
        
        if not isinstance(vector, dict):
            return "Erreur: le paramètre 'vectors' doit être une dict."
        for element in self.data:
            # Vérifier si le label de l'élément correspond au label fourni
            if element['label']==label:
                #Ajouter le vecteur à la liste des vecteurs de l'élément
                element['vectors'].append(vector)
                # Retourner un message de succès pour terminer la méthode
                return "L'ajout de données a été effectué avec succès."
        # Si la méthode n'a pas été interrompue avant, imprimer un message d'échec
        return "Échec de l'ajout de données. Le label n'existe pas."
        
    def del_class(self, label: str) -> str:
        # Cette méthode supprime une classe en utilisant son label.
        if not isinstance(label, str):
            return "Erreur: le paramètre 'label' doit être une chaîne de caractères."
        
        if not hasattr(self, 'data'):
            return "L'objet doit avoir des attributs 'data'"
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
        if not isinstance(filename, str):
            return "Erreur: le paramètre 'label' doit être une chaîne de caractères."
        if not hasattr(self, 'description') or not hasattr(self, 'data'):
            return "L'objet doit avoir des attributs 'description' et 'data'"
        # Créer un dictionnaire contenant la description et les données de l'objet

        data_dict = {'description': self.description, "data": self.data}
        
        # Utiliser une instruction try-except pour gérer les erreurs d'ouverture de fichier
        try:
            # Ouvrir le fichier en mode écriture ('w')
            with open(filename, 'w') as f:
                # Écrire les données au format JSON dans le fichier
                json.dump(data_dict, f)
            
            # Retourner un message indiquant que l'enregistrement a réussi
            return "save success"
        except (IOError, json.JSONDecodeError):
            # Retourner un message d'erreur si l'ouverture du fichier échoue
            return "rreur d'ouverture du fichier"
    
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
        
        if not hasattr(self, 'description') or not hasattr(self, 'data'):
            return "L'objet doit avoir des attributs 'description' et 'data'"
                
        # Si la fonction de similarité n'est pas fournie, on utilise la fonction 'sim_cosinus' par défaut.
        if sim_func is None:
            sim_func = VectDistance.sim_cosinus
        # Initialisation d'un dictionnaire pour stocker les résultats de la comparaison entre le vecteur d'entrée et chaque vecteur de chaque classe.
        res_diff_vect = {}
        # On parcourt chaque classe.
        for class_data in self.data:
            # On parcourt chaque vecteur dans la classe.
            for vec_dans_class in class_data["vectors"]:
                # On calcule la similarité entre le vecteur d'entrée et le vecteur actuel de la classe.
                # On stocke le résultat dans le dictionnaire 'res_diff_vect'
                try:
                    if class_data["label"] in res_diff_vect:
                        res_diff_vect[class_data["label"]].append(sim_func(vector, vec_dans_class))
                    else:
                        res_diff_vect[class_data["label"]]=[sim_func(vector, vec_dans_class)]
                except ValueError as e:
                    print(e)
                    return str(e)

        # On décide de l'ordre de tri en fonction de la fonction de similarité fournie.
        # Si la fonction est une distance, on veut le tri croissant. Sinon, on veut le tri décroissant.
        reverse_order = sim_func not in [VectDistance.euclidean_distance,VectDistance.manhattan_distance]

        # On utilise le module 'heapq' pour obtenir les 'k' éléments les plus similaires (ou les plus proches) du vecteur d'entrée.
        all_values = [v for values in res_diff_vect.values() for v in values]
        if reverse_order:
            top_k = heapq.nlargest(k, all_values)
        else:
            top_k = heapq.nsmallest(k, all_values)

        result = [[key, [v for v in values if v in top_k]] for key, values in res_diff_vect.items() if set(values).intersection(top_k)]
        # On construit une chaîne de caractères pour afficher le résultat.
        res=''
        for element in result:
            res+="label: "+str(element[0])+", n:"+str(len(element[1]))+". average_sim :"+str(sum(element[1])/len(element[1]))+"\n"
        
        #Le principal objectif de ce code est de trouver le type de document correspondant au résultat le plus fréquent parmi les K résultats. 
        #Si plusieurs résultats sont les plus fréquents, il retourne celui avec la valeur moyenne la plus élevée (ou la plus basse, en fonction de la fonction de distance utilisée).
        # Calculer la longueur maximale de la liste
        max_length = max(len(item[1]) for item in result)

        # Trouver l'élément ayant la plus grande longueur
        longest_items = [item for item in result if len(item[1]) == max_length]

        # Si l'élément ayant la plus grande longueur est unique, le retourner directement
        if len(longest_items) == 1:
            resultdetype = longest_items[0][0]
        else:
            # Si plusieurs éléments ont la plus grande longueur, calculer leur valeur moyenne et retourner l'élément avec la valeur moyenne la plus élevée (ou petit)
            avg_values = [(item[0], sum(item[1]) / len(item[1])) for item in longest_items]
            if reverse_order:
                max_avg_key = max(avg_values, key=lambda x: x[1])[0]
                resultdetype = [item for item in longest_items if item[0] == max_avg_key][0][0]
            else:
                min_avg_key = min(avg_values, key=lambda x: x[1])[0]
                resultdetype = [item for item in longest_items if item[0] == min_avg_key][0][0]
        res+="Le type de dossier est : " + resultdetype
        return res


    def printjson(self): 
        if not hasattr(self, 'description') or not hasattr(self, 'data'):
            return "L'objet doit avoir des attributs 'description' et 'data'"
        res="description: "+self.description+"\n" # Concaténer la chaîne "description: " avec la description de l'objet
        res+="data: \n" # Ajouter la chaîne "data: \n" à la chaîne précédente
        for item in self.data: # Parcourir chaque élément dans la liste de données de l'objet
            res+=str(item)+"\n" # Ajouter la représentation chaîne de caractères de l'élément à la chaîne de résultat
        return res # Retourner la chaîne de résultat

    def changedata(self,new_data): # Fonction pour changer les données de l'objet
        self.data=new_data # Remplacer les données de l'objet par les nouvelles données fournies
        
  