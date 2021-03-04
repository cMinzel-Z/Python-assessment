def random_converter(x):
    import random
    # set random list
    seq = [int, complex, float, str, bool]
    a = random.choice(seq)
    print('The type want to change: ',a)
    print('-------------------------------')
    # type change from string to others
    # str -> int
    if type(x) == str and a == int:
        # e.g. x = '123234' "int"
        if x.isdigit():
            x2 = a(x)
            print('x is: ', x2)
            print('After convert type: ', type(x2))
        else:
            print("Cannot be converted!")
            return None
    # str -> float
    elif type(x) == str and a == float:
        # e.g. x = '23.3232323' "float'
        if x.replace(".", "", 1).isdigit():
            x2 = a(x)
            print('x is: ', x2)
            print('After convert type: ', type(x2))
        else:
            print("Cannot be converted!")
            return None
    # str -> complex
    elif type(x) == str and a == complex:
        # e.g. x = '-2323.3232-32323.323j' "complex"
        # if right one is "+" or "-" get error
        if x[-1] == '+' or x[-1] == '-':
            print("Cannot be converted!")
            return None
        else:
            if x.count('j') == 1:
                # remove left ("+" or "-') and right "j" from "complex"
                x_after = x.lstrip('+-').rstrip("j")
                if x_after.count('j') == 0:
                    # make sure only one "-" between 2 numbers part
                    if "-" in x_after and x_after.count('-') == 1:
                        x_a_rm = x_after.split("-", 1)
                    # make sure only one "+" between 2 numbers part
                    elif "+" in x_after and x_after.count('+') == 1:
                        x_a_rm = x_after.split("+", 1)
                    else:
                        print("Cannot be converted!")
                        return None
                else:
                    print("Cannot be converted!")
                    return None
                # make it into one str for counting "."
                x_a_rm_s = "".join(x_a_rm)
                if x_a_rm_s.count('.') == 2:
                    # avoid one number part has 2 dots e.g x = '-2232.232.232-2323j' would get error
                    x_a_rm_1 = x_a_rm.pop()
                    # check left number part only has one dot
                    if str(x_a_rm_1).count('.') == 1:
                        x_a_rm_2 = x_a_rm_1.replace('.', '', 1)
                        if x_a_rm_2.isdigit():
                            x2 = a(x)
                            print('x is: ', x2)
                            print('After convert type: ', type(x2))
                        else:
                            print("Cannot be converted!")
                            return None
                    else:
                        print("Cannot be converted!")
                        return None
                else:
                    print("Cannot be converted!")
                    return None
            else:
                print("Cannot be converted!")
                return None
    # type change from complex to others
    # complex -> int
    elif type(x) == complex and a == int:
        print("Cannot be converted!")
        return None
    # complex -> float
    elif type(x) == complex and a == float:
        print("Cannot be converted!")
        return None
    else:
        x2 = a(x)
        print('x is: ', x2)
        print('After convert type: ', type(x2))
