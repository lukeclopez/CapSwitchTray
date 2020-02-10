from pynput.keyboard import Key, Controller, Listener
import pyperclip
import pyautogui
import threading


class CapSwitch:
    def __init__(self):
        self.controller = Controller()
        self.pause_pressed = False
        self.end_pressed = False
        self.down_pressed = False

        self.caps_lock = True
        self.running = False
        self.need_capswitch = True

        # Empty the clipboard so it doesn't
        # paste something random.
        pyperclip.copy("")

    def on_press(self, key):
        # These three statements are required to see
        # If these keys are being pressed at the same time.
        if key == Key.pause:
            self.pause_pressed = True

        elif key == Key.end:
            self.end_pressed = True

        elif key == Key.down:
            self.down_pressed = True

    def on_release(self, key):
        if key == Key.caps_lock and self.need_capswitch:
            self.capswitch()

        elif key == Key.pause:
            self.pause_pressed = False

        elif key == Key.end:
            self.end_pressed = False

        elif key == Key.end:
            self.down_pressed = False

        # Require the user to press all three buttons to end the listener.
        # This way, it is unlikely the user will end it by accident.
        elif self.pause_pressed and self.end_pressed and self.down_pressed:
            return False

    def capswitch(self):
        # Control + C to copy
        with self.controller.pressed(Key.ctrl_l):
            self.controller.press('c')
            self.controller.release('c')

        copied_text = pyperclip.paste()
        if copied_text != "":
            # Take what was copied and swap the case
            clipboard = copied_text.swapcase()

            # Copy the "swap cased" text to the clipboard
            pyperclip.copy(clipboard)

            # Control + V to paste
            with self.controller.pressed(Key.ctrl_l):
                self.controller.press('v')
                self.controller.release('v')

            # Clear the clipboard
            pyperclip.copy("")

            # Toggle caps lock again to leave it
            # as it was before we called capswitch.
            # However, don't do a capswitch this time,
            # as we don't want an infinite loop.
            self.need_capswitch = False
            self.controller.press(Key.caps_lock)
            self.controller.release(Key.caps_lock)
            self.need_capswitch = True

    def start_listener(self):
        self.running = True
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
        self.running = False


if __name__ == "__main__":
    cw = CapSwitch()
    cw.start_listener()
