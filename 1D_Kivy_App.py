from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage

class mainScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)

    def