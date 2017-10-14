from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from firebase import firebase

token = 'LQdeuWHXvtgCg5Sdx3JUfuGV1ZaUmfbA7Nah5hE3'
url = 'https://dmini-internet-of-things.firebaseio.com/'
firebase = firebase.FirebaseApplication(url, token)


class GuiKivy(App):

    def build(self):
        layout = GridLayout(cols=2)
        self.labelYellow = Label(text='Yellow LED', font_size=24, halign='center', valign='middle')
        self.labelRed = Label(text='Red LED', font_size=24, halign='center', valign='middle')
        self.toggleYellow = ToggleButton(text='off', on_press=self.updateStatus)
        self.toggleRed = ToggleButton(text='off', on_press=self.updateStatus)
        status_list = firebase.get('/lights')
        self.toggleRed.state = status_list[1]
        self.toggleYellow.state = status_list[0]
        if self.toggleRed.state == 'normal':
            self.toggleRed.text = 'off'
        elif self.toggleRed.state == 'down':
            self.toggleRed.text = 'on'
        if self.toggleYellow.state == 'normal':
            self.toggleYellow.text = 'off'
        elif self.toggleYellow.state == 'down':
            self.toggleYellow.text = 'on'
        layout.add_widget(self.labelYellow)
        layout.add_widget(self.toggleYellow)
        layout.add_widget(self.labelRed)
        layout.add_widget(self.toggleRed)
        return layout

    def updateStatus(self, instance):
        if self.toggleRed.state == 'normal':
            self.toggleRed.text = 'off'
        elif self.toggleRed.state == 'down':
            self.toggleRed.text = 'on'
        if self.toggleYellow.state == 'normal':
            self.toggleYellow.text = 'off'
        elif self.toggleYellow.state == 'down':
            self.toggleYellow.text = 'on'
        status_list = [self.toggleYellow.state,self.toggleRed.state]
        firebase.put('/lights','/',status_list)


# status_list = firebase.get('/lights')
# print status_list
GuiKivy().run()
