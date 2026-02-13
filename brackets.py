
s = '[((())()(())]]'

def validate_brackets(s):
    pairs = {")": "(", "]": "["}
    stack = []
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack:
                return "Not valid - no opening bracket to match"
            top = stack.pop()
            if top != pairs[char]:
                return "Not valid - mismatched brackets"
    if len(stack) == 0:
        return "Sequence is valid"
    else:
        return f"Not valid - {len(stack)} unclosed bracket(s)"