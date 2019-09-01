from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.app import App



class TextOutputScreen(Screen):
    initial_touch_x = None
    initial_touch_y = None
    def on_touch_down(self, touch):
        self.initial_touch_x = touch.x
        self.initial_touch_y = touch.y

    def on_touch_up(self, touch):
        diff_x = touch.x - self.initial_touch_x
        diff_y = touch.y - self.initial_touch_y

        if self._is_swipe_right_move(diff_x, diff_y):
            app = App.get_running_app()
            app.screen_manager.transition.direction = 'right'
            app.screen_manager.current = 'MainScreen'
    
    def _is_swipe_right_move(self, diff_x, diff_y):
        size = Window.size
        if diff_x/size[0] > 0.6 and abs(diff_y)/size[1] < 0.2:
            return True
        return False

    def _is_scroll_move(self, diff_x):
        size = Window.size
        return abs(diff_x/size[0]) < 0.2
            
