import re
import copy
import math
import os
"""
class TextProcessing:
    def tokenize(text, tok_grm):
        Tokenise le texte en utilisant l'expression régulière fournie.

        Arguments :
            - text : Le texte à tokeniser (str)
            - tok_grm : L'expression régulière à utiliser pour la tokenisation (re.Pattern)

        Retour :
            - tokens : Une liste de tokens extraits du texte (list[str])

    def vectorise(tokens):
        Crée un dictionnaire de fréquences pour les tokens donnés.

        Arguments :
            - tokens : Liste de tokens à vectoriser (list[str])

        Retour :
            - token_freq : Dictionnaire des fréquences des tokens (dict)

    def read_texts(dossier_names: list):
        Lit les textes à partir d'une liste de noms de dossiers.

        Arguments :
            - dossier_names : Liste des noms de dossiers contenant les textes (list[str])

        Retour :
            - data : Liste de dictionnaires contenant les labels et les vecteurs des textes (list[dict])

    def read_text(dossier_name: str):

        Lit un fichier texte et retourne un dictionnaire contenant le label et les vecteurs du texte.

        Arguments :
            - dossier_name : Le nom du dossier contenant le texte (str)

        Retour :
            - data : Liste de dictionnaires contenant le label et les vecteurs du texte (list[dict])


    def filtrage(stoplist: set, documents, non_hapax):

        Filtrer les documents en fonction de la stoplist et de la fréquence des mots (si non_hapax).

        Arguments :
            - stoplist : Liste des mots à ignorer (set[str])
            - documents : Liste des documents à filtrer (list[dict])
            - non_hapax : Si True, conserver uniquement les mots dont la fréquence est supérieure à 1 (bool)

        Retour :
            - documents_filtre : Liste des documents filtrés (list[dict])
        

    
    def tf_idf(documents: list) -> list:
    
        Calcule les scores tf-idf pour les documents donnés.

        Arguments :
            - documents : Liste des documents pour lesquels calculer les scores tf-idf (list[dict])

        Retour :
            - documents_new : Liste des documents avec les scores tf-idf (list[dict])
        

    
    def TestDocument_to_vector(cls) -> list:
        
        Lit, filtre et calcule les scores tf-idf pour les documents dans le répertoire "./TestDocuments".

        Retour :
            - doc_filtres_tfidf : Liste des documents filtrés avec les scores tf-idf (list[dict])
        

    
    def document_to_vector(cls, filename: str) -> list:
        
        Lit, filtre et calcule les scores tf-idf pour un document spécifique.

        Arguments :
            - filename : Le nom du fichier contenant le document (str)

        Retour :
            - vecteurs
"""

class TextProcessing:
    french_stop_list={' ',',','.','?','-','—','gens', 'dont', 'hein', 'car', 'devers', 'onzième', 'vers', 'tel', 'voilà', 'après', 'hurrah', 'nombreuses', 'etant', 'doivent', 'cinq', 'effet', 'désormais', 'qui', 'fait', 'certain', 'maint', 'malgré', 'voient', 'certaine', 'tandis', 'tiens', 'vif', 'sous', 'certains', 'des', 'quarante', 'r', 'vôtre', 'à', 'onze', 'moins', 'quoi', 'revoici', 'plupart', 'vingt', 'essai', 'vive', 'dedans', 'diverses', 'brrr', 'nos', 'auront', 'valeur', 'leur', 'mêmes', 'n', 'premièrement', 'aux', 'ou', 'excepté', 'jusqu', 'dix-sept', 'bah', 'pan', 'ceux-là', 'neuf', 'par', 'près', 'vous-mêmes', 'vé', 'dix-neuf', 'lès', 'parmi', 'troisièmement', 'elles', 'durant', 'quel', 'tiennes', 'trente', 'tien', 'aucune', 'huit', 'chiche', 'tels', 'bon', 'combien', 'pfut', 'outre', 'deuxièmement', 'votre', 'cinquantième', 'celles', 'nous', 'vont', 'plutôt', 'autres', 'crac', 'différent', 'celui-là', 'autre', 'sixième', 'ayant', 'quelconque', 'allô', 'passé', 'dixième', 'aura', 'étaient', 'nôtre', 'j', 'comme', 'lesquelles', 'miennes', 'vu', 'maintenant', 'g', 'septième', 'personne', 'soi', 'chacun', 'ho', 'miens', 'fi', 'diverse', 'devant', 'pendant', 'telles', 'celle-là', 'ai', 'quinze', 'avais', 'na', 'voici', 'force', 'sinon', 'pièce', 'différents', 'lesquels', 'particulier', 'jusque', 'q', 'tellement', 'ici', 'chaque', 'qu', 'etc', 'un', 'celles-ci', 'avaient', 'il', 'toc', 'ceux', 'rien', 'lequel', 'toi', 'tout', 'concernant', 'tu', 'étions', 'dire', 'hum', 'treize', 'pas', 'plus', 'quant-à-soi', 'droite', 'lui', 'juste', 'devrait', 'olé', 'es', 'nommés', 'plouf', 'vous', 'té', 'je', 'au', 'début', 'cent', 'contre', 'dans', 'quatorze', 'fais', 'aie', 'tes', 'six', 'ne', 'mes', 'nôtres', 'elle', 'd', 'trop', 'sur', "aujourd'hui", 'va', 'avec', 'encore', 'peux', 'boum', 'quelles', 'façon', 'desquelles', 'sienne', 'tant', 'dring', 'et', 'que', 'merci', 'donc', 'notre', 'ollé', 'vais', 'ceux-ci', 'a', 'nous-mêmes', 'premier', 'avoir', 'comment', 'stop', 'faites', 'ci', 'ouf', 'aucun', 'nombreux', 'sans', 'deux', 'aujourd', 'troisième', 'différentes', 'floc', 'ceci', 'via', 'quatre', 'p', 'étais', 'en', 'pour', 'pff', 'w', 'ès', 'cher', 'hormis', 'x', 'clac', 'sien', 'devra', 'bien', 'moi-même', 'ses', 'ouias', 'cela', 'environ', 'seulement', 'alors', 'partant', 'toutes', 'état', 'auquel', 'divers', 'vivat', 'moyennant', 'ainsi', 'etre', 'quant', 'si', 'celui', 'chez', 'psitt', 'personnes', 'las', 'k', 'pfft', 'son', 'hue', 'hop', 'â', 'de', 'pourquoi', 'desquels', 'proche', 'suis', 'trois', 'cinquième', 'b', 'dès', 'fois', 'ta', 'vives', 'non', 'pif', 'beaucoup', 'flac', 'où', 'toute', 'allaient', 'différente', 'tsouin', 'auxquelles', 'quiconque', 'f', 'elle-même', 'tsoin', 'da', 'voie', 'leurs', 'sauf', 'quelque', 'hep', 'hou', 'houp', 'on', 'été', 'huitième', 'tic', 'douzième', 'sapristi', 'quoique', 'siennes', 'doit', 'mine', 'l', 'entre', 'soixante', 'debout', 'uns', 'avait', 'le', 'la', 'quand', 'ouste', 'surtout', 'aussi', "quelqu'un", 'assez', 'mille', 'toujours', 'compris', 'tienne', 'derrière', 'ce', 'avant', 'mienne', 'chut', 'dix-huit', 'très', 'tous', 'cinquante', 'mais', 'mien', 'mince', 'parce', 'est', 's', 'vôtres', 'hélas', 'sacrebleu', 'chères', 'soyez', 'quatrièmement', 'bravo', 'mon', 'ohé', 'touchant', 't', 'elles-mêmes', 'particulière', 'ton', 'oh', 'hui', 'paf', 'haut', 'vifs', 'u', 'néanmoins', 'douze', 'telle', 'longtemps', 'allons', 'faisant', 'cet', 'laquelle', 'puisque', 'quelle', 'c', 'seize', 'moi', 'oust', 'sa', 'z', 'depuis', 'chers', 'tac', 'être', 'aucuns', 'ore', 'euh', 'plusieurs', 'même', 'chère', 'certes', 'neuvième', 'deuxième', 'faisaient', 'ô', 'envers', 'ils', 'peu', 'seront', 'sujet', 'étant', 'lorsque', 'peut', 'attendu', 'dessus', 'toi-même', 'nouveaux', 'eh', 'celui-ci', 'ça', 'sera', 'clic', 'me', 'quatre-vingt', 'ont', 'hors', 'parole', 'hi', 'eu', 'duquel', 'ma', 'sept', 'selon', 'vas', 'delà', 'hé', 'quels', 'o', 'zut', 'i', 'abord', 'm', 'siens', 'unes', 'cinquantaine', 'revoilà', 'vos', 'dos', 'celle-ci', 'soit', 'celle', 'sont', 'se', 'e', 'cependant', 'mot', 'dehors', 'auxquels', 'du', 'quatrième', 'dix', 'certaines', 'y', 'ah', 'soi-même', 'feront', 'vlan', 'afin', 'quanta', 'te', 'peuvent', 'celles-là', 'pouah', 'hem', 'première', 'suivant', 'couic', 'ces', 'tenant', 'allo', 'dessous', 'lui-même', 'ha', 'particulièrement', 'v', 'font', 'était', 'eux', 'nul', 'une', 'les', 'bigre', 'là', 'h', 'ni', 'o|', 'eux-mêmes', 'plein', 'quelques', 'holà', 'cette', 'importe'}
    tok_grm=re.compile(r"""
        (?:etc.|p.ex.|cf.|M.)|
        \w+(?=(?:-(?:je|tu|ils?|elles?|nous|vous|leur|lui|les?|ce|t-|même|ci|là)))|
        [\w\-]+'?| # peut-être
        .
        """,re.X)
    @staticmethod
    def tokenize(text, tok_grm):
    # Tokenisation du texte en utilisant l'expression régulière fournie
        return tok_grm.findall(text)

    @staticmethod
    def vectorise(tokens):
        # Initialisation d'un dictionnaire pour stocker les fréquences des tokens
        token_freq = {}
        
        # Parcours des tokens et mise à jour de leurs fréquences dans le dictionnaire
        for token in tokens:
            token_freq[token] = token_freq.get(token, 0) + 1
            
        # Retour du dictionnaire des fréquences des tokens
        return token_freq

    @staticmethod
    def read_texts(dossier_names: list):
        # Initialisation de la liste de données à retourner
        data = []
        
        # Définition de l'expression régulière pour la tokenisation
        tok_grm = re.compile(r"""
                (?:etc.|p.ex.|cf.|M.)|
                \w+(?=(?:-(?:je|tu|ils?|elles?|nous|vous|leur|lui|les?|ce|t-|même|ci|là)))|
                [\w\-]+'?| # peut-être
                .
            """, re.X)

        # Parcours des noms de dossiers
        for dossier_name in dossier_names:
            # Liste des noms de fichiers dans le dossier courant
            filenames = [f.name for f in os.scandir("./TestDocuments/"+dossier_name) if f.is_file()]
            
            # Initialisation de la liste des vecteurs
            vector=[]
            
            # Parcours des noms de fichiers
            for file_name in filenames:
                # Ouverture et lecture du fichier
                with open("./TestDocuments/"+dossier_name+"/"+file_name, mode="r", encoding="utf8") as input_file:
                    # Tokenisation de chaque ligne du fichier et ajout à la liste des tokens
                    tokens = [tok for line in input_file for tok in TextProcessing.tokenize(line.strip(), tok_grm)]
                    
                    # Vectorisation des tokens et ajout à la liste des vecteurs
                    vector.append(TextProcessing.vectorise(tokens))
                    
            # Ajout des données du dossier (étiquette et vecteurs) à la liste de données
            data.append({'label': dossier_name, 'vectors': vector})

        # Retour de la liste de données
        return data
    
    @staticmethod
    def read_text(dossier_name: str):
        # Initialisation de la liste des données
        data = []
        
        # Compilation du modèle de regex pour la tokenisation
        tok_grm = re.compile(r"""
                (?:etc.|p.ex.|cf.|M.)|
                \w+(?=(?:-(?:je|tu|ils?|elles?|nous|vous|leur|lui|les?|ce|t-|même|ci|là)))|
                [\w\-]+'?|
                .
            """, re.X)

        # Ouverture et lecture du fichier texte
        with open(dossier_name, mode="r", encoding="utf8") as input_file:
            # Tokenisation de chaque ligne du fichier texte
            tokens = [tok for line in input_file for tok in TextProcessing.tokenize(line.strip(), tok_grm)]
            
            # Création du vecteur à partir des tokens
            vector=[]
            vector.append(TextProcessing.vectorise(tokens))
            
            # Ajout des données (label et vecteurs) à la liste 'data'
            data.append({'label': dossier_name, 'vectors': vector})
        
        # Retourne la liste des données
        return data

    @staticmethod
    def filtrage(stoplist: set, documents, non_hapax):
        # Initialisation de la liste des documents filtrés
        documents_filtre = []

        # Filtrage des documents
        for document in documents:
            # Création d'un nouveau document avec le label du document original
            document_filtre = {"label": document["label"]}
            
            # Filtrage des tokens et ajout au nouveau document
            document_filtre["vectors"] = []
            for tokens in document["vectors"]:
                # Filtrage des tokens en fonction de la stoplist et de la fréquence des mots (si non_hapax)
                tokens_filtre = {token: freq for token, freq in tokens.items()
                            if token.lower() not in stoplist and (not non_hapax or freq > 1)}
                document_filtre["vectors"].append(tokens_filtre)
            
            # Ajout du document filtré à la liste des documents filtrés
            documents_filtre.append(document_filtre)             
        
        # Retourne la liste des documents filtrés
        return documents_filtre

    @staticmethod
    def tf_idf(documents: list) -> list:
        # Création d'une copie profonde des documents
        documents_new = copy.deepcopy(documents)
        
        # Récupération de l'ensemble des mots présents dans les documents
        mots = {word for doc in documents for vector in doc["vectors"] for word in vector}
        
        # Calcul de la fréquence des documents pour chaque mot
        freq_doc = {}
        for word in mots:
            freq_doc[word] = sum(1 for doc in documents for vector in doc["vectors"] if word in vector)

        # Calcul du score tf-idf pour chaque mot dans chaque document
        for doc in documents_new:
            for vector in doc["vectors"]:
                for word in vector:
                    vector[word]/= math.log(1 + freq_doc[word])
        
        # Retourne la liste des documents avec les scores tf-idf
        return documents_new

    @classmethod
    def TestDocument_to_vector(cls)->list:
        # Récupération des noms de dossiers dans le répertoire "./TestDocuments"
        dossiername=[f.name for f in os.scandir("./TestDocuments") if f.is_dir()]
        # Lecture des textes à partir des noms de dossiers récupérés
        texts=cls.read_texts(dossiername)
        
        # Filtrage des documents en utilisant la stoplist française et en conservant tous les mots (non_hapax=False)
        doc_filtres=cls.filtrage(cls.french_stop_list, texts, non_hapax=False)
        
        # Calcul des scores tf-idf pour les documents filtrés
        doc_filtres_tfidf=cls.tf_idf(doc_filtres)
        
        # Retourne les documents filtrés avec les scores tf-idf
        return doc_filtres_tfidf
    
    @classmethod
    def document_to_vector(cls,filename:str)->list:
        # Lecture du texte à partir du nom de fichier donné
        texts=cls.read_text(filename)
        
        # Filtrage des documents en utilisant la stoplist française et en conservant tous les mots (non_hapax=False)
        doc_filtres=cls.filtrage(cls.french_stop_list, texts, non_hapax=False)
        
        # Calcul des scores tf-idf pour les documents filtrés
        doc_filtres_tfidf=cls.tf_idf(doc_filtres)
        
        # Retourne le premier vecteur du premier document filtré avec les scores tf-idf
        return doc_filtres_tfidf[0]["vectors"][0]