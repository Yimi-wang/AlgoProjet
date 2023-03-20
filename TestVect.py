import math
import numpy as np
import re
import copy
class TestVect:    
    def sim_cosinus(vec1: dict, vec2: dict) -> float:
        keys = set(vec1.keys()) & set(vec2.keys())  # 获取共同的键

        if not keys:
            return 0.0

        vec1_values = np.array([vec1[key] for key in keys])
        vec2_values = np.array([vec2[key] for key in keys])

        dot_product = np.dot(vec1_values, vec2_values)
        magnitude_vec1 = np.linalg.norm(vec1_values)
        magnitude_vec2 = np.linalg.norm(vec2_values)

        if magnitude_vec1 == 0 or magnitude_vec2 == 0:
            return 0.0

        cosine_sim = dot_product / (magnitude_vec1 * magnitude_vec2)
        return cosine_sim
    
    #欧氏距离
    def euclidean_distance(vec1: dict, vec2: dict)->float:
        distance = 0

        # 遍历两个字典的所有键
        for key in set(vec1.keys()).union(vec2.keys()):
            value1 = vec1.get(key, 0)  # 如果键不存在于 dict1 中，返回 0
            value2 = vec2.get(key, 0)  # 如果键不存在于 dict2 中，返回 0

            distance += (value1 - value2) ** 2

        return math.sqrt(distance)

    #曼哈顿距离
    def manhattan_distance(vec1: dict, vec2: dict)->float:
        distance = 0

        # 遍历两个字典的所有键
        for key in set(vec1.keys()).union(vec2.keys()):
            value1 = vec1.get(key, 0)  # 如果键不存在于 dict1 中，返回 0
            value2 = vec2.get(key, 0)  # 如果键不存在于 dict2 中，返回 0

            distance += abs(value1 - value2)

        return distance
    
    def pearson_correlation_coefficient(vect1, vect2):
        keys = set(vect1.keys()) & set(vect2.keys())
        values1 = [vect1[key] for key in keys]
        values2 = [vect2[key] for key in keys]
        
        if len(values1) == 0 or len(values2) == 0:
            raise ValueError("没用公共键")
        
        n = len(values1)
        sum1 = sum(values1)
        sum2 = sum(values2)
        
        sum1_sq = sum([pow(v, 2) for v in values1])
        sum2_sq = sum([pow(v, 2) for v in values2])
        
        prod_sum = sum([values1[i] * values2[i] for i in range(n)])
        
        num = prod_sum - (sum1 * sum2 / n)
        den = ((sum1_sq - pow(sum1, 2) / n) * (sum2_sq - pow(sum2, 2) / n)) ** 0.5
        
        if den == 0:
            return 0
        
        return num / den
    
