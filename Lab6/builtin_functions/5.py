t = input()
def convert(x):
    if x.lower() == "true":
        return True
    elif x.lower() == "false":
        return False
    elif x.isdigit():
        return int(x)
    elif x == '""':
        return False
    else:
        return x



m_t = tuple(convert(x) for x in t.split())
print(all(m_t))