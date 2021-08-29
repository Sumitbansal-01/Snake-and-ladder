import json
def boardcreater():
		print("\n\t\t\t\t\t\tCreate board")
		a=input("Enter your name: ")
		while True:
			b=input("Enter the total number of snake: ")
			c=input("Enter the total number of ladder ")
			if b.isdigit() and c.isdigit():
				b=int(b)
				c=int(c)
				break
			else:
				print("Invalid Input")
		ss=[]
		se=[]
		ls=[]
		le=[]
		for i in range(b):
			while True:
				d=input("\nEnter the head position of snake ")
				e=input("Enter the tail position of snake ")
				if d.isdigit() and e.isdigit():
					d=int(d)
					e=int(e)
					break
				else:
					print("Invalid Input")
			ss.append(d)
			se.append(e)
			
		for j in range(c):
			while True:
				f=input("\nEnter the start position of ladder ")
				g=input("Enter the end position of ladder ")
				if f.isdigit() and g.isdigit():
					f=int(f)
					g=int(g)
					break
				else:
					print("Invalid Input")
			ls.append(g)
			le.append(f)
		js={"name":a,"sh":ss,"st":se,"lh":ls,"lt":le}
		return js
		
def createboard():
		js=boardcreater()
		jso=json.dumps(js)
		fp=open("board.json","a")
		fp.write(jso+"\n")
		fp.close()
		print("\nYour board is created successfully\n\n")