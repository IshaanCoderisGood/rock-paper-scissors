from tkinter import *
import random 

window = Tk()
window.title("Rock Paper Scissors App")
window.geometry('400x400')
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print (computer_choice)
lbl = Label(window)
lbl.pack()
def rock():
    user_choice = "rock"
    final_answer(computer_choice, user_choice)
    return
   
def paper():
    user_choice = "paper"
    final_answer(computer_choice, user_choice)
    return
    
def scissors():
    user_choice = "scissors"
    final_answer(computer_choice, user_choice)
    return
   
btn = Button(window, text="Rock", command=rock)
btn.pack()
btn1 = Button(window, text="Paper", command=paper)
btn1.pack()
btn2 = Button(window, text="Scissors", command=scissors)
btn2.pack()

def final_answer(computer_choice, user_choice):
    if computer_choice == user_choice:
        lbl["text"]="Draw"
    if user_choice == "rock":
        if computer_choice == "paper":
            lbl["text"]="Lose"
        elif computer_choice =="scissors":
            lbl["text"]="Win"
    if user_choice == "paper":
        if computer_choice == "scissors":
            lbl["text"]="Lose"
        elif computer_choice =="rock":
            lbl["text"]="Win"
    if user_choice == "scissors":
        if computer_choice == "rock":
            lbl["text"]="Lose"
        elif computer_choice =="paper":
            lbl["text"]="Win"
    

     




window.mainloop()