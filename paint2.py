from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.colorpicker import ColorPicker
from kivy.properties import ListProperty
from kivy.uix.popup import Popup

from qwtpainterwidget import QwtPainterWidget

sline = False
clr=[1,1,0.5,1]
pre_clr=clr
xs=0
ys=0
xboun=0
yboun=0
rect=False
press=0
wide=5

def reset():
    global rect, ell, sline
    rect=ell=sline=False
def retclr():
    return clr

def incanvasxy(self,x,y):
    if x > 0.25* self.width and y >0.2 *self.height and x < self.width*0.75 and y < self.height*0.8:
        return True
def default (self):
    with self.canvas.after:
        col =[1,1,1,1]    
        Color(*col)
        Line(rectangle=(0.25* self.width-13, 0.2 *self.height-13, self.width*0.5 +26, self.height*0.6+26),width=13)
    with self.canvas:
        col =[0,0,0,1]    
        Color(*col)
        Line(rectangle=(0.25* self.width-25, 0.2 *self.height-25, self.width*0.5 +50, self.height*0.6+50),width=25)

class Cpicker(ColorPicker):
    pass

class popup(Popup):
    def hello (self, y):
        global clr,pre_clr
        pre_clr=clr    
        clr=y 


class MainScreen(Screen):
    
    def open_it1(self):
        popup().open()

    # def open_it2(self):
    #     popup2().open()
    
    def eraser(self):
        global clr,pre_clr,sline
        reset()
        pre_clr = clr
        clr= [0,0,0,1]
    
    def thick(self,*args):
        global wide
        wide = args[1]
        self.lab.text = "Width : " + str(args[1])
    def pencil(self):
        global clr,pre_clr,sline
        clr=pre_clr
        reset()

    def sl(self):
        global sline,rect,pre_clr,clr
        reset()
        clr=pre_clr
        sline= True
        
    def rect(self):
        global rect,sline,pre_clr,clr
        reset()
        clr=pre_clr
        rect= True
                




