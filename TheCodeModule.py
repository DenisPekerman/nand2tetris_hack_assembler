from instruction_tables import comp_dict_a0, comp_dict_a1, dest_dict, jump_dict, symbol_dict
import re

class TheCodeModule:
    '''input: dest field from Parser, returns bin vlaue of dest field'''
    def dest(self, string):           
        if string in dest_dict or string == None:
            return dest_dict.get(string, '000')
        return 'CODE DEST ERR'
    
    '''input: jump field from Parser, returns bin vlaue of jump field'''
    def jump(self, string):           
        if string in jump_dict or string == None:
            return jump_dict.get(string, '000')
        return 'CODE JMP ERR'
    
    '''input: comp field from Parser, returns bin vlaue of comp field'''
    def comp(self, string):         
        if string in comp_dict_a0: 
            comp_bin_value = comp_dict_a0[string]
        elif string in comp_dict_a1:
            comp_bin_value = comp_dict_a1[string]
        else:
            return 'CODE COMP ERR'
        return comp_bin_value
    
    '''helper function, converts numeric to binary'''
    def convert_number_to_bin_str(self, string):
        bin_numeric = int(string)
        bin_numeric = bin(bin_numeric)
        bin_numeric = bin_numeric.replace('0b', '')
        bin_numeric = bin_numeric.rjust(16, '0')
        return bin_numeric

    '''input: L_INSTRUCTION, LOOP/END/STOP --> 'xxx', returns bin value of line number of lable'''
    def label(self, string):   
        if string in symbol_dict:
            lable_deci_val = symbol_dict[string]
            return self.convert_number_to_bin_str(lable_deci_val)
        return 'CODE LABEL NOT FOUND'
    
    '''input: A_INSTRUCTION, 2/sum/i/54 --> 'numeric' or 'symbol', returns bin value of numeric or symbolic A instruction'''
    def code_a_instruction(self, string): 
        if string.isnumeric():
            return self.convert_number_to_bin_str(string)
        else: 
            a_symbol = symbol_dict[string]
            return self.convert_number_to_bin_str(a_symbol)
        


    


if __name__ == "__main__":
    code = TheCodeModule()
    print(code.label('R15'))
    print(code.comp('A+1'))
    print(code.dest("AM"))
    print(code.jump('JEQ'))
    print(code.code_a_instruction('R14'))
            

        