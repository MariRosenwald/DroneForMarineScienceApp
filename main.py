import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.videoplayer import VideoPlayer
import os


# import track.py

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

        # unknown_dir = os.system("cd doesnotexist")
        # print("`cd doesnotexis` ran with exit code %d" % unknown_dir)
        # sv = subprocess.run(
        #     ["python", "track.py", "--source", "sharkvideo.mp4", "--yolo_model", "NicholasWachterSPModel.pt",
        #      "--conf-thres", "0.3", "--save-vid"])
        # print(track.save_path)
        # print("The exit code was: %d" % sv.returncode)

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
        self.bottomGrid = GridLayout()
        self.bottomGrid.cols = 1

        # make sure pillow and ffpyplayer
        # need to have a video downloaded here, note that they were too large for github so access from
        # google drive:
        self.ret = "sharkvideo.mp4"
        self.player = VideoPlayer(source="sharkvideo.mp4")
        self.player.state = "play"
        self.player.allow_stretch = True
        self.topGrid.add_widget(self.player)

        self.add_widget(self.topGrid)

        self.backBtn = Button(text="back", font_size=40)
        self.backBtn.bind(on_press=self.pressedBack)
        self.bottomGrid.add_widget(self.backBtn)

        self.DLBtn = Button(text="Run Deep Learning", font_size=40)
        self.DLBtn.bind(on_press=self.pressedDL)
        self.bottomGrid.add_widget(self.DLBtn)

        self.add_widget(self.bottomGrid)

    def pressedBack(self, instance):
        print("back")

        sm.current = "WM"

    def pressedDL(self, instance):
        # self.DLBtn = Button(text="Running", font_size=40)
        sv = os.system("python track.py --source sharkvideo.mp4 --yolo_model "
                       "NicholasWachterSPModel.pt --conf-thres 0.3 --save-vid > out.txt")
        # print("`cd ~` ran with exit code %d" % sv)
        out = open("out.txt", "r+")
        for line in out:
            if len(line) > 5:
                ret = line
            print(line)
        print("return ", ret)
        str = ret.split("\n")

        # self.remove_widget(self.player)
        self.remove_widget(self.topGrid)
        self.remove_widget(self.bottomGrid)

        self.Rplayer = VideoPlayer(source=str[0])
        # self.Rplayer = VideoPlayer(source="v2.mp4")
        self.Rplayer.state = "play"
        self.Rplayer.allow_stretch = True
        self.add_widget(self.Rplayer)

        self.backBtn2 = Button(text="back", font_size=40)
        self.backBtn2.bind(on_press=self.pressedBack2)
        self.add_widget(self.backBtn2)

    def pressedBack2(self, instance):
        print("back")

        self.remove_widget(self.Rplayer)
        self.remove_widget(self.backBtn2)

        self.add_widget(self.topGrid)
        self.add_widget(self.bottomGrid)


class SharkModelScreen(Screen):
    def __init__(self, **kwargs):
        super(SharkModelScreen, self).__init__(**kwargs)

        self.add_widget(SharkScreenGrid())


class SharkRScreenGrid(GridLayout):
    def __init__(self, **kwargs):
        super(SharkRScreenGrid, self).__init__(**kwargs)
        self.cols = 1

        self.topGrid = GridLayout()
        self.topGrid.cols = 1
        self.bottomGrid = GridLayout()
        self.bottomGrid.cols = 1

        self.player = VideoPlayer(source=ret)
        self.player.state = "play"
        self.player.allow_stretch = True
        self.topGrid.add_widget(self.player)

        self.add_widget(self.topGrid)

        self.backBtn = Button(text="back", font_size=40)
        self.backBtn.bind(on_press=self.pressedBack)
        self.bottomGrid.add_widget(self.backBtn)

        self.add_widget(self.bottomGrid)

    def pressedBack(self, instance):
        print("back")

        sm.current = "SharkModelScreen"


class SharkResultScreen(Screen):
    def __init__(self, **kwargs):
        super(SharkResultScreen, self).__init__(**kwargs)

        self.add_widget(SharkRScreenGrid())


sm = ScreenManager()
sm.add_widget(OpenScreen(name="OpenScreen"))
sm.add_widget(WhichModelScreen(name="WM"))
sm.add_widget(SharkModelScreen(name="SharkModelScreen"))
sm.current = "OpenScreen"
ret = "sharkvideo.mp4"


class CSCApp(App):

    def build(self):
        return sm


if __name__ == "__main__":
    CSCApp().run()
