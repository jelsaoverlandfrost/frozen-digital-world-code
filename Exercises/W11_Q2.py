from kivy.app import App
from kivy.uix.label import Label


class SlideDetectApp(App):
	def build(self):
		self.myLabel = Label(text='Slide!', font_size=72)
		self.myLabel.bind(on_touch_move=self.detect)
		return self.myLabel

	def detect(self, instance, touch):
		# if not instance.collide_point(touch.x, touch.y):
		# 	return False
		if touch.dx < -40:
			self.myLabel.text = 'Slide Left'
			# return self.myLabel
		if touch.dx > 40:
			self.myLabel.text = 'Slide Right'
			# return self.myLabel
		if touch.dy < -40:
			self.myLabel.text = 'Slide Down'
			# return self.myLabel
		if touch.dy > 40:
			self.myLabel.text = 'Slide Up'
			# return self.myLabel
		return True


if __name__ == '__main__':
	SlideDetectApp().run()
