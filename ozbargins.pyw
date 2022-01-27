import requests
import tkinter as tk
import tkinter.scrolledtext as st
from bs4 import BeautifulSoup

window = tk.Tk()
window.geometry("600x300")
window.resizable(0,0)
window.title("Oz Bargins")

url = "https://www.ozbargain.com.au/deals"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,"html.parser")
title = soup.find("title")
bargins = soup.findAll(class_="title")

tk.Label(window,text=title.text,font=('arial', 12, 'bold')).pack()
txt = st.ScrolledText(window, undo=True)
txt['font'] = ('arial', '12')
txt.pack(expand=True, fill='both')

for bargin in bargins:
    if bargin.text.find("expired") == 1:
        pass
    else:
        txt.insert(tk.INSERT, bargin.text + "\n\n")
txt.config(state=tk.DISABLED)
window.mainloop()




