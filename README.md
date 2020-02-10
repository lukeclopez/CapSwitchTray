# CapSwitchTray

A system tray app to toggle the case of selected text using the caps lock button.

[Demo Video](https://youtu.be/NFr7n3NHSmA)

## Setup

After cloning the repo, you may decide to create a virtual environment. Either way, continue like so:

1. Run `pip install -r requirements.txt`
2. From the `CapSwitchTray` folder, run `python systray.py` for the system tray app or `python cs.py` for the standalone script.

## Usage

1. Select the text you want to switch the case of.
2. Press `Caps Lock` twice.

## To Do

1. Make it so user only has to press `Caps Lock` once to use it.
2. Use `Pynput`'s new Global Hotkey feature!
3. Figure out why programmatically pressing `Ctrl` + `C` doesn't always work as intended.
