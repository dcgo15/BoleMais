from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class BoleMais(App):
    def build(self):
        lbl = GridLayout(cols = 1, row_force_default=True, row_default_height=40,
                         spacing=15, padding = 10)
        self.label = Label(text="BoleMais")
        self.nome = TextInput(text="Digite seu nome aqui")
        
        self.email = TextInput(text="Digite seu email aqui")
        submit = Button(text="Salvar", on_press = self.submit)
        lbl.add_widget(self.label)
        lbl.add_widget(self.nome)
        lbl.add_widget(self.email)
        lbl.add_widget(submit)
        return lbl

    def submit(self, obj):
        print("Nome: ", self.nome.text)
        print("Email: ", self.email.text)

BoleMais().run()
