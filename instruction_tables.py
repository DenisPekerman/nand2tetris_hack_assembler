comp_dict_a0 = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",  # A register
    "!D": "0001101",
    "!A": "0110001",  # A register
    "-D": "0001111",
    "-A": "0110011",  # A register
    "D+1": "0011111",
    "A+1": "0110111",  # A register
    "D-1": "0001110",
    "A-1": "0110010",  # A register
    "D+A": "0000010",  # A register
    "D-A": "0010011",  # A register
    "A-D": "0000111",  # A register
    "D&A": "0000000",  # A register
    "D|A": "0010101"   # A register
}

comp_dict_a1 = {
    "M": "1110000",    # M register
    "!M": "1110001",   # M register
    "-M": "1110011",   # M register
    "M+1": "1110111",  # M register
    "M-1": "1110010",  # M register
    "D+M": "1000010",  # M register
    "D-M": "1010011",  # M register
    "M-D": "1000111",  # M register
    "D&M": "1000000",  # M register
    "D|M": "1010101"   # M register
}

dest_dict = {
    "M": "001",     # RAM[A]
    "D": "010",     # D register
    "MD": "011",    # RAM[A] and D register
    "A": "100",     # A register
    "AM": "101",    # A register and RAM[A]
    "AD": "110",    # A register and D register
    "AMD": "111"    # A register, RAM[A], and D register
}

jump_dict = {
    "JGT": "001",   # if out > 0 jump
    "JEQ": "010",   # if out = 0 jump
    "JGE": "011",   # if out >= 0 jump
    "JLT": "100",   # if out < 0 jump
    "JNE": "101",   # if out != 0 jump
    "JLE": "110",   # if out <= 0 jump
    "JMP": "111"    # Unconditional jump
}

symbol_dict = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}


