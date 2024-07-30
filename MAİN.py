import tkinter as tk
import requests
from tkinter import messagebox


class Discord(object):
    def __init__(self,aut,m_url):
        self.aut = aut
        self.m_url = m_url
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('Discord')
        self.root.resizable(False, False)
        self.label = tk.Label(self.root, text='Message')
        self.label.place(relx=0.5, rely=0.25, anchor='center')
        self.entry = tk.Entry(master=self.root,
                              width=40)
        self.entry.place(relx=0.5, rely=0.3, anchor='center')
        self.label_num = tk.Label(self.root, text='number of messages')
        self.label_num.place(relx=0.5, rely=0.35, anchor='center')
        self.entry_num = tk.Entry(master=self.root,
                              width=40)
        self.entry_num.place(relx=0.5, rely=0.4, anchor='center')
        self.button =tk.Button(master=self.root,text="Send",command=self.reg)
        self.button.place(relx=0.5, rely=0.5, anchor='center')
        self.root.mainloop()


        self.message = {"content" : self.entry.get()}
        self.aut = {"authorization": f"{self.aut}"}
        self.url = f"{self.m_url}"

    def reg(self):
        message = {"content": self.entry.get()}
        aut = {"authorization": f"{self.aut}"}
        url = f"{self.url}"
        num = self.entry_num.get()
        def message_num(num):
            for i in range(num):
                r = requests.post(url, headers=aut, data=message)
        try:
            num = int(num)
            message_num(num)
        except:
            message = messagebox.showinfo(message="enter number",title="Invalid Number")

aut = input("Authorization Token: ")
message_url = input("Message URL: ")

if __name__ == '__main__':
    d = Discord(aut=aut,
                m_url=message_url)