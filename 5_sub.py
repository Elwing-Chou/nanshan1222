# MAC/LINUX: ls -al
# Windows: dir(只有從終端機才看得到)
# shell=True: 字串
# shell=False: list, 第一個位置會是執行檔, 後面位置被當成參數
# ["ls", "-al", "rm", "-rf"], rm會被當成參數, 完全不執行
import subprocess

# subprocess.run("ls -al;rm -rf", shell=True)
# WIN:
# subprocess.run("dir", shell=True)
# f = open("log.txt", "w")
with open("log.txt", "w") as f, open("error.txt", "w") as e:
    result = subprocess.run(["ls", "-al"], stdout=f, stderr=e)
print(result)

with open("log2.txt", "w") as f, open("error2.txt", "w") as e:
    result = subprocess.run(["pip", "install", "jieba"], stdout=f, stderr=e)
print(result)

with open("log3.txt", "w") as f, open("error3.txt", "w") as e:
    result = subprocess.run(["python", "4_gui.py"], stdout=f, stderr=e)
print(result)
