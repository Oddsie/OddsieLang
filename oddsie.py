from sys import argv
import subprocess
print("ODDSIE (c) 2022 LFWJ")
if argv[1]=="help":
	print("oddsie [option] [file]")
	print("OPTIONS")
	print("help			Brings up this menu.")
	print("transpile		Transpiles [file] into python from Oddsie.")
	print("keywords		Shows list of Oddsie keywords.")
if argv[1]=="keywords":
	print("define,die,display,do,ifot,otherwise,end,if,loop,use,var")
if argv[1]=="transpile":
	i_f=open(argv[2])
	o_f=open(argv[2].replace(".od","")+".py","w")
	o_l=[]
	l_t=0
	l_n=1
	print("PROCESS: Starting lexing of "+i_f.name+"...")
	for line in i_f:
		l_i=""
		l_t=int(l_t)
		line=line.replace("\n","")
		tokens=line.replace("\t","").split()
		if tokens[0]=="end":
			l_t-=1
			print("KEYWORD FOUND: END")
		elif tokens[0]=="define":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"def "+tokens[1])
			print("KEYWORD FOUND: DEFINE")
		elif tokens[0]=="die":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"quit()")
			print("KEYWORD FOUND: DIE")
		elif tokens[0]=="display":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"print("+tokens[1].replace(";s"," ")+")")
			print("KEYWORD FOUND: DISPLAY")
		elif tokens[0]=="do":
			for i in range(l_t):l_i=l_i+"\t"
			try:o_l.append(tokens[1]+"("+tokens[2].replace(";s"," ")+")")
			except IndexError:o_l.append(tokens[1]+"()")
			print("KEYWORD FOUND: DO")
		elif tokens[0]=="ifot":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"elif "+tokens[1])
			print("KEYWORD FOUND: IFOT")
		elif tokens[0]=="otherwise:":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"else:")
			print("KEYWORD FOUND: OTHERWISE")
		elif tokens[0]=="if":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"if "+tokens[1])
			print("KEYWORD FOUND: IF")
		elif tokens[0]=="loop":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+"for i in range("+tokens[1]+"):")
			print("KEYWORD FOUND: LOOP")
		elif tokens[0]=="use":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append("import "+tokens[1])
			print("KEYWORD FOUND: USE")
		elif tokens[0]=="var":
			for i in range(l_t):l_i=l_i+"\t"
			o_l.append(l_i+tokens[1].replace(";s"," "))
			print("KEYWORD FOUND: VAR")
		elif tokens[0]==";":
			o_l.append("#"+tokens[1].replace(";s"," "))
			print("KEYWORD FOUND: COMMENT")
		else:print("WARNING: No keywords detected at line "+str(l_n))
		if line.endswith(":"):l_t+=1
		l_n+=1
	print("Done")
	print("PROCESS: Starting to write translation to "+o_f.name+"...")
	i=1
	for item in o_l:
		print("LINE WRITTEN: "+str(i))
		o_f.write(item+"\n")
		i+=1
	print("Done")