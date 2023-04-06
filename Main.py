from KNNClasses import KNNClasses
from VectDistance import VectDistance
from TestToVect import TestToVect
import tkinter as tk
import ast    
"""
Cet API définit plusieurs fonctions de gestion des événements liés aux différents boutons présents dans l'interface graphique. 
Ces fonctions permettent d'ajouter ou de supprimer des classes, d'ajouter des vecteurs, de sauvegarder et de charger des données au format JSON, 
d'afficher les données JSON et de classifier le document.
on_add_class_click() : Cette fonction gère le clic sur le bouton "Ajouter une classe". 
Elle crée une nouvelle fenêtre pour saisir les informations de la classe et ajoute la classe avec les informations entrées.

on_add_vector_click() : Cette fonction gère le clic sur le bouton "Ajouter un vecteur". 
Elle crée une nouvelle fenêtre pour saisir les informations du vecteur et ajoute le vecteur avec les informations entrées.

on_del_class_click() : Cette fonction gère le clic sur le bouton "Supprimer une classe". 
Elle crée une nouvelle fenêtre pour saisir le nom de la classe à supprimer et supprime la classe avec le nom entré.

on_save_as_json_click() : Cette fonction gère le clic sur le bouton "Enregistrer en JSON". 
Elle crée une nouvelle fenêtre pour saisir le nom du fichier dans lequel sauvegarder les données et enregistre les données au format JSON avec le nom entré.

on_load_as_json_click() : Cette fonction gère le clic sur le bouton "Charger à partir d'un fichier JSON". 
Elle crée une nouvelle fenêtre pour saisir le nom du fichier à charger et charge les données à partir du fichier JSON avec le nom entré.

show_json() : Cette fonction affiche les données JSON dans une nouvelle fenêtre lorsqu'on clique sur le bouton "Afficher JSON".

classify_main() : Cette fonction gère le clic sur le bouton "Classer". 
Elle crée une nouvelle fenêtre pour saisir les informations nécessaires au processus de classification (nom du fichier, valeur de k, fonction de distance) et affiche les résultats de la classification.
"""
def on_add_class_click():
    # Fonction à appeler lors du clic sur le bouton "Submit"
    def on_submit_click():
        # Fonction pour afficher la fenêtre de résultat
        def show_result_window(result):
            # Création d'une nouvelle fenêtre
            result_window = tk.Toplevel(root)

            # Création et ajout d'un label pour afficher "message"
            result_label = tk.Label(result_window, text="message")
            result_label.pack(pady=10)

            # Création et ajout d'un widget Text pour afficher le résultat
            result_text_widget = tk.Text(result_window, wrap=tk.WORD)
            result_text_widget.insert(tk.END, str(result))
            result_text_widget.pack(padx=10, pady=10)

            # Création et ajout d'un bouton "Close" pour fermer la fenêtre
            close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
            close_button.pack(pady=(0, 10))

        # Récupération des valeurs des champs de saisie
        label_value = label_entry.get()
        vector_value = vector_entry.get()

        # Conversion de la valeur du vecteur en liste
        try:
            vector_list = ast.literal_eval(vector_value)
        except (ValueError, SyntaxError):
            res = "Le format de la chaîne entrée par l'utilisateur est incorrect, veuillez vous assurer que vous entrez un format de liste Python standard."
            show_result_window(res)
            top_level.destroy()
            return

        # Appel de la méthode add_class avec les paramètres saisis
        res = Kcl.add_class(label_value, vector_list)

        # Affichage du résultat et fermeture de la fenêtre
        show_result_window(res)
        top_level.destroy()

    # Création d'une nouvelle fenêtre principale
    top_level = tk.Toplevel(root)

    # Création et ajout du premier label et champ de saisie dans la fenêtre principale
    label_label = tk.Label(top_level, text="Label:")
    label_label.grid(row=0, column=0)
    label_entry = tk.Entry(top_level)
    label_entry.grid(row=0, column=1)

    # Création et ajout du deuxième label et champ de saisie dans la fenêtre principale
    vector_label = tk.Label(top_level, text="Vector:")
    vector_label.grid(row=1, column=0)
    vector_entry = tk.Entry(top_level)
    vector_entry.grid(row=1, column=1)

    # Création et ajout d'un bouton "Submit" dans la fenêtre principale
    submit_button = tk.Button(top_level, text="Submit", command=on_submit_click)
    submit_button.grid(row=2, column=1)

def on_add_vector_click():
    def on_submit_click():
        def show_result_window(result):
            # Création d'une nouvelle fenêtre
            result_window = tk.Toplevel(root)

            # Création et ajout d'un label pour afficher "message"
            result_label = tk.Label(result_window, text="message")
            result_label.pack(pady=10)

            # Création et ajout d'un widget Text pour afficher le résultat
            result_text_widget = tk.Text(result_window, wrap=tk.WORD)
            result_text_widget.insert(tk.END, str(result))
            result_text_widget.pack(padx=10, pady=10)

            # Création et ajout d'un bouton "Close" pour fermer la fenêtre
            close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
            close_button.pack(pady=(0, 10))

        res = ''
        # Récupérer les valeurs des champs de saisie
        label_value = label_entry.get()
        vector_value = vector_entry.get()

        try:
            vector_list = ast.literal_eval(vector_value)
        except (ValueError, SyntaxError):
            res = "Le format de la chaîne entrée par l'utilisateur est incorrect. Veuillez vous assurer que vous avez entré un format de liste Python standard."
        
        # Si le format saisi par l'utilisateur est correct, appeler la méthode add_class ici avec les paramètres entrés
        if res == '':
            res = Kcl.add_vector(label_value, vector_list)

        # Afficher le résultat et fermer la fenêtre
        show_result_window(res)
        top_level.destroy()

    # Créer une nouvelle fenêtre de premier niveau
    top_level = tk.Toplevel(root)

    # Créer le premier label et champ de saisie et les ajouter à la fenêtre de premier niveau
    label_label = tk.Label(top_level, text="Label :")
    label_label.grid(row=0, column=0)
    label_entry = tk.Entry(top_level)
    label_entry.grid(row=0, column=1)

    # Créer le deuxième label et champ de saisie et les ajouter à la fenêtre de premier niveau
    vector_label = tk.Label(top_level, text="Vecteur :")
    vector_label.grid(row=1, column=0)
    vector_entry = tk.Entry(top_level)
    vector_entry.grid(row=1, column=1)

    # Créer un bouton "Submit" et l'ajouter à la fenêtre de premier niveau
    submit_button = tk.Button(top_level, text="Soumettre", command=on_submit_click)
    submit_button.grid(row=2, column=1)


def on_del_class_click():
    def on_submit_click():
        def show_result_window(result):
            # Création d'une nouvelle fenêtre
            result_window = tk.Toplevel(root)

            # Création et ajout d'un label pour afficher "message"
            result_label = tk.Label(result_window, text="message")
            result_label.pack(pady=10)

            # Création et ajout d'un widget Text pour afficher le résultat
            result_text_widget = tk.Text(result_window, wrap=tk.WORD)
            result_text_widget.insert(tk.END, str(result))
            result_text_widget.pack(padx=10, pady=10)

            # Création et ajout d'un bouton "Close" pour fermer la fenêtre
            close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
            close_button.pack(pady=(0, 10))
        
        # Récupération de la valeur de l'entrée
        label_value = label_entry.get()
        # Appel de la méthode del_class avec les paramètres entrés
        res = Kcl.del_class(label_value)
        show_result_window(res)
        top_level.destroy()

    # Création d'une nouvelle fenêtre de niveau supérieur
    top_level = tk.Toplevel(root)

    # Création du premier label et de l'entrée, et ajout à la fenêtre de niveau supérieur
    label_label = tk.Label(top_level, text="Label :")
    label_label.grid(row=0, column=0)
    label_entry = tk.Entry(top_level)
    label_entry.grid(row=0, column=1)

    # Création d'un bouton "Submit" et ajout à la fenêtre de niveau supérieur
    submit_button = tk.Button(top_level, text="Submit", command=on_submit_click)
    submit_button.grid(row=1, column=1)

def on_save_as_json_click():
    # Fonction à appeler lorsque le bouton "Submit" est cliqué
    def on_submit_click():
        # Fonction pour afficher le résultat dans une nouvelle fenêtre
        def show_result_window(result):
            # Création d'une nouvelle fenêtre
            result_window = tk.Toplevel(root)

            # Création et ajout d'un label pour afficher "message"
            result_label = tk.Label(result_window, text="message")
            result_label.pack(pady=10)

            # Création et ajout d'un widget Text pour afficher le résultat
            result_text_widget = tk.Text(result_window, wrap=tk.WORD)
            result_text_widget.insert(tk.END, str(result))
            result_text_widget.pack(padx=10, pady=10)

            # Création et ajout d'un bouton "Close" pour fermer la fenêtre

            close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
            close_button.pack(pady=(0, 10))
        # Récupération de la valeur dans la zone de texte
        filename_value = filename_entry.get()
        # Appel de la méthode add_class avec les paramètres saisis
        res = Kcl.save_as_json(filename_value)
        # Affichage du résultat et fermeture de la fenêtre
        show_result_window(res)
        top_level.destroy()

    # Création d'une nouvelle fenêtre de niveau supérieur
    top_level = tk.Toplevel(root)

    # Création du premier label et de la zone de texte, ajoutés à la fenêtre de niveau supérieur
    label_label = tk.Label(top_level, text="Nom du fichier :")
    label_label.grid(row=0, column=0)
    filename_entry = tk.Entry(top_level)
    filename_entry.grid(row=0, column=1)

    # Création d'un bouton "Submit" et ajout à la fenêtre de niveau supérieur
    submit_button = tk.Button(top_level, text="Soumettre", command=on_submit_click)
    submit_button.grid(row=1, column=1)

def on_load_as_json_click():
    def on_submit_click():
        def show_result_window(result):
            # Création d'une nouvelle fenêtre
            result_window = tk.Toplevel(root)

            # Création et ajout d'un label pour afficher "message"
            result_label = tk.Label(result_window, text="message")
            result_label.pack(pady=10)

            # Création et ajout d'un widget Text pour afficher le résultat
            result_text_widget = tk.Text(result_window, wrap=tk.WORD)
            result_text_widget.insert(tk.END, str(result))
            result_text_widget.pack(padx=10, pady=10)

            # Création et ajout d'un bouton "Close" pour fermer la fenêtre
            close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
            close_button.pack(pady=(0, 10))

        # Récupération de la valeur dans l'entrée
        filename_value = filename_entry.get()

        # Appel de la méthode add_class en passant les paramètres d'entrée
        res = Kcl.load_as_json(filename_value)

        # Affichage du résultat et fermeture de la fenêtre
        show_result_window(res)
        top_level.destroy()

    # Création d'une nouvelle fenêtre de niveau supérieur
    top_level = tk.Toplevel(root)

    # Création du premier label et de la zone de saisie, puis ajout à la fenêtre de niveau supérieur
    label_label = tk.Label(top_level, text="Nom du fichier :")
    label_label.grid(row=0, column=0)
    filename_entry = tk.Entry(top_level)
    filename_entry.grid(row=0, column=1)

    # Création d'un bouton de soumission et ajout à la fenêtre de niveau supérieur
    submit_button = tk.Button(top_level, text="Valider", command=on_submit_click)
    submit_button.grid(row=1, column=1)

def show_json():
    # 创建一个新窗口
    new_window = tk.Toplevel(root)

    # 调用 print_json 方法（此处需根据你的实际对象和方法进行调用）
    json_data = Kcl.printjson()

    # 创建一个文本框并将 JSON 数据插入其中
    text_widget = tk.Text(new_window, wrap=tk.WORD)
    text_widget.insert(tk.END, json_data)
    text_widget.pack(padx=10, pady=10)

    # 为新窗口添加一个关闭按钮
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=(0, 10))

def classify_main():
    def on_submit_click():
        def show_result_window(result):
            result_window = tk.Toplevel(root)

            result_label = tk.Label(result_window, text="res：")
            result_label.pack(pady=10)

            result_text_widget = tk.Text(result_window, wrap=tk.WORD)
            result_text_widget.insert(tk.END, str(result))
            result_text_widget.pack(padx=10, pady=10)

            close_button = tk.Button(result_window, text="Fermer", command=result_window.destroy)
            close_button.pack(pady=(0, 10))
        # Récupérer les valeurs des champs de saisie
        Filename_value = Filename_entry.get()
        k_value = k_entry.get()
        k_value=int(k_value)
        Function_value=function_entry.get()
        
        # Appeler la méthode avec les paramètres saisis
        vector_classify=TestToVect.document_to_vector(Filename_value)
        print(vector_classify)
        match Function_value:
            case "":
                print("sim_cosinus")
                res=Kcl.classify(vector_classify,k_value)
            case "e":
                print("euclidean_distance")
                res=Kcl.classify(vector_classify,k_value,VectDistance.euclidean_distance)
            case "m":
                print("manhattan_distance")
                res=Kcl.classify(vector_classify,k_value,VectDistance.manhattan_distance)
            case "p":
                print("pearson_correlation_coefficient")
                res=Kcl.classify(vector_classify,k_value,VectDistance.pearson_correlation_coefficient)
            case _:
                res="erreur,la valeur Function n'est pas correcte"
        show_result_window(res)   
        top_level.destroy()


    # Créer une nouvelle fenêtre de niveau supérieur
    top_level = tk.Toplevel(root)

    # Créer le premier label et le champ de saisie, puis les ajouter à la fenêtre de niveau supérieur
    Filename_label = tk.Label(top_level, text="Nom du fichier :")
    Filename_label.grid(row=0, column=0)
    Filename_entry = tk.Entry(top_level)
    Filename_entry.grid(row=0, column=1)

    # Créer le deuxième label et le champ de saisie, puis les ajouter à la fenêtre de niveau supérieur
    k_label = tk.Label(top_level, text="k :")
    k_label.grid(row=1, column=0)
    k_entry = tk.Entry(top_level)
    k_entry.grid(row=1, column=1)

    # Créer le troisième label et le champ de saisie, puis les ajouter à la fenêtre de niveau supérieur
    function_label = tk.Label(top_level, text="Fonction :")
    function_label.grid(row=2, column=0)
    function_entry = tk.Entry(top_level)
    function_entry.grid(row=2, column=1)
    
    # Créer un bouton de soumission et l'ajouter à la fenêtre de niveau supérieur
    submit_button = tk.Button(top_level, text="Valider", command=on_submit_click)
    submit_button.grid(row=3, column=1)


if __name__ == "__main__":
    # Ouvrir le fichier contenant la description des documents de test
    with open ("./TestDocuments/description.txt") as input_file:
        description=input_file.read()
    # Convertir les documents de test en vecteurs
    data=TestToVect.TestDocument_to_vector()
    
    # Créer une instance de KNNClasses avec la description et les données
    Kcl=KNNClasses(description,data)
    # Créer une fenêtre principale
    root = tk.Tk()

    # Bouton "Ajouter une classe"
    add_class_button = tk.Button(root, text="Ajouter une classe", command=on_add_class_click)
    add_class_button.pack(side=tk.TOP, pady=(10, 5))

    # Bouton "Ajouter un vecteur"
    add_vector_button = tk.Button(root, text="Ajouter un vecteur", command=on_add_vector_click)
    add_vector_button.pack(side=tk.TOP, pady=(0, 5))

    # Bouton "Supprimer une classe"
    del_class_button = tk.Button(root, text="Supprimer une classe", command=on_del_class_click)
    del_class_button.pack(side=tk.TOP, pady=(0, 5))

    # Bouton "Enregistrer en JSON"
    save_as_json_button = tk.Button(root, text="Enregistrer en JSON", command=on_save_as_json_click)
    save_as_json_button.pack(side=tk.TOP, pady=(0, 5))

    # Bouton "Charger à partir d'un fichier JSON"
    load_as_json_button = tk.Button(root, text="Charger à partir d'un fichier JSON", command=on_load_as_json_click)
    load_as_json_button.pack(side=tk.TOP, pady=(0, 5))

    # Bouton "Afficher JSON"
    print_json_button = tk.Button(root, text="Afficher JSON", command=show_json)
    print_json_button.pack(side=tk.TOP, pady=(0, 5))

    # Bouton "Classer"
    classify_button = tk.Button(root, text="Classer", command=classify_main)
    classify_button.pack(side=tk.TOP, pady=(0, 10))

    # Lancer la boucle principale de la fenêtre
    root.mainloop()