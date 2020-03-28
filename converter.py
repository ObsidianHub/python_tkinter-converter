from tkinter import *
from tkinter import ttk
import urllib.request
import json
from tkinter import messagebox

root = Tk()
root.title('Конвертер валют')
root.geometry('300x250+1000+300')
root.resizable(False, False)

START_AMOUNT = 1000

# func
def exchange():
  pass

# header frame
header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

# Header
h_currency = Label(header_frame, text="Валюта", bg="#ccc", font="Arial 12 bold")
h_currency.grid(row=0, column=0, sticky=EW)
h_buy = Label(header_frame, text="Покупка", bg="#ccc", font="Arial 12 bold")
h_buy.grid(row=0, column=1, sticky=EW)
h_sale = Label(header_frame, text="Продажа", bg="#ccc", font="Arial 12 bold")
h_sale.grid(row=0, column=2, sticky=EW)

root.mainloop()