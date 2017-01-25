#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, ListProperty


class SnekChunk(Widget):
    def __init__(self, chunk_x, chunk_y, **kwargs):
        super().__init__(**kwargs)
        self.pos = chunk_x * 25, chunk_y * 25


class Snek(Widget):
    chunks = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chunks = [SnekChunk(2,2), SnekChunk(3,2)]

    def on_chunks(self, *largs):
        self.clear_widgets()
        for widge in self.chunks:
            self.add_widget(widge)


class SnekGame(Widget):

    snek = ObjectProperty(None)

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
