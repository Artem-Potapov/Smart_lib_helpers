import json, os, tkinter as tk

app = tk.Tk()
app.geometry('350x400')
appframe = tk.Frame(app)
author: str = ''
name: str = ''
genre: str = ''
age: str = ''
rate: int = 5
img: str = ''
download: str = ''
    # Интерфейс

info = tk.Label(appframe, justify=tk.CENTER, text='Привет! Это постройка авторов!')
authortxt = tk.Label(appframe, text='Введи автора)')
authoretr = tk.Entry(appframe)
nmetxt = tk.Label(appframe, text='Введи имя книги)')
nmeetr = tk.Entry(appframe)
gnrtxt = tk.Label(appframe, text='Жанр:')
gnretr = tk.Entry(appframe, width=400)
agetxt = tk.Label(appframe, text='Возраст')
ageetr = tk.Entry(appframe)
rtetxt = tk.Label(appframe, text='Рейтинг')
rteetr = tk.Entry(appframe)
imgtxt = tk.Label(appframe, text='Ссылка на изображение')
imgetr = tk.Entry(appframe)
dldtxt = tk.Label(appframe, text='Ссылка на загрузку')
dldetr = tk.Entry(appframe)


# Код
def getall():
    global author, name, genre, age, rate, img, download
    author = authoretr.get()
    name = nmeetr.get()
    genre = gnretr.get()
    age = ageetr.get()
    rate = rteetr.get()
    img = imgetr.get()
    download = dldetr.get()
    noParam=False
    mass: dict = {"author": author,
                   "name": name,
                   "age": age,
                   "rate": rate,
                   "genre": genre,
                   "img": img,
                   "download": download}
    for ma in mass:
        if mass.get(ma) == '':
            noParam = True
        else:
            pass
    if noParam:
        pass
    else:
        app.quit()
    file = open("C:\\Users\\potap\\PycharmProjects\\Smart_library\\boos.json", "r+", encoding="UTF-8")
    file_loaded = json.load(file)
    file_loaded.append(mass)

    file_loaded = json.dumps(file_loaded)
    file.close()
    os.remove("C:\\Users\\potap\\PycharmProjects\\Smart_library\\boos.json")
    file = open("C:\\Users\\potap\\PycharmProjects\\Smart_library\\boos.json", "w", encoding="UTF-8")
    file.write(file_loaded)
    file.close()
    print(mass)


open("C:\\Users\\potap\\3D Objects\\scale_1200.jpg")
enter = tk.Button(appframe, text='Готовченко', command=getall)
# Пак-раздел
info.pack()
authortxt.pack()
authoretr.pack(fill=tk.BOTH)
nmetxt.pack()
nmeetr.pack(fill=tk.BOTH)
gnrtxt.pack()
gnretr.pack()
agetxt.pack()
ageetr.pack(fill=tk.BOTH)
rtetxt.pack()
rteetr.pack(fill=tk.BOTH)
imgtxt.pack()
imgetr.pack(fill=tk.BOTH)
dldtxt.pack()
dldetr.pack(fill=tk.BOTH)
enter.pack()
appframe.pack()
app.mainloop()

mass = dict = {"author": author,
               "name": name,
               "age": age,
               "rate": rate,
               "genre": genre,
               "img": img,
               "download": download}


