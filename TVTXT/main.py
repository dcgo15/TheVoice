import tkinter as tk
from tkinter import ttk, Menu
import os

bg_=("#8a8888")


HELP = """
O programa TheVoiceText é um editor
de texto para pessoas que possuem preguiça
de escrever um texto ou não têm tempo para
o mesmo. Segue aqui, um breve tutorial
de como usar-lo:
-
-
* TELA INICIAL *
-
Na tela inicial é possivel ver vários
botões , um deles é o de gravar que
sua função é gravar seu audio e
digitalizar-la , já o de parar
é quando você deseja interromper
a gravação , ou seja, o programa
só irá escrever até onde você
parou
-
* MENU BAR *
-
No menu existem 3 grupos de botões:

- File
- Temas
- Ajuda

No file irá ter algumas opções para o
arquivo:

- Novo : Você irá criar um novo arquivo
- Abrir: Você irá abrir um arquivo
- Salvar: Você irá salvar o arquivo
- Deletar: Você irá deletar o arquivo
- Exit: Sair

Em temas existem duas opções, que nada
mais são que questões estéticas, o dark
é para pessoas que gostam do tema
mais escuro e o light mais claro

E finalizando , não menos importante, temos
o de ajuda que irá servir como um tutorial para
você.
"""

class tvtxt(tk.Tk):

    def get_page(self, page_class):
        return self.frames[page_class]
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        menubar = MenuBar(self)
        self.config(menu=menubar)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Inicio, dois):

            frame = F(container, self, bg=bg_)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Inicio)


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class Inicio(tk.Frame):

    def __init__(self, parent, controller,bg=None):
        tk.Frame.__init__(self, parent, bg=bg)

        self.txt = tk.Text(self, bg="white", fg="black", font="arial 12", width=151, height=30)
        self.txt.place(x=0,y=50)
         
        scrollbar = ttk.Scrollbar(self.txt)
        scrollbar.place(relheight=1, relx=0.990)

        grav = tk.Button(self, text="GRAVAR", width=60,height=3,
                         bg=bg_,fg="white", font="arial 12 bold")
        grav.place(x=10, y=610)

        stop = tk.Button(self, text="× PARAR", width=60,height=3,
                         bg=bg_,fg="white", font="arial 12 bold")
        stop.place(x=740, y=610)

        self.nome = tk.Label(self, text="arquivo.txt", bg=bg_, fg="white", font="arial 15 bold")
        self.nome.place(x=10,y=10)

        dire = tk.Label(self, text="C:/Programs/TVTXT", bg=bg_, fg="white", font="arial 12 bold")
        dire.pack()

        LOGO = tk.Label(self, text="TheVoice Text", bg=bg_, fg="white", font="arial 15 bold")
        LOGO.place(x=1200,y=10)

class dois(tk.Frame):

    def __init__(self, parent, controller, bg=None):
        tk.Frame.__init__(self, parent)

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.controller = parent

        def onexit():
            app.destroy()

        def helpa():
            app = tk.Tk()
            app.title("Help- TVTXT")
            app.geometry("300x400")
            app.resizable(0,0)

            def ok():
                app.destroy()

            tk.Label(app, text="Manual de Ajuda", font="arial 12").pack()

            self.txt = tk.Text(app,
                               bg="white", fg="black", font="arial 10", width=45, height=15)
            self.txt.place(x=0,y=45)

            self.txt.insert(tk.END, HELP)
         
            scrollbar = ttk.Scrollbar(self.txt)
            scrollbar.place(relheight=1, relx=0.890)

            ttk.Button(app, text="Ok", width=16, command=ok).place(x=170, y=350)

            
            app.mainloop()

        def light():
            ini = self.controller.get_page(Inicio)
            ini.txt["bg"] = "white"
            ini.txt["fg"] = "black"

        def dark():
            ini = self.controller.get_page(Inicio)
            ini.txt["bg"] = "#121212"
            ini.txt["fg"] = "white"

        def new():
            app.destroy()
            os.popen("main.py")

        fileMenu = tk.Menu(self, tearoff=False)
        fileMenu2 = tk.Menu(self, tearoff=False)
        fileMenu3 = tk.Menu(self, tearoff=False)
        
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Novo", underline=0,command=new)
        fileMenu.add_command(label="Abrir", underline=0)
        fileMenu.add_command(label="Salvar", underline=0)
        fileMenu.add_command(label="Deletar", underline=0)

        fileMenu.add_command(label="Exit", underline=1, command=onexit)

        self.add_cascade(label="Temas",underline=0, menu=fileMenu2)
        fileMenu2.add_command(label="Light", underline=0, command=light)
        fileMenu2.add_command(label="Dark", underline=0, command=dark)
        
        self.add_cascade(label="Ajuda",underline=0, menu=fileMenu3)
        fileMenu3.add_command(label="Tutorial", underline=0, command=helpa)

if __name__ == "__main__":
    app = tvtxt()
    app.geometry("1400x1000")
    app.title("TheVoiceText - v0.6.6")
    app.mainloop()

        
