

class Parser:
    file = None
    line = None

    def __init__(self, filename):
        self.file = open(filename, "r")

    def _hasMoreLines(self):
        self.line = self.file.readline()
        if not self.line:
            return False
        else:
            self.line = self.line.strip()
            return True

    
    '''cleaning white space and comments'''
    def advance(self):
        while self._hasMoreLines():
            if self.line.startswith("//"): 
                continue
            if self.line.strip() == '': 
                continue
            return True

    '''
    classifying instructions
    A_INSTRUCTION (address) symbolics : @xxx
    L_INSTRUCTION (label) symbolics : (xxx)
    C_INSTRUCTION (computation) symbolics : dest = comp ; jump'''
   
    def instructionType(self):  
        if self.line.startswith('@'):
            return 'A_INSTRUCTION'    
        if self.line.startswith('(') and self.line.endswith(')'):
            return 'L_INSTRUCTION'
        if '=' in self.line or ';' in self.line:
            return 'C_INSTRUCTION'
        return 'INST TYPE ERR'


    '''cleaning lines from '@ and '()' '''
    def symbol(self):
        if self.instructionType() == 'A_INSTRUCTION': 
            return self.line[1:] 
        if self.instructionType() == 'L_INSTRUCTION': 
            return self.line[1:-1]
        return 'SYM ERR'
    
    '''next three func --> C_INSTRUCTION processing, dest/jump/comp'''

    '''if '=' is present, returns everything left to the '=' '''
    def dest(self):
        if self.instructionType() == 'C_INSTRUCTION': 
            idx = self.line.find('=')
            if idx == -1:
                return None
            return self.line[:idx].strip()

    '''if ';' is present, returns everything to the right of the ';'  '''
    def jump(self):
        if self.instructionType() == 'C_INSTRUCTION': 
            idx = self.line.find(';')
            if idx == -1:
                return None  
            return self.line[idx+1:].strip() 
    
    '''
    if 'dest' present and no 'jump', return everything to the right of '='
    if no 'dest' present and 'jump' does, return everything left to the ';'
    if both are present, return anything in between them'''
    def comp(self):
        if self.instructionType() == 'C_INSTRUCTION':
            dest = self.dest()
            jump = self.jump()
            if dest and not jump:             
                idx = self.line.find('=')
                return self.line[idx+1:].strip()
            if not dest and jump:             
                idx = self.line.find(';')
                return self.line[:idx].strip()                  
            if dest and jump:                 
                eq_idx = self.line.find('=')
                col_idx = self.line.find(';')
                return self.line[eq_idx+1:col_idx]
            return 'COMP ERR'


if __name__ == "__main__":
    parser = Parser("Pong.asm")
    parser.line = "AD=A+1;JMP"
    #print(parser.comp() == 'A+1')
    # print(parser.comp())
    # print(parser.jump())
    # print(parser.dest())
    # print(parser.symbol())
    print(parser.instructionType())