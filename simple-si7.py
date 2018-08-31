#!/usr/bin/env python
from samplebase import SampleBase
import time
import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(19, GPIO.IN)



class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)
    #defining the borders
    def draw_border(self, mydisplay, xcord, r, g, b):
        # Borders (on edges)
        for x in range(0, 15):
            mydisplay.SetPixel(x+xcord, 0, r, g, b)
            mydisplay.SetPixel(x+xcord, 15, r, g, b)
            mydisplay.SetPixel(0+xcord, x, r, g, b)
            mydisplay.SetPixel(14+xcord, x, r, g, b)
    def draw_w(self, mydisplay, r, g, b):
        mydisplay.SetPixel(9, 15, r, g, b)
        mydisplay.SetPixel(10, 15, r, g, b)
        mydisplay.SetPixel(10, 14, r, g, b)
        mydisplay.SetPixel(11, 14, r, g, b)
        mydisplay.SetPixel(11, 13, r, g, b)
        mydisplay.SetPixel(12, 13, r, g, b)
        mydisplay.SetPixel(12, 12, r, g, b)
        mydisplay.SetPixel(13, 12, r, g, b)
        mydisplay.SetPixel(13, 11, r, g, b)
        mydisplay.SetPixel(14, 11, r, g, b)
        mydisplay.SetPixel(14, 10, r, g, b)
        mydisplay.SetPixel(15, 10, r, g, b)
        mydisplay.SetPixel(15, 9, r, g, b)
        mydisplay.SetPixel(16, 9, r, g, b)
        mydisplay.SetPixel(16, 10, r, g, b)
        mydisplay.SetPixel(16, 9, r, g, b)
        mydisplay.SetPixel(17, 9, r, g, b)
        mydisplay.SetPixel(17, 10, r, g, b)
        mydisplay.SetPixel(18, 10, r, g, b)        
        mydisplay.SetPixel(18, 11, r, g, b)
        mydisplay.SetPixel(19, 11, r, g, b)
        mydisplay.SetPixel(19, 12, r, g, b)
        mydisplay.SetPixel(20, 12, r, g, b)
        mydisplay.SetPixel(20, 13, r, g, b)
        mydisplay.SetPixel(21, 13, r, g, b)
        mydisplay.SetPixel(21, 14, r, g, b)
        mydisplay.SetPixel(22, 14, r, g, b)
        mydisplay.SetPixel(22, 15, r, g, b)       
        mydisplay.SetPixel(23, 15, r, g, b)
        mydisplay.SetPixel(23, 15, r, g, b)
        mydisplay.SetPixel(24, 15, r, g, b)
        mydisplay.SetPixel(24, 15, r, g, b)
        for x in range(3, 16):
            mydisplay.SetPixel(8, x, r, g, b)
            mydisplay.SetPixel(24, x, r, g, b)
        for x in range(3, 16):
            mydisplay.SetPixel(7, x, r, g, b)
            mydisplay.SetPixel(25, x, r, g, b)
    
    
    def draw_pig(self, mydisplay, r, g, b):
        for x in range(9, 16):
            mydisplay.SetPixel (x, 15, r, g, b)
        for x in range(17, 24):
            mydisplay.SetPixel (x, 15, r, g, b)
        for x in range(10, 15):
            mydisplay.SetPixel (x, 14, r, g, b)
        for x in range(18, 23):
            mydisplay.SetPixel (x, 14, r, g, b)
        for x in range(18, 23):
            mydisplay.SetPixel (x, 13, r, g, b)
        for x in range (10, 15):
            mydisplay.SetPixel (x, 13, r, g, b)
        for x in range (9, 24):
            mydisplay.SetPixel (x, 12, r, g, b)
        for x in range (8, 25):
            mydisplay.SetPixel (x, 11, r, g, b)
        for x in range (8, 25):
            mydisplay.SetPixel (x, 10, r, g, b)
        for x in range (8, 25):
            mydisplay.SetPixel (x, 9, r, g, b)
        for x in range (8, 25):
            mydisplay.SetPixel (x, 8, r, g, b)
        for x in range (8, 25):
            mydisplay.SetPixel (x, 7, r, g, b)
        for x in range (8, 25):
            mydisplay.SetPixel (x, 6, r, g, b)
        for x in range (8, 25):
            mydisplay.SetPixel (x, 5, r, g, b)
        for x in range (8, 25):
            mydisplay.SetPixel (x, 4, r, g, b)
        for x in range (9, 24):
            mydisplay.SetPixel (x, 3, r, g, b)
        for x in range (10, 23):
            mydisplay.SetPixel (x, 2, r, g, b)
        for x in range (7, 11):
            mydisplay.SetPixel (x, 1, r, g, b)
        for x in range (8, 11):
            mydisplay.SetPixel (x, 0, r, g, b)
        for x in range (22, 26):
            mydisplay.SetPixel (x, 1, r, g, b)
        for x in range (22, 25):
            mydisplay.SetPixel (x, 0, r, g, b)
        for x in range (11, 14):
            mydisplay.SetPixel (x, 3, 255, 255, 255)
        for x in range (11, 14):
            mydisplay.SetPixel (x, 4, 255, 255, 255)
        for x in range (11, 14):
            mydisplay.SetPixel (x, 5, 255, 255, 255)
            mydisplay.SetPixel (12, 4, 0, 0, 255)
        for x in range (19, 22):
            mydisplay.SetPixel (x, 3, 255, 255, 255)
        for x in range (19, 22):
            mydisplay.SetPixel (x, 4, 255, 255, 255)
        for x in range (19, 22):
            mydisplay.SetPixel (x, 5, 255, 255, 255)
            mydisplay.SetPixel (20, 4, 0, 0, 255)
        for x in range (14, 19):
            mydisplay.SetPixel (x, 6, 0, 0, 0)
        for x in range (14, 19):
            mydisplay.SetPixel (x, 6, 0, 0, 0)
        for x in range (7, 10):
            mydisplay.SetPixel (19, x, 0, 0, 0)
        for x in range (7, 10):
            mydisplay.SetPixel (13, x, 0, 0, 0)
        for x in range (14, 19):
            mydisplay.SetPixel (x, 10, 0, 0, 0)
        mydisplay.SetPixel (15, 8, 0, 0, 0)
        mydisplay.SetPixel (17, 8, 0, 0, 0)
        mydisplay.SetPixel (14, 12, 0, 0, 0)
        mydisplay.SetPixel (18, 12, 0, 0, 0)
    
    def clear_pig(self, mydisplay):
        for x in range (11, 14):
            mydisplay.SetPixel (x, 3, 0, 0, 0)
        for x in range (11, 14):
            mydisplay.SetPixel (x, 4, 0, 0, 0)
        for x in range (11, 14):
            mydisplay.SetPixel (x, 5, 0, 0, 0)
            mydisplay.SetPixel (12, 4, 0, 0, 0)
        for x in range (19, 22):
            mydisplay.SetPixel (x, 3, 0, 0, 0)
        for x in range (19, 22):
            mydisplay.SetPixel (x, 4, 0, 0, 0)
        for x in range (19, 22):
            mydisplay.SetPixel (x, 5, 0, 0, 0)
            mydisplay.SetPixel (20, 4, 0, 0, 0)
    
    #defining winners screen       
    def draw_win(self, mydisplay, r, g, b):
        for x in range(0, 32):            
            mydisplay.SetPixel(x, 0, r, g ,b)
            mydisplay.SetPixel(x, 1, r, g ,b)
            mydisplay.SetPixel(x, 2, r, g ,b)
            mydisplay.SetPixel(x, 3, r, g ,b)
            mydisplay.SetPixel(x, 4, r, g ,b)
            mydisplay.SetPixel(x, 5, r, g ,b)
            mydisplay.SetPixel(x, 6, r, g ,b)
            mydisplay.SetPixel(x, 7, r, g ,b)
            mydisplay.SetPixel(x, 8, r, g ,b)
            mydisplay.SetPixel(x, 9, r, g ,b)
            mydisplay.SetPixel(x, 10, r, g ,b)
            mydisplay.SetPixel(x, 11, r, g ,b)
            mydisplay.SetPixel(x, 12, r, g ,b)
            mydisplay.SetPixel(x, 13, r, g ,b)
            mydisplay.SetPixel(x, 14, r, g ,b)
            mydisplay.SetPixel(x, 15, r, g ,b)
            mydisplay.SetPixel(x, 16, r, g ,b)
    #defining P
    def draw_p(self, mydisplay, xcord, r, g, b):
        for x in range(5, 11):
            mydisplay.SetPixel(xcord, x, r, g, b)
        for x in range(xcord, xcord+4):
            mydisplay.SetPixel(x, 5, r, g, b)
            mydisplay.SetPixel(x, 7, r, g, b)  
        for x in range(5, 8):
            mydisplay.SetPixel(xcord+3, x, r, g, b)
    #defining I
    def draw_i(self, mydisplay, xcord, r, g , b):
        for x in range(5, 11):
            mydisplay.SetPixel(xcord, x, r, g, b)
    #defining G
    def draw_g(self, mydisplay, xcord, r, g, b):
        for x in range(5, 11):
            mydisplay.SetPixel(xcord, x, r, g, b)
        for x in range(xcord, xcord+4):
            mydisplay.SetPixel(x, 5, r, g, b)
            mydisplay.SetPixel(x, 10, r, g, b)      
        for x in range(8, 11):  
            mydisplay.SetPixel(xcord+3, x, r, g, b)
            mydisplay.SetPixel(xcord+2, 8, r, g, b)
        
        
    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        press = 0
        press2 = 0
        press3 = 0
        
        while True:
            #waiting for start button to be pressed
            if not GPIO.input(19):
                start=1
                while start:
                    #start button pressed
                    if GPIO.input(19):
                        press=0
                        press2=0
                        start=0
                        self.draw_border(offset_canvas, 0, 0, 0, 0)
                        self.draw_border(offset_canvas, 17, 0, 0, 0)
                        self.draw_p(offset_canvas, 2, 0, 0, 0)
                        self.draw_i(offset_canvas, 7, 0, 0, 0)
                        self.draw_g(offset_canvas, 9, 0, 0, 0)
                        self.draw_p(offset_canvas, 19, 0, 0, 0)            
                        self.draw_i(offset_canvas, 24, 0, 0, 0)           
                        self.draw_g(offset_canvas, 26, 0, 0, 0)
                        #self.draw_pig(offset_canvas, 0, 0, 0)
                        self.draw_w(offset_canvas, 0, 0, 0)
                        self.draw_win(offset_canvas, 0, 0, 0)
                        self.draw_pig(offset_canvas, 255, 20, 147)
                        offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(.1)
                    #on and off
                if press3==1:
                    press3=0
                else:
                    press3=press3+1                          
            #game off
            if press3==0:
                '''
                for col in (0, 32):
                    for row in (0, 16):
                        offset_canvas.SetPixel(row, col, 0, 0, 0)
                        time.sleep(0.1)
                '''
                self.draw_border(offset_canvas, 0, 0, 0, 0)
                self.draw_border(offset_canvas, 17, 0, 0, 0)
                self.draw_p(offset_canvas, 2, 0, 0, 0)
                self.draw_i(offset_canvas, 7, 0, 0, 0)
                self.draw_g(offset_canvas, 9, 0, 0, 0)
                self.draw_p(offset_canvas, 19, 0, 0, 0)            
                self.draw_i(offset_canvas, 24, 0, 0, 0)           
                self.draw_g(offset_canvas, 26, 0, 0, 0)
                #self.draw_pig(offset_canvas, 0, 0, 0)
                self.draw_w(offset_canvas, 0, 0, 0)
                self.draw_win(offset_canvas, 0, 0, 0)
                self.draw_pig(offset_canvas, 255, 20, 147)
                offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                
                
            #game on
            if press3==1:
                self.draw_pig(offset_canvas, 0, 0, 0)
                self.clear_pig(offset_canvas)
                self.draw_border(offset_canvas, 0, 132, 222, 2)
                self.draw_border(offset_canvas, 17, 255, 128, 0)            
                #waiting for player 1 button to be pressed               
                if not GPIO.input(18):
                    button=1
                    while button:
                    #player 1 button pressed
                        if GPIO.input(18):
                            button=0
                        time.sleep(.15)
                    if press==5:
                        press=0
                    else:
                        press=press+1
            #player 1 has no letters
                if press==0:
                    self.draw_p(offset_canvas, 2, 0, 0, 0)
                    self.draw_i(offset_canvas, 7, 0, 0, 0)
                    self.draw_g(offset_canvas, 9, 0, 0, 0)
            #player 1 has a P
                if press==1:
                    self.draw_p(offset_canvas, 2, 132, 222, 2)
                    self.draw_i(offset_canvas, 7, 0, 0, 0)
                    self.draw_g(offset_canvas, 9, 0, 0, 0)
            #player 1 has a PI
                if press==2:
                    self.draw_p(offset_canvas, 2, 132, 222, 2)
                    self.draw_i(offset_canvas, 7, 132, 222, 2)
                    self.draw_g(offset_canvas, 9, 0, 0, 0)
            #player 1 has a PIG
                if press==3:
                    self.draw_p(offset_canvas, 2, 132, 222, 2)
                    self.draw_i(offset_canvas, 7, 132, 222, 2)
                    self.draw_g(offset_canvas, 9, 132, 222, 2)
                if press==4:
                    self.draw_win(offset_canvas, 255, 128, 0)
                    self.draw_w(offset_canvas, 0, 0, 0)
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(1)
                    self.draw_win(offset_canvas, 0, 0, 0)
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(1)
                    self.draw_win(offset_canvas, 0, 0, 0)
                    self.draw_w(offset_canvas, 0, 0, 0)
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(1)
                    '''
                    self.draw_win(offset_canvas, 255, 128, 0)
                    self.draw_w(offset_canvas, 0, 0, 0)
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(1)
                    self.draw_pig(offset_canvas, 255, 20, 147)
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(1)
                    game_end=1
                    '''
                           
            #waiting for player 2 button to be pressed
                if not GPIO.input(25):
                    button2=1
                    while button2:
                    #player 2 button press
                        if GPIO.input(25):
                            button2=0
                        time.sleep(.15)
                    if press2==4:
                        press2=0
                    else:
                        press2=press2+1
                print("press2="+str(press2)+"")
            #player 2 has no letters
                if press2==0:
                    self.draw_p(offset_canvas, 19, 0, 0, 0)            
                    self.draw_i(offset_canvas, 24, 0, 0, 0)           
                    self.draw_g(offset_canvas, 26, 0, 0, 0)
                
            #player 2 has a P
                if press2==1:
                    self.draw_p(offset_canvas, 19, 255, 128, 0)
                    self.draw_i(offset_canvas, 24, 0, 0, 0) 
                    self.draw_g(offset_canvas, 26, 0, 0, 0)
            #player 2 has a PI
                if press2==2:
                    self.draw_p(offset_canvas, 19, 255, 128, 0)
                    self.draw_i(offset_canvas, 24, 255, 128, 0)
                    self.draw_g(offset_canvas, 26, 0, 0, 0)
            #player 2 has PIG
                if press2==3:
                    self.draw_p(offset_canvas, 19, 255, 128, 0)
                    self.draw_i(offset_canvas, 24, 255, 128, 0)
                    self.draw_g(offset_canvas, 26, 255, 128, 0)
                if press2==4:
                    self.draw_win(offset_canvas, 132, 222, 2)
                    self.draw_w(offset_canvas, 0, 0, 0)
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(1)
                    self.draw_win(offset_canvas, 0, 0, 0)
                    self.draw_w(offset_canvas, 0, 0, 0)
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(1)
                    '''
                    self.draw_win(offset_canvas, 132, 222, 2)
                    self.draw_w(offset_canvas, 0, 0, 0)
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(1)
                    self.draw_pig(offset_canvas, 255, 20, 147)
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(1)
                    game_end=1
                    '''
                    
            #Displays information
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)


# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    
    if (not simple_square.process()):
        simple_square.print_help()