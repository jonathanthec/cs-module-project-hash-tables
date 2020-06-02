import collections


def process_input(file):
    with open(file) as f:
        words = f.read()
    return words


def frequency_analysis(words):
    etaoins = 'etaoinshrdlcumwfgypbvkjxqz'.upper()
    frequency = {}

    for letter in words:
        if letter.isalpha():
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    output = []
    for item in sorted_frequency:
        item = list(item)
        output.append(item)

    for i in range(len(output)):
        output[i][1] = etaoins[i]

    return output


def translate(filename):
    answer = ""
    words = process_input(filename)
    translation = frequency_analysis(words)
    caesar_dictionary = {word[0]: word[1:] for word in translation}

    for letter in words:
        if letter not in caesar_dictionary:
            answer += letter
        else:
            answer += caesar_dictionary[letter][0]
    return answer


if __name__ == '__main__':
    print(translate('ciphertext.txt'))
