from kivy.uix.screenmanager import Screen
from kivy.app import App
from constants import NAVIGATION_MAP
import paramiko

class NewConnection(Screen):
    def navigate(self, text):
        app = App.get_running_app()
        app.screen_manager.current = NAVIGATION_MAP[text]

    def on_enter(self):
        self.ids.menuSpinner.text = 'New connection'

    def connect(self):
        app = App.get_running_app()
        if app.connection is not None:
            app.connection.close()
        self.ids.statusField.text = 'STATUS: Connecting...'
        app.connection = paramiko.SSHClient()
        app.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        username = self.ids.usernameInput.text
        host = self.ids.hostInput.text
        port = int(self.ids.portInput.text)
        passwd = self.ids.passwdInput.text
        try:
            app.connection.connect(hostname=host, port=port, password=passwd, username=username)
            self.ids.statusField.text = 'STATUS: Successfully connected'
            sm = app.screen_manager
            sm.transition.direction = 'right'
            sm.current = 'MainScreen'
        except Exception as exc:
            self.ids.statusField.text = 'STATUS: Could not connect'
            print(str(exc))
