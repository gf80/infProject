from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
import json

Builder.load_file('main_screen.kv')

class MainScreen(Screen):
    pass

class SavedGroupScreen(Screen):
    pass

class CreateGroupScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main_screen"))
        sm.add_widget(SavedGroupScreen(name="saved_group_screen"))
        sm.add_widget(CreateGroupScreen(name="create_group_screen"))
        return sm

if __name__ == "__main__":
    MyApp().run()