from kivymd.app import MDApp
from kivy.lang import Builder
import hardware_info


class Test(MDApp):
    boot_time = hardware_info.boot_time()

    def callback(self):
        print("Callback is working")

    def build(self):
        self.theme_cls.primary_palette = "Gray"


Test().run()
