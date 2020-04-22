import sys
ip = sys.argv[2]
usr = sys.argv[4]
psw = sys.argv[5]
non = False
def parse():
    if sys.argv[1] == '-ip':
        return ip
    if sys.argv[3] == '-usr':
        return usr
    if sys.argv[5] == '-psw':
        return psw
    else:
        non = True
        return non

