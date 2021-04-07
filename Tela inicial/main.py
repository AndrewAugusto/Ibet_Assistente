from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class sm(ScreenManager):
    def MudarMenu(self):
        self.current = 'menu'
        self.nome = self.get_screen('pinicial').ids.nome.text
        self.email = self.get_screen('pinicial').ids.email.text
        #self.get_screen('menu').ids.infos.text = f'Olá {self.nome}, seu email: {self.email}'
        
 
    def MudarPaginaInicial(self):
        self.current = 'pinicial'

class PaginaInicial(Screen):
    pass

class MenuInicial(Screen):
    pass



class teste(App):
    def build(self):
        return sm()

if __name__ == "__main__":
    teste().run()