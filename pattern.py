def pattern_by_char(ch, i):
    ch = ch.lower()
    result = ""

    match ch:
        case 'a':
            for j in range(1, 6):
                if (i == 1 and j == 3) or (i == 2 and j in [2, 4]) or i == 3 or (i in [4, 5] and j in [1, 5]):
                    result += "* "
                else:
                    result += "  "
        case 'b':
            for j in range(1, 6):
                if (i in [1, 3, 5] and j < 5) or j == 1 or (i in [2, 4] and j == 5):
                    result += "* "
                else:
                    result += "  "
        case 'c':
            for j in range(1, 6):
                if (i in [1, 5] and j > 1) or (1 < i < 5 and j == 1):
                    result += "* "
                else:
                    result += "  "
        case 'd':
            for j in range(1, 6):
                if j == 1 or (i in [1, 5] and j < 5) or (1 < i < 5 and j == 5):
                    result += "* "
                else:
                    result += "  "
        case 'e':
            for j in range(1, 6):
                if (i in [1, 5] and j > 1) or i == 3 or j == 1:
                    result += "* "
                else:
                    result += "  "
        case 'f':
            for j in range(1, 6):
                if j == 1 or i == 1 or i == 3:
                    result += "* "
                else:
                    result += "  "
        case 'g':
            for j in range(1, 6):
                if (i == 1 and j > 1) or (1 < i < 5 and j == 1) or (i == 5 and j in [2, 3, 5]) or (i == 4 and j in [4, 5]) or (i == 3 and j > 2):
                    result += "* "
                else:
                    result += "  "
        case 'h':
            for j in range(1, 6):
                if j == 1 or j == 5 or i == 3:
                    result += "* "
                else:
                    result += "  "
        case 'i':
            for j in range(1, 6):
                if i in [1, 5] or j == 3:
                    result += "* "
                else:
                    result += "  "
        case 'j':
            for j in range(1, 6):
                if i == 1 or j == 3 or (i in [3, 4, 5] and j == 1) or (i == 5 and j == 2):
                    result += "* "
                else:
                    result += "  "
        case 'k':
            for j in range(1, 6):
                if j == 1 or (i in [1, 5] and j == 5) or (i in [2, 4] and j == 4) or (i == 3 and j in [2, 3]):
                    result += "* "
                else:
                    result += "  "
        case 'l':
            for j in range(1, 6):
                if j == 1 or i == 5:
                    result += "* "
                else:
                    result += "  "
        case 'm':
            for j in range(1, 6):
                if j == 1 or j == 5 or (i == 2 and j in [2, 4]) or (i == 3 and j == 3):
                    result += "* "
                else:
                    result += "  "
        case 'n':
            for j in range(1, 6):
                if j == 1 or j == 5 or i == j:
                    result += "* "
                else:
                    result += "  "
        case 'o':
            for j in range(1, 6):
                if (i in [1, 5] and 1 < j < 5) or (j in [1, 5] and 1 < i < 5):
                    result += "* "
                else:
                    result += "  "
        case 'p':
            for j in range(1, 6):
                if j == 1 or ((i == 1 or i == 3) and j < 5) or (i == 2 and j == 5):
                    result += "* "
                else:
                    result += "  "
        case 'q':
            for j in range(1, 6):
                if (i in [1, 5] and 1 < j < 5) or (j in [1, 5] and 1 < i < 5) or (i > 2 and i == j):
                    result += "* "
                else:
                    result += "  "
        case 'r':
            for j in range(1, 6):
                if j == 1 or ((i == 1 or i == 3) and j < 5) or (i == 2 and j == 5) or (i > 3 and i == j):
                    result += "* "
                else:
                    result += "  "
        case 's':
            for j in range(1, 6):
                if (j == 1 and i in [2, 5]) or (i in [1, 3, 5] and 1 < j < 5) or ((i in [1, 4]) and j == 5):
                    result += "* "
                else:
                    result += "  "
        case 't':
            for j in range(1, 6):
                if i == 1 or j == 3:
                    result += "* "
                else:
                    result += "  "
        case 'u':
            for j in range(1, 6):
                if (j in [1, 5] and i < 5) or (i == 5 and 1 < j < 5):
                    result += "* "
                else:
                    result += "  "
        case 'v':
            for j in range(1, 6):
                if (j in [1, 5] and i < 4) or (i == 4 and j in [2, 4]) or (i == 5 and j == 3):
                    result += "* "
                else:
                    result += "  "
        case 'w':
            for j in range(1, 6):
                if j in [1, 5] or (i == 4 and j in [2, 4]) or (i == 3 and j == 3):
                    result += "* "
                else:
                    result += "  "
        case 'x':
            for j in range(1, 6):
                if i == j or j == 6 - i:
                    result += "* "
                else:
                    result += "  "
        case 'y':
            for j in range(1, 6):
                if (i == j and i < 4) or j == 6 - i:
                    result += "* "
                else:
                    result += "  "
        case 'z':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 6 - i:
                    result += "* "
                else:
                    result += "  "
        case _:
            result += "      "
    return result


def main():
    name = ''.join(filter(str.isalpha, input("Please Enter Your Name: ")))  
    for i in range(1, 6):  
        for ch in name:
            print(pattern_by_char(ch, i), end=" ")
        print()  


if __name__ == "__main__":
    main()
