from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


#Nao coloque letra minuscula
#verifique a identaçao do kv
class Primeira(Screen):
    pass

class Segunda(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("tela.kv")


class MeuApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MeuApp().run()
