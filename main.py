

def user_input():
    s = input("Enter your value: ")
    return s

def check_number(s):
    try: si = float(s)
    except ValueError as e:
        return f"Caught an error {e}"
    if si > 7:
        return 'Hello'
    else: 
        return "Number is lower than 7 or equal to 7"

def look_for_John(s):
    if s == 'John':
        return 'Hello, John'
    try:
        float(s)
        return "Inputted value is number"
    except:
        pass
    if any(sep in s for sep in [",", ";", " "]):
        return "Inputted value is array"
    return "There is no such name"

def is_it_array(s):
    separators = [",", ";"]
    def_separator = " "
    chosen_sep = def_separator
    for i in separators: 
        if i in s:
            chosen_sep = i
            break
    list_s = s.split(chosen_sep)
    result = []
    multiples = []
    try: 
        for i in list_s:
            stripped_list_s = i.strip()
            if not stripped_list_s:
                continue
            result.append(float(stripped_list_s))
    except ValueError as e:
        return f"Caught an error {e}"
    for j in result:
        if j % 3 == 0:
            multiples.append(int(j))
    if multiples:
        return " ".join(str(x) for x in multiples)
    else: 
        return "Array is empty"


if __name__ == "__main__":
    while True:
        print("Choose mode")
        print("1 - Single input (all checks)")
        print("2 - Separate inputs (one per checks)")
        mode = input("Enter mode: ")
        if mode == "1":
            s = user_input()
            print("--- Check 1 ---")
            print(check_number(s))
            print("--- Check 2 ---")
            print(look_for_John(s))
            print("--- Check 3 ---")
            print(is_it_array(s))
            print("Thank you!")
            break
        elif mode == "2":
            s1 = input("Enter a number: ")
            print(check_number(s1))
            s2 = input("Enter a name: ")
            print(look_for_John(s2))
            s3 = input("Enter an array: ")
            print(is_it_array(s3))
            print("Thank you!")
            break
        else: 
            print("You need to choose mode.")