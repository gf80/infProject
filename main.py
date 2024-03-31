from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
import bd

Builder.load_file('main_screen.kv')


class TransparentButton(Button):
    pass


class MainScreen(MDScreen):
    pass


class SavedGroupScreen(MDScreen):
    pass


class CreateGroupScreen(MDScreen):

    def create(self):
        app = MDApp.get_running_app()
        conn, cursor = app.conn, app.cursor
        name = self.ids.name_group.text
        print(name)
        if name != "":
            bd.create_record(cursor, "lessons", (None, name,))
            conn.commit()
            self.manager.current = "main_screen"
        else:
            self.ids.warning.text = "Поле не может быть пустым"


class MyApp(MDApp):

    # conn, cursor = bd.connect_to_bd("info.db")
    # bd.create_table(cursor, "lessons", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT")
    # bd.create_table(cursor, "lesson_info", "id INTEGER PRIMARY KEY AUTOINCREMENT, id_group INTEGER, name TEXT, "
    #                                        "description TEXT, files TEXT, photo TEXT")
    # bd.create_table(cursor, "lectures", "id INTEGER PRIMARY KEY AUTOINCREMENT, id_group INTEGER, id_lesson INTEGER, "
    #                                     "name TEXT, description TEXT, phone TEXT, auditorium TEXT, departament TEXT")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        sm = MDScreenManager()
        sm.add_widget(MainScreen(name="main_screen"))
        sm.add_widget(SavedGroupScreen(name="saved_group_screen"))
        sm.add_widget(CreateGroupScreen(name="create_group_screen"))
        return sm


if __name__ == "__main__":
    MyApp().run()