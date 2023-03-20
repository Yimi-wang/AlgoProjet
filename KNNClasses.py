import json
import heapq
from TestVect import TestVect
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
        #self.test_vect = TestVect()

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

    def save_as_json(self,filename:str)->None: #测试通过
        data_dict={'description':self.description,"data":self.data}
        try:
            with open(filename,'w') as f:
                json.dump(data_dict,f)
        except IOError:
            print("Erreur de ouvrir le fichier")
    
    def load_as_json(self,filename:str)->None: # 测试通过
        try:
            with open(filename) as f:
                data_json=json.load(f)
        except IOError:
            print("Erreur de ouvrir le fichier")
        self.description=data_json["description"]
        self.data=data_json["data"]
        
    def classify(self, vector: dict, k: int, sim_func=None):
        if sim_func is None:
            sim_func = TestVect.sim_cosinus

        class_score = {}

        for class_data in self.data:
            res_diff_vect = []
            for vec_dans_class in class_data["vectors"]:
                res_diff_vect.append((vec_dans_class, sim_func(vector, vec_dans_class)))

            # 根据 sim_func 是否为距离度量来决定排序顺序
            reverse_order = sim_func not in [TestVect.euclidean_distance,TestVect.manhattan_distance]

            # 使用 heapq 获取前 k 个最相似（或距离最小）的向量
            if reverse_order:
                top_k = heapq.nlargest(k, res_diff_vect, key=lambda x: x[1])
            else:
                top_k = heapq.nsmallest(k, res_diff_vect, key=lambda x: x[1])

            # 计算平均相似度或距离并将其添加到类别分数字典中
            avg_similarity = sum([similarity for _, similarity in top_k]) / k
            class_score[class_data['label']] = avg_similarity

        # 使用 heapq 对类别分数进行排序
        sorted_class_score = heapq.nlargest(len(class_score), class_score.items(), key=lambda x: x[1] * (-1 if not reverse_order else 1))
        print(sorted_class_score)
        print(reverse_order)
        return sorted_class_score

#测试用函数
    def printjson(self):#测试通过
        res="description: "+self.description+"\n"
        res+="data: \n"
        for item in self.data:
            res+=str(item)+"\n"
        return res
        print("description: "+self.description)
        print("data: ")
        for item in self.data:
            print(item,end="\n")
    
  