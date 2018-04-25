from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class MyLayout(Screen):

    def __init__(self, **kwargs):
        Builder.load_file("grid_example.kv")
        super(MyLayout, self).__init__(**kwargs)


class MyApp(App):

    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()