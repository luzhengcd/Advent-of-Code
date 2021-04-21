import string
import regex as re
import sys
    

req1 = {'abc', 'bcd', 'cde', 'def', 'efg', 'fgh',
        'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz'}

req1_pattern = '|'.join([''.join(list(i)[::-1]) for i in req1])
req2_exclude = {'i', 'o', 'l'}

valid_letter = [i for i in string.ascii_lowercase if i not in req2_exclude]
alpha_to_num = {letter: idx for idx, letter in enumerate(valid_letter)}
num_to_alpha = {idx: letter for idx, letter in enumerate(valid_letter)}

def check_req1(s):
    return re.finditer(req1_pattern, s, overlapped=True)
    

def check_req2(s):
    pattern = r'([a-z])\1'
    return len(set(re.findall(pattern, s)))

def check_pass(s):
    # check requirement 1
    iterator = check_req1(s)
    for _ in iterator:
        # check requirement 2
        if check_req2(s) >= 2:
            return True
    return False

def get_next(pass_reversed, idx):
    '''
    password is a list of letters in the password in reversed order
    '''
    if idx == 8:
        print('The password has reached its upper bound')
        return
    else:  
        curr = alpha_to_num[pass_reversed[idx]]
        if curr == 22:
            pass_reversed[idx] = 'a'
            get_next(pass_reversed, idx + 1)
        else:
            pass_reversed[idx] = num_to_alpha[curr + 1]
            return

def main(password):
    p = False
    pass_lst = list(password)[::-1]
    while not p:
        get_next(pass_lst, 0)
        pass_reverse = ''.join(pass_lst) 
        p = check_pass(pass_reverse)
        
    return pass_lst

if __name__ == '__main__':
    # password = 'vzbxxyzz'
    password = open(sys.argv[1], 'r').read().strip()
    print('input is ', password)
    ans1_reverse = main(password)
    ans1 = ''.join(ans1_reverse[::-1]) 
    print('Answer for part1: ', ans1)
    ans2_reverse = main(ans1)
    ans2 = ''.join(ans2_reverse[::-1])  
    print('Answer for part2: ', ans2) 

        