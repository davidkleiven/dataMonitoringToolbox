from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from main_screen import MainScreen
from new_connection import NewConnection
from text_output_screen import TextOutputScreen

Builder.load_file("master_layout.kv")

class DMTApp(App):
    connection = None
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(MainScreen(name='MainScreen'))
        self.screen_manager.add_widget(NewConnection(name='NewConnection'))
        self.screen_manager.add_widget(TextOutputScreen(name='TextOutputScreen'))
        return self.screen_manager

    def on_stop(self):
        if self.connection is not None:
            self.connection.close()
            print("Closing connection...")


if __name__ == '__main__':
    DMTApp().run()