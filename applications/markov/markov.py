import random

with open("input.txt") as f:
    words = f.read()

words = words.split()
my_dict = {}

# TODO: analyze which words can follow other words
for i in range(len(words)-1):
    if words[i] not in my_dict:
        my_dict[words[i]] = []
        my_dict[words[i]].append(words[i+1])
    else:
        my_dict[words[i]].append(words[i+1])


# TODO: construct 5 random sentences
def random_generate(dictionary, n):
    random_start = []
    random_stop = []
    for word in dictionary:
        if word[0].isupper() or (word[0] == '"' and word[1].isupper()) and (word[-1] != '!' or word[-1] != '.' or word[-1] != '?'):
            random_start.append(word)
        if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
            random_stop.append(word)

    for i in range(n):
        r1 = random.randint(0, len(random_start)-1)
        start_word = random_start[r1]
        curr_word = start_word
        answer = ""

        while curr_word not in random_stop:
            answer += curr_word
            answer += " "
            next_words = dictionary[curr_word]
            r_next = random.randint(0, len(next_words)-1)
            curr_word = next_words[r_next]
        answer += curr_word
        if answer.count('"')%2 != 0:
            answer += '"'
        print(answer, end="\n")


random_generate(my_dict, 5)
