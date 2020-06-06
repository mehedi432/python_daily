from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import os


class ConnectPage(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        if os.path.isfile('previous_info.txt'):
            with open('previous_info.txt', 'r') as f:
                data = f.read().split(',')
                ip = data[0]
                port = data[1]
                name = data[2]
                password = data[3]
        else:
            ip = ''
            port = ''
            name = ''
            password = ''

        self.add_widget(Label(text="IP:"))
        self.ip = TextInput(text=ip, multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port:"))
        self.port = TextInput(text=port, multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Name:"))
        self.name = TextInput(text=name, multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(text=password, multiline=False)
        self.add_widget(self.password)

        self.join = Button(text="Join", on_press=self.join_button)
        self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.join)

    def join_button(self, instance):
        ip = self.ip.text
        port = self.port.text
        name = self.name.text
        password = self.password.text

        with open('previous_info.txt', 'w') as f:
            f.write(f"{ip}, {port}, {name}, {password}")
        print(f"Joining as {ip}:{port} as {name}")


class Main(App):
    def build(self):
        return ConnectPage()


if __name__ == "__main__":
    Main().run()
