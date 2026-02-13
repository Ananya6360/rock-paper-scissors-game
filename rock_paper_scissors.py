import random  #it will chose a random number
import tkinter as tk #using a GUI foe creating a button
import pyttsx3 #it will text to speech

def say(result): # calling a function say inside the brace is to speak
    machine = pyttsx3.init() # it will start to speak
    machine.say(result) # it will send the text to speak
    machine.runAndWait() # it will start the speaking  process

def game(user_choice): # calling a function game
    computer = random.randint(0, 2) # it will random number to select a 0 to 2 number
    choice = ["Rock", "Paper", "Scissors"]# computer chose only this 3

    if user_choice == computer: # comparing
        result = "It's a draw" #show the result
        emoji="🤝"

    elif (user_choice == 0 and computer == 2) or (user_choice == 1 and computer == 0) or (user_choice == 2 and computer == 1):
        result = "You win"
        emoji="🎉"
    else:
        result = "You lose"
        emoji="😒"
    message_label.config(text=result, font=("Arial", 10), fg="black")
    result_label.config(text=emoji,font=("Arial",50),fg="light blue")
    say(result)# speak the result

window = tk.Tk() #it will create a empty window using tkinter
window.title("Rock Paper Scissors") # title
window.geometry("800x900")#it will measure a height and width
window.configure(bg="purple")# color for window
tk.Label(window, text=" Choose one :").pack(pady=10) # it will create a label

tk.Button(window, text="    🪨Rock     ", bg="lightblue", command=lambda: game(0)).pack(pady=10)
tk.Button(window, text="    📄Paper     ",bg="lightblue", command=lambda :game(1)).pack(pady=10)
tk.Button(window, text="    ✂️Scissors     ",bg="lightblue", command=lambda:game(2)).pack(pady=10)

message_label=tk.Label(window, text=" ",width=10,height=3,bg="purple")
message_label.pack(pady=2) #it will display  emoji

result_label=tk.Label(window, text=" ",bg="purple") # it will display the result in text with voice
result_label.pack(pady=1)

tk.Button(window, text="quit",width=20,bg="lightblue", command=window.quit).pack(pady=5)#final exit button

window.mainloop() # without this line window will open and close very quickly




