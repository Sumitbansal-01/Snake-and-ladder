import random
import customboard as cb

class cgame :
	detail=dict()
		
	def cdice(self):
		self.sdice=[]
		self.dice=[]
		print("\n\nDice Selection\n\n")
		x=input("How many number you want in your dice: ")
		print("\n")
		for i in range(int(x)):
			self.dice.append(int(input(f"Out of {x} enter your {i+1} dice number: ")))
		while True:
			self.sdice.append(int(input("\nEnter the number of your dice by which you want of start: ")))
			z=input("\nAre you want to enter more starting number?\nIf yes press '1' else any other key ")
			if z!="1":
				break
		
		a=input("\nYou want your dice to be biased\nIf yes press '1' else any other key: ")
		if a=="1":
			b=input("\nBy which number: ")
			c=input("How many time: ")
			for j in range(int(c)):
				self.dice.append(int(b))
		self.board()
			
	def rolldice(self):
		return random.choice(self.dice)
		
	def showboard(self):
		print("\n")
		print("SH=Snake Head\nST=Snake Tail\nLH=Ladder Head\nLT=Ladder Tail\nFIN=Finish\nSTR=Start\n")
		for i in range(int(cgame.detail["Size"]),0,-1):
				sh=self.js["sh"]
				st=self.js["st"]
				lh=self.js["lh"]
				lt=self.js["lt"]
			
				if i in sh:
					a=str(sh.index(i)+1)
					j=f"SH{a}"
					print(j,end=" ")
					
				elif i == int(cgame.detail["End"]):
					print("FIN",end=" ")
					
				elif i == int(cgame.detail["Start"]):
					print("STR",end=" ")
				
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
					
				elif i<100 and i >9:
					print(f"0{i}",end=" ")
			
				elif i<10:
					print(f"00{i}",end=" ")
					
				else:
					print(i,end=" ")
					
				if (i-1)%10==0 and i!=100:
					print("\n",end="")
		self.start()
		
		
	def board(self):
		self.js=cb.boardcreater()
		self.showboard()
		
	def rules(self):
		print("\n\n\t\t\t\t\t    Customized Game\n\n")
		print("______________________General Guide_________________________ \nThis is one of the unique feature of this game here you can customized the whole game starting from rule to board to dice. If you want you can use increase or decrease the size of the normal board from 100 to any number. Any number you can make your finishing point either it last number or starting zero number or in between them. You can make any number as a starting point either it is zero or number before the finishing point or after it. If you make the starting point after the finishing point then we have added a reverse mode also basically when you at the end point then your dice start moving in reverse order or you move in reverse for example you are 96 and ending point is 100 and you roll the dice on 6 then your new position will be 98 (i.e. 96+6 - 100) now if your dice roll on 2 then your position will 98-2=96 and this will repear until the counter is not reaching to zero here end point is not equal to finishing point. If you want you can also enable striking mode also it just same as it in ludo. If a counter strike the other counter then the other one return on the starting point not zero. Not only this you can cutomized your dice also if you want you can make it baised also.\n____________________________________________________________ \n\n")
		print("\n\nRules Customization\n\n")
		a=input("Enter the total number of squares: ")
		b=input("Enter the position of Winning square: ")
		c=input("Enter the position of Starting square: ")
		d=input("\nStriking allowed?\nEnter '1' for Yes  or any other key for not: ")
		cgame.detail["Size"]=a
		cgame.detail["End"]=b
		cgame.detail["Start"]=c
		cgame.detail["beat"]=d
		self.cdice()
		
	def start(self):
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

		ss=self.js["sh"]
		se=self.js["st"]
		ls=self.js["lt"]
		le=self.js["lh"]
		f=int(cgame.detail["End"])
		g=int(cgame.detail["Start"])
		h=int(cgame.detail["Size"])
		p=cgame.detail["beat"]
		p1=0
		p2=0
		s=0
		while True:
			s+=1
			if s%2!=0:
				c=input(f"\n{self.name} press any key for throwing the dice\n")
				a=self.rolldice()
				print("Dice -",a)
				print(f"{self.name}'s current position - {abs(p1)}")
				if a in self.sdice and p1==0:
					p1=g
					print(f"{self.name} new position - {abs(p1)}")
				elif abs(p1)>=1:
					p1=p1+a
					print(f"{self.name}'s new position - {abs(p1)}")
					
					if abs(p1) in ss:
						d=ss.index(abs(p1))
						p1=se[d]
						print(f"Oops! Its a Snaaakkkeeeee\n{self.name}'s new position - {abs(p1)}")
					elif abs(p1) in ls:
						h=ls.index(abs(p1))
						p1=le[h]
						print(f"Yeah! Its a ladder\n{self.name}'s new position - {abs(p1)}")
					elif p=="1" and abs(p2)==abs(p1):
						print(f" You striked {self.vsname}")
						p2=g
					elif p1>h:
						if h==f:
							p1=p1-a
							print(f"Sorry this move will not be counted to move bring {a} or less than it")
							print(f"{self.name}'s new current position - {p1}")
						else:
							p1=-(2*h-p1)
							print(f"No {self.name} is moving in reverse order\n{self.name}'s new current position - {abs(p1)}")
						
					elif abs(p1)==f:
						print(f"\n\n\t\t\tHoorah! {self.name} won")
						break
				print(f"{self.vsname}'s current position - {abs(p2)}")
									
			else:
				c=input(f"\n{self.vsname} press any key for throwing the dice\n")
				a=self.rolldice()
				print("Dice - ",a)
				print(f"{self.vsname}'s current position - {p2}")
				if a in self.sdice and p2==0 :
					p2=g
					print(f"{self.vsname}'s new position - {abs(p2)}")
				elif abs(p2)>=1:
					p2=p2+a
					print(f"{self.vsname}'s new position - {abs(p2)}")
					if abs(p2) in ss:
						dd=ss.index(abs(p2))
						p2=se[dd]
						print( f"Oops! Its a Snaaakkeeee\n{self.vsname}'s new position - {abs(p2)}")
					elif abs(p2) in ls:
						h=ls.index(abs(p2))
						p2=le[h]
						print(f"Yeah! Its a ladder\n{self.vsname}'s new position - {abs(p2)}")
						
					elif p=="1" and abs(p2)==abs(p1):
						print(f" You striked {self.name}")
						p1=g
						
					elif p2>h:
						if h==f:
							p2=p2-a
							print(f"Sorry this move will not be counted to move bring {a} or less than it")
							print(f"{self.vsname}'s new current position - {p1}")
						else:
							p2=-(2*h-p2)
							print(f"No {self.vsname} is moving in reverse order\n{self.vsname}'s new current position - {abs(p2)}")
							
					elif abs(p2)==f:
						print(f"\n\n\t\t\tHoorah! {self.vsname} win")
						break
						
				print(f"{self.name}'s current position - {abs(p1)}")
				
a=cgame()
	
	
