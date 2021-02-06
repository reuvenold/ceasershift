abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = abc.upper()

ret = 'ret'
pri = 'pri'


def ceaser_shift(text, shift=0, mode=pri):
    """
    Decodes and incodes ceaser shift.
    :return: the coded message.
    """
    output = str()

    def retvalid(n):
        if n + shift > 25:
            return n - 26
        if n + shift < 0:
            return n + 26
        return n

    for tv in text:
        if tv not in abc + ABC:
            output += tv
            continue
        if tv in abc:
            for av in abc:
                if tv == av:
                    pos = abc.index(tv)
                    try:
                        output += abc[retvalid(pos) + shift]
                    except:
                        output += abc[retvalid(retvalid(pos)) + shift]
        if tv in ABC:
            for av in ABC:
                if tv == av:
                    pos = ABC.index(tv)
                    try:
                        output += ABC[retvalid(pos) + shift]
                    except:
                        output += ABC[retvalid(retvalid(pos)) + shift]
    if mode == ret: return output
    if mode == pri:
        print(output)
        return


while True:
    a = ["" * 26]
    print("-\t" * 10)
    text = input("text:\t")
    shift = input("shift:\t")
    if shift == "options":
        for i in range(26):
            a.append(ceaser_shift(text, i, ret) + f"\t{i} or {i + 26}")
        for i in a:
            print(f"\t{i}")
        continue
    try:
        shift = int(shift)
    except:
        print("      invalid")
        continue
    print("\t" + ceaser_shift(text, shift, ret))
