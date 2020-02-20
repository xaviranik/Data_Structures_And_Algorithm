def balanced_expression_checker(s):
    stack = []
    for i, char in enumerate(s):
        if char == '<':
            stack.append(char)
        if char == '/' and s[i + 1] != '>':
            break
        if char == '>':
            stack.pop()

    if len(stack) == 0:
        print('balanced')
    else:
        print('not balanced')


balanced_expression_checker('<item/>item<item/>')
balanced_expression_checker('item<item>item<item/>')
balanced_expression_checker('<<item>/>')
