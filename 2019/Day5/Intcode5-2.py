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
                print("Output =", instruction["param1"])
                i += 2
            elif instruction["opcode"] == 5:
                if instruction["param1"] != 0:
                    i = instruction["param2"]
                else:
                    i += 3                    
            elif instruction["opcode"] == 6:
                if instruction["param1"] == 0:
                    i = instruction["param2"]
                else:
                    i += 3                    
            elif instruction["opcode"] == 7:
                if instruction["param1"] < instruction["param2"]:
                    self.data[instruction["param3"]] = 1
                else:
                    self.data[instruction["param3"]] = 0                    
                i += 4
            elif instruction["opcode"] == 8:
                if instruction["param1"] == instruction["param2"]:
                    self.data[instruction["param3"]] = 1
                else:
                    self.data[instruction["param3"]] = 0                    
                i += 4
            elif instruction["opcode"] == 99:
                isHalt = True
            else:
                print("Unexpected Opcode")
                isHalt = True
        
    def parseOpcode(self, instIndex):
        instruction = self.data[instIndex]
        parsedOpcode = {
            "opcode": instruction % 100,
            "param1": 0,
            "param2": 0,
            "param3": 0
        }
        if parsedOpcode["opcode"] == 99:
            return parsedOpcode

        # Check parameter 1 mode
        if ((int(instruction / 100) % 10) == 1):
            # Immediate mode, param 1 is raw data
            parsedOpcode["param1"] = self.data[instIndex+1]
        else:
            # Position mode, param 1 is index of data
            tempIndex = self.data[instIndex+1]
            parsedOpcode["param1"] = self.data[tempIndex]
        if parsedOpcode["opcode"] == 3 or parsedOpcode["opcode"] == 4:
            return parsedOpcode
        
        # Check parameter 2 mode
        if ((int(instruction / 1000) % 10) == 1):
            # Immediate mode, param 2 is raw data
            parsedOpcode["param2"] = self.data[instIndex+2]
        else:
            # Position mode, param 2 is index of data
            tempIndex = self.data[instIndex+2]
            print("tempIndex is", tempIndex)
            print("param2 is", self.data[tempIndex])
            parsedOpcode["param2"] = self.data[tempIndex]

        # Parameter 3
        parsedOpcode["param3"] = self.data[instIndex+3]
        return parsedOpcode
