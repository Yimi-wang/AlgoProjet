import re
import copy
import math
import os


class TextProcessing:
    french_stop_list={'gens', 'dont', 'hein', 'car', 'devers', 'onzième', 'vers', 'tel', 'voilà', 'après', 'hurrah', 'nombreuses', 'etant', 'doivent', 'cinq', 'effet', 'désormais', 'qui', 'fait', 'certain', 'maint', 'malgré', 'voient', 'certaine', 'tandis', 'tiens', 'vif', 'sous', 'certains', 'des', 'quarante', 'r', 'vôtre', 'à', 'onze', 'moins', 'quoi', 'revoici', 'plupart', 'vingt', 'essai', 'vive', 'dedans', 'diverses', 'brrr', 'nos', 'auront', 'valeur', 'leur', 'mêmes', 'n', 'premièrement', 'aux', 'ou', 'excepté', 'jusqu', 'dix-sept', 'bah', 'pan', 'ceux-là', 'neuf', 'par', 'près', 'vous-mêmes', 'vé', 'dix-neuf', 'lès', 'parmi', 'troisièmement', 'elles', 'durant', 'quel', 'tiennes', 'trente', 'tien', 'aucune', 'huit', 'chiche', 'tels', 'bon', 'combien', 'pfut', 'outre', 'deuxièmement', 'votre', 'cinquantième', 'celles', 'nous', 'vont', 'plutôt', 'autres', 'crac', 'différent', 'celui-là', 'autre', 'sixième', 'ayant', 'quelconque', 'allô', 'passé', 'dixième', 'aura', 'étaient', 'nôtre', 'j', 'comme', 'lesquelles', 'miennes', 'vu', 'maintenant', 'g', 'septième', 'personne', 'soi', 'chacun', 'ho', 'miens', 'fi', 'diverse', 'devant', 'pendant', 'telles', 'celle-là', 'ai', 'quinze', 'avais', 'na', 'voici', 'force', 'sinon', 'pièce', 'différents', 'lesquels', 'particulier', 'jusque', 'q', 'tellement', 'ici', 'chaque', 'qu', 'etc', 'un', 'celles-ci', 'avaient', 'il', 'toc', 'ceux', 'rien', 'lequel', 'toi', 'tout', 'concernant', 'tu', 'étions', 'dire', 'hum', 'treize', 'pas', 'plus', 'quant-à-soi', 'droite', 'lui', 'juste', 'devrait', 'olé', 'es', 'nommés', 'plouf', 'vous', 'té', 'je', 'au', 'début', 'cent', 'contre', 'dans', 'quatorze', 'fais', 'aie', 'tes', 'six', 'ne', 'mes', 'nôtres', 'elle', 'd', 'trop', 'sur', "aujourd'hui", 'va', 'avec', 'encore', 'peux', 'boum', 'quelles', 'façon', 'desquelles', 'sienne', 'tant', 'dring', 'et', 'que', 'merci', 'donc', 'notre', 'ollé', 'vais', 'ceux-ci', 'a', 'nous-mêmes', 'premier', 'avoir', 'comment', 'stop', 'faites', 'ci', 'ouf', 'aucun', 'nombreux', 'sans', 'deux', 'aujourd', 'troisième', 'différentes', 'floc', 'ceci', 'via', 'quatre', 'p', 'étais', 'en', 'pour', 'pff', 'w', 'ès', 'cher', 'hormis', 'x', 'clac', 'sien', 'devra', 'bien', 'moi-même', 'ses', 'ouias', 'cela', 'environ', 'seulement', 'alors', 'partant', 'toutes', 'état', 'auquel', 'divers', 'vivat', 'moyennant', 'ainsi', 'etre', 'quant', 'si', 'celui', 'chez', 'psitt', 'personnes', 'las', 'k', 'pfft', 'son', 'hue', 'hop', 'â', 'de', 'pourquoi', 'desquels', 'proche', 'suis', 'trois', 'cinquième', 'b', 'dès', 'fois', 'ta', 'vives', 'non', 'pif', 'beaucoup', 'flac', 'où', 'toute', 'allaient', 'différente', 'tsouin', 'auxquelles', 'quiconque', 'f', 'elle-même', 'tsoin', 'da', 'voie', 'leurs', 'sauf', 'quelque', 'hep', 'hou', 'houp', 'on', 'été', 'huitième', 'tic', 'douzième', 'sapristi', 'quoique', 'siennes', 'doit', 'mine', 'l', 'entre', 'soixante', 'debout', 'uns', 'avait', 'le', 'la', 'quand', 'ouste', 'surtout', 'aussi', "quelqu'un", 'assez', 'mille', 'toujours', 'compris', 'tienne', 'derrière', 'ce', 'avant', 'mienne', 'chut', 'dix-huit', 'très', 'tous', 'cinquante', 'mais', 'mien', 'mince', 'parce', 'est', 's', 'vôtres', 'hélas', 'sacrebleu', 'chères', 'soyez', 'quatrièmement', 'bravo', 'mon', 'ohé', 'touchant', 't', 'elles-mêmes', 'particulière', 'ton', 'oh', 'hui', 'paf', 'haut', 'vifs', 'u', 'néanmoins', 'douze', 'telle', 'longtemps', 'allons', 'faisant', 'cet', 'laquelle', 'puisque', 'quelle', 'c', 'seize', 'moi', 'oust', 'sa', 'z', 'depuis', 'chers', 'tac', 'être', 'aucuns', 'ore', 'euh', 'plusieurs', 'même', 'chère', 'certes', 'neuvième', 'deuxième', 'faisaient', 'ô', 'envers', 'ils', 'peu', 'seront', 'sujet', 'étant', 'lorsque', 'peut', 'attendu', 'dessus', 'toi-même', 'nouveaux', 'eh', 'celui-ci', 'ça', 'sera', 'clic', 'me', 'quatre-vingt', 'ont', 'hors', 'parole', 'hi', 'eu', 'duquel', 'ma', 'sept', 'selon', 'vas', 'delà', 'hé', 'quels', 'o', 'zut', 'i', 'abord', 'm', 'siens', 'unes', 'cinquantaine', 'revoilà', 'vos', 'dos', 'celle-ci', 'soit', 'celle', 'sont', 'se', 'e', 'cependant', 'mot', 'dehors', 'auxquels', 'du', 'quatrième', 'dix', 'certaines', 'y', 'ah', 'soi-même', 'feront', 'vlan', 'afin', 'quanta', 'te', 'peuvent', 'celles-là', 'pouah', 'hem', 'première', 'suivant', 'couic', 'ces', 'tenant', 'allo', 'dessous', 'lui-même', 'ha', 'particulièrement', 'v', 'font', 'était', 'eux', 'nul', 'une', 'les', 'bigre', 'là', 'h', 'ni', 'o|', 'eux-mêmes', 'plein', 'quelques', 'holà', 'cette', 'importe'}
    tok_grm=re.compile(r"""
        (?:etc.|p.ex.|cf.|M.)|
        \w+(?=(?:-(?:je|tu|ils?|elles?|nous|vous|leur|lui|les?|ce|t-|même|ci|là)))|
        [\w\-]+'?| # peut-être
        .
        """,re.X)
    @staticmethod
    def tokenize(text, tok_grm):
        return tok_grm.findall(text)

    @staticmethod
    def vectorise(tokens):
        token_freq = {}
        for token in tokens:
            token_freq[token] = token_freq.get(token, 0) + 1
        return token_freq

    @staticmethod
    def read_texts(file_names: list):
        data = []
        tok_grm = re.compile(r"""
                (?:etc.|p.ex.|cf.|M.)|
                \w+(?=(?:-(?:je|tu|ils?|elles?|nous|vous|leur|lui|les?|ce|t-|même|ci|là)))|
                [\w\-]+'?| # peut-être
                .
            """, re.X)

        for file_name in file_names:
            with open(file_name, mode="r", encoding="utf8") as input_file:
                tokens = [tok for line in input_file for tok in TextProcessing.tokenize(line.strip(), tok_grm)]
                vector=[]
                vector.append(TextProcessing.vectorise(tokens))
                data.append({'label': os.path.basename(file_name), 'vectors': vector})

        return data

    @staticmethod
    def filtrage(stoplist: set, documents, non_hapax):
        documents_filtre = []

        for document in documents:
            document_filtre = {"label": document["label"]}
            ###
            tokens = document["vectors"][0]
            ###
            tokens_filtre = {token: freq for token, freq in tokens.items()
                             if token.lower() not in stoplist and (not non_hapax or freq > 1)}
            document_filtre["vectors"] = []
            document_filtre["vectors"].append(tokens_filtre)
            documents_filtre.append(document_filtre)

        return documents_filtre

    @staticmethod
    def tf_idf(documents: list) -> list:
        documents_new = copy.deepcopy(documents)
        mots = {word for doc in documents for word in doc["vectors"][0]}
        freq_doc = {}

        for word in mots:
            freq_doc[word] = sum(1 for doc in documents if word in doc["vectors"][0])

        for doc in documents_new:
            for word in doc["vectors"][0]:
                doc["vectors"][0][word] /= math.log(1 + freq_doc[word])

        return documents_new
    
    @classmethod
    def TestDocument_to_vector(cls)->list:
        filename=[ "./TestDocuments"+"/"+f for f in os.listdir('./TestDocuments') if f[0]!="." and not os.path.isdir('./TestDocuments'+"/"+f)]
        texts=cls.read_texts(filename)
        doc_filtres=cls.filtrage(cls.french_stop_list, texts, non_hapax=False)
        doc_filtres_tfidf=cls.tf_idf(doc_filtres)
        return doc_filtres_tfidf

    @classmethod
    def document_to_vector(cls,filename:str)->list:
        filenamelist=[]
        filenamelist.append(filename)
        texts=cls.read_texts(filenamelist)
        doc_filtres=cls.filtrage(cls.french_stop_list, texts, non_hapax=False)
        doc_filtres_tfidf=cls.tf_idf(doc_filtres)
        return doc_filtres_tfidf
        