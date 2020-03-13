class Intcode:
    def __init__(self, memory):
        self.data = memory
        self.compute()
        
    def compute(self):
        i = 0
        isHalt = False

        while ((isHalt == False) and (i < self.data.size)):
            if self.data[i] == 1:
                self.add(self.data[i+1], self.data[i+2], self.data[i+3])
            elif self.data[i] == 2:
                self.multiply(self.data[i+1], self.data[i+2], self.data[i+3])
            elif self.data[i] == 99:
                isHalt = True
            else:
                print("Unexpected Opcode")
                isHalt = True
            i += 4
        print(self.data[0])
        
    def add(self, noun, verb, dest):
        self.data[dest] = self.data[noun] + self.data[verb]

    def multiply(self, noun, verb, dest):
        self.data[dest] = self.data[noun] * self.data[verb]
