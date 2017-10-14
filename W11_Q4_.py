from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = BoxLayout()
        self.button1 = Button(text='Settings')
        self.button2 = Button(text='Quit')
        self.layout.add_widget(self.button1)
        self.layout.add_widget(self.button2)
        self.button1.bind(on_press=self.change_to_setting)
        self.button2.bind(on_press=self.quit_app)
        self.add_widget(self.layout)

    def change_to_setting(self, value):
        self.manager.transition.direction = 'left'
        self.manager.current = 'settings'

    def quit_app(self, value):
        App.get_running_app().stop()


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = BoxLayout()
        self.label = Label(text='Settings Screen')
        self.button3 = Button(text='Back to Menu')
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button3)
        self.button3.bind(on_press=self.change_to_menu)
        self.add_widget(self.layout)

    def change_to_menu(self, value):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'


class SwitchScreenApp(App):
    def build(self):
        sm = ScreenManager()
        ms = MenuScreen(name='menu')
        st = SettingsScreen(name='settings')
        sm.add_widget(ms)
        sm.add_widget(st)
        sm.current = 'menu'
        return sm


if __name__ == '__main__':
    SwitchScreenApp().run()