from kivy.app import App
from dmt.main_screen import MainScreen

class DMTApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    DMTApp().run()