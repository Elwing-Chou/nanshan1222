import tkinter as tk

class MyFrame(tk.LabelFrame):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="BMI計算")
        self.l1 = tk.Label(self, text="體重:")
        self.l1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.e1 = tk.Entry(self)
        self.e1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.l2 = tk.Label(self, text="身高:")
        self.l2.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.e2 = tk.Entry(self)
        self.e2.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        # dic["欄位"]: 型態: dic, 操作: []
        # print(3): 型態: print(步驟型態), 操作: (3)
        self.b1 = tk.Button(self, text="計算", command=self.bmi)
        self.b1.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.result = tk.Label(self, text="點擊按鈕進行計算")
        self.result.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

    def bmi(self):
        weight = float(self.e1.get())
        height = float(self.e2.get())
        ans = weight / (height / 100) ** 2
        self.result["text"] = str(ans)

# 創造元件(父元件)
# 元件.排版(pack/grid/absolute)
window = tk.Tk()
window.geometry("500x500+250+250")
# 容器: Frame
f1 = MyFrame(window)
f1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20)
f2 = MyFrame(window)
f2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20)
window.mainloop()