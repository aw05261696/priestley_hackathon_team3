from outputting_data import alldata
from tkinter import *
from tkinter import ttk

main = Tk()
main.geometry("1920x1080")
main.configure(bg="#819e80")

def exitgame():
    main.destroy()
    main.quit()
    
def menu():
    label=Label(main, text="Greener Priestley", font=("Helvetica 36 bold"), bg="#819e80")
    label.pack(pady=100)
    label=Label(main, text="Smart Sprinkler Solution", font=("Helvetica 10 bold"), bg="#819e80")
    label.pack(pady=0)

    ttk.Button(main, text= "1. view field sprinklers", width=150, command= alldata).pack(pady=40)
    ttk.Button(main, text= "1. view driveway sprinklers",width=150, command= alldata).pack(pady=40)
    ttk.Button(main, text= "1. view bush sprinklers",width=150, command= alldata).pack(pady=40)
    ttk.Button(main, text= "2. exit",width= 150, command= exitgame).pack(pady=40)

menu()

main.mainloop()
