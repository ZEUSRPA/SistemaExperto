from ctypes import sizeof
from logging import RootLogger
from operator import length_hint
from select import select
from tkinter import *
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
        self.image=""

        #Caracteristics
        self.caracteristics={}
        

class visualizer:
    def __init__(self,menu,frame1,bird,rules)->None:
        self.frame1=frame1
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
        self.menuButton=Button(self.frame1,text="Menu Principal",command=self.main_window,bg="#7a7b7c", fg="white")
        self.menuButton.config(height=2,width=15)
        self.showBird()


    def show(self):
        self.name.pack()
        self.image.pack()
        self.size.pack()
        self.description.pack()
        self.habitat.pack()
        self.comments.pack()
        self.explanation.pack()
    
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
        
        self.loadall()
        
    def loadall(self):
        
        self.good=False
        self.doing=True
        self.aves=[]
        self.default_ave=bird()
        self.load_birds()
        self.rules={}
        
        self.visual=visualizer(self.menu_window,self.frame1,self.aves[0],self.rules)
        self.possible_rules={}
        self.possible_aves=[]

        
        
    def load_birds(self):
        self.default_ave.name="Desconocida"
        self.default_ave.image="sources/garceta_pie_dorado.jpg"

        
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
        self.aux.caracteristics["pecho"]="blanquecino"
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
        self.possible_aves=self.aves
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

            self.visual=visualizer(self.menu_window,self.frame1,avetoshow,self.rules)
        else:
            self.visual=visualizer(self.menu_window,self.frame1,self.default_ave,self.rules)
        
        self.visual.show()
    

    def show(self):
        self.title.pack()
        self.menuButton.pack(side=TOP)
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