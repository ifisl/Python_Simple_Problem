def check_pairs(exp):
    # exp_split = exp.split("")

    exp_dict = {
        '}' : '{',
        ']' : '[',
        ')' : '('
    }

    exp_list = []

    for counter, e in enumerate(exp):
        if e in exp_dict.values():
            exp_list.append(e)
        elif e in exp_dict.keys() and len(exp_list) > 0:
            if exp_list[-1] == exp_dict[e]:
                exp_list.pop()
            else:
                return False
        elif e in exp_dict.keys() and len(exp_list) == 0:
            return False
        else:
            pass

    return not exp_list

# test

print(check_pairs("[()]{}{[()()]()}"))

print(check_pairs("![()]{}{[()()]()}"))

print(check_pairs("[(])"))

print(check_pairs("[()]{}{[()()]()}}"))

print(check_pairs("][(])"))

print(check_pairs("#][(])"))