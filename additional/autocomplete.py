# @Author: Matt Small
# @Purpose: Autocomplete function.


def setup():    # initialises trie and dictionaries to store given data (frequency and definition)
    f = open('Dictionary.txt', 'r')
    f_dictionary = {}
    d_dictionary = {}
    count = 0
    for line in f:
        count += 1
        if line[0] == 'w':
            word = line[6:-1]
            f_dictionary[word] = next(f)[11:-1]
            d_dictionary[word] = next(f)[12:-1]
    _end = '_end_'
    root = dict()
    for word in d_dictionary:
        current = root
        for c in word:
            current = current.setdefault(c, {})
        current[_end] = _end
    return [root, f_dictionary, d_dictionary]


def search(dictionary, prefix):     # uses a Breadth First Search to find all child nodes
    options = []
    d = [[dictionary, prefix]]
    while len(d) > 0:
        try:
            for n in range(len(d)):
                current = d.pop(n)
                if '_end_' in current[0]:
                    options.append(current[1])
                for key, value in current[0].items():
                    if value != '_end_':
                        d.append([value, current[1] + key])
        except IndexError:
            pass
    return options


def find_words(trie, prefix):   # finds the node corresponding to the prefix if it exists
    current = trie
    for c in prefix:
        if c in current:
            current = current[c]
        else:
            return False
    options = search(current, prefix)
    return options


def main():
    tmp = setup()
    trie = tmp[0]
    frequencies = tmp[1]
    definitions = tmp[2]
    while True:
        prefix = input("Please enter a prefix: ")
        if prefix == '***':
            break
        words = find_words(trie, prefix)
        if words is False:
            print('There is no word in the dictionary that has ', prefix,  ' as a prefix.')
        else:
            max = [None, 0]
            for word in range(len(words)):      # find option with best frequency
                f = int(frequencies[words[word]])
                if f == max[1]:
                    if len(words[word]) < len(max[0]):  # ensures shortest word given if frequencies are equal
                        max = [words[word], f]
                elif f > max[1]:
                    max = [words[word], f]
            print('Auto-complete suggestion: ', max[0])
            print('Definition: ', definitions[max[0]])
            print('There are ', str(len(words)), ' words in the dictionary that have ', prefix, 'as a prefix')

main()


