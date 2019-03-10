# All of this is done in the Jupyter GUI

import pandas
import os
os.listdir()

df1 = pandas.read_csv("supermarkets.csv")
df1.set_index("ID")

df2 = pandas.read_json("supermarket.json")
df2.set_index("ID")

df3 = pandas.read_excel("supermarket.xlsx", sheetname=0)
df3

df4 = pandas.read_csv("supermarket.txt")
df4

df5 = pandas.read_csv("supermarket_semi-colons.txt", seperator=";")
df5

df6 = pandas.read_csv("http://pythonhow.com/supermarkets.csv")
df6

df7 = pandas.read_json("http://pythonhow.com/supermarkets.json")
df7
