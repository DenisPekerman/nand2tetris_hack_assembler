#!/usr/bin/env python3

import sys
import re
from c_instruction_tables import comp_dict_a0, comp_dict_a1, dest_dict, jump_dict

def main(input_file, output_file):
    binary_output = []
    with open(input_file) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('@'):
                #process A inst
                res = process_a(line)
                binary_output.append(res)
            elif line.startswith('//') or len(line)==0:
                pass

            else:
                #process C inst
                res = process_c(line)
                binary_output.append(res)

    with open(output_file, 'w') as out_file:
        joined_output = '\n'.join(binary_output)
        out_file.write(joined_output)

def process_a(instruction): 
    process = instruction.replace('@', '')
    process = int(process)
    process = bin(process)
    process = process.replace('0b', '')
    process = process.rjust(16, '0')
    return process

def process_c(instruction):
    pattern = r"([AMD]+)?=?([^;]+);?([A-Z]+)?"
    match = re.match(pattern, instruction)

    if not match:
        #problem
        return 
    
    dest = match.group(1)
    comp = match.group(2)
    jump = match.group(3)

    dest_bin_value = dest_dict[dest] if dest in dest_dict else '000'
    jump_bin_value = jump_dict[jump] if jump in jump_dict else '000'
    
    if comp in comp_dict_a0.keys():
        comp_bin_value = comp_dict_a0[comp]
    else: 
        comp_bin_value = comp_dict_a1[comp]

    c_instruction = '111{}{}{}'.format(comp_bin_value, dest_bin_value, jump_bin_value)
  
    return c_instruction
             



if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
