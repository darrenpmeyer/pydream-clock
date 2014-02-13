#!/usr/bin/env python
import pydream
import datetime
import time

class clock():

    def __init__(self):
        self.sign = pydream.display()
        if not self.sign.connect():
            raise StandardError("Cannot connect to display")

        self._fullbar = []
        for i in range(0,20):
            self._fullbar.append(1)

        self._fullbar = [ self._fullbar ]

    def render_clock(self):
        self.sign.clear()

        hour   = self.dt.hour
        minute = self.dt.minute
        second = self.dt.second

        if hour > 12:
            hour -= 12
            self.sign.light_on(21,0)

        for x in range(0,hour):
            self.sign.light_on(x,0)

        row = 1
        if minute > 40:
            self.sign.put_sprite(0, row, self._fullbar)
            self.sign.put_sprite(0, row+1, self._fullbar)
            minute -= 40
            row += 2

        elif minute > 20:
            self.sign.put_sprite(0, row, sprite=self._fullbar)
            minute -= 20
            row += 1

        for s in range(0,minute):
            self.sign.light_on(s, row)

        row = 4
        if second > 40:
            self.sign.put_sprite(0, row, self._fullbar)
            self.sign.put_sprite(0, row+1, self._fullbar)
            second -= 40
            row += 2

        elif second > 20:
            self.sign.put_sprite(0, row, self._fullbar)
            second -= 20
            row += 1

        for s in range(0,second):
            self.sign.light_on(s, row)


        self.sign.refresh()

    def run(self):
        while True:
            self.dt = datetime.datetime.now().time()
            self.render_clock()
            time.sleep(0.1)


c = clock()
c.run()
