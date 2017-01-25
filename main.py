#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, ListProperty


class SnekChunk(Widget):
    def __init__(self, chunk_x, chunk_y, **kwargs):
        super().__init__(**kwargs)
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
        self.pos = chunk_x * 25, chunk_y * 25


class Snek(Widget):
    chunks = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chunks = [SnekChunk(3,2), SnekChunk(2,2)]

    def on_chunks(self, *largs):
        self.clear_widgets()
        for widge in self.chunks:
            self.add_widget(widge)

    def move(self, direction):
        self.chunks.pop()
        new_chunk_x = self.chunks[0].chunk_x
        new_chunk_y = self.chunks[0].chunk_y
        #FIXME: don't allow reverse
        #FIXME: detect collision
        if direction == "left":
            new_chunk_x -= 1
        elif direction == "right":
            new_chunk_x += 1
        elif direction == "down":
            new_chunk_y -= 1
        else:
            new_chunk_y += 1
        self.chunks.insert(0, SnekChunk(new_chunk_x, new_chunk_y))


class SnekGame(Widget):

    snek = ObjectProperty(None)

    def on_touch_down(self, touch):
        x = touch.x / self.width * 100.0
        y = touch.y / self.height * 100.0
        if x < 33.3 and 33.3 < y < 66.6:
            self.snek.move("left")
        elif x > 66.6 and 33.3 < y < 66.6:
            self.snek.move("right")
        elif y < 33.3 and 33.3 < x < 66.6:
            self.snek.move("down")
        elif y > 66.6 and 33.3 < x < 66.6:
            self.snek.move("up")


class SnekApp(App):
    def build(self):
        game = SnekGame()
        return game


if __name__ == '__main__':
    SnekApp().run()
