class Intcode:
    def __init__(self, memory):
        self.data = memory
        self.compute()
        
    def compute(self):
        i = 0
        isHalt = False

        while ((isHalt == False) and (i < self.data.size)):
            instruction = self.parseOpcode(i)
            print(instruction)
            if instruction["opcode"] == 1:
                self.data[instruction["param3"]] = instruction["param1"] + instruction["param2"]
                i += 4
            elif instruction["opcode"] == 2:
                self.data[instruction["param3"]] = instruction["param1"] * instruction["param2"]
                i += 4
            elif instruction["opcode"] == 3:
                self.data[self.data[i+1]] = input("Enter the System ID: ")
                i += 2
            elif instruction["opcode"] == 4:
                print("Output =", self.data[self.data[i+1]])
                i += 2
            elif instruction["opcode"] == 99:
                isHalt = True
            else:
                print("Unexpected Opcode")
                isHalt = True
        
    def parseOpcode(self, instIndex):
        instruction = self.data[instIndex]
        # Isolate Opcode
        opcode = instruction % 100
        if opcode == 99:
            parsedOpcode = {
                "opcode": opcode
            }
            return parsedOpcode

        # Truncate instruction
        instruction = int(instruction / 100)
        # Isolate parameter 1 mode
        paramMode1 = ((instruction % 10) == 1)
        if paramMode1:
            # Immediate mode, param 1 is raw data
            param1 = self.data[instIndex+1]
        else:
            # Position mode, param 1 is index of data
            param1 = self.data[self.data[instIndex+1]]
        if opcode > 2:
            parsedOpcode = {
                "opcode": opcode,
                "param1": param1
            }
            return parsedOpcode
        
        # Truncate instruction
        instruction = int(instruction / 10)
        # Isolate parameter 2 mode
        paramMode2 = ((instruction % 10) == 1)
        if paramMode2:
            # Immediate mode, param 2 is raw data
            param2 = self.data[instIndex+2]
        else:
            # Position mode, param 2 is index of data
            param2 = self.data[self.data[instIndex+2]]
        # Truncate instruction
        instruction = int(instruction / 10)
        # Position mode, param 2 is index of data
        param3 = self.data[instIndex+3]
        parsedOpcode = {
            "opcode": opcode,
            "param1": param1,
            "param2": param2,
            "param3": param3
        }
        return parsedOpcode
