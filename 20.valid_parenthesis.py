def isValid(s):
    left = ['(', '{', '[']
    right = [']', '}', ')']
    parent_map = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    new_list = []
    for i in s:
        if i in left:
            new_list.append(i)
        elif i in right:
            if len(new_list) <= 0:
                return False
            last_piece = new_list.pop()
            if last_piece == parent_map[i]:
                continue
            else:
                return False

    if len(new_list) == 0:
        return True

if __name__ == '__main__':
    s = "()[]{}"
    s2 = "([)]"
    isValid(s)
    isValid(s2)