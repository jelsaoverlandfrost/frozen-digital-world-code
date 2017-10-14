from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        self.mylabel = Label(text='It\'s fun to program', font_size = 72)
        self.mylabel.bind(on_touch_down = self.alternate)
        self.state = 0
        return self.mylabel
    def alternate(self,instance,touch):
        if self.state == 0:
            self.mylabel.text = 'It\'s fun to program'
            self.state = 1
        elif self.state == 1:
            self.mylabel.text = 'Programming is fun'
            self.state = 0

if __name__ == '__main__':
    MyApp().run()