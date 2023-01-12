from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class TrovaTemperatura(App) :
    #funzione utilizzata per costruire la struttura del'app
    def build(self) :
        #crea griglia 
        self.window = GridLayout()
        #N colonne
        self.window.cols = 1
        #dimensione x, y
        Window.size = (360, 640)
        
#Lancio dell'applicazione
TrovaTemperatura().run()