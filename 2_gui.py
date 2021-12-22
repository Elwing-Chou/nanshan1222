import tkinter as tk

# 創造元件(父元件)
# 元件.排版(pack/grid/absolute)
window = tk.Tk()
window.geometry("500x500+250+250")
# 容器: Frame
f1 = tk.Frame(window)
f1.pack()
l1 = tk.Label(f1, text="體重:")
l1.pack()
e1 = tk.Entry(f1)
e1.pack()
l2 = tk.Label(f1, text="身高:")
l2.pack()
e2 = tk.Entry(f1)
e2.pack()
b1 = tk.Button(f1, text="計算")
b1.pack()
result = tk.Label(f1, text="點擊按鈕進行計算")
result.pack()
window.mainloop()