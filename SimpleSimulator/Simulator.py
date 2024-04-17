from SystemDesc import *

memoryDict = {
    "0x00010000":0,
    "0x00010004":0,
    "0x00010008":0,
    "0x0001000c":0,
    "0x00010010":0,
    "0x00010014":0,
    "0x00010018":0,
    "0x0001001c":0,
    "0x00010020":0,
    "0x00010024":0,
    "0x00010028":0,
    "0x0001002c":0,
    "0x00010030":0,
    "0x00010034":0,
    "0x00010038":0,
    "0x0001003c":0,
    "0x00010040":0,
    "0x00010044":0,
    "0x00010048":0,
    "0x0001004c":0,
    "0x00010050":0,
    "0x00010054":0,
    "0x00010058":0,
    "0x0001005c":0,
    "0x00010060":0,
    "0x00010064":0,
    "0x00010068":0,
    "0x0001006c":0,
    "0x00010070":0,
    "0x00010074":0,
    "0x00010078":0,
    "0x0001007c":0,
}

regMem={ 
    "zero": "00000000000000000000000000000010", 
    "ra": "00000000000000000000000000000000",
    "sp": "00000000000000000000000000000000",
    "gp": "00000000000000000000000000000000",
    "tp": "00000000000000000000000000000000",
    "t0": "00000000000000000000000000000000",
    "t1": "00000000000000000000000000000000",
    "t2": "00000000000000000000000000000000",
    "s0": "00000000000000000000000000000000",
    "fp": "00000000000000000000000000000000",
    "s1": "00000000000000000000000000000000",
    "a0": "00000000000000000000000000000000",
    "a1": "00000000000000000000000000000000",
    "a2": "00000000000000000000000000000000",
    "a3": "00000000000000000000000000000000",
    "a4": "00000000000000000000000000000000",
    "a5": "00000000000000000000000000000000",
    "a6": "00000000000000000000000000000000",
    "a7": "00000000000000000000000000000000",
    "s2": "00000000000000000000000000000000",
    "s3": "00000000000000000000000000000000",
    "s4": "00000000000000000000000000000000",
    "s5": "00000000000000000000000000000000",
    "s6": "00000000000000000000000000000000",
    "s7": "00000000000000000000000000000000",
    "s8": "00000000000000000000000000000000",
    "s9": "00000000000000000000000000000000",
    "s10": "00000000000000000000000000000000",
    "s11": "00000000000000000000000000000000",
    "t3": "00000000000000000000000000000000",
    "t4": "00000000000000000000000000000000",
    "t5": "00000000000000000000000000000000",
    "t6":"00000000000000000000000000000000",
}

def readFile():
    file = open("SimpleSimulator\input.txt","r")
    f = file.readlines()
    for each in f:
        if(each[-1] == "\n"):
            each = each[0:(len(each)-1)]
        commands.append(each)
    file.close()

commands = []
readFile()

def DecimalToBinary(num,k):
        n=num
        if num<0:
            n=num*(-1)
        s=""
        while n>=1:
            s+=str(n%2)
            n=n//2
        s=s[::-1]
        l=len(s)
        if l<=k:
            str1="0"*(k-l)
            s=str1+s
            l= k

            str2=""
            if num<0:
                for i in range(l):
                    if s[i]=="0":
                        str2+="1"
                    else:
                        str2+="0"
                temp=list(str2)
                for i in range(len(temp)-1,-1,-1):
                    if str2[i]=="1":
                        temp[i]="0"
                    else:
                        temp[i]="1"
                        break
                s=""
                for i in temp:
                    s+=i
            return s 
        
        else:
            return "FLAG"
        
def findTwoscomplement(str):
    n=len(str)
    i=n-1
    while(i>=0):
        if(str[i]=='1'):
            break
 
        i-=1
    if i==-1:
        return '1'+str
    k=i-1
    while(k >= 0):
        if (str[k] == '1'):
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)
 
        k -= 1
    return str

def conv(s):
    if s[0]=="1":
        s=findTwoscomplement(s)
        return (int(s,2)*-1)
    else:
        return (int(s,2))
        

def signedconv(s):
    str=s[1::]
    if s[0]=='0':
        return int(str,2)
    else:
        return (int(str,2))*-1
    
for i in commands:

    currentCommand = i.strip()
    opcode = currentCommand[25::]


    #R Type
    if(opcode == "0110011"):
        rd = currentCommand[20:25]
        funct3 = currentCommand[17:20]
        rs1 = currentCommand[12:17]
        rs2 = currentCommand[7:12]
        funct7=currentCommand[0:7]

        rdNameIndex = list(regDesc.values()).index(rd)
        rdName = list(regDesc.keys())[rdNameIndex]

        rs1NameIndex = list(regDesc.values()).index(rs1)
        rs1Name = list(regDesc.keys())[rs1NameIndex]

        rs2NameIndex = list(regDesc.values()).index(rs2)
        rs2Name = list(regDesc.keys())[rs2NameIndex]

        #Add
        if(funct3 == "000" and funct7== "0000000"):
            temp = conv(regMem[rs2Name]) + conv(regMem[rs2Name])
            regMem[rdName] = DecimalToBinary(temp,32)
        if funct3=="000" and funct7=="0000000":
            temp=conv(regMem[rs2Name])*-1
            regMem[rdName] = DecimalToBinary(temp,32)
        if funct3=="001":
            temp=signedconv(regMem[rs1Name])-signedconv(regMem[rs2Name])
            regMem[rdName]=DecimalToBinary(temp,32)
        if funct3=="010":
            if int(regMem[rs1Name],2)<int(regMem[rs2Name],2):
                regMem[rdName]=DecimalToBinary(1,32)
        if funct3 =="011":
            if int(regMem[rs1Name],2)<int(regMem[rs2Name],2):
                regMem[rdName]=DecimalToBinary(1,32)