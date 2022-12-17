from tkinter import *
from tkinter import ttk, messagebox as mg
from ttkthemes import themed_tk as tk
import sqlite3
import _datetime as d
import os
import tempfile


dated = d.datetime.today()
table_name = dated.date()

year = table_name.year
month = table_name.month
day = table_name.day

index = 1
global Daily
Daily = f"{str(day)}_{str(month)}_{str(year)}"

con = sqlite3.connect("Mary_Daniella.db")
cursor = con.cursor()

customer = f"""CREATE TABLE IF NOT EXISTS Customers_{year}(
    Customers text,
    Kg text
)"""

if(cursor.execute(table)):
    print(table)
else:
    print("Not Successful")