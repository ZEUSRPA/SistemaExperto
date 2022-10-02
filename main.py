from ctypes import sizeof
from operator import length_hint
from select import select
from tkinter import *  
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import threading
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
    def __init__(self,menu,bird,rules)->None:
        self.name=Label(root,text="AVE")
        self.name.configure(font=("Arial",50))
        self.size=Label(root,text="AVE")
        self.size.configure(font=("Arial",40))
        self.description=Label(root,text="AVE")
        self.description.configure(font=("Arial",40))
        self.habitat=Label(root,text="AVE")
        self.habitat.configure(font=("Arial",40))
        self.comments=Label(root,text="AVE")
        self.comments.configure(font=("Arial",40))
        self.explanation=Label(root,text="AVE")
        self.explanation.configure(font=("Arial",40))
        self.menu_window=menu
        self.bird=bird
        self.rules=rules
        self.menuButton=Button(root,text="Main Menu",command=self.main_window,bg="orange")
        self.menuButton.config(height=2,width=15)
        self.showBird()


    def show(self):
        self.name.pack()
        self.size.pack()
        self.description.pack()
        self.habitat.pack()
        self.comments.pack()
        self.explanation.pack()
    
        self.menuButton.pack(side=TOP)
    
    #Oculta la vista de la descripción del ave
    def hide(self):
        self.name.pack_forget()
        
        self.size.pack_forget()
        self.description.pack_forget()
        self.habitat.pack_forget()
        self.comments.pack_forget()
        self.explanation.pack_forget()
        self.menuButton.pack_forget()

    def showBird(self):
        self.name=Label(root,text=self.bird.name)
        self.name.configure(font=("Arial",35))
        self.size=Label(root,text=self.bird.size,wraplength=800)
        self.size.configure(font=("Arial",15))
        self.description=Label(root,text=self.bird.description,wraplength=800)
        self.description.configure(font=("Arial",15))
        self.habitat=Label(root,text=self.bird.habitat,wraplength=800)
        self.habitat.configure(font=("Arial",15))
        self.comments=Label(root,text=self.bird.comments,wraplength=800)
        self.comments.configure(font=("Arial",15))
        exp="\n\n\nEl ave fue encontrada en base a las siguientes características:\n"
        for key in self.rules.keys():
            exp+=key+":"+self.rules[key]+"\n"

        self.explanation=Label(root,text=exp,wraplength=800)
        self.explanation.configure(font=("Arial",15))
    

    #Muestra la vista principal
    def main_window(self):
        self.hide()
        self.menu_window.show()
    
    def closing(self):
        del self

        
#En esta clase se tienen los metodos para clasificar
class clasifier:
    #Constructor de la clase
    def __init__(self,menu) -> None:
        self.title=Label(root,text="Clasificador de aves")
        self.title.configure(font=("Arial",35))
        self.menu_window=menu
        self.menuButton=Button(root,text="Main Menu",command=self.main_window,bg="orange")
        self.menuButton.config(height=10,width=50)
        self.good=False
        self.doing=True
        self.aves=[]
        self.default_ave=bird()
        self.load_birds()
        self.rules={}
        self.visual=visualizer(self.menu_window,self.aves[0],self.rules)

        self.possible_rules={}
        self.possible_aves=[]

        
        
    def load_birds(self):
        self.default_ave.name="Desconocida"

        
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


        self.aves.append(self.aux)



    def question(self,q,opt):
        options=[]
        options.append("otro")
        for key in opt.keys():
            options.append(key)
        self.selection=StringVar()
        self.chooses=StringVar()
        self.chooses.set("otro")
        self.instructions=Label(root,text="Seleccione el color de las siguientes partes del ave:\n\n")
        self.instructions.configure(font=("Arial",25))
        self.instructions.pack()
        self.caracteristica=Label(root,text=q)
        self.caracteristica.configure(font=("Arial",25))
        self.caracteristica.pack()
        self.drop=OptionMenu(root,self.chooses,*options)
        self.drop.config(height=1,width=20)
        self.drop.pack()
        self.button=Button(root,text="Siguiente",command=self.clicked,bg="light green")
        self.button.config(height=2,width=10)
        self.button.pack()
        self.button.wait_variable(self.selection)
        self.cont=0
        self.listo = False
        self.instructions.pack_forget()
        self.drop.pack_forget()
        self.button.pack_forget()
        self.caracteristica.pack_forget()
        return self.selection
        
    def clicked(self):
        print(self.chooses.get())
        self.selection.set(self.chooses.get())




    def clasify(self):
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

            self.visual=visualizer(self.menu_window,avetoshow,self.rules)
        else:
            self.visual=visualizer(self.menu_window,self.default_ave,self.rules)
        
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
        self.title=Label(root, text="Clasificador de aves\n\n\n",font=("Arial",25))
        self.clasifier_button=Button(root,text="Encontrar ave",command=self.show_clasifier_window,bg="sky blue")
        self.clasifier_button.config(height=5,width=30)
        self.clasifier_window = clasifier(self)

    #Muestra la vista principal
    def show(self):
        self.title.pack()
        self.clasifier_button.pack()
    
    #Oculta la vista principal
    def hide(self):
        self.title.pack_forget()
        self.clasifier_button.pack_forget()

    #Muestra la vista del clasificador
    def show_clasifier_window(self):
        self.hide()
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
        root.geometry("1000x800")
        program=main_menu()
        program.show()
        root.mainloop()
    except:
        quit()