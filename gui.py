from tkinter import *
from PIL import ImageTk, Image, ImageFilter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from scrapper import scraper

raj = tk.Tk()
logo = PhotoImage('logo.ico')
raj.iconbitmap(True, logo)
raj.title('SIP 2024')
raj.attributes("-alpha", 0.90)
raj.geometry('500x350')


raj.configure(background= "#212121")


text = tk.Label(raj, text='SIP 2024', font=("montserrat", 16, "bold italic underline"), bg =raj['bg'] , fg ="white")
text.pack(padx=20, pady=20)

scraper_instance = scraper() #instance of scraper class of scrapper file 


def buttons(option):
    # Create an entry widget for user input
    user_input = tk.Entry(raj, width=20)
    user_input.pack(pady=10)

    def process_input():
        input_text = user_input.get()
        if option == "Option 1":
            result = scraper_instance.cheat_sheet_scraper(input_text)
            messagebox.showinfo("Cheatsheet Scrapper", f"Input: {input_text}")
        elif option == "Option 2":
            result = scraper_instance.newslink_scraper(input_text)
            messagebox.showinfo("News Scrapper", f"Input: {input_text}")
        elif option == "Option 3":
            result = scraper_instance.minitv_scraper(input_text)
            messagebox.showinfo("MiniTV Scrapper", f"Input: {input_text}")
        user_input.destroy()
        submit_button.destroy()

    # Create a submit button to process the input
    submit_button = tk.Button(raj, text="Submit", command=process_input)
    submit_button.pack(pady=10)

# Create option buttons
option1 = tk.Button(raj, text="Cheatsheet Scrapper", command=lambda: buttons("Option 1"), activebackground= '#4ecc93', border= 0, bg= '#8de0bb')
option1.pack(pady=10)

option2 = tk.Button(raj, text="News link Scrapper", command=lambda: buttons("Option 2"), activebackground= '#4ecc93', border= 0, bg= '#8de0bb')
option2.pack(pady=10)

option3 = tk.Button(raj, text="Minitv Scrapper", command=lambda: buttons("Option 3"), activebackground= '#4ecc93', border= 0, bg= '#8de0bb')
option3.pack(pady=10)

raj.mainloop()
