from KNNClasses import KNNClasses
class test:    
    if __name__ == "__main__":
        print("123")
        description="C'est un test"
        data=[
            {
            "label":"test_1",
            "vectors": [
			{ "key_1_1_1": 1.0, "key_1_1_2":2.0 },
			{ "key_1_2_1": 3.0, "key_1_2_2":3.5 },
            { "key_1_3_1": 2.5, "key_1_3_2":2.6 }
            ]
            },
            {
            "label":"test_2",
            "vectors": [
			{ "key_2_1_1": 5.0, "key_2_1_2":3.0 },
			{ "key_2_2_1": 8.0, "key_2_2_2":7.5 },
            { "key_2_3_1": 2.7, "key_2_3_2":4.6 }
            ]
            },
            {
            "label":"test_3",
            "vectors": [
			{ "key_3_1_1": 1.0, "key_3_1_2":1.58 },
			{ "key_3_2_1": 8.2, "key_3_2_2":2.5 },
            { "key_3_3_1": 9.5, "key_3_3_2":11.58 }
            ]
            }
        ]
        Kcl=KNNClasses(description,data)
        Kcl.printjson() 
        Kcl.save_as_json("01.json")
        label="test_4"
        vectors=[
			{ "key_4_1_1": 9.0, "key_4_1_2":9.0 },
			{ "key_4_2_1": 9.0, "key_4_2_2":9.5 },
            { "key_4_3_1": 9.7, "key_4_3_2":9.6 }
            ]
        Kcl.add_class(label,vectors)
        Kcl.add_vector(label,{"key_5_3_1": 11.1, "key_5_3_2":1.11})
        Kcl.load_as_json("01.json")
        Kcl.printjson()