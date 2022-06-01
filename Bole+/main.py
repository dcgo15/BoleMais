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


class BoleMais(App):
    def build(self):
        return kiv

if __name__ == "__main__":
    BoleMais().run()
