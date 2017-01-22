#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.widget import Widget


class SnekGame(Widget):

    def on_touch_down(self, touch):
        x = touch.x / self.width * 100.0
        y = touch.y / self.height * 100.0
        if x < 33.3 and 33.3 < y < 66.6:
            print("left")
        elif x > 66.6 and 33.3 < y < 66.6:
            print("right")
        elif y < 33.3 and 33.3 < x < 66.6:
            print("down")
        elif y > 66.6 and 33.3 < x < 66.6:
            print("up")


class SnekApp(App):
    def build(self):
        game = SnekGame()
        return game


if __name__ == '__main__':
    SnekApp().run()
