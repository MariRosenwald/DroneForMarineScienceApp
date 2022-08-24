import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.videoplayer import VideoPlayer


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

        sm.current = "WM"


class OpenScreen(Screen):

    def __init__(self, **kwargs):
        super(OpenScreen, self).__init__(**kwargs)

        self.add_widget(OpenScreenGrid())


class WhichModelGrid(GridLayout):
    def __init__(self, **kwargs):
        super(WhichModelGrid, self).__init__(**kwargs)
        self.cols = 1

        self.sharkbtn = Button(text="Shark Model", font_size=40)
        self.sharkbtn.bind(on_press=self.pressedShark)
        self.add_widget(self.sharkbtn)

        self.cowbtn = Button(text="Cow Model", font_size=40)
        self.cowbtn.bind(on_press=self.pressedCow)
        self.add_widget(self.cowbtn)

        self.backBtn = Button(text="back", font_size=40)
        self.backBtn.bind(on_press=self.pressedBack)
        self.add_widget(self.backBtn)

    def pressedShark(self, instance):
        print("shark")

        sm.current = "SharkModelScreen"

    def pressedCow(self, instance):
        print("cow")

        sm.current = "OpenScreen"

    def pressedBack(self, instance):
        print("back")

        sm.current = "OpenScreen"


class WhichModelScreen(Screen):
    def __init__(self, **kwargs):
        super(WhichModelScreen, self).__init__(**kwargs)

        self.add_widget(WhichModelGrid())


class SharkScreenGrid(GridLayout):
    def __init__(self, **kwargs):
        super(SharkScreenGrid, self).__init__(**kwargs)
        self.cols = 1

        self.topGrid = GridLayout()
        self.topGrid.cols = 1

        # make sure pillow and ffpyplayer
        self.player = VideoPlayer(source='/Users/marirosenwald/Downloads/sharkvideo.mp4')
        self.player.state = "play"
        self.player.allow_stretch = True
        self.topGrid.add_widget(self.player)

        self.add_widget(self.topGrid)

        self.backBtn = Button(text="back", font_size=40)
        self.backBtn.bind(on_press=self.pressedBack)
        self.add_widget(self.backBtn)

    def pressedBack(self, instance):
        print("back")

        sm.current = "OpenScreen"

class SharkModelScreen(Screen):
    def __init__(self, **kwargs):
        super(SharkModelScreen, self).__init__(**kwargs)

        self.add_widget(SharkScreenGrid())



sm = ScreenManager()
sm.add_widget(OpenScreen(name="OpenScreen"))
sm.add_widget(WhichModelScreen(name="WM"))
sm.add_widget(SharkModelScreen(name="SharkModelScreen"))
sm.current = "OpenScreen"


class CSCApp(App):

    def build(self):
        return sm

if __name__ == "__main__":
    CSCApp().run()
