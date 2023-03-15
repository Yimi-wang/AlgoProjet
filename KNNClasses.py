import json
class KNNClasses:
    def __init__(self,description,data) -> None:
        self.description =description 
        '''
        [  
	{ 
		"label": "XXX_1",
		"vectors": [
			{ "key_1_1_1": float_1_1_1, "key_1_1_2":float_1_1_2,... },
			{ "key_1_2_1": float_1_2_1, "key_1_2_2":float_1_2_2,... },
			...
	},
	{ 
		"label": "XXX_2",
		"vectors": [
			{ "key_2_1_1": float_2_1_1, "key_2_1_2":float_2_1_2,... },
			{ "key_2_2_1": float_2_2_1, "key_2_2_2":float_2_2_2,... },
			...
	},
	...
]
    一个list，里面的元素是dict
        '''
        self.data=data

    def add_class(self,label:str,vectors:list) -> None: #测试通过
        add_element={"label":label,"vectors":vectors}
        self.data.append(add_element)

    def add_vector(self,label:str,vector:dict) -> None: #测试通过
        for element in self.data:
            if element['label']==label:
                element['vectors'].append(vector)
                print("L'ajout de données a été effectué avec succès.")
                return
        print("Échec de l'ajout de données.")
        
    def del_class(self,label:str)->None: #测试通过
        for element in self.data:
            if element['label']==label:
                self.data.remove(element)
                return
        print("Erreur,Label ne trouve pas.")

    def save_as_json(self,filename:str)->None:
        data_dict={'description':self.description,"data":self.data}
        try:
            with open(filename,'w') as f:
                json.dump(data_dict)
        except IOError:
            print("Erreur de ouvrir le fichier")
    
    def load_as_json(self,filename:str)->None:
        try:
            with open(filename) as f:
                data_json=json.load(f)
        except IOError:
            print("Erreur de ouvrir le fichier")
        self.description=data_json["description"]
        self.data=data_json["data"]
#测试用函数
    def printjson(self):#测试通过
        print("description: "+self.description)
        print("data: ")
        for item in self.data:
            print(item,end="\n")
    
  