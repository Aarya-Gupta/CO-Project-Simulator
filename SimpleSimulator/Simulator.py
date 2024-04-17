from SystemDesc import *
import sys
import os

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 Simulator.py <input_machine_code_file_path> <output_trace_file_path>")
        return

    inputFilePath = sys.argv[1]
    outputFilePath = sys.argv[2]

    if not os.path.exists(inputFilePath):
        print(f"Error: Input file '{inputFilePath}' not found.")
        return


    memoryDict = {
        "0x00010000":"00000000000000000000000000000000",
        "0x00010004":"00000000000000000000000000000000",
        "0x00010008":"00000000000000000000000000000000",
        "0x0001000c":"00000000000000000000000000000000",
        "0x00010010":"00000000000000000000000000000000",
        "0x00010014":"00000000000000000000000000000000",
        "0x00010018":"00000000000000000000000000000000",
        "0x0001001c":"00000000000000000000000000000000",
        "0x00010020":"00000000000000000000000000000000",
        "0x00010024":"00000000000000000000000000000000",
        "0x00010028":"00000000000000000000000000000000",
        "0x0001002c":"00000000000000000000000000000000",
        "0x00010030":"00000000000000000000000000000000",
        "0x00010034":"00000000000000000000000000000000",
        "0x00010038":"00000000000000000000000000000000",
        "0x0001003c":"00000000000000000000000000000000",
        "0x00010040":"00000000000000000000000000000000",
        "0x00010044":"00000000000000000000000000000000",
        "0x00010048":"00000000000000000000000000000000",
        "0x0001004c":"00000000000000000000000000000000",
        "0x00010050":"00000000000000000000000000000000",
        "0x00010054":"00000000000000000000000000000000",
        "0x00010058":"00000000000000000000000000000000",
        "0x0001005c":"00000000000000000000000000000000",
        "0x00010060":"00000000000000000000000000000000",
        "0x00010064":"00000000000000000000000000000000",
        "0x00010068":"00000000000000000000000000000000",
        "0x0001006c":"00000000000000000000000000000000",
        "0x00010070":"00000000000000000000000000000000",
        "0x00010074":"00000000000000000000000000000000",
        "0x00010078":"00000000000000000000000000000000",
        "0x0001007c":"00000000000000000000000000000000",
    }

    regMem={ 
        "zero": "00000000000000000000000000000000", 
        "ra": "00000000000000000000000000000000",
        "sp": "00000000000000000000000000000000",
        "gp": "00000000000000000000000000000000",
        "tp": "00000000000000000000000000000000",
        "t0": "00000000000000000000000000000000",
        "t1": "00000000000000000000000000000000",
        "t2": "00000000000000000000000000000000",
        "s0": "00000000000000000000000000000000",
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
        file = open(inputFilePath,"r")
        f = file.readlines()
        for each in f:
            if(each[-1] == "\n"):
                each = each[0:(len(each)-1)]
            commands.append(each)
        file.close()

    commands = []
    programCounter = 4
    finalList = []

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
        n = len(str)
        i = n - 1
        while(i >= 0):
            if (str[i] == '1'):
                break
            i -= 1
        if (i == -1):
            return '1'+str
        k = i - 1
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
        
    def binary_to_hex(binary_str):
        hex_str = ''
        binary_str = binary_str[::-1]
        padding = 4 - (len(binary_str) % 4)
        binary_str = '0' * padding + binary_str
        for i in range(0, len(binary_str), 4):
            chunk = binary_str[i:i + 4]
            decimal_value = 0
            for bit in chunk:
                decimal_value = decimal_value * 2 + int(bit)
            if decimal_value < 10:
                hex_str = str(decimal_value) + hex_str
            else:
                hex_str = chr(ord('a') + decimal_value - 10) + hex_str
        return hex_str[::-1]

    def bitwiseOR(a,b):
        c = []
        for i in range(0,4):
            if a[i] == "0" and b[i] == "0":
                c.append("0")
            else:
                c.append("1")
        result = "".join(c)
        return result

    def bitwiseXOR(a,b):
        c = []
        for i in range(0,4):
            if a[i] == "0" and b[i] == "0":
                c.append("0")
            elif a[i] == "1" and b[i] == "1":
                c.append("0")
            elif a[i] == "0" and b[i] == "1":
                c.append("1")
            else:
                c.append("1")
        result = "".join(c)
        return result

    def bitwiseAND(a,b):
        c = []
        for i in range(0, 4):
            if a[i] == '1' and b[i] == '1':
                c.append('1')
            else:
                c.append('0')
        result = ''.join(c)
        return result

    def sext(str):
        return ((32-len(str))*'0')+str
    
    while(programCounter <= len(commands)*4):

        currentCommand = commands[(programCounter//4)-1].strip()
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
                temp = conv(sext(regMem[rs1Name])) + conv(sext(regMem[rs2Name]))
                regMem[rdName] = DecimalToBinary(temp,32)
            if funct3=="000" and funct7=="0100000" and rs1Name=="x0":
                temp=conv(regMem[rs2Name])*(-1)
                regMem[rdName] = DecimalToBinary(temp,32)
            if funct3=="000" and funct7=="0100000":
                temp=signedconv(regMem[rs1Name])-signedconv(regMem[rs2Name])
                regMem[rdName]=DecimalToBinary(temp,32)
            if funct3=="010":
                if conv(regMem[rs1Name])<conv(regMem[rs2Name]):
                    regMem[rdName]=DecimalToBinary(1,32)
            if funct3 =="011":
                if int(regMem[rs1Name],2)<int(regMem[rs2Name],2):
                    regMem[rdName]=DecimalToBinary(1,32)
            if funct3 =="100":
                regMem[rdName] = bitwiseXOR(regMem[rs1Name], regMem[rs2Name])
            if funct3 =="110":
                regMem[rdName] = bitwiseOR(regMem[rs1Name], regMem[rs2Name])
            if funct3 =="111":
                regMem[rdName] = bitwiseAND(regMem[rs1Name], regMem[rs2Name])
            if funct3=="001":
                regMem[rdName]=DecimalToBinary(int(regMem[rs1Name],2)<<int(regMem[rs2Name],2),32)
            if funct3=="101":
                regMem[rdName]=DecimalToBinary(int(regMem[rs1Name],2)>>int(regMem[rs2Name],2))
            




        #I Type
        if(opcode == "0000011" or opcode == "0010011" or opcode == "1100111"):
            rd = currentCommand[20:25]
            funct3 = currentCommand[17:20]
            rs1 = currentCommand[12:17]
            immediate = currentCommand[0:12]

            rdNameIndex = list(regDesc.values()).index(rd)
            rdName = list(regDesc.keys())[rdNameIndex]

            rs1NameIndex = list(regDesc.values()).index(rs1)
            rs1Name = list(regDesc.keys())[rs1NameIndex]

            #lw
            if(funct3 == "010"):
                newVal = DecimalToBinary(conv(regMem[rs1Name]) + conv(immediate),32)
                if("0x" + binary_to_hex(newVal) in memoryDict.keys()):
                    regMem[rdName] = memoryDict["0x" + binary_to_hex(newVal)]
                else:
                    regMem[rdName] = memoryDict["0x00010000"]

            #addi
            if(opcode == "0010011" and funct3 == "000"):
                regMem[rdName] = DecimalToBinary(conv(regMem[rs1Name]) + conv(immediate),32)
            
            #sltiu
            if(funct3 == "011"):
                if(int(regMem[rs1Name],2) < int(immediate,2)):
                    regMem[rdName] = DecimalToBinary(1,32)

            #jalr
            if(opcode == "1100111"):
                regMem[rdName] = DecimalToBinary(programCounter+4,32)

                binPC = DecimalToBinary(programCounter,32)
                binPC = binPC[0:31] + "0"
                programCounter = conv(binPC)
                
                programCounter = conv(regMem[rs1Name]) + conv(immediate)

        #S Type
        if(opcode == "0100011"):
            immediate1 = currentCommand[20:25]
            funct3 = currentCommand[17:20]
            rs1 = currentCommand[12:17]
            rs2 = currentCommand[7:12]
            immediate2 = currentCommand[0:7]

            relImmediate = currentCommand[0:7] + currentCommand[20:25]

            rs1NameIndex = list(regDesc.values()).index(rs1)
            rs1Name = list(regDesc.keys())[rs1NameIndex]

            rs2NameIndex = list(regDesc.values()).index(rs2)
            rs2Name = list(regDesc.keys())[rs2NameIndex]

            if("0x" + binary_to_hex(DecimalToBinary(conv(regMem[rs1Name]) + conv(relImmediate),32)) in list(memoryDict.keys())):
                memoryDict["0x" + binary_to_hex(DecimalToBinary(conv(regMem[rs1Name]) + conv(relImmediate),32))] = regMem[rs2Name]
            else:
                memoryDict["0x00010000"] = regMem[rs2Name]

        
        #U Type lui
        if(opcode == "0110111"):
            rd = currentCommand[20:25]
            immediate = currentCommand[0:20] + (12*"0")

            rdNameIndex = list(regDesc.values()).index(rd)
            rdName = list(regDesc.keys())[rdNameIndex]

            regMem[rdName] = DecimalToBinary(conv(immediate),32)

        #U Type auipc
        if(opcode == "0010111"):
            rd = currentCommand[20:25]
            immediate = currentCommand[0:20] + (12*"0")

            rdNameIndex = list(regDesc.values()).index(rd)
            rdName = list(regDesc.keys())[rdNameIndex]

            regMem[rdName] = DecimalToBinary(programCounter + conv(immediate),32)


        #J Type
        if(opcode == "1101111"):
            rd = currentCommand[20:25]
            immediate = currentCommand[0] + currentCommand[12:20] + currentCommand[11] + currentCommand[1:11] + "0"

            rdNameIndex = list(regDesc.values()).index(rd)
            rdName = list(regDesc.keys())[rdNameIndex]

            regMem[rdName] = DecimalToBinary(programCounter + 4,32)

            binPC = DecimalToBinary(programCounter,32)
            binPC = binPC[0:31] + "0"
            programCounter = conv(binPC)

            programCounter = programCounter + conv(immediate) 

        
        #B Type
        if(opcode == "1100011"):
            immediate = currentCommand[0] + currentCommand[24] + currentCommand[1:7] + currentCommand[20:24] + "0"
            
            funct3 = currentCommand[17:20]
            rs1 = currentCommand[12:17]
            rs2 = currentCommand[7:12]

            rs1NameIndex = list(regDesc.values()).index(rs1)
            rs1Name = list(regDesc.keys())[rs1NameIndex]

            rs2NameIndex = list(regDesc.values()).index(rs2)
            rs2Name = list(regDesc.keys())[rs2NameIndex]


            #bew
            if(funct3 == "000"):
                newval = programCounter + conv(immediate)
                if(conv(regMem[rs1Name]) == conv(regMem[rs2Name])):
                    programCounter = newval
            #bne
            if(funct3 == "001"):
                newval = programCounter + conv(immediate)
                if(conv(regMem[rs1Name]) != conv(regMem[rs2Name])):
                    programCounter = newval
            #bge
            if(funct3 == "101"):
                newval = programCounter + conv(immediate)
                if(conv(regMem[rs1Name]) >= conv(regMem[rs2Name])):
                    programCounter = newval
            #bgeu
            if(funct3 == "111"):
                newval = programCounter + signedconv(immediate)
                if(int(regMem[rs1Name],2) == int(regMem[rs2Name],2)):
                    programCounter = newval
            #blt
            if(funct3 == "100"):
                immediate = currentCommand[0] + currentCommand[24] + currentCommand[1:7] + currentCommand[20:24] + "10"
                newval = programCounter + conv(immediate)
                if(conv(regMem[rs1Name]) < conv(regMem[rs2Name])):
                    programCounter = newval
            #bltu
            if(funct3 == "110"):
                newval = programCounter + conv(immediate)
                if(int(regMem[rs1Name],2) < int(regMem[rs2Name],2)):
                    programCounter = newval







        programCounter += 4
                
            





        keyValues = list(regMem.keys())
        binPC = DecimalToBinary(programCounter, 32)
        regValues = "0b" + binPC + " "
        
        for i in keyValues:
            regValues = regValues + "0b" + regMem[i] + " "
        
        finalList.append(regValues)

    memoryList = []
    for i in range(len(memoryDict.keys())):
        keyList = list(memoryDict.keys())
        valList = list(memoryDict.values())
        valueMain = keyList[i] + ":" + valList[i]
        memoryList.append(valueMain)


    for i in range(len(finalList)):
        finalList[i] = finalList[i].strip()
    
    f = open(outputFilePath, "w")
    for i in finalList:
        f.write(i + "\n")
    for i in memoryList:
        f.write(i + "\n")
    f.close()

main()
