import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random

m=tk.Tk()
m.configure(background= "DarkSlateGray1")
Label(m,font=("Dancing Script","28"), text="Rock Paper Scissor",background="DarkSlateGray1").place(x=750,y=10)

style=Style()
style.configure('W.TButton',font=("Times New Roman",15,"bold"),foreground="orangered")

def pplay():
	play.destroy()
	d=0
	l=0
	w=0
	
	
	def res(d,w,l,var,ccvar):
		r.destroy()
		p.destroy()
		s.destroy()
		v=Label(m,text="You Choose:",background= "DarkSlateGray1")
		v.place(x=200,y=200)
		va=Label(m,text=var,background= "DarkSlateGray1")
		va.place(x=650,y=200)
		ca=Label(m,text=ccvar,background= "DarkSlateGray1")
		ca.place(x=650,y=260)
		c=Label(m,text="Computer Choose:",background= "DarkSlateGray1")
		c.place(x=200,y=260)
		if d==1:
			ress=Label(m,text="Draw",background= "DarkSlateGray1")
			ress.place(x=450,y=850)
		if w==1:
			ress=Label(m,text="Win",background= "DarkSlateGray1")
			ress.place(x=450,y=850)
		if l==1:
			ress=Label(m,text="Lose",background= "DarkSlateGray1")
			ress.place(x=450,y=850)
			
		def des():
			play1.destroy()
			v.destroy()
			va.destroy()
			c.destroy()
			ca.destroy()
			ress.destroy()
			pplay()
			
		play1=Button(m,text="Play Again",command= lambda : des())
		play1.place(x=400,y=200)
		Button(m,text="Quit",command= m.destroy).place(x=400,y=1050)
		
	
	
	def rock(d,w,l):
		ccvar=str(cvar)
		var= "ROCK"
		if (cvar=="ROCK"):
			d+=1
		elif (cvar=="PAPER"):
	 		l+=1
		elif (cvar=="SCISSOR"):
			w+=1
		res(d,w,l,var,ccvar)
	def paper(d,w,l):
		ccvar=cvar
		var= "PAPER"
		if (cvar=="ROCK"):
		    w+=1
		elif (cvar=="PAPER"):
		    d+=1
		elif (cvar=="SCISSOR"):
			l+=1
		res(d,w,l,var,ccvar)
	def scissor(d,w,l):
		ccvar=cvar
		var= "SCISSOR"
		if (cvar=="ROCK"):
		    l+=1
		elif (cvar=="PAPER"):
		    w+=1
		elif (cvar=="SCISSOR"):
		    d+=1
		res(d,w,l,var,ccvar)
	cvar= random.choice(["ROCK","PAPER","SCISSOR"])
	r=Button(m,text="Rock",command= lambda:rock(d,w,l))
	r.place(x=400,y=100)
	p=Button(m,text="Paper",command= lambda:paper(d,w,l))
	p.place(x=400, y=150)
	s=Button(m,text="Scissor",command= lambda:scissor(d,w,l))
	s.place(x=400,y=200)
	
play=Button(text="Play",command=pplay,style="W.TButton")
play.place(x=730,y=200)

tk.mainloop()
