import tkinter as tk

def bmi():
    global e1, e2, result
    weight = float(e1.get())
    height = float(e2.get())
    ans = weight / (height / 100) ** 2
    result["text"] = str(ans)

# 創造元件(父元件)
# 元件.排版(pack/grid/absolute)
window = tk.Tk()
window.geometry("500x500+250+250")
# 容器: Frame
f1 = tk.Frame(window)
f1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
l1 = tk.Label(f1, text="體重:")
l1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
e1 = tk.Entry(f1)
e1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
l2 = tk.Label(f1, text="身高:")
l2.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
e2 = tk.Entry(f1)
e2.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
# dic["欄位"]: 型態: dic, 操作: []
# print(3): 型態: print(步驟型態), 操作: (3)
b1 = tk.Button(f1, text="計算", command=bmi)
b1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
result = tk.Label(f1, text="點擊按鈕進行計算")
result.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
window.mainloop()