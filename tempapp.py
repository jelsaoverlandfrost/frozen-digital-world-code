from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage

import io


class MainScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)

    def starter(self):
        Clock.schedule_interval(self.update, 0.5)

    def update(self, dt):
        self.ids.camImg_id.reload()  # TODO get actual video images (if the folder keeps receiving an influx of replace images...)

        # self.ids.Identification_Display_id.txt = pass #TODO get list of identified objects

    pass


class AnotherScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)

    def forward(self):
        pass

    def backwards(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def stop(self):
        pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("tempkivy.kv")


class MainApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return presentation


if __name__ == "__main__":
    MainApp().run()
