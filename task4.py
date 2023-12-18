from tkinter import *
from tkinter import ttk
import random


root= Tk()


root.geometry("750x450")


root.title("ROCK PAPER SCISSOR GAME")


player_2 = {
   "0":"Rock",
   "1":"Paper",
   "2":"Scissor"
}


def button_off():
   b1.config(state= "disabled")
   b2.config(state= "disabled")
   b3.config(state= "disabled")


def isrock():
   value = player_2[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "MATCH TIE"
   elif value=="Scissor":
      match_result = "YOU WON!"
   else:
      match_result = "YOU LOST !"
   label.config(text = match_result)
   l1.config(text = "Rock")
   l3.config(text =value)
   button_off()


def ispaper():
   value = player_2[str(random.randint(0, 2))]
   if value == "Paper":
      match_result = "MATCH TIE"
   elif value=="Scissor":
      match_result = "YOU LOST!"
   else:
      match_result = "YOU WON!"
   label.config(text = match_result)
   l1.config(text = "Paper")
   l3.config(text = value)
   button_off()


def isscissor():
   value = player_2[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "YOU LOST !"
   elif value == "Scissor":
      match_result = "MATCH TIE"
   else:
      match_result = "YOU WON !"
   label.config(text = match_result)
   l1.config(text = "Scissor")
   l3.config(text = value)
   button_off()


def play_again():
   b1.config(state= "active")
   b2.config(state= "active")
   b3.config(state= "active")
   l1.config(text = "Player")
   l3.config(text = "Computer")
   label.config(text = "")


labelframe= LabelFrame(root, text= "Rock Paper Scissor Game", font= ('Arial 20 bold'),labelanchor= "n",bd=5,bg= "grey",width= 600, height= 450, cursor= "target")
labelframe.pack(expand= True, fill= BOTH)


l1= Label(labelframe, text="Player",bg="lime", font= ('Arial 18 bold'))
l1.place(relx= .18, rely= .1)


l2= Label(labelframe, text="VS", font= ('Arial 18 bold'), bg="grey")
l2.place(relx= .45, rely= .1)


l3= Label(labelframe, text="Computer", bg="pink",font= ('Arial 18 bold'))
l3.place(relx= .65, rely= .1)


label= Label(labelframe, text="", font=('Coveat', 25,'bold'), bg= "grey")
label.pack(pady=150)


b1= Button(labelframe, text= "Rock",bg= "yellow", font= ("Arial ",15,"bold"), width= 7, command= isrock)
b1.place(relx=.25, rely= .62)
b2= Button(labelframe, text= "Paper",bg= "salmon", font= ("Arial ",15,"bold"), width= 7 ,command= ispaper)
b2.place(relx= .41,rely= .62)
b3= Button(labelframe, text= "Scissor", bg= "cyan",font= ("Arial ",15,"bold"), width= 7, command= isscissor)
b3.place(relx= .58, rely= .62)


play_again= Button(labelframe, text= "reset",bg= "orchid", fg= "black",width= 7, font=("Arial ",15,"bold") ,command= play_again)
play_again.place(relx= .8, rely= .62)
root.mainloop()
