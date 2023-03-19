
import numpy as np
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
    
     
