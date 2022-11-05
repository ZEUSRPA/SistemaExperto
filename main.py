from ctypes import sizeof
from lib2to3.pgen2.token import LEFTSHIFT
from logging import RootLogger
from operator import length_hint
from select import select
from tkinter import *
from tkinter import filedialog as fd
import shutil
import copy
import os
import tkinter
from turtle import width  
from PIL import ImageTk,Image
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import threading
import os
import random
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#Frame utilizado para mostrar los graficos
class graph_frame(Frame):
    def __init__(self):
        Frame.__init__(self,root)
       
    
    def add_graph(self,fig):
        self.mpl_canvas=FigureCanvasTkAgg(fig,self)
        
        self.mpl_canvas.get_tk_widget().pack(fill=BOTH,expand=True)
        self.mpl_canvas._tkcanvas.pack( fill=BOTH, expand=True)
    def remove_graph(self):
        self.mpl_canvas.get_tk_widget().pack_forget()
        self.mpl_canvas._tkcanvas.pack_forget()
        del self.mpl_canvas

class bird:
    def __init__(self)->None:
        self.name=""
        self.size=""
        self.description=""
        self.habitat=""
        self.comments=""
        self.other_names=""
        self.distribution=""
        self.jalisco_distribution=""
        self.image="sources/default.jpeg"

        #Caracteristics
        self.caracteristics={}
        

class visualizer:
    def __init__(self,menu,frame1,bird,rules,clasifier)->None:
        self.frame1=frame1
        self.clasifier=clasifier
        self.name=Label(self.frame1,text="AVE",background='#353437')
        self.name.configure(font=("Arial",50))
        
        openImage=Image.open(bird.image)
        img=openImage.resize((200,300))
        self.photo=ImageTk.PhotoImage(img)
        self.image=Label(self.frame1,image=self.photo)

        self.size=Label(self.frame1,text="AVE",background='#353437')
        self.size.configure(font=("Arial",40))
        self.description=Label(self.frame1,text="AVE",background='#353437')
        self.description.configure(font=("Arial",40))
        self.habitat=Label(self.frame1,text="AVE",background='#353437')
        self.habitat.configure(font=("Arial",40))
        self.comments=Label(self.frame1,text="AVE",background='#353437')
        self.comments.configure(font=("Arial",40))
        self.explanation=Label(self.frame1,text="AVE",background='#353437')
        self.explanation.configure(font=("Arial",40))
        self.menu_window=menu
        self.bird=bird
        self.rules=rules
        self.addButton=Button(self.frame1,text="Agregar Ave",command=self.add_bird,bg="#7a7b7c", fg="white")
        self.addButton.config(height=2,width=15)
        self.menuButton=Button(self.frame1,text="Menu Principal",command=self.main_window,bg="#7a7b7c", fg="white")
        self.menuButton.config(height=2,width=15)
        self.showBird()


    def add_bird(self):
        self.addfunction=addBird(self.menu_window,self.frame1,self.clasifier)
        self.hide()
        self.addfunction.show()

    def show(self):
        self.name.pack()
        self.image.pack()
        self.size.pack()
        self.description.pack()
        self.habitat.pack()
        self.comments.pack()
        self.explanation.pack()

        if(self.bird.name=="Desconocida"):
            self.addButton.pack(side=TOP)
        self.menuButton.pack(side=TOP)
    
    #Oculta la vista de la descripción del ave
    def hide(self):
        self.name.pack_forget()
        self.image.pack_forget()
        self.size.pack_forget()
        self.description.pack_forget()
        self.habitat.pack_forget()
        self.comments.pack_forget()
        self.explanation.pack_forget()
        if(self.bird.name=="Desconocida"):
            self.addButton.pack_forget()
        self.menuButton.pack_forget()

    def showBird(self):
        self.name=Label(self.frame1,text=self.bird.name,background='#353437',fg="white")
        self.name.configure(font=("Arial",35))

        openImage=Image.open(self.bird.image)
        img=openImage.resize((200,200))
        self.photo=ImageTk.PhotoImage(img)       
        self.image=Label(self.frame1,image=self.photo)

        self.size=Label(self.frame1,text=self.bird.size,wraplength=1200,background='#353437',fg="white")
        self.size.configure(font=("Arial",14))
        self.description=Label(self.frame1,text=self.bird.description,wraplength=1200,background='#353437',fg="white")
        self.description.configure(font=("Arial",14))
        self.habitat=Label(self.frame1,text=self.bird.habitat,wraplength=1200,background='#353437',fg="white")
        self.habitat.configure(font=("Arial",14))
        self.comments=Label(self.frame1,text=self.bird.comments,wraplength=1200,background='#353437',fg="white")
        self.comments.configure(font=("Arial",14))
        exp="\n\n\nEl ave fue encontrada en base a las siguientes características:\n"
        for key in self.rules.keys():
            exp+=key+":"+self.rules[key]+"\n"

        self.explanation=Label(self.frame1,text=exp,wraplength=1200,background='#353437',fg="white")
        self.explanation.configure(font=("Arial",14))

    

    #Muestra la vista principal
    def main_window(self):
        self.hide()
        self.menu_window.show()
    
    def closing(self):
        del self

class addBird:
    def __init__(self,menu,frame1,clasifier)->None:
        self.frame1=frame1
        self.main_menu=menu
        self.clasifier=clasifier
        self.load_caracteristics()
        # self.name=Label(self.frame1,text="AVE",background='#353437')
        # self.name.configure(font=("Arial",50))

        # openImage=Image.open(bird.image)
        # img=openImage.resize((200,300))
        # self.photo=ImageTk.PhotoImage(img)
        # self.image=Label(self.frame1,image=self.photo)
        self.labels = []
        self.entries = []

        for caracteristic in self.caracteristics:
            self.labels.append(Label(self.frame1,text=caracteristic.capitalize(),background='#353437',fg="white"))
            if(caracteristic=="descripcion" or caracteristic=="habitat" or caracteristic=="comentarios"):
                self.entries.append(Text(self.frame1, height=2, width=45))
            else:
                self.entries.append(Entry(self.frame1,width=60))

        




        # self.description=Label(self.frame1,text="AVE",background='#353437')
        # self.description.configure(font=("Arial",40))
        # self.habitat=Label(self.frame1,text="AVE",background='#353437')
        # self.habitat.configure(font=("Arial",40))
        # self.comments=Label(self.frame1,text="AVE",background='#353437')
        # self.comments.configure(font=("Arial",40))
        # self.explanation=Label(self.frame1,text="AVE",background='#353437')
        # self.explanation.configure(font=("Arial",40))
        # self.menu_window=menu
        # self.bird=bird
        # self.rules=rules
        # self.menuButton=Button(self.frame1,text="Menu Principal",command=self.main_window,bg="#7a7b7c", fg="white")
        # self.menuButton.config(height=2,width=15)
        # self.showBird()
    def load_caracteristics(self):
        self.caracteristics = []
        self.caracteristics.append("nombre")
        self.caracteristics.append("descripcion")
        self.caracteristics.append("habitat")
        self.caracteristics.append("comentarios")     
        self.caracteristics.append("ojos")
        self.caracteristics.append("pico")
        self.caracteristics.append("loras")
        self.caracteristics.append("cuerpo")
        self.caracteristics.append("tarsos")
        self.caracteristics.append("cola")
        self.caracteristics.append("alas")
        self.caracteristics.append("corona")
        self.caracteristics.append("garganta")
        self.caracteristics.append("pecho")
        self.caracteristics.append("vientre")
        self.caracteristics.append("espalda")
        self.caracteristics.append("cabeza")
        self.caracteristics.append("cere")
    
    def show(self):
        self.title=Label(self.frame1,text="Agregar Ave",background='#353437',fg="white")
        self.title.configure(font=("Arial",20))
        self.title.grid(column=1,row=1,columnspan=5)
        self.currentpos=3
        for i in range(len(self.labels)):
            self.labels[i].configure(font=("Arial",15))
            self.labels[i].grid(column=1,row=self.currentpos)
            self.entries[i].grid(column=2, row=self.currentpos)
            if(self.caracteristics[i]=="comentarios"):
                self.currentpos+=1
                self.instructions=Label(self.frame1,text="Indique los colores del ave",background='#353437',fg="white")
                self.instructions.configure(font=("Arial",20))
                self.instructions.grid(column=1, row=self.currentpos,columnspan=2)
            self.currentpos+=1

        self.filename=StringVar()
        self.image=Label(self.frame1,text="Imagen",background='#353437',fg="white")
        self.image.configure(font=("Arial",15))
        self.image.grid(column=1,row=23)
        self.showRute=Entry(self.frame1,textvariable=self.filename)
        self.showRute.config(state='disabled',width=60)
        self.showRute.grid(column=2,row=23)
        self.chooseImage=Button(self.frame1,text="Seleccionar Imagen",command=self.selectImage,bg="#7a7b7c",fg="white")
        self.chooseImage.config(height=1,width=15)
        self.chooseImage.grid(column=3,row=23)
        self.saveButton=Button(self.frame1,text="Guardar",command=self.save,bg="#7a7b7c",fg="white")
        self.saveButton.config(height=2,width=15)
        self.saveButton.grid(column=2,row=27)
        self.menuButton=Button(self.frame1,text="Menu Principal",command=self.main_window,bg="#7a7b7c", fg="white")
        self.menuButton.config(height=2,width=15)
        self.menuButton.grid(column=1,row=27)

    def selectImage(self):
        self.filename.set(fd.askopenfilename(initialdir = "/",title = "Seleccionar imagen",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))))
        

    def hide(self):
        self.title.grid_remove()
        for i in range(len(self.labels)):
            self.labels[i].grid_remove()
            self.entries[i].grid_remove()
        self.chooseImage.grid_remove()
        self.instructions.grid_remove()
        self.image.grid_remove()
        self.showRute.grid_remove()
        self.saveButton.grid_remove()
        self.menuButton.grid_remove()
        

    def save(self):
        self.aux = bird()
        for i in range(len(self.entries)):
            if(self.caracteristics[i]=="descripcion" or self.caracteristics[i]=="habitat" or self.caracteristics[i]=="comentarios"):
                if(self.caracteristics[i]=="descripcion"):
                    self.aux.description=self.entries[i].get(1.0,"end-1c")
                elif(self.caracteristics[i]=="habitat"):
                    self.aux.habitat=self.entries[i].get(1.0,"end-1c")
                elif(self.caracteristics[i]=="comentarios"):
                    self.aux.comments=self.entries[i].get(1.0,"end-1c")
            else:
                if(self.entries[i].get()!=""):
                    if(self.caracteristics[i]=="nombre"):
                        self.aux.name=self.entries[i].get()
                    else:
                        self.aux.caracteristics[self.caracteristics[i]]=self.entries[i].get()
        self.currentpath = os.getcwd()
        self.currentpath+="\\sources\\"
        shutil.copy(self.filename.get(),self.currentpath)
        self.words=self.filename.get().split("/")
        self.aux.image="sources/"+self.words[-1]
        self.clasifier.aves.append(self.aux)
        self.hide()
        self.main_menu.show()
    
    def main_window(self):
        self.hide()
        self.main_menu.show()


        
#En esta clase se tienen los metodos para clasificar
class clasifier:
    #Constructor de la clase
    def __init__(self,menu,frame1) -> None:
        self.menu_window=menu
        self.frame1=frame1
        self.title=Label(self.frame1,text="Clasificador de aves",background='#353437',fg="white")
        self.title.configure(font=("Arial",35))

        self.menuButton=Button(self.frame1,text="Main Menu",command=self.main_window,bg="#7a7b7c",fg="white")
        self.menuButton.config(height=10,width=50)
        self.aves=[]
        self.default_ave=bird()
        self.load_birds()
        self.loadall()
        
    def loadall(self):
        
        self.good=False
        self.doing=True
        
        
        # self.load_birds()
        self.rules={}
        self.decition=self.aves[0]
        self.visual=visualizer(self.menu_window,self.frame1,self.decition,self.rules,self)
        self.possible_rules={}
        self.possible_aves=[]

        
        
    def load_birds(self):
        self.default_ave.name="Desconocida"
        self.default_ave.image="sources/default.jpeg"
        
        self.aux=bird()
        self.aux.name="Garceta pie dorado"
        self.aux.description="Adulto: (sexos similares) Ojos amarillos, pico negro. Loras amarillas (en ocasiones anaranjadas). Cuerpo blanco. Tarsos negros, patas amarillas. Juvenil: Parecido al adulto pero con pico negro (o amarillo con la punta negra), patas y tarsos amarillos (en ocasiones verde amarillento)."
        self.aux.habitat="Prácticamente cualquier hábitat acuático (e.g., lagos, pantanos, charcas, playas y manglares). Sitios de posible observación en el bosque: comúnmente sobrevuela el bosque al amanecer en dirección Suroeste-Noreste."
        self.aux.comments="Se alimenta principalmente de peces, insectos y crustáceos. Ocasionalmente consume caracoles, ranas, lagartijas y pequeños roedores. Anteriormente, en los 1800s, sus plumas eran utilizadas para decorar sombreros, razón por la cual sus poblaciones decayeron. Afortunadamente, en la actualidad ya no es utilizada con ese fin y sus poblaciones han vuelto a la normalidad."
        self.aux.caracteristics["ojos"]="amarillo"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["loras"]="amarillo"
        self.aux.caracteristics["cuerpo"]="blanco"
        self.aux.caracteristics["tarsos"]="negro"
        self.aux.image="sources/garceta_pie_dorado.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Garceta verde"
        self.aux.description="Adulto: (sexos similares) Ojos amarillos, pico negro con base amarillenta. Corona verde oscuro, zona malar blanquecina, resto de la cabeza rojiza. Garganta rojiza, pecho rojizo levemente jaspeado de blanco, vientre grisáceo. Nuca rojiza; espalda y rabadilla verdes. Alas verde oscuro con borde de plumas verde claro o blanquecino. Cola verde oscuro. Patas y tarsos amarillos o anaranjados. Juvenil: Parecido al adulto pero con auriculares cafés, pecho blanco jaspeado de café, espalda gris-café y alas azulosas a cafés"
        self.aux.habitat="Cuerpos de agua dulce y salobre con vegetación circundante densa (e.g., lagos, charcas, pantanos y manglares). Sitios de posible observación en el bosque: únicamente registrada en manantial ubicado al Norte del Estanque de los patos."
        self.aux.comments="Se alimenta principalmente de peces, ranas e insectos. Su técnica de alimentación pescadora se basa fundamentalmente en utilizar su pico largo como una lanza. En caso de estar alarmada levanta una pequeña cresta, estira el cuello y mueve nerviosamente la cola."
        self.aux.caracteristics["ojos"]="amarillo"
        self.aux.caracteristics["pico"]="negro con base amarillenta"
        self.aux.caracteristics["alas"]="verde oscuro"
        self.aux.caracteristics["cola"]="verde oscuro"
        self.aux.caracteristics["tarsos"]="amarillos"
        self.aux.image="sources/garceta_verde.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Pedrete corona negra"
        self.aux.description="Adulto: (sexos similares) Ojos rojos, pico negro. Corona negra, resto de la cabeza blanco-grisácea. Garganta blanquecina; pecho y vientre grisáceos. Espalda negra. Alas y cola grises. Patas y tarsos amarillos. Subadulto: Parecido al adulto pero con pecho blanquecino levemente jaspeado de café y con corona, nuca, espalda y alas grises. Juvenil: Parecido al adulto pero con maxila negra, mandíbula amarillenta; cabeza, garganta, pecho y vientre cafés jaspeados de blanco, espalda gris con pequeñas motas blancas y alas grises con borde blanco en plumas de vuelo."
        self.aux.habitat="Cuerpos de agua dulce y salobre (e.g., lagos, pantanos, ríos arbolados). Sitios de posible observación en el bosque: únicamente registrada en vegetación adjunta al Estanque de los Patos. "
        self.aux.comments="Se alimenta principalmente de peces, eventualmente consume algas, lombrices, insectos, crustáceos, anfibios y pequeños roedores. "
        self.aux.caracteristics["ojos"]="rojo"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["corona"]="negro"
        self.aux.caracteristics["garganta"]="blanquecino"
        self.aux.caracteristics["pecho"]="grisáceo"
        self.aux.caracteristics["vientre"]="grisáceo"
        self.aux.caracteristics["espalda"]="negro"
        self.aux.caracteristics["alas"]="gris"
        self.aux.caracteristics["cola"]="gris"
        self.aux.image="sources/pedrete_corona_negra.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Zopilote común"
        self.aux.description="Adulto: (sexos similares) Ojos negros, pico negro con la punta de la maxila blanca. Cabeza grisácea con pliegues notorios. Cuerpo negruzco. Al vuelo exhibe cola corta negra y punta de las plumas primarias blancas. Juvenil: Parecido al adulto pero con cabeza gris oscuro (aparentemente negra) y pico totalmente negro."
        self.aux.habitat="Zonas boscosas y áreas abiertas en general. Sitios de posible observación en el bosque: comúnmente sobrevuela el bosque, rara vez se percha antes del crepúsculo. "
        self.aux.comments="Se alimenta principalmente de carroña. Generalmente vuela en grandes grupos (entremezclado con zopilotes aura; Cathartes aura) en busca de cadáveres. A diferencia del zopilote aura, el zopilote común depende de su visión para encontrar alimento. "
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["cabeza"]="grisácea"
        self.aux.caracteristics["cuerpo"]="negruzco"
        self.aux.caracteristics["cola"]="negro"
        self.aux.image="sources/zopilote_comun.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Zopilote aura"
        self.aux.description="Adulto: (sexos similares) Ojos negros, pico con base rojiza y punta blanca. Cabeza roja. Cuerpo café oscuro. Al vuelo exhibe plumas de vuelo gris claro (contrastantes con el resto del ala) y cola larga gris. Juvenil: Parecido al adulto pero con cabeza gris rosácea (muy oscura) y pico gris-café."
        self.aux.habitat="Zonas boscosas y áreas abiertas en general. Sitios de posible observación en el bosque: comúnmente sobrevuela el bosque, rara vez se percha antes del crepúsculo."
        self.aux.comments="Se alimenta principalmente de carroña y ocasionalmente caza su alimento. Generalmente vuela en grandes grupos (entremezclados con zopilotes comunes; Coragyps atratus) en busca de alimento. A diferencia del zopilote común, el zopilote aura se basa principalmente en su olfato para encontrar su alimento."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="base rojiza y punta blanca"
        self.aux.caracteristics["cabeza"]="roja"
        self.aux.caracteristics["cuerpo"]="café oscuro"
        self.aux.caracteristics["cola"]="gris"
        self.aux.image="sources/zopilote_aura.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Gavilán pecho rufo"
        self.aux.description="Adulto: Macho: Ojos rojos, cere amarillo, pico gris oscuro. Auriculares gris-rojizas, resto de la cabeza gris. Pecho y vientre blancos jaspeados de anaranjado-rojizo, cobertoras inferiores de la cola blancas. Espalda gris. Alas grises con primarias negras. Cola larga gris con tres franjas horizontales negras. Patas y tarsos amarillos. Hembra: Parecida al macho adulto pero con auriculares gris claro. Juvenil: Ojos amarillos. Cabeza café jaspeada de blanco, línea superciliar blanquecina. Pecho y vientre blancos jaspeados de café, cobertoras inferiores de la cola blancas. Espalda café. Alas cafés con plumas primarias negras. Cola similar a la de los adultos."
        self.aux.habitat="Bosques templados (e.g., pino, pino-encino, encino). Durante la época migratoria puede encontrarse prácticamente en cualquier hábitat. Sitios de posible observación en el bosque:cualquier área densamente arbolada (e.g., La araña, arbolados urbicados al Norte del jardín mexicano)."
        self.aux.comments="Se alimenta principalmente de aves pequeñas y roedores. Este es el gavilán, perteneciente al género Accipiter, más pequeño del país (y una de las aves de presa más ágiles dentro de zonas boscosas)."
        self.aux.caracteristics["ojos"]="rojo"
        self.aux.caracteristics["pico"]="gris oscuro"
        self.aux.caracteristics["cere"]="amarilla"
        self.aux.caracteristics["pecho"]="blanco"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="gris"
        self.aux.caracteristics["alas"]="gris"
        self.aux.caracteristics["patas"]="amarillo"
        self.aux.caracteristics["tarsos"]="amarillo"
        self.aux.image="sources/gavilan_pecho_rufo.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Aguililla cola roja"
        self.aux.description="Adulto: Ojos negros o amarillos, cere amarillo, pico gris oscuro. Coloración del plumaje general variable, normalmente compuesto por tonos cafés, rojizos y/o blanquecinos. Cola generalmente rojiza con banda subterminal negra. Al vuelo exhibe marca patagial oscura. Juvenil: Parecido al adulto pero sin coloraciones rojizas."
        self.aux.habitat="Áreas abiertas (e.g., valles, praderas, cultivos), bosques y cableado eléctrico paralelo a carreteras. Sitios de posible observación en el bosque: raramente sobrevuela el bosque y/o se percha en árboles altos."
        self.aux.comments="Se alimenta principalmente de roedores, otros mamíferos pequeños, aves, reptiles, anfibios y ocasionalmente carroña. Sin duda alguna, esta es la aguililla más común en el país."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="gris"
        self.aux.caracteristics["cere"]="amarilla"
        self.aux.caracteristics["pecho"]="blanco"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="cafe"
        self.aux.caracteristics["alas"]="negras"
        self.aux.caracteristics["cola"]="roja"
        self.aux.image="sources/aguililla_cola_roja.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Cernícalo americano"
        self.aux.description="Edades similares: Macho: Ojos negros, cere amarillo, pico gris oscuro. Corona azul-gris con centro rojizo, zona malar y borde de auriculares negros. Garganta blanca, pecho anaranjado deslavado; vientre, lados y flancos blancos con motas negras. Nuca anaranjada con un parche negro al centro, espalda barrada de rojizo y negro, rabadilla rojiza. Alas azulgris con motas negras. Cola rojiza con banda terminal negra. Hembra: Parecida al macho pero con corona azul-gris claro (sin centro rojizo), pecho y vientre blancos jaspeados de rojizo y alas barradas de café y negro."
        self.aux.habitat="Áreas abiertas (e.g., valles, praderas, cultivos), bordes de bosques, matorrales y ciudades. Sitios de posible observación en el bosque: áreas abiertas (generalmente perchados en rejas y cables) y zonas boscosas con árboles dispersos (principalmente eucaliptales)."
        self.aux.comments="Se alimenta principalmente de insectos, mamíferos pequeños, aves y reptiles. El cernícalo americano es el ave rapaz diurna más colorida y pequeña del país."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["corona"]="azul-gris"
        self.aux.caracteristics["cere"]="amarilla"
        self.aux.caracteristics["pecho"]="anaranjado"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="roja"
        self.aux.caracteristics["alas"]="azul-gris"
        self.aux.caracteristics["cola"]="roja"
        self.aux.image="sources/cernicalo_americano.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Tórtola cola larga"
        self.aux.description="Adulto: (sexos similares) Ojos rojos, pico gris. Frente, barbilla y anillo ocular blanquecinos; resto de la cabeza café grisácea (borde de plumas oscuro). Cuerpo café grisáceo con apariencia escamosa. Cobertoras inferiores de la cola levemente barradas blanco y negro. Cola larga café grisáceo con rectrices exteriores blancas. Patas y tarsos anaranjados. Al vuelo exhibe coloración rojiza en las alas. Juvenil: Parecido al adulto pero con ojos café claro y plumaje general café amarillento (sin apariencia escamosa)."
        self.aux.habitat="Matorrales, bordes de bosques, granjas y ciudades. Sitios de posible observación en el bosque: áreas altamente frecuentadas por los usuarios del bosque (e.g., caminos, kioscos, área de pic-nic, accesos), sotobosques clareados y arbolados dispersos."
        self.aux.comments="Se alimenta de una gran variedad de semillas y frutos. La tórtola cola larga es uno de los mejores ejemplos de una especie adaptada a los sistemas urbanos. Es común observar grandes grupos de tórtolas alimentándose en el suelo."
        self.aux.caracteristics["ojos"]="rojo"
        self.aux.caracteristics["pico"]="gris"
        self.aux.caracteristics["alas"]="rojas"
        self.aux.caracteristics["patas"]="anaranjado"
        self.aux.caracteristics["cola"]="cafe"
        self.aux.caracteristics["tarsos"]="anaranjado"
        self.aux.image="sources/tortola_cola_larga.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Garrapatero pijuy"
        self.aux.description="Adulto: (sexos similares) Ojos negros, pico ancho y surcado gris. Cuerpo negro. Cola larga y articulada negra. Juvenil: Parecido al adulto pero con pico más delgado y plumaje general café oscuro"
        self.aux.habitat="Matorrales densos, pastizales, tierras agrícolas y bordes de bosques tropicales. Sitios de posible observación en el bosque: sotobosques clareados, áreas de eucalipto y/o casuarina, vegetación secundaria nativa y vegetación adyacente a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de insectos, semillas y frutos. Debido a que la coloración general de este garrapatero es totalmente negra, puede ser confundido con el zanate mexicano (Quiscalus mexicanus). No obstante, cuando el garrapatero se percha, mueve su cola articulada ascendente y descendentemente."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="gris"
        self.aux.caracteristics["corona"]="negra"
        self.aux.caracteristics["pecho"]="negro"
        self.aux.caracteristics["vientre"]="negro"
        self.aux.caracteristics["espalda"]="negro"
        self.aux.caracteristics["alas"]="negras"
        self.aux.caracteristics["cola"]="negra"
        self.aux.image="sources/garrapatero_pijuy.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Lechuza de campanario"
        self.aux.description="Edades similares. Macho: Ojos negros, pico gris claro con base rosácea (generalmente inconspicua). Cara blanca en forma de corazón delimitada por una línea rojiza. Pecho y vientre blanco grisáceos con pequeños puntos negros. Resto del cuerpo anaranjado amarillento claro con áreas (parches) grises. Hembra: Parecida al macho adulto pero con pecho anaranjado amarillento y vientre amarillo deslavado."
        self.aux.habitat="Áreas abiertas, borde de bosques semiáridos a semihúmedos, granjas, graneros y zonas urbanas (en parques, campanarios, casas abandonadas, bodegas). Sitios de posible observación en el bosque: áreas de pino y eucalipto con árboles altos."
        self.aux.comments="Se alimenta principalmente de mamíferos pequeños (e.g., ratas, ratones, conejos, musarañas), aves pequeñas y lagartijas. Como es común entre las aves rapaces nocturnas, la lechuza de campanario es de hábitos generalmente nocturnos, sin embargo actividades crepusculares o diurnas son comunes."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="gris"
        self.aux.caracteristics["pecho"]="blanco"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["alas"]="anaranjadas"
        self.aux.caracteristics["cola"]="anaranjada"
        self.aux.image="sources/lechuza-campanario.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Chotacabras zumbón"
        self.aux.description="Adulto: Macho: Ojos y pico negros. Línea superciliar gris claro, corona oscura; barbilla y borde de auriculares rojizos. Garganta blanca, pecho barrado de gris-café oscuro y negro, vientre barrado de blanco y café. Espalda grisácea; plumas cobertoras del ala negras con motas rojizas. Alas barradas de gris y negro; plumas primarias negras. Cola barrada de café oscuro y negro. Al vuelo exhibe parche vertical blanco cerca de base de primarias y banda subterminal blanca. Hembra: Parecida al macho adulto pero con garganta rojiza, pecho barrado de amarillo oscuro y café y sin banda subterminal blanca. Juvenil: Parecido a la hembra adulta pero con coloración general grisácea clara o rojiza."
        self.aux.habitat="Áreas abiertas y semiabiertas (e.g., llanuras, ciudades, praderas), bosques de pino y borde de bosques húmedos. Sitios de posible observación en el bosque: en el día se puede observar en el suelo de áreas semiabiertas y/o matorrales, por la noche es común observarlos sobrevolando el bosque en áreas abiertas."
        self.aux.comments="Se alimenta principalmente de insectos. Al igual que el resto de los chotacabras, su coloración le permite camuflarse durante el día"
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["pecho"]="cafe"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="gris"
        self.aux.caracteristics["alas"]="negras"
        self.aux.caracteristics["cola"]="cafe"
        self.aux.image="sources/chotacabras_zumbon.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Colibrí pico ancho"
        self.aux.description="Adulto: Macho: Ojos negros, pico rojo con punta negra. Línea ocular blanca (generalmente inconspicua), gorja azul iridiscente, resto de la cabeza verde iridiscente. Pecho y vientre verde iridiscentes. Alas oscuras. Cola emarginada azul. Hembra: Cabeza verde (no iridiscente), línea ocular blanquecina conspicua. Garganta grisácea; pecho y vientre gris oscuro. Espalda, rabadilla y cobertoras del ala verde opaco. Cola parecida a la del macho adulto pero con rectrices exteriores con puntas blancas. Juvenil: Parecido a la hembra adulta pero con tonos más opacos (en ocasiones el macho subadulto exhibe manchones azules en la gorja"
        self.aux.habitat="Matorrales arbolados, bosques de encino, bosques húmedos, vegetación riparia y ciudades. Sitios de posible observación en el bosque: prácticamente en cualquier sitio del bosque con plantas en floración o sitios cercanos a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de néctar floral, en ocasiones consume insectos y rara vez pequeñas arañas. El colibrí pico ancho se ha adaptado eficientemente a los ambientes urbanos y es actualmente el colibrí más común tanto dentro del bosque, como de la ciudad."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="rojo"
        self.aux.caracteristics["pecho"]="verde"
        self.aux.caracteristics["vientre"]="verde"
        self.aux.caracteristics["alas"]="negras"
        self.aux.caracteristics["cola"]="azul"
        self.aux.image="sources/colibri_pico_ancho.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Zafiro oreja blanca"
        self.aux.description="Adulto: Macho: Ojos negros, pico rojo con la punta negra. Línea ocular blanca (muy conspicua), resto de la cabeza y gorja morado iridiscentes (aparentemente negras). Lados y flancos verdes; vientre y cobertoras inferiores de la cola blanquecinas. Espalda y cobertoras alares verdes. Cola redondeada oscura. Hembra: Parecida al macho adulto pero con frente grisácea, zona malar blanca, nuca verde, vientre grisáceo, punta de rectrices exteriores blancas y garganta, pecho, flancos y lados blanquecinos con filas de motas verdes. Juvenil: Parecido a la hembra adulta pero con tonos más opacos y deslavados."
        self.aux.habitat="claros y bordes de bosques montañosos (e.g., pino, pino-encino, encino) cercanos a arroyos. Sitios de posible observación en el bosque: claros en áreas de pino y eucalipto, vegetación secundaria nativa y vegetación circundante a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de néctar floral y en ocasiones consume insectos pequeños y arañas. Dado que el zafiro oreja blanca no es muy afín a los ecosistemas urbanos, cuando entra a ellos prefiere áreas con niveles bajos de perturbación, por lo que no se observa fuera de suburbios, parques y relictos de vegetación nativa."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="rojo"
        self.aux.caracteristics["pecho"]="verde"
        self.aux.caracteristics["vientre"]="verde"
        self.aux.caracteristics["espalda"]="morada"
        self.aux.caracteristics["alas"]="negras"
        self.aux.caracteristics["cola"]="azul"
        self.aux.image="sources/zafiro_oreja_blanca.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Colibrí berilo"
        self.aux.description="Adulto: Macho: Ojos negros, pico rojo con la punta negra. Línea ocular blanca (generalmente inconspicua), resto de la cabeza verde oscuro iridiscente. Flancos, lados y vientre grisáceos. Espalda verde; rabadilla y cobertoras superiores de la cola café-canela. Alas café rojizo. Cola cuadrada (levemente emarginada) rojiza. Hembra: Parecida al macho adulto pero con coloración general verde opaca (no iridiscente). Juvenil: Parecido a la hembra adulta pero con vientre blanquecino y coloración general más clara."
        self.aux.habitat="Ecotonos y claros de bosques montañosos (principalmente encino) y sembradíos tropicales. Sitios de posible observación en el bosque: áreas arboladas con sotobosque en floración y vegetación circundante a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de néctar floral, en ocasiones consume insectos y rara vez pequeñas arañas. El colibrí berilo es uno de los colibríes endémicos de México y Centro América. Sin embargo, existen registros ocasionales en el Sur de Arizona y Suroeste de Texas (EUA)."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="rojo"
        self.aux.caracteristics["pecho"]="verde"
        self.aux.caracteristics["vientre"]="gris"
        self.aux.caracteristics["espalda"]="morada"
        self.aux.caracteristics["alas"]="cafe"
        self.aux.caracteristics["cola"]="azul"
        self.aux.image="sources/colibri_berilo.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Colibrí corona violeta"
        self.aux.description="Adulto: (sexos similares) Ojos negros, pico rojo con la punta negra. Corona violeta. Garganta, pecho y vientre blancos, lados y flancos verde claro. Nuca, espalda y cobertoras del ala verde olivo. Alas oscuras. Cola emarginada verde olivo. Juvenil: Parecido al adulto pero con corona verde (en ocasiones con violeta claro en la frente)."
        self.aux.habitat="Matorrales, bosques, vegetación riparia y áreas semiabiertas. Sitios de posible observación en el bosque: prácticamente en cualquier sitio del bosque con plantas en floración y sitios cercanos a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de néctar floral, en ocasiones consume insectos y rara vez pequeñas arañas. Dadas las preferencias de hábitat del colibrí corona violeta, es común observarlo cercano a cuerpos de agua."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="rojo"
        self.aux.caracteristics["corona"]="violeta"
        self.aux.caracteristics["pecho"]="blanco"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="verde"
        self.aux.caracteristics["alas"]="cafe"
        self.aux.caracteristics["cola"]="verde"
        self.aux.image="sources/colibri_corona_violeta.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Momoto corona café"
        self.aux.description="Adulto: (sexos similares) Ojos cafés, pico largo y punteado negro. Corona rojiza, máscara negra rodeada por plumas azules y/o moradas. Pecho verde con mota central negra, vientre verde amarillento. Alas azul-verde. Cola verde (en ocasiones con tonalidades azules) con dos raquetas terminales (base azul-verde y punta negra). Juvenil: Parecido al adulto pero con coloración general menos intensa."
        self.aux.habitat="Bosques y matorrales. Sitios de posible observación en el bosque: áreas boscosas (e.g., pino, eucalipto, casuarina), cañadas con vegetación secundaria nativa y vegetación aledaña a cuerpos de agua."
        self.aux.comments="Se alimenta principalmente de frutos e insectos. El momoto corona café es una de las aves más coloridas y vistosas del Bosque Los Colomos. Debido al movimiento pendular de su cola larga, también recibe el nombre de pájaro reloj, o simplemente péndulo."
        self.aux.caracteristics["ojos"]="cafe"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["corona"]="cafe"
        self.aux.caracteristics["pecho"]="verde"
        self.aux.caracteristics["vientre"]="verde"
        self.aux.caracteristics["alas"]="Azul-verde"
        self.aux.caracteristics["cola"]="verde"
        self.aux.image="sources/momoto_corona_cafe.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Martín pescador norteño"
        self.aux.description="Adulto: Macho: Ojos negros, pico negro con base gris. Marca loral blanca, resto de la cabeza azul con copete prominente. Collar blanco, franja pectoral azul con motas rojizas (inconspicuas generalmente), pecho y vientre blancos, flancos azules. Espalda, rabadilla y cobertoras superiores de la cola azules. Alas azules con motas blancas. Cola azul con rectrices exteriores barradas de blanco y negro. Hembra: Parecida al macho adulto pero con franja pectoral azul (con parches rojizos), una franja pectoral inferior rojiza, y lados y flancos rojizos. Juvenil: Parecido a la hembra adulta pero sin franja pectoral inferior."
        self.aux.habitat="Prácticamente en cualquier cuerpo de agua (e.g., ríos, lagos, pantanos, estuarios, bahías). Sitios de posible observación en el bosque: únicamente registrado en el Estanque de los patos."
        self.aux.comments="Se alimenta básicamente de peces y ocasionalmente consume cangrejos, ranas, mamíferos pequeños, aves pequeñas, lagartijas y frutos. Después del martín-pescador de collar (Megaceryle torquata), el martín pescador norteño es el martín pescador más grande del país."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["pecho"]="blanco"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="azul"
        self.aux.caracteristics["alas"]="azul"
        self.aux.caracteristics["cola"]="azul"
        self.aux.image="sources/martin_pescador.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Carpintero del desierto"
        self.aux.description="Adulto: Macho: Ojos negros, pico gris oscuro (aparentemente negro). Corona roja, resto de la cabeza café-gris claro. Pecho café-gris claro, vientre amarillento, cobertoras inferiores de la cola barradas de blanco y negro. Espalda, rabadilla y alas barradas de blanco y negro. Cola negra con rectrices centrales y exteriores barradas de negro y blanco. Al vuelo exhibe parche blanquecino en la base de primarias. Hembra: Parecida al macho adulto pero sin corona roja. Juvenil: Parecido a la hembra adulta pero con el pico más corto"
        self.aux.habitat="Zonas áridas a semihúmedas (e.g., matorrales xerófitos, plantaciones). Sitios de posible observación en el bosque: principalmente eucaliptales, no obstante se puede observar en cualquier arbolado del bosque."
        self.aux.comments="Se alimenta de insectos, frutos, semillas y néctar floral. Durante la época reproductiva emite vocalizaciones fuertes y el cinceleo contra los árboles es mucho más frecuente. Al igual que la mayoría de los pájaros carpinteros, el carpintero del desierto anida en cavidades"
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="gris"
        self.aux.caracteristics["corona"]="rojo"
        self.aux.caracteristics["pecho"]="cafe"
        self.aux.caracteristics["vientre"]="amarillo"
        self.aux.caracteristics["espalda"]="blanco negro"
        self.aux.caracteristics["alas"]="blanco negro"
        self.aux.caracteristics["cola"]="blanco negro"
        self.aux.image="sources/carpintero_del_desierto.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Chupasavia maculado"
        self.aux.description="Adulto: Macho: Ojos negros, pico gris oscuro. Corona roja con borde negro, línea superciliar blanca, línea ocular negra, franja blanca de la frente a la nuca (unida a franja pectoral levemente amarillenta). Garganta roja con borde negro, vientre y cobertoras inferiores de la cola blancas jaspeadas de negro. Espalda barrada de blanco y negro. Alas negras con banda vertical blanca, plumas primarias barradas levemente de negro y blanco. Cola negra con rectrices centrales blancas barradas con negro. Hembra: Parecida al macho adulto pero con garganta blanca y con coloración amarillenta en pecho, cuello, nuca y espalda. Juvenil: Con mismos caracteres que los adultos pero con coloración general café amarillento claro."
        self.aux.habitat="Bosques de encino-pino, bordes de arbolados y huertos. Sitios de posible observación en el bosque: solamente registrado en áreas de casuarina y pino ubicadas al Norte del Estanque de los patos."
        self.aux.comments="Se alimenta de savia, insectos y frutos. Por su hábito alimenticio, el chupasavia maculado deja anillos de perforaciones en los árboles, elemento con el cual se puede inferir su presencia (en algunos casos). Este chupasavia es silencioso en comparación con los demás pájaros carpinteros, por lo que en ocasiones puede pasar desapercibido."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="gris"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="blanco negro"
        self.aux.caracteristics["alas"]="blanco negro"
        self.aux.caracteristics["cola"]="negro"
        self.aux.image="sources/chupasavia_maculado.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Mosquero copetón"
        self.aux.description="Adulto: (sexos similares) Ojos negros, maxila negra, mandíbula rosácea. Anillo ocular blanco proyectado hacia el dorso, cabeza café rojiza con copete prominente. Cara, garganta y pecho café-canela, vientre amarillo-canela. Nuca y espalda café-olivo. Alas café oscuro con dos barras alares blanquecinas y borde de secundarias y terciarias amarillo-canela. Cola café. Juvenil: Parecido al adulto pero con coloración general más pálida y con barras alares más anchas"
        self.aux.habitat="Bosques de niebla, de pino, pino-encino, encino y áreas semiáridas abiertas. Sitios de posible observación en el bosque: áreas con arbolados densos (e.g., zonas de eucalipto, pino y/o casuarina)."
        self.aux.comments="Se alimenta principalmente de insectos. Comúnmente se posa en perchas visibles. En caso de estar alarmado, su comportamiento se torna inquieto, mueve incesantemente la cola y eleva aún más su copete."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="cafe"
        self.aux.caracteristics["pecho"]="cafe-canela"
        self.aux.caracteristics["vientre"]="amarillo-canela"
        self.aux.caracteristics["alas"]="cafe"
        self.aux.caracteristics["cola"]="cafe"
        self.aux.image="sources/mosquero_copeton.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Pibí Tengofrío"
        self.aux.description="Adulto: (Sexos similares) Ojos negros, maxila negra, mandíbula rosácea. Anillo ocular blanquecino, loras gris claro, resto de la cabeza gris oscuro con copete prominente. Garganta y pecho gris claro, vientre amarillo deslavado. Alas oscuras con dos barras alares grises. Escapulares gris claro. Cola gris. Juvenil: Parecido al adulto pero con cobertoras inferiores de la cola y vientre amarillo claros; barras alares café claro."
        self.aux.habitat="Bosques de pino, pino-encino y encino. Sitios de posible observación en el bosque: Prácticamente en cualquier área del bosque."
        self.aux.comments="Se alimenta principalmente de insectos. Al igual que la mayoría de los tiránidos, este pibí se posa en perchas visibles y las utiliza como sitio base para acechar a los insectos que caza al vuelo."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="cafe"
        self.aux.caracteristics["pecho"]="gris"
        self.aux.caracteristics["vientre"]="amarillo"
        self.aux.caracteristics["alas"]="cafe"
        self.aux.caracteristics["cola"]="cafe"
        self.aux.image="sources/pibi_tengofrio.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Mosquero mínimo"
        self.aux.description="Adulto: (sexos similares) Ojos negros, pico negro con la base de la mandíbula amarillo-anaranjada. Anillo ocular y loras blancas, resto de la cabeza gris-café. Garganta y vientre blancos, pecho gris-café claro. Espalda y rabadilla grises. Alas negras con dos barras alares blancas; secundarias y terciarias con borde blanquecino. Cola emarginada gris. Juvenil: Parecido al adulto pero con toda la mandíbula inferior amarillo-anaranjada, dos barras alares café claro y vientre amarillo deslavado."
        self.aux.habitat="Bosques, pastizales y borde de caminos rurales. Sitios de posible observación en el bosque: prácticamente en cualquier área del bosque con excepción de áreas altamente frecuentadas por los usuarios del bosque y/o no arboladas."
        self.aux.comments="Se alimenta principalmente de insectos y arañas, ocasionalmente consume frutos. Debido a que algunas especies del género Empidonax son prácticamente indistinguibles entre sí, se recomienda identificarlos hasta nivel de género. No obstante, el canto es una de sus marcas de campo más confiables. El canto del mosquero mínimo es un psí metálico constante en grupos de 4 a 9 emisiones por vocalización (número de repeticiones variable)."
        self.aux.caracteristics["ojos"]="negro"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["pecho"]="gris cafe"
        self.aux.caracteristics["vientre"]="blanco"
        self.aux.caracteristics["espalda"]="gris"
        self.aux.caracteristics["alas"]="negro"
        self.aux.caracteristics["cola"]="gris"
        self.aux.image="sources/mosquetero_minimo.jpg"
        self.aves.append(self.aux)

        #self.aves.append(self.aux)

    def question(self,q,opt):
        options=[]
        options.append("Otro")
        for key in opt.keys():
            options.append(key)
        self.selection=StringVar()
        self.chooses=StringVar()
        self.chooses.set("Otro")
        self.instructions=Label(self.frame1,text="Seleccione el color de las siguientes partes del ave:\n\n",background='#353437',fg="white")
        self.instructions.configure(font=("Arial",25))
        self.instructions.pack()
        # self.image=ImageTk.PhotoImage(Image.open("bird_main_menu.png"))
        # self.panel=Label(self.frame1,image=self.image)
        # self.panel.pack(side="bottom",fill="both",expand="yes")
        self.caracteristica=Label(self.frame1,text=q,background='#353437',fg="white")
        self.caracteristica.configure(font=("Arial",25))
        self.caracteristica.pack()
        self.drop=OptionMenu(self.frame1,self.chooses,*options)
        self.drop.config(height=1,width=20)
        self.drop.pack()
        self.button=Button(self.frame1,text="Siguiente",command=self.clicked,bg="#7a7b7c",fg="white")
        self.button.config(height=2,width=10)
        self.button.pack()
        self.button.wait_variable(self.selection)
        self.cont = 0
        self.listo = False
        # self.panel.pack_forget()
        self.instructions.pack_forget()
        self.drop.pack_forget()
       # self.panel.pack_forget()
        self.button.pack_forget()
        self.caracteristica.pack_forget()
        return self.selection
        
    def clicked(self):
        print(self.chooses.get())
        self.selection.set(self.chooses.get())




    def clasify(self):
        #self.load_birds()
        self.loadall()
        self.possible_aves=copy.copy(self.aves)
        self.possible_rules={}
        self.rules={}
        other=True
        while(other):
            self.possible_rules={}
            for ave in self.possible_aves:
                for key in ave.caracteristics.keys():
                    if(key not in self.rules):
                        if(key not in self.possible_rules):
                            self.possible_rules[key]={}
                        if(ave.caracteristics[key] not in self.possible_rules[key]):
                            self.possible_rules[key][ave.caracteristics[key]]=1
                        else:
                            self.possible_rules[key][ave.caracteristics[key]]+=1
                        
            color=StringVar()
            caracteristic=""
            for key in self.possible_rules.keys():
                color.set(self.question(key,self.possible_rules[key]).get())
                caracteristic=key
                self.rules[key]=color.get()
                print(color.get())
                break
            index=0
            elements=len(self.possible_aves)
            while index < elements:
                print(self.possible_aves[index].name)
                if(caracteristic not in self.possible_aves[index].caracteristics):
                    self.possible_aves[index].caracteristics[caracteristic]="otro"
                if(self.possible_aves[index].caracteristics[caracteristic]!=color.get()):
                    del self.possible_aves[index]
                    elements-=1
                else:
                    index+=1
            
            
            if(len(self.possible_aves)<2):
                other=False
            
        
        if(len(self.possible_aves)==1):
            avetoshow=self.possible_aves[0]

            self.visual=visualizer(self.menu_window,self.frame1,avetoshow,self.rules,self)
        else:
            self.visual=visualizer(self.menu_window,self.frame1,self.default_ave,self.rules,self)
        
        self.visual.show()
    

    def show(self):
        self.title.pack()
        self.clasify()
        

    #Oculta la vista del apartado de clasificación
    def hide(self):
        self.title.pack_forget()
        self.menuButton.pack_forget()
        
  
    #Muestra la vista principal
    def main_window(self):
        self.hide()
        
        self.menu_window.show()

    def closing(self):
        self.visual.closing()
        del self

   

class main_menu:
    def __init__(self) -> None:
        
        
        openImage=Image.open("sources/bird.jpg")
        img=openImage.resize((1550,800))
        # self.image=ImageTk.PhotoImage(img)
                
        # self.panel=Label(root,image=self.image)
        self.frame1 = Frame(root,background='#353437')
        self.title=Label(self.frame1, text="Clasificador de aves\n\n\n",font=("Arial",25),background='#353437',fg="white")
        self.clasifier_button=Button(self.frame1,text="Encontrar ave",command=self.show_clasifier_window,bg="#7a7b7c",fg="white")
        self.clasifier_button.config(height=5,width=30)
        self.clasifier_window = clasifier(self,self.frame1)

    #Muestra la vista principal
    def show(self):
        
        # self.panel.place(x=0,y=0)
        self.frame1.pack(pady = 20 )
        self.title.pack()
        self.clasifier_button.pack()
    
    #Oculta la vista principal
    def hide(self):
        self.title.pack_forget()
        self.clasifier_button.pack_forget()

    #Muestra la vista del clasificador
    def show_clasifier_window(self):
        self.hide()
        
        #self.clasifier_window.load_birds()
        self.clasifier_window.clasify()

    #Funcion para terminar los procesos 
    def closing(self):
        self.clasifier_window.closing()
        del self


if __name__ == "__main__":
    try:
        root = Tk()
        def on_closing():
            program.closing()
            root.destroy()
            
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.title("Sistema experto")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d" % (w, h))
        root.configure(bg='#353437')
        program=main_menu()
        program.show()
        root.mainloop()
    except:
        quit()