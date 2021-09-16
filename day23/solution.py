class Register:
    def __init__(self, val):
        self.val = val

    def hlf(self):
        self.val = int(.5 * self.val)

    def tpl(self):
        self.val = self.val * 3

    def inc(self):
        self.val += 1

    def jmp(self, seq_no, jmp_step):
        return seq_no + jmp_step 
    
    def jie(self, seq_no, jmp_step):
        if self.val % 2 == 0:
            return self.jmp(seq_no, jmp_step)
        return seq_no
    
    def jio(self, seq_no, jmp_step):
        if self.val == 1:
            return self.jmp(seq_no, jmp_step)
        return seq_no

A = Register(0)
B = Register(0)

def parse_input(path = 'input.txt'):
    with open(path) as f:
        lines = f.readlines()
    return {key: val.strip() for key, val in enumerate(lines)}

def solve(instruction_seq, seq_no):
    if seq_no >= len(instruction_seq):
        return
    curr_instruction_line = instruction_seq[seq_no]
    
    instruction_split = curr_instruction_line.split()

    instruction = instruction_split[0]
    register = instruction_split[1].strip(',')
    if instruction == 'hlf':
        if register == 'a':
            A.hlf()
        else:
            B.hlf()
        solve(instruction_seq, seq_no + 1)
    elif instruction == 'tpl':
        if register == 'a':
            A.tpl()
        else:
            B.tpl()
        solve(instruction_seq, seq_no + 1)
    elif instruction == 'inc':
        if register == 'a':
            A.inc()
        else:
            B.inc() 
        solve(instruction_seq, seq_no + 1) 
    elif instruction == 'jmp':
        step = instruction_split[-1] 
        solve(instruction_seq, seq_no + step) 
    elif instruction == 'jio':
        step = int(instruction_split[-1])
        if register == 'a':
            solve(instruction_seq, A.jio(seq_no, step))
        else:
            solve(instruction_seq, B.jio(seq_no, step))
    elif instruction == 'jie':
        step = int(instruction_split[-1])
        if register == 'a':
            solve(instruction_seq, A.jie(seq_no, step))
        else:
            solve(instruction_seq, B.jie(seq_no, step))
    else:
        return 

if __name__ == '__main__':
   instruction_seq = parse_input()
   solve(instruction_seq, 0)
   print(A.val, B.val) 