def inverseBinaryConvert(a, bits) :
    ans = ""
    while a > 1 :
        ans += str(a % 2)
        a = int(a/2)
    ans += "1"
    while len(ans) != bits :
        ans += "0"
    return ans


# Prerequisites
asToBin = {
    "ADD" : "01000",
    "SUB" : "11000",
    "ORR" : "00100",
    "NOR" : "10100",
    "AND" : "01100",
    "NND" : "11100",
    "XOR" : "00010",
    "XNR" : "10010",
    "RSH" : "01010",
    "LDI" : "11010",
    "JMP" : "00110",
    "BCH" : "10110",
    "CAL" : "01110",
    "RET" : "11110",
    "LOD" : "00001",
    "STO" : "10001",
    "LDP" : "01001",
    "STP" : "11001"
}
flags = {"NZ" : "00", "Z" : "10", "C" : "01", "NC" : "11"}
# Open file
try :
    programFile = open("program.asm", "r")
except :
    print("Error in reading file!")
# Creating output file
with open("program.mc", "w") as outFile :
    # Parsing
    for line in programFile :
        try :
            # Stripping sLine
            sLine = line.strip()
            opcode = sLine[0] + sLine[1] + sLine[2]
            # NOP - No operands
            if sLine.startswith("NOP") or sLine.startswith("nop") :
                outFile.write("00000000000000000")
            # HLT - No operands
            elif sLine.startswith("HLT") or sLine.startswith("hlt") :
                outFile.write("10000000000000000")
            # RET - No operands
            elif sLine.startswith("RET") or sLine.startswith("ret") :
                outFile.write("11110000000000000")
            # In the dictionary asToBin
            elif opcode.upper() in asToBin.keys() :
                outFile.write(asToBin[opcode.upper()])
                sLine = sLine.replace(opcode, "")
                sLine = sLine[:0] + sLine[1:]
                operands = sLine.split()
                # Three register operand operations
                if opcode.upper() in ["ADD", "SUB", "ORR", "NOR", "AND", "NND", "XOR", "XNR"] :
                    for i in range(0, 3) :
                        operands[i] = operands[i].replace("r", "")
                        operands[i] = operands[i].replace("R", "")
                        outFile.write(inverseBinaryConvert(int(operands[i]), 4))
                # LDI - Immediate operation with two operands
                elif opcode.upper() == "LDI" :
                    operands[1] = operands[1].replace("r", "")
                    operands[1] = operands[1].replace("R", "")
                    outFile.write(inverseBinaryConvert(int(operands[0]), 8))
                    outFile.write(inverseBinaryConvert(int(operands[1]), 4))
                # JMP, BCH and CAL - Address and flag operation with 1 or 2 operands
                elif opcode.upper() in ["JMP", "BCH", "CAL"] :
                    outFile.write(inverseBinaryConvert(int(operands[0]), 10))
                    outFile.write("00" if opcode.upper() != "BCH" else flags[operands[1].upper()])
                # LOD, STO and RSH - Two register operand operations
                elif opcode.upper() in ["LOD", "STO", "RSH"] :
                    for i in range(0, 2) :
                        operands[i] = operands[i].replace("r", "")
                        operands[i] = operands[i].replace("R", "")
                    if opcode.upper() in ["LOD", "RSH"] :
                        outFile.write(inverseBinaryConvert(int(operands[0]), 4) + "0000")
                        outFile.write(inverseBinaryConvert(int(operands[1]), 4))
                    else :
                        outFile.write(inverseBinaryConvert(int(operands[0]), 4))
                        outFile.write(inverseBinaryConvert(int(operands[1]), 4) + "0000")
            # Invalid Opcode Error
            else :
                print("Syntax Error in line '" + line.strip() + "' : Invalid opcode!")
                print("Press return to continue...")
                input()
        # Any other kind of error
        except :
            print("Error in line '" + line.strip() + "' : Unknown Error! Go check for yourself.")
            print("Press return to continue...")
            input()

        #Adding newline
        outFile.write("\n")
