import tkinter as tk
from tkinter import ttk, Menu, filedialog
from PIL import Image, ImageTk
import speech_recognition as sr
import os

bg_=("#797978")

############ANOTAÇÕES
#TEMAS MELHORES
#COMANDOS POR TECLAS
#COMANDOS DE VOZES NO MENUBAR
#TAB, 2 PONTOS , /
#Funções em class

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
- Edits
- Temas
- Ajuda

No file irá ter algumas opções para o
arquivo:

- Novo : Você irá criar um novo arquivo
- Abrir: Você irá abrir um arquivo
- Salvar: Você irá salvar o arquivo
- Deletar: Você irá deletar o arquivo
- Exit: Sair

Em Edit terá opções como colar, copiar
e recortar .

Em temas existem duas opções, que nada
mais são que questões estéticas, o dark
é para pessoas que gostam do tema
mais escuro e o light mais claro

E o de ajuda que irá servir como
um tutorial para você.


"""

global select
select = False

####### Função ajuda

def helpa():
    app = tk.Tk()
    app.title("Help - TVTXT")
    app.geometry("300x400")
    app.iconbitmap("logo.ico")
    app.resizable(0,0)
    def ok():
        app.destroy()

    tk.Label(app, text="Manual de Ajuda", font="arial 12").pack()

    txt = tk.Text(app,
                bg="white", fg="black", font="arial 10", width=45, height=15)
    txt.place(x=0,y=45)

    txt.insert(tk.END, HELP)
         
    scrollbar = ttk.Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.890)

    ttk.Button(app, text="Ok", width=16, command=ok).place(x=170, y=350)

            
    app.mainloop()


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
        global helpa
        def gravar():
            mic = sr.Recognizer()

            with sr.Microphone() as source:

                mic.adjust_for_ambient_noise(source)

                print("Diga alguma coisa:")

                audio = mic.listen(source)

            try:

                frase = mic.recognize_google(audio, language="pt-BR").lower()

                print("Você disse: ", frase)

            except sr.UnkownValueError:
                print("Não entendi")


            ### Codigo usando a frase

            #Funções menubar


            if "digite" in frase:
                fra = frase.replace("digite ", "")
                dd = frase.replace("dois pontos", ":")

                
                self.txt.insert(tk.END, fra)


            if "sair" in frase:
                app.destroy()


            if "ajuda" in frase:
                helpa()

            if "mude" in frase:
                fra = frase.replace("mude para tema ", "")
                if fra == "dark":
                    self.txt["bg"] = "#121212"
                elif fra=="branco":
                    self.txt["bg"] = "white"

                else:
                    print("não entendi")

            

                
        image2 = Image.open("bg3.png")
        photo2 = ImageTk.PhotoImage(image2)
        self.imagem2 = tk.Label(self,image=photo2, bg=bg_,width=10)
        self.imagem2.image = photo2
        self.imagem2.place(x=100,y=900)
            

        image = Image.open("bg-logo.png")
        photo = ImageTk.PhotoImage(image)
        self.imagem = tk.Label(self,image=photo, bg=bg_)
        self.imagem.image = photo
        self.imagem.place(x=1121,y=0)

        self.txt = tk.Text(self, bg="white", fg="black", font="arial 12", width=151, height=25)
        self.txt.place(x=0,y=50)

        
         
        scrollbar = ttk.Scrollbar(self.txt)
        scrollbar.place(relheight=1, relx=0.990)

        grav = tk.Button(self,image=photo2, width=200,height=200,
                         bg=bg_,fg="white", font="arial 12 bold", command=gravar,borderwidth=0)
        grav.place(x=560, y=506)

        self.nome = tk.Label(self, text="Novo arquivo", bg=bg_, fg="white", font="arial 15 bold")
        self.nome.place(x=10,y=10)


        

class dois(tk.Frame):

    def __init__(self, parent, controller, bg=None):
        tk.Frame.__init__(self, parent)




    

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.controller = parent

        global helpa

        def onexit():
            app.destroy()

        

        def light():
            ini = self.controller.get_page(Inicio)
            ini.txt["bg"] = "white"
            ini.txt["fg"] = "black"

        def dark():
            ini = self.controller.get_page(Inicio)
            ini.txt["bg"] = "#121212"
            ini.txt["fg"] = "white"

        def new():
            ini = self.controller.get_page(Inicio)
            ini.txt.delete("1.0", tk.END)
            ini.nome["text"] = "Novo arquivo"

        def abrir():
            ini = self.controller.get_page(Inicio)
            ini.txt.delete("1.0", tk.END)

            file = filedialog.askopenfilename(initialdir="C:/Program Files/TVTXT", title="Escolha o arquivo",
                                              filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")))
            file.replace(file, "")
            ini.nome["text"] = file

            text = open(file, "r")
            ler = text.read()

            ini.txt.insert(tk.END, ler)
            text.close()

        def save_as():
            ini = self.controller.get_page(Inicio)
            
            file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Program Files/TVTXT",
                                                title="Salvar o arquivo", filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")))

            if file:
                ini.nome["text"] = file

                file = open(file, "w")
                file.write(ini.txt.get(1.0, tk.END))
                file.close()



        def recort():
            global select
            ini = self.controller.get_page(Inicio)
            if ini.txt.get(1.0, tk.END):
                select = ini.txt.get(1.0, tk.END)
                ini.txt.delete("sel.first", "sel.last")

        def copy():
            global select
            ini = self.controller.get_page(Inicio)
            if ini.txt.selection_get():
                select=ini.txt.selection_get()

        def paste():
            ini = self.controller.get_page(Inicio)
            global select
            ini.txt.insert(tk.END,select)

        def save():
            ini = self.controller.get_page(Inicio)
            file = open(ini.nome["text"], "w")
            file.write(ini.txt.get(1.0, tk.END))
            file.close()

        

        fileMenu = tk.Menu(self, tearoff=False)
        fileMenu2 = tk.Menu(self, tearoff=False)
        fileMenu3 = tk.Menu(self, tearoff=False)
        fileMenu4 = tk.Menu(self, tearoff=False)
        
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Novo", underline=0,command=new)
        fileMenu.add_command(label="Abrir", underline=0, command=abrir)
        fileMenu.add_command(label="Salvar", underline=0, command=save)
        fileMenu.add_command(label="Salvar como", underline=0, command=save_as)

        #add o outro save mais tarde

        
        

        fileMenu.add_separator()

        fileMenu.add_command(label="Exit", underline=1, command=onexit)

        self.add_cascade(label="Edit",underline=0, menu=fileMenu4)

        fileMenu4.add_command(label="Recortar", command=recort)
        fileMenu4.add_command(label="Copiar", command=copy)
        fileMenu4.add_command(label="Colar", command=paste)

        self.add_cascade(label="Temas",underline=0, menu=fileMenu2)
        fileMenu2.add_command(label="Light", underline=0, command=light)
        fileMenu2.add_command(label="Dark", underline=0, command=dark)
        
        self.add_cascade(label="Ajuda",underline=0, menu=fileMenu3)
        fileMenu3.add_command(label="Tutorial", underline=0, command=helpa)




if __name__ == "__main__":
    app = tvtxt()
    app.geometry("1400x1000")
    app.title("TheVoiceText - v0.8.7")
    app.iconbitmap("logo.ico")
    app.mainloop()

        
