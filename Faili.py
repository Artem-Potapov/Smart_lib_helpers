import tkinter as tk, json, os

file = open("C:\\Users\\potap\\PycharmProjects\\Smart_library\\boos.json", "r+", encoding='UTF-8')
file_parsed = json.load(file)
window = tk.Tk()
a = 8


def isint(self: int or float or str):
    if str(self).find == -1:
        return True
    else:
        return False


def addon():
    app = tk.Toplevel()
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
        noParam = False
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


def onselect(event):
    selected = (listNodes.curselection()[0])

    def find_info(selected: int) -> list:
        info = []
        for i in file_parsed[selected]:
            info.append(file_parsed[selected].get(i))
        return info

    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)

    info = find_info(selected=selected)
    listSelection.delete(0, tk.END)
    listSelection.insert(tk.END, "Имя: " + str(info[0]))
    listSelection.insert(tk.END, "Автор: " + str(info[1]))
    listSelection.insert(tk.END, "Жанр: " + str(info[5]))
    listSelection.insert(tk.END, "Возраст: " + str(info[6]))
    listSelection.insert(tk.END, "Рейтинг: " + str(info[3]))
    listSelection.insert(tk.END, "Изображение: " + str(info[2]))
    listSelection.insert(tk.END, "Скачать: " + str(info[4]))


def onChange():
    file.close()
    selected = listNodes.curselection()[0]
    file_to_parse = file_parsed[selected]
    listNodes.delete(0, "end")
    file_parsed.remove(file_to_parse)
    os.remove("C:\\Users\\potap\\PycharmProjects\\Smart_library\\boos.json")
    new_file = open("C:\\Users\\potap\\PycharmProjects\\Smart_library\\boos.json", "w+", encoding="UTF-8")
    new_file.write(json.dumps(file_parsed))
    for i in file_parsed:
        listNodes.insert(tk.END, i.get('name'))
    listNodes.place_forget()
    listNodes.place(x=1, y=40)





edit = tk.Button(master=window, text=" Delete ", height=2, font=("Helevetica", 12, "normal"), relief=tk.GROOVE,
                 command=onChange)
current_id = 0

# create window
window.configure(bg='white')
window.title("UKHASnet Node Manager")
window.geometry("680x400")

lbl1 = tk.Label(window, text="Node List:", fg='black', font=("Helvetica", 16, "bold"))
lbl2 = tk.Label(window, text="Node Information:", fg='black', font=("Helvetica", 16, "bold"))
lbl1.place(x=0, y=0)
lbl2.place(x=200, y=0)

scrollbar = tk.Scrollbar(window, orient="vertical")
listNodes = tk.Listbox(window, width=20, height=20, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
scrollbar.config(command=listNodes.yview)
scrollbar.pack(side="right", fill="y")
for i in file_parsed:
    listNodes.insert(tk.END, i.get('name'))

listSelection = tk.Listbox(window, width=50, height=7, font=("Helvetica", 12))
listNodes.bind('<<ListboxSelect>>', onselect)
# pack objects onto window
listNodes.place(x=1, y=40)
listSelection.place(x=200, y=40)
edit.place(x=200, y=190)

window.mainloop()
file.close()
