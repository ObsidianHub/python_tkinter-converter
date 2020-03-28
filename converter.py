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

# USD course
usd_currency = Label(header_frame, text="USD", font="Arial 10")
usd_currency.grid(row=1, column=0, sticky=EW)
usd_buy = Label(header_frame, text="25.50", font="Arial 10")
usd_buy.grid(row=1, column=1, sticky=EW)
usd_sale = Label(header_frame, text="25.60", font="Arial 10")
usd_sale.grid(row=1, column=2, sticky=EW)

# EUR course
eur_currency = Label(header_frame, text="EUR", bg="#ccc", font="Arial 10")
eur_currency.grid(row=2, column=0, sticky=EW)
eur_buy = Label(header_frame, text="27.50", bg="#ccc", font="Arial 10")
eur_buy.grid(row=2, column=1, sticky=EW)
eur_sale = Label(header_frame, text="27.60", bg="#ccc", font="Arial 10")
eur_sale.grid(row=2, column=2, sticky=EW)

# RUB course
rub_currency = Label(header_frame, text="RUB", font="Arial 10")
rub_currency.grid(row=3, column=0, sticky=EW)
rub_buy = Label(header_frame, text="0.35", font="Arial 10")
rub_buy.grid(row=3, column=1, sticky=EW)
rub_sale = Label(header_frame, text="0.39", font="Arial 10")
rub_sale.grid(row=3, column=2, sticky=EW)

root.mainloop()