from kivy.uix.screenmanager import Screen
from kivy.app import App
from constants import NAVIGATION_MAP

class MainScreen(Screen):
    def execute_cmd(self):
        cmd = self.ids.cmdField.text
        return cmd

    def navigate(self, text):
        app = App.get_running_app()
        app.screen_manager.current = NAVIGATION_MAP[text]

    def on_enter(self):
        self.ids.menuSpinner.text = 'Main'
        