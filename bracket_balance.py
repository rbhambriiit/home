
def check_bracket(text):
    if len(text) %2 != 0:
        return False

    stack = []
    left_braces = ['(', '{', '[']
    right_braces = [')', '}', ']']
    matched_pair = dict(zip(right_braces, left_braces))

    for char in text:
        if char in left_braces:
            # push to stack
            stack.append(char)
        else:
            if stack:
                last = stack[-1]
                if char in right_braces:
                    # check if evenly placed
                    if last == matched_pair[char]:
                        # remove last
                        stack.pop()
                        continue
                    # uneven
            return False

    # stack is pending means unbalanced
    if stack:
        return False
    return True



# main

# s = '{[()]}'
# s = '{{[[(())]]}'
s = ')('

status = check_bracket(s)
if status:
    print 'YES'
else:
    print 'NO'