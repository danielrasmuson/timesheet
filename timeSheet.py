#get clipboard data
from tkinter import Tk
r = Tk()
r.withdraw()
result = r.selection_get(selection = "CLIPBOARD")

#remove illegal - and put in list
result = result.replace("–","-").split("\n")

#strip spaces
calendarDataLines = []
for line in result:
	calendarDataLines.append(line.strip())

#format data on the same day to add day
holdLine = ""
resultLine = []
for line in calendarDataLines:
	if line[0].isdigit():
		resultLine.append(" ".join(holdLine.split()[0:3])+" "+line)
	else:		
		holdLine = line
		resultLine.append(line)

#format for excel
for line in resultLine:
	line = line.replace("am","").replace("pm","").split()
	print(" ".join(line[1:3])+",",end="")
	print(line[3]+",",end="")
	print(line[5])