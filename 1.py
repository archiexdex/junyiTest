
def f1(s):
    ret = ""
    for i in range(len(s)-1, -1, -1):
        ret += s[i]
    return ret

def f2(s):
    ret = ""    
    buf = s.split(" ")
    for idx, item in enumerate(buf):
        # buf[idx] = f1(item)
        ret += f1(item)
        if idx != len(buf)-1:
            ret += " "
    return ret


if __name__ == "__main__": 
    s1 = f1("junyiacademy")
    print(s1)
    s2 = f2("flipped class room is important")
    print(s2)
    