import re

symbolTable={"R0":0,"R1":1,"R2":2,"R3":3,"R4":4,"R5":5,"R6":6,"R7":7,"R8":8,"R9":9,"R10":10,"R11":11,"R12":12,"R13":13,"R14":14,"R15":15,"SP":0,"LCL":1,"ARG":2,"THIS":3,"THAT":4,"SCREEN":16384,"KBD":"24576"}

dest_dict={"":"000","M":"001","D":"010","A":"100","MD":"011","AM":"101","AD":"110","AMD":"111"}

jump_dict={"":"000","JGT":"001","JEQ":"010","JGE":"011","JLT":"100","JNE":"101","JLE":"110","JMP":"111"}

comp_dict={"0":"0101010","1":"0111111","-1":"0111010","D":"0001100","A":"0110000","M":"1110000","!D":"0001101","!A":"0110001","!M":"1110001","-D":"0001111","-A":"0110011","-M":"1110011","D+1":"0011111","A+1":"0110111","M+1":"1110111","D-1":"0001110","A-1":"0110010","M-1":"1110010","D+A":"0000010","D+M":"1000010","D-A":"0010011","D-M":"1010011","A-D":"0000111","M-D":"1000111","D&A":"0000000","D&M":"1000000","D|A":"0010101","D|M":"1010101"}

file1=input()
with open(file1,'r') as file:
    code=[]
    for line in file:
        code.append(line.strip())
    removelist=[]
    for i in code:
        if (i[0:2]=="//" or i==""):
            removelist.append(i)
    for i in removelist:
        code.remove(i)
    code1=[]
    for i in code:
        temp=i.split("//")
        code1.append(temp[0].strip())
file.close()
code=code1
binaryInstructions=[]

def getBinary(n):
    s=""
    while (n!=0):
        if (n%2==0):
            s="0"+s
        else:
            s="1"+s
        n=n//2
    while (len(s)<15):
        s="0"+s
    return s

def Assembler():
    global code
    global symbolTable
    global binaryInstructions
    global jump_dict
    global dest_dict
    global comp_dict
    line_no=0
    remLabels=[]
    vars=16
    for i in code:
        if (i[0]=="("):
            symbolTable[i[1:len(i)-1]]=line_no+1
            remLabels.append(i)
        else:
            line_no+=1
    for i in remLabels:
        code.remove(i)
    for i in code:
        if i[0]=="@":
            try:
                v=eval(i[1:len(i)])
            except ValueError:
                if i[1:] in symbolTable.keys():
                    v=symbolTable[i[1:]]
                else:
                    symbolTable[i[1:]]=vars
                    v=vars
                    vars+=1
            instr="0"+getBinary(v)
            binaryInstructions.append(instr)
        else:
            c=re.split("=|;",i)
            instr="111"
            if (len(c)==3):
                instr=instr+comp_dict(c[1])+dest_dict(c[0])+jump_dict(c[2])
            else:
                if len(i.split("="))==2:
                    instr=instr+comp_dict(c[1])+dest_dict(c[0])+"000"
                else:
                    instr=instr+comp_dict(c[0])+"000"+jump_dict(c[1])
            binaryInstructions.append(instr)

Assembler()

with open("program.hack",'w') as write:
    for i in binaryInstructions:
        write.write(i)
        write.write('\n')