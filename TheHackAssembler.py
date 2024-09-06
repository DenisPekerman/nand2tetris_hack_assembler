from Parser import Parser
from TheCodeModule import TheCodeModule
from instruction_tables import symbol_dict
import sys


class TheHackAssembler:
    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.binary_output = []
 
        
    def first_pass(self):
        line_counter = 0
        parser = Parser(self.input_file)
        while parser.advance():
            instruction_type = parser.instructionType()
            if instruction_type == 'L_INSTRUCTION':
                # line_counter -= 1
                symbol = parser.symbol()
                if symbol not in symbol_dict:
                    symbol_dict[symbol] = line_counter
            else:
                line_counter += 1
          

    def second_pass(self):
        register_counter = 16
        parser = Parser(self.input_file)
        while parser.advance():
            instruction_type = parser.instructionType()
            if instruction_type == 'A_INSTRUCTION':
                symbol = parser.symbol()
                if symbol not in symbol_dict and not symbol.isnumeric():
                    symbol_dict[symbol] = register_counter
                    register_counter += 1
                
        

    def translation(self):
        parser = Parser(self.input_file)
        code = TheCodeModule()
        while parser.advance():
            line = parser.instructionType()
            if line == 'A_INSTRUCTION':
                symbol_txt  = parser.symbol()
                bin_line = code.code_a_instruction(symbol_txt)
                self.binary_output.append(bin_line)
            # elif line == 'L_INSTRUCTION':
            #     symbol_txt = parser.symbol()
            #     bin_line = code.label(symbol_txt)
            #     self.binary_output.append(bin_line)
            elif line == 'C_INSTRUCTION':
                
                comp_txt = parser.comp()
                comp = code.comp(comp_txt)
                
                dest_txt = parser.dest()
                dest = code.dest(dest_txt)
            
                jump_txt = parser.jump()
                jump = code.jump(jump_txt)
                
                c_instruction = '111{}{}{}'.format(comp, dest, jump)
                self.binary_output.append(c_instruction)
        

    def out_file(self):
        with open(output_file, 'w') as out_file:
            joined_output = '\n'.join(self.binary_output)
            out_file.write(joined_output)



if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    x = TheHackAssembler(input_file, output_file)
    x.first_pass()
    x.second_pass()
    x.translation()
    x.out_file()
    
