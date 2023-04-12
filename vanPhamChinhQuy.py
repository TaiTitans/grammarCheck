import re
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
def checkGrammar():
    # Đọc dữ liệu từ file
    with open('grammar.txt', 'r') as file:
        grammar_data = file.read()

    # Biểu thức chính quy để kiểm tra văn phạm
    regex = r'^\s*([A-Za-z0-9]+)\s*->\s*((\s*([A-Za-z0-9]+)\s*)+\|?)*$'

    # Tách các văn phạm bằng dấu '---'
    grammars = grammar_data.split('---')
    # Kiểm tra từng văn phạm trong file
    result = ""
    # Kiểm tra từng văn phạm trong file
    for grammar in grammars:
        # Loại bỏ khoảng trắng thừa ở đầu và cuối mỗi văn phạm
        grammar = grammar.strip()

        # Kiểm tra xem văn phạm có hợp lệ hay không
        if re.match(regex, grammar):
            result += '=====Văn phạm=====\n'
            result += f'{grammar}\n'
            result += '=>Là văn phạm chính quy.\n'
            # Kiểm tra xem văn phạm là văn phạm trái hay văn phạm phải - hàm issuper() trả về char có kí tự in hoa không ( phải thì true - không phải thì false)
            if grammar[3].isupper():
                result += '==>Văn phạm trái.\n'
            elif grammar[-1].isupper():
                result += '==>Văn phạm phải.\n'
        else:
            result += '=====Văn phạm=====\n'
            result += f'{grammar}\n'
            result += "=>Không phải văn phạm chính quy.\n"

    # Hiển thị kết quả kiểm tra văn phạm trong cửa sổ đồ họa
    messagebox.showinfo("Kết quả kiểm tra văn phạm", result)

# Tạo cửa sổ đồ họa
root = tk.Tk()
root.title("Grammar Check")
root.geometry("500x400")

# Tạo nút Kiểm tra
btn_check = tk.Button(root, text="Kiểm tra", command=checkGrammar, font=("Helvetica", 16), fg='white', bg='green')
btn_check.pack(pady=20)

# Tạo widget nhãn hiển thị kết quả
result_label = tk.Label(root, text="", fg='black')
result_label.pack()

# Đọc và hiển thị hình ảnh check.png
image = Image.open("check.png")
image = image.resize((400, 300))  # Điều chỉnh kích thước hình ảnh
image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=image)
image_label.pack()



# Chạy vòng lặp
root.mainloop()