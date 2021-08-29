import random
import json
import customboard as cb
class snakeladder:	
	board=[]
		
	def newgame(self):
		print("\n\t\t\t\t\t\tNew Game")
		self.name=input("\nEnter your name: ")		
		while True:
			print("\n1. Computer\n2. Player")
			vs=input("\nSelect your opponent: ")
			if vs=="1":
				self.vsname=("Computer")
				break
			elif vs=="2":
				self.vsname=input("\nEnter your opponent name: ")
				break
			else:
				print("Enter the correct number")
		self.selectboard()
		
	def selectboard(self):
		print("\nChoose your favourite board")
		self.showboard()
		self.board_num=int(input("\nEnter your favourite board serial number "))
		self.num=self.board_num-1
		self.start()
		
		
	def showboard(self):
		fp=open("board.json","r")
		b=fp.readlines()
		for js in b:
			c=json.loads(js)
			snakeladder.board.append(c)
		fp.close()
		for num in range(len(snakeladder.board)):
			print(f"\nSerial Number - {num+1}")
			print("Created by -",snakeladder.board[num]["name"],"\nTotal number of snakes=",len(snakeladder.board[num]["sh"]),"\nTotal number of ladders=",len(snakeladder.board[num]["lh"]))
			print("\n")
			print("SH=Snake Head\nST=Snake Tail\nLH=Ladder Head\nLT=Ladder Tail\n")
			
			for i in range(100,0,-1):
				sh=snakeladder.board[num]["sh"]
				st=snakeladder.board[num]["st"]
				lh=snakeladder.board[num]["lh"]
				lt=snakeladder.board[num]["lt"]
			
				if i in sh:
					a=str(sh.index(i)+1)
					j=f"SH{a}"
					print(j,end=" ")
				elif i in st:
					a=str(st.index(i)+1)
					k=f"ST{a}"
					print(k,end=" ")
		
				elif i in lh:
					a=str(lh.index(i)+1)
					l=f"LH{a}"
					print(l,end=" ")	
		
				elif i in lt:
					a=str(lt.index(i)+1)
					j=f"LT{a}"
					print(j,end=" ")
			
				elif i<10:
					print(f"00{i}",end=" ")
				elif i==100:
					print(i,end=" ")
				else:
					print(f"0{i}",end=" ")
				if (i-1)%10==0 and i!=100:
					print("\n",end="")
			
	def start(self):
		ss=snakeladder.board[self.num]["sh"]
		se=snakeladder.board[self.num]["st"]
		ls=snakeladder.board[self.num]["lt"]
		le=snakeladder.board[self.num]["lh"]
		p1=0
		p2=0
		s=0
		while True:
			s+=1
			if s%2!=0:
				c=input(f"\n{self.name} press any key for throwing the dice\n")
				a=self.dice()
				print("Dice -",a)
				print(f"{self.name}'s current position - {p1}")
				if a==1 and p1==0:
					p1=1
					print(f"{self.name} new position - {p1}")
				elif p1>=1:
					p1=p1+a
					print(f"{self.name}'s new position - {p1}")
					if p1 in ss:
						d=ss.index(p1)
						p1=se[d]
						print(f"Oops! Its a Snaaakkkeeeee\n{self.name}'s new position - {p1}")
					elif p1 in ls:
						h=ls.index(p1)
						p1=le[h]
						print(f"Yeah! Its a ladder\n{self.name}'s new position - {p1}")
					elif p1>100:
						p1=p1-a
						print(f"Sorry this move will not be counted because to win you want only  {100-p1} but your dice roll on {a}")
						print(f"{self.name}'s new current position - {p1}")
					elif p1==100:
						print(f"\n\n\t\t\tHoorah! {self.name} won")
						break
				print(f"{self.vsname}'s current position - {p2}")
									
			else:
				c=input(f"\n{self.vsname} press any key for throwing the dice\n")
				a=self.dice()
				print("Dice - ",a)
				print(f"{self.vsname}'s current position - {p2}")
				if a==1 and p2==0 :
					p2=1
					print(f"{self.vsname}'s new position - {p2}")
				elif p2>=1:
					p2=p2+a
					print(f"{self.vsname}'s new position - {p2}")
					if p2 in ss:
						dd=ss.index(p2)
						p2=se[dd]
						print( f"Oops! Its a Snaaakkeeee\n{self.vsname}'s new position - {p2}")
					elif p2 in ls:
						h=ls.index(p2)
						p2=le[h]
						print(f"Yeah! Its a ladder\n{self.vsname}'s new position - {p2}")
					elif p2>100:
						p2=p2-a
						print(f"Sorry this move will not be counted because to win you want only  {100-p2} but your dice roll on {a}")
						print(f"{self.vsname}'s new current position - {p2}")
					elif p2==100:
						print(f"\n\n\t\t\tHoorah! {self.vsname} win")
						break
						
				print(f"{self.name}'s current position - {p1}")
						
					
	def dice(self):
		return random.randint(1,6)
		
	
x=snakeladder()		
		
