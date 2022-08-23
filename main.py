import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager


class OpenScreenGrid(GridLayout):
    def __init__(self, **kwargs):
        super(OpenScreenGrid, self).__init__(**kwargs)
        self.cols = 1

        self.topGrid = GridLayout()
        self.topGrid.cols = 2

        self.topGrid.add_widget(Label(text="Drone Name: "))
        self.name = TextInput(multiline=False)
        self.topGrid.add_widget(self.name)

        self.topGrid.add_widget(Label(text="Date: "))
        self.date = TextInput(multiline=False)
        self.topGrid.add_widget(self.date)

        self.topGrid.add_widget(Label(text="Flight area: "))
        self.area = TextInput(multiline=False)
        self.topGrid.add_widget(self.area)

        self.add_widget(self.topGrid)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        date = self.date.text
        area = self.area.text

        print(name)
        print(date)
        print(area)

        self.name.text = ""
        self.date.text = ""
        self.area.text = ""


class OpenScreen(Screen):

    def __init__(self, **kwargs):
        super(OpenScreen, self).__init__(**kwargs)

        # self.add_widget(OpenScreenGrid)


# class WhichModelScreen(Screen):
#     def
# def buttonScreen(GridLayout):
#     def __init__(self, **kwargs):
#         super(buttonScreen, self).__init__(**kwargs)


class CSCApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(OpenScreen(name="OpenScreen"))
        # sm.current_screen()
        return sm


if __name__ == "__main__":
    CSCApp().run()
