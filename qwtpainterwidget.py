from enum import Enum

from kivy.uix.widget import Widget

class PlotToolType(Enum):
    """
    绘图类型
    """
    # 铅笔
    PENCIL = 1
    # 直线
    LINE = 2
    # 矩形
    RECTANGLE = 3


class QwtPainterWidget(Widget):
    """
        代表绘图的widget
    """

    # 默认绘图类型
    plot_tool_type: PlotToolType = PlotToolType.PENCIL

    # todo 定义 plot tool 的多个子类，使用策略的方式实现各种绘图


    def save(self):
        self.export_to_png("image.png")


    def on_touch_down(self, touch):
        print("touch down: ", touch.x, touch.y)
        # print "down"
        global xs ,ys ,xboun ,yboun ,press ,wide
        press = 1
        if incanvasxy(self ,touch.x ,touch.y):

            self.co l= retclr()
            if Widget.on_touch_down(self, touch):
                x s =touch.x
                y s =touch.y
                return True

            with self.canvas:
                Color(*self.col)
                # d = 30
                # Ellipse(pos=(touch.x - d / 2,touch.y - d / 2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y) ,width=wide)
                # if sline:
                x s =touch.x
                y s =touch.y
        else:
            x s =touch.x
            y s =touch.y
        default(self)
    def on_touch_move(self, touch):
        # print "move"
        global xs ,ys ,xboun ,yboun ,wide
        if incanvasxy(self ,touch.x ,touch.y) and incanvasxy(self ,xs ,ys) :
            self.co l= retclr()
            if sline:
                if Widget.on_touch_move(self, touch):
                    return True
                with self.canvas.after:
                    self.canvas.after.clear()
                    # if skip > 5:
                    #   Color(*[0,0,0,1])
                    #  Line(points=(xp,yp,xs,ys),width=4)
                    Color(*self.col)
                    Line(points=(touch.x ,touch.y ,xs ,ys) ,width=wide)
                xbou n =touch.x
                ybou n =touch.y
            elif rect:
                if Widget.on_touch_move(self, touch):
                    return True
                with self.canvas.after:
                    self.canvas.after.clear()
                    Color(*self.col)
                    Line(rectangle=(xs, ys, touch. x -xs, touch. y -ys) ,width=wide)
                xbou n =touch.x
                ybou n =touch.y

            else:
                if incanvasxy(self ,xs ,ys):
                    touch.ud["line"].points += [touch.x, touch.y]
        default(self)
    def on_touch_up(self, touch):
        # print "up"
        global xs ,ys ,press ,wide

        if incanvasxy(self ,xs ,ys):
            if incanvasxy(self ,touch.x ,touch.y) :

                if sline:

                    self.co l= retclr()

                    if Widget.on_touch_down(self, touch):
                        return True
                    with self.canvas:
                        Color(*self.col)
                        Line(points=(touch.x ,touch.y ,xs ,ys) ,width=wide)
                if rect:

                    self.co l= retclr()

                    if Widget.on_touch_down(self, touch):
                        return True
                    with self.canvas:
                        Color(*self.col)
                        Line(rectangle=(xs, ys, touch. x -xs, touch. y -ys) ,width=wide)
            else:
                if press:
                    if sline :
                        with self.canvas:
                            if xboun:
                                Color(*self.col)
                                Line(points=(xboun ,yboun ,xs ,ys) ,width=wide)
                        self.canvas.after.clear()
                    if rect :
                        with self.canvas:
                            if xboun:
                                Color(*self.col)
                                Line(rectangle=(xs, ys, xbou n -xs, ybou n -ys) ,width=wide)
                        self.canvas.after.clear()
        self.canvas.after.clear()
        default(self)
        pres s =0
