import kivy

kivy.require("1.9.1")

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock
from threading import Thread
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty

from kivy.lang import Builder

Builder.load_file('screen1.kv')


class ControlScreenLayout(Screen, BoxLayout):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)

    def nextscreen(self, value):
        self.manager.transition.direction = 'left'
        self.manager.current = 'infoScreen'

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


class ScreenLayout(Screen, BoxLayout):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)

        def starter(self):
            Clock.schedule_interval(self.update, 0.5)

        def update(self, dt):
            pass
            # TODO get the video (update every 0.5 seconds)
            # or just get an image that we update...
            # self.ids.vid_id.img = pass
            # self.ids.Identification_Display_id.txt = pass #TODO get list of identified objects

    def nextscreen(self, value):
        self.manager.transition.direction = 'right'
        self.manager.current = 'controlScreen'


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("screen1.kv")


class ScreensA(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        # sm = ScreenManager()
        # ms = ScreenLayout(name='infoScreen')
        # st = ControlScreenLayout(name='controlScreen')
        # sm.add_widget(ms)
        # sm.add_widget(st)
        # sm.current = 'infoScreen'
        return presentation


if __name__ == '__main__':
    ScreensA().run()
