from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class pathapp(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Путь'))
        self.path = TextInput(multiline=False)
        self.add_widget(self.path)
        self.submit_button = Button(text='Submit')
        self.label = TextInput(text="")
        self.submit_button.on_press = self.submit
        self.add_widget(self.submit_button)
        self.add_widget(self.label)

    def submit(self):
        try:
            f = open('%s' % self.path.text)
            self.label.text = f.read()
        except Exception as e:
            self.label.text = "%s" % e


class MyApp(App):
    def build(self):
        return pathapp()


MyApp().run()



