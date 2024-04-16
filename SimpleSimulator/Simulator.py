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
    "zero": 2, 
    "ra": 0,
    "sp": 0,
    "gp": 0,
    "tp": 0,
    "t0": 0,
    "t1": 0,
    "t2": 0,
    "s0": 0,
    "fp": 0,
    "s1": 0,
    "a0": 0,
    "a1": 0,
    "a2": 0,
    "a3": 0,
    "a4": 0,
    "a5": 0,
    "a6": 0,
    "a7": 0,
    "s2": 0,
    "s3": 0,
    "s4": 0,
    "s5": 0,
    "s6": 0,
    "s7": 0,
    "s8": 0,
    "s9": 0,
    "s10": 0,
    "s11": 0,
    "t3": 0,
    "t4": 0,
    "t5": 0,
    "t6": 0,
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

for i in commands:

    currentCommand = i.strip()
    opcode = currentCommand[25::]


    #R Type
    if(opcode == "0110011"):
        rd = currentCommand[20:25]
        funct3 = currentCommand[17:20]
        rs1 = currentCommand[12:17]
        rs2 = currentCommand[7:12]

        rdNameIndex = list(regDesc.values()).index(rd)
        rdName = list(regDesc.keys())[rdNameIndex]

        rs1NameIndex = list(regDesc.values()).index(rs1)
        rs1Name = list(regDesc.keys())[rs1NameIndex]

        rs2NameIndex = list(regDesc.values()).index(rs2)
        rs2Name = list(regDesc.keys())[rs2NameIndex]

        #Add
        if(funct3 == "000"):
            regMem[rdName] = regMem[rs1Name] + regMem[rs2Name]
            print(regMem[rdName])

        



