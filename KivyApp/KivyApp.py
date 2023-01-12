from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class TrovaTemperatura(App) :
    #funzione utilizzata per costruire la struttura del'app
    def build(self) :
        #crea griglia 
        self.window = GridLayout()
        #N colonne
        self.window.cols = 1
        #gestione margini
        self.window.size_hint= (0.8, 0.9)
        #posizionamento centrale dell'app
        self.window.pos_hint= {"center_x": 0.5 , "center_y": 0.5}
        #dimensione x, y
        Window.size = (360, 640)
        #impostazione sfondo
        self.window.add_widget(Image(source="logo.png"))
        
        #creo delle variabili per widget
        
        self.testo_input = TextInput( 
                                size_hint= (1, 0.2), #dimensione percentuale (100%, 20%)
                                font_size = '20sp', #dimensione caratteri 20 RELATIVO
                                padding_y = '12sp',
                                halign = 'center'
                                )
        self.bottone = Button(
                            text="VIA!",
                            size_hint= (1, 0.2),
                            bold = True,
                            background_color = '#0099ff'
                            )
        self.testo_output = Label(
                                text="Cerca una città ...",
                                font_size= '20sp',
                                color = '#007dd1'
                                )
        #widget
        self.window.add_widget(self.testo_input)
        self.window.add_widget(self.bottone)
        self.window.add_widget(self.testo_output)
        #logica
        self.bottone.bind(on_press = self.trova_temp)
        
        return self.window
    
    def trova_tempo(self, instance) :
        self.testo_output.text = f"Oggi a {self.testo_input.text} Ci saranno " 
        #la 'f' posta prima della stringa la rende formattata
        
#Lancio dell'applicazione
TrovaTemperatura().run()