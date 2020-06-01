specials = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']


def replace_special(main, toBeReplaces, newString):
    for elem in toBeReplaces:
        if elem in main:
            main = main.replace(elem, newString)
    return main


def word_count(s):
    count = {}
    new_s = replace_special(s, specials, '')
    new_s = new_s.split()
    for i in range(len(new_s)):
        new_s[i] = new_s[i].lower()
        if new_s[i] in count:
            count[new_s[i]] += 1
        elif new_s[i] != '':
            count[new_s[i]] = 1
    return count


if __name__ == "__main__":
    print(word_count('a a\ra\na\ta \t\r\n'))
