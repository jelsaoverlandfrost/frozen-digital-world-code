from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyLabel(Label):
    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding = (20, 20)


class Investment(App):
    def build(self):
        layout = GridLayout(cols=2)
        self.label1 = MyLabel(text="Investment Amount", font_size=24, halign='center', valign='middle')
        self.label2 = MyLabel(text="Years", font_size=24, halign='center', valign='middle')
        self.label3 = MyLabel(text="Annual Interest Rate", font_size=24, halign='center', valign='middle')
        self.label4 = MyLabel(text="Future Value", font_size=24, halign='center', valign='middle')
        self.textbox1 = TextInput(text='Input', multiline=False)
        self.textbox2 = TextInput(text='Input', multiline=False)
        self.textbox3 = TextInput(text='Input', multiline=False)
        self.txt_future_val = MyLabel(text='', font_size=24, halign='center', valign='middle')
        btn = Button(text="Calculate", on_press=self.calculate, font_size=24)
        layout.add_widget(self.label1)
        layout.add_widget(self.textbox1)
        layout.add_widget(self.label2)
        layout.add_widget(self.textbox2)
        layout.add_widget(self.label3)
        layout.add_widget(self.textbox3)
        layout.add_widget(self.label4)
        layout.add_widget(self.txt_future_val)
        layout.add_widget(btn)
        return layout

    def calculate(self, instance):
        inv_amt = float(self.textbox1.text)
        years = float(self.textbox2.text)
        mth_int_rate = float(self.textbox3.text)
        self.txt_future_val.text = '$' + str(round(inv_amt * ((1 + mth_int_rate / 1200) ** (years * 12)), 2))


Investment().run()
