from pystray import *
from PIL import Image
from pynput.keyboard import Key, Controller
import threading
from cs import CapSwitch


class SysTrayUI:
    def __init__(self):
        self.cs = CapSwitch()
        
        #Run CapSwitch when it is opened
        self.init_thread(target=self.cs.start_listener)
        
        # *** Attributes ***
        self.icon_path = "icon.png"

        # *** Setup Menu ***
        self.menu_items = [
            MenuItem(self.check_status, self.toggle),
            MenuItem("Exit", self.exit),
        ]
        self.menu = Menu(*self.menu_items)

        # *** Create System Tray Icon ***
        self.icon = Icon("CapSwitch", menu=self.menu)
        self.icon.icon = Image.open(self.icon_path)
        self.icon.run()
        
    def toggle(self, *args):
        if not self.cs.running:
            self.init_thread(target=self.cs.start_listener)
        else:
            c = Controller()
            with c.pressed(Key.pause):
                with c.pressed(Key.end):
                        c.press(Key.down)
                        c.release(Key.down)
        
    def check_status(self, *args):
        name = "CapSwitch"
        
        if self.cs.running:
            return f"Disable {name}"
        else:
            return f"Enable {name}"

    def init_thread(self, target, *args):
        new_thread = threading.Thread(target=target)
        new_thread.start()

    def exit(self, *args):
        self.icon.stop()
        if self.cs.running:
            self.toggle()


app = SysTrayUI()
