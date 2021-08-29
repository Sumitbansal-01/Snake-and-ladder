import salmain as sal
import cmode as cm
import customboard as cb

while True:
	print("\n\n\t\t   Welcome to Snake&Ladder\n\n\n")
	print("\n1. New Game\n2. Create board\n3. Customized game\n4. Exit")
	while True:
			b=input("\nEnter your number: ")
			if b==str(1):
				sal.x.newgame()
				break
			elif b=="2":
				cb.createboard()
				break
			elif b==str(3):
				cm.a.rules()
				break
			elif b==str(4):				
				print("\n\t\t   Thanks for joining us")
				quit()
			else:
				print("\nYou entered the wrong number")