from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

level=15
target=""

class mybox(BoxLayout):

    level_id=ObjectProperty("")
    target_id=ObjectProperty("")
    text_id=ObjectProperty("")
    bar_id=ObjectProperty("")


    def minus(self):
        global level
        if(level!=1):
            level-=1
            self.ids.level_id.text=str(level)

    def plus(self):
        global level
        if(level!=33):
            level+=1
            self.ids.level_id.text=str(level)

    def reset(self):
        global target
        target=""
        self.ids.bar_id.value=0
        self.ids.text_id.text="cyber attack progress"
        self.ids.target_id.text=""

    def tar(self):
        global target
        target=self.ids.target_id.text

    def attack(self):
        global target
        if(target!=""):
            self.ids.bar_id.value += 25
            self.ids.text_id.text = f"level {level} attack on {target} : {str(self.ids.bar_id.value)} %"

class attackApp(App):
    Window.size=(960,540)

attackApp().run()
