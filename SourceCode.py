import tkinter as tk
from tkinter import *
import math
window = Tk()
window.geometry('300x250')
window.title('Degree Angle Calculator')

input_a = tk.Entry(window)
input_a.pack()

input_b = tk.Entry(window)
input_b.pack()

shape = tk.Entry(window)
shape.pack() 

def find_theta():
    get_shape = shape.get()
    get_a = int(input_a.get())
    get_b = int(input_b.get())
    list_shape = ['sin','cos','tan']

    if get_shape == list_shape[0]: 
        sin_theta = math.asin(get_a/get_b)
        sin_angle = math.degrees(sin_theta)
        result_label0 = tk.Label(window, text=sin_angle)
        result_label0.pack()

    if get_shape == list_shape[1]: 
        cos_theta = math.acos(get_a/get_b)
        cos_angle = math.degrees(cos_theta)
        result_label1 = tk.Label(window, text=cos_angle)
        result_label1.pack()

    if get_shape == list_shape[2]:
        tan_theta = math.atan(get_a/get_b)
        tan_angle = math.degrees(tan_theta)
        result_label2 = tk.Label(window, text=tan_angle)
        result_label2.pack()

result_button = tk.Button(window, text='Calculate Angle (Theta)',command=find_theta)
result_button.pack()
window.mainloop()
