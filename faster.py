from collections import defaultdict
from itertools import product

from dictionary import read_dictionary
from timer import timing


def all_concatenations_for_length(length, dictionary):
    words_by_length = defaultdict(list)
    targets = set()
    for word in dictionary:
        n = len(word)
        if n < length:
            words_by_length[n].append(word)
        elif n == length:
            targets.add(word)

    for prefix_length in range(1, length):
        suffix_length = length - prefix_length
        for prefix, suffix in product(words_by_length[prefix_length], words_by_length[suffix_length]):
            if (prefix + suffix) in targets:
                yield (prefix, suffix, prefix + suffix)


if __name__ == '__main__':
    d = read_dictionary()
    with timing():
        results = tuple(all_concatenations_for_length(6, d))
        print(len(results))
