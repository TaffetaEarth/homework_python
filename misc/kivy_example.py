from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.submit_button = Button(text='Submit')
        self.submit_button.on_release = self.submit
        self.add_widget(self.submit_button)
        self.clear_button = Button(text='Clear')
        self.clear_button.on_release = self.clear
        self.add_widget(self.clear_button)

    def submit(self):
        print(self.username.text)
        print(self.password.text)

    def clear(self):
        self.username.text = ''
        self.password.text = ''


class MyApp(App):

    def build(self):
        return LoginScreen()


MyApp().run()
