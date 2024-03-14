'''
License: Apache
Author Email:bilibili_wulihb@outlookcom
'''
import turtle

class init:
    global img
    img = turtle.Turtle()
    def goto(x,y):
        img.goto(x,y)
    def make(num):
        if num<3:
            print('Error!Num Cannot be smaller than 3')
            return False
        i=0
        degree=360/num
        while True:
            if i==num:
                break
            img.forward(100)
            img.left(degree)
            i=i+1
    def clear():
        img.clear()
    def hgoto(x,y):
        img.penup()
        img.goto(x,y)
        img.pendown()
