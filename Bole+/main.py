from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder

class Inicio(Screen):
    pass

class Calcul(Screen):
    pass

class Boletim(Screen):
    pass

class Janela(ScreenManager):
    pass

kiv = Builder.load_file("janela.kv")

#PEGAR DEPOIS
#on_press:print(float(Num.text) - float(Ndois.text))


class BoleMais(App):
    def build(self):
        return kiv
    


        '''
        self.L = pandas.DataFrame({str(self.Materia.text), float(self.Nota1.text), float(self.Nota2.text),
                                   float(self.Nota3.text)})

        self.Materia.text = ''
        self.Nota1.text = ''
        self.Nota2.text = ''
        self.Nota3.text = ''
        print(self.L)
        with pandas.ExcelWriter('info_boletim.xlsx') as writer:
            self.L.to_excel(writer)
        '''
    '''
    def calculo(self):
        diferença = float(Num.text) - float(Ndois.text)
        lbl = Label(text=diferença)
        self.add_widget(lbl)
       ''' 
        

if __name__ == "__main__":
    BoleMais().run()

#text: "Digite o minimo de pontos para passar"
#text: "Quantos voce tem"
