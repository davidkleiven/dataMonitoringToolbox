from kivy.uix.screenmanager import Screen
from kivy.app import App
from constants import NAVIGATION_MAP

class MainScreen(Screen):
    def execute_cmd(self):
        cmd = self.ids.cmdField.text

        expected_output = self.ids.typeSpinner.text
        if expected_output == 'Stats':
            app = App.get_running_app()
            app.screen_manager.current = 'TextOutputScreen'
            self._execute_text_output(cmd)
        return cmd

    def _execute_text_output(self, cmd):
        app = App.get_running_app()
        if app.connection is None:
            print("No connection!")
            return
        client = app.connection
        _, stdout, _ = client.exec_command(cmd)
        stdout = stdout.readlines()
        
        output_screen = app.screen_manager.get_screen('TextOutputScreen')
        output = ''.join(stdout)
        output_screen.ids.output.text = 'Swipe right to return\n\n' + output



    def navigate(self, text):
        app = App.get_running_app()
        app.screen_manager.current = NAVIGATION_MAP[text]

    def on_enter(self):
        self.ids.menuSpinner.text = 'Main'
        