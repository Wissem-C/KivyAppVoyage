from re import S
from turtle import textinput
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from searchpopupmenu import SearchPopupMenu
from kivy.uix.popup import Popup
from kivy_garden.mapview import MapSource, MapView
from kivymd.uix.card import MDCard
from kivymd.uix.screen import Screen
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty
import requests
import datetime
from kivymd.uix.label import MDLabel


def get_date():
        now = str(datetime.datetime.today())         
        return(now)



Window.clearcolor = (1,1,1,1)
Window.size = (360,600)

class Content_voyage(BoxLayout):
    pass

class Content_point_interet(BoxLayout):
    pass


class MainApp(MDApp): 
    url = 'https://carnetprojet-default-rtdb.europe-west1.firebasedatabase.app/'
    dialog = None
    nom_input = StringProperty()
    

   

    def show_confirmation_dialog_pt_interet(self):
            self.dialog = MDDialog(
                title="Point d'interet:",
                type="custom",
                content_cls=Content_point_interet(),  
                buttons=[
                    MDFlatButton(
                        text="AJOUT",
                        theme_text_color="Custom",
            
                        on_release= self.get_data_pt_interet,
                    ),
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
            
                        on_release=lambda _:  self.dialog.dismiss()
                    ),
                ],   
            )
            self.dialog.content_cls.ids.date_input.text = get_date()

            self.dialog.open()
    
    
    def show_confirmation_dialog_voyage(self):
            self.dialog = MDDialog(
                title="Nouveau Voyage :",
                type="custom",
                content_cls=Content_voyage(),
                buttons=[
                    
                    MDFlatButton(
                        text="DEMARRER",
                        theme_text_color="Custom",
                        on_release =  self.get_data_voyage,
                    ),
                    
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        on_release=lambda _:  self.dialog.dismiss()
                    ),
                ],   
            )
            self.dialog.content_cls.ids.date_input.text = get_date()
            self.dialog.open()
            
    def get_data_voyage (self,obj):
        print(self.dialog.content_cls.ids.nom_input.text)
        self.dismiss_dialog()
    
    def get_data_pt_interet (self,obj):
        print(self.dialog.content_cls.ids.nom_input.text)
        print(self.dialog.content_cls.ids.type_input.text)
        print(self.dialog.content_cls.ids.date_input.text)
        print(self.dialog.content_cls.ids.commentaire_input.text)
        print(self.dialog.content_cls.ids.note_input.text)
        self.dismiss_dialog()
        
    def dismiss_dialog(self):
        self.dialog.dismiss()
        
        
        
        
if __name__ == "__main__":
    MainApp().run()