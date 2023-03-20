from KNNClasses import KNNClasses
from TestVect import TestVect
from TextProcessing import TextProcessing
import tkinter as tk
import ast    
import tkinter as tk

def on_add_class_click():
    def on_submit_click():
        # 获取输入框中的值
        label_value = label_entry.get()
        vector_value = vector_entry.get()
        try:
            vector_list = ast.literal_eval(vector_value)
            print(vector_list)  # 输出: [1, 2, 3]
        except (ValueError, SyntaxError):
            print("用户输入的字符串格式不正确，请确保输入的是一个标准的 Python 列表格式。")
        # 在这里调用 add_class 方法，并传入输入的参数
        Kcl.add_class(label_value,vector_list)
        top_level.destroy()

    # 创建一个新的顶层窗口
    top_level = tk.Toplevel(root)

    # 创建第一个标签和输入框，并将其添加到顶层窗口
    label_label = tk.Label(top_level, text="Label:")
    label_label.grid(row=0, column=0)
    label_entry = tk.Entry(top_level)
    label_entry.grid(row=0, column=1)

    # 创建第二个标签和输入框，并将其添加到顶层窗口
    vector_label = tk.Label(top_level, text="Vector:")
    vector_label.grid(row=1, column=0)
    vector_entry = tk.Entry(top_level)
    vector_entry.grid(row=1, column=1)

    # 创建一个确定按钮，并将其添加到顶层窗口
    submit_button = tk.Button(top_level, text="Submit", command=on_submit_click)
    submit_button.grid(row=2, column=1)

def on_add_vector_click():
    def on_submit_click():
        # 获取输入框中的值
        label_value = label_entry.get()
        vector_value = vector_entry.get()
        try:
            vector_list = ast.literal_eval(vector_value)
            print(vector_list)  # 输出: [1, 2, 3]
        except (ValueError, SyntaxError):
            print("用户输入的字符串格式不正确，请确保输入的是一个标准的 Python 列表格式。")
        # 在这里调用 add_class 方法，并传入输入的参数
        Kcl.add_vector(label_value,vector_list)
        top_level.destroy()

    # 创建一个新的顶层窗口
    top_level = tk.Toplevel(root)

    # 创建第一个标签和输入框，并将其添加到顶层窗口
    label_label = tk.Label(top_level, text="Label:")
    label_label.grid(row=0, column=0)
    label_entry = tk.Entry(top_level)
    label_entry.grid(row=0, column=1)

    # 创建第二个标签和输入框，并将其添加到顶层窗口
    vector_label = tk.Label(top_level, text="Vector:")
    vector_label.grid(row=1, column=0)
    vector_entry = tk.Entry(top_level)
    vector_entry.grid(row=1, column=1)

    # 创建一个确定按钮，并将其添加到顶层窗口
    submit_button = tk.Button(top_level, text="Submit", command=on_submit_click)
    submit_button.grid(row=2, column=1)

def on_del_class_click():
    def on_submit_click():
        # 获取输入框中的值
        label_value = label_entry.get()
        # 在这里调用 add_class 方法，并传入输入的参数
        Kcl.del_class(label_value)
        top_level.destroy()

    # 创建一个新的顶层窗口
    top_level = tk.Toplevel(root)

    # 创建第一个标签和输入框，并将其添加到顶层窗口
    label_label = tk.Label(top_level, text="Label:")
    label_label.grid(row=0, column=0)
    label_entry = tk.Entry(top_level)
    label_entry.grid(row=0, column=1)

    # 创建一个确定按钮，并将其添加到顶层窗口
    submit_button = tk.Button(top_level, text="Submit", command=on_submit_click)
    submit_button.grid(row=1, column=1)

def on_save_as_json_click():
    def on_submit_click():
        # 获取输入框中的值
        filename_value = filename_entry.get()
        # 在这里调用 add_class 方法，并传入输入的参数
        Kcl.save_as_json(filename_value)
        top_level.destroy()

    # 创建一个新的顶层窗口
    top_level = tk.Toplevel(root)

    # 创建第一个标签和输入框，并将其添加到顶层窗口
    label_label = tk.Label(top_level, text="Filename:")
    label_label.grid(row=0, column=0)
    filename_entry = tk.Entry(top_level)
    filename_entry.grid(row=0, column=1)

    # 创建一个确定按钮，并将其添加到顶层窗口
    submit_button = tk.Button(top_level, text="Submit", command=on_submit_click)
    submit_button.grid(row=1, column=1)

def on_load_as_json_click():
    def on_submit_click():
        # 获取输入框中的值
        filename_value = filename_entry.get()
        # 在这里调用 add_class 方法，并传入输入的参数
        Kcl.load_as_json(filename_value)
        top_level.destroy()

    # 创建一个新的顶层窗口
    top_level = tk.Toplevel(root)

    # 创建第一个标签和输入框，并将其添加到顶层窗口
    label_label = tk.Label(top_level, text="Filename:")
    label_label.grid(row=0, column=0)
    filename_entry = tk.Entry(top_level)
    filename_entry.grid(row=0, column=1)

    # 创建一个确定按钮，并将其添加到顶层窗口
    submit_button = tk.Button(top_level, text="Submit", command=on_submit_click)
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

            close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
            close_button.pack(pady=(0, 10))
        # 获取输入框中的值
        Filename_value = Filename_entry.get()
        k_value = k_entry.get()
        k_value=int(k_value)
        Function_value=function_entry.get()
        
        # 在这里调用  方法，并传入输入的参数
        Kcl.changedata(TextProcessing.TestDocument_to_vector())
        vector_classify=TextProcessing.document_to_vector(Filename_value)
        print(vector_classify)
        match Function_value:
            case "":
                print("sim_cosinus")
                res=Kcl.classify(vector_classify,k_value)
            case "e":
                print("euclidean_distance")
                res=Kcl.classify(vector_classify,k_value,TestVect.euclidean_distance)
            case "m":
                print("manhattan_distance")
                res=Kcl.classify(vector_classify,k_value,TestVect.manhattan_distance)
            case "p":
                print("pearson_correlation_coefficient")
                res=Kcl.classify(vector_classify,k_value,TestVect.pearson_correlation_coefficient)
            case _:
                res="erreur,la valeur Function n'est pas correct"
        show_result_window(res)   
        top_level.destroy()


    # 创建一个新的顶层窗口
    top_level = tk.Toplevel(root)

    # 创建第一个标签和输入框，并将其添加到顶层窗口
    Filename_label = tk.Label(top_level, text="Filename:")
    Filename_label.grid(row=0, column=0)
    Filename_entry = tk.Entry(top_level)
    Filename_entry.grid(row=0, column=1)

    # 创建第二个标签和输入框，并将其添加到顶层窗口
    k_label = tk.Label(top_level, text="k:")
    k_label.grid(row=1, column=0)
    k_entry = tk.Entry(top_level)
    k_entry.grid(row=1, column=1)

    # 创建第三个标签和输入框，并将其添加到顶层窗口
    function_label = tk.Label(top_level, text="Function:")
    function_label.grid(row=2, column=0)
    function_entry = tk.Entry(top_level)
    function_entry.grid(row=2, column=1)
    # 创建一个确定按钮，并将其添加到顶层窗口
    submit_button = tk.Button(top_level, text="Submit", command=on_submit_click)
    submit_button.grid(row=3, column=1)

if __name__ == "__main__":
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
    # 创建一个主窗口
    root = tk.Tk()

    # add class 的按钮
    add_class_button = tk.Button(root, text="Add Class", command=on_add_class_click)
    add_class_button.pack(side=tk.TOP, pady=(10, 5))

    # add vector 的按钮
    add_vector_button = tk.Button(root, text="Add Vector", command=on_add_vector_click)
    add_vector_button.pack(side=tk.TOP, pady=(0, 5))

    # del class 的按钮
    del_class_button = tk.Button(root, text="Del Class", command=on_del_class_click)
    del_class_button.pack(side=tk.TOP, pady=(0, 5))

    # save as json 的按钮
    save_as_json_button = tk.Button(root, text="Save As Json", command=on_save_as_json_click)
    save_as_json_button.pack(side=tk.TOP, pady=(0, 5))

    # load as json 的按钮
    load_as_json_button = tk.Button(root, text="Load As Json", command=on_load_as_json_click)
    load_as_json_button.pack(side=tk.TOP, pady=(0, 5))

    # load as json 的按钮
    load_as_json_button = tk.Button(root, text="Load As Json", command=on_load_as_json_click)
    load_as_json_button.pack(side=tk.TOP, pady=(0, 5))

    # print json 的按钮
    print_json_button = tk.Button(root, text="Print Json", command=show_json)
    print_json_button.pack(side=tk.TOP, pady=(0, 5))

    #classify 的按钮
    classify_button = tk.Button(root, text="classify", command=classify_main)
    classify_button.pack(side=tk.TOP, pady=(0, 10))
    root.mainloop()