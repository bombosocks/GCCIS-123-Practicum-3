"""
Practicum 3 practice units 8, 9, 10
"""

import random

def make_tuple(a, b, c):
    tup = (a, b, c)
    return tup

def reverse_tuple(sequence):
    new_list = sequence[::-1]
    new_tup = tuple(new_list)
    return new_tup

def make_list(a, b, c):
    return [a, b, c]
    
def nth_list(sequence, n):
    list = []
    for i in sequence:
        if i % n == 0:
            list.append(i)
    return list

def splice(a_list, b_list):
    a_list = a_list + b_list
    return a_list

def odds_before_evens(a_list):
    odds = []
    evens = []
    for i in a_list:
        if i % 2 == 1:
            odds.append(i)

    for i in a_list:
        if i % 2 == 0:
            evens.append(i)

    new_list = odds + evens
    return new_list

def bisect(a_list):
    length =  len(a_list)
    mid = length // 2
    front_list = a_list[0:mid]
    back_list = a_list[mid:length]
    return front_list, back_list

def equivalent(seq_a, seq_b):
    try:
        if len(seq_a) == len(seq_b):
            count = 0
            while count < len(seq_a):
                if seq_a[count] == seq_b[count]:
                    count += 1
                else:
                    return False
            return True
        else:
            return False
    except:
        return False

class Domino:
    __slots__ = ["a", "b"]

    def __init__(self, a, b):
        self.a = a
        self.b = b

def domino_to_string(domino):
    dommy = "[" + str(domino.a) + "|" + str(domino.b) + "]"
    return dommy

def is_match(dom_1, dom_2):
    if dom_1.a == dom_2.a or dom_1.a == dom_2.b:
        return True
    elif dom_1.b == dom_2.a or dom_1.b == dom_2.b:
        return True
    else:
        return False

def list_range(m, n):
    c = [x for x in range(m, n, 1)]
    return c

def multiples(sequence, n):
    list = [x for x in sequence if x % n == 0]
    return list

def only_vowels(a_string):
    vowels = ["a", "e", "i", "o", "u"]
    list = [x for x in a_string if x in vowels]
    return list

def random_count(n):
    sety = set()
    count = 0
    while True:
        c = random.randint(0, n)
        sety.add(c)
        count += 1
        if len(sety) == n + 1:
            break
    return count

def main():
    print(reverse_tuple([1, 3, 4, 5, 6, 7]))
    print(reverse_tuple((1, 5, 6, 6, 7)))

    the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nth_list(the_list, 2))

    a_list = [1, 2]
    b_list = ["a", "b"]
    splice(a_list, b_list)
    print(a_list)

    print(odds_before_evens(the_list))
    print(bisect(the_list))

    seq_a = "abcdefg"
    seq_b = "abcdefg"
    print(equivalent(seq_a, seq_b))

    seq_a = "abcdefg"
    seq_b = "abcdeff"
    print(equivalent(seq_a, seq_b))

    seq_a = 1
    seq_b = "abcdeff"
    print(equivalent(seq_a, seq_b))

    a = Domino(4, 5)
    print(domino_to_string(a))

    b = Domino(5, 3)
    c = Domino(1, 2)

    print(is_match(a, b))
    print(is_match(a, c))

    print(list_range(0, 10))

    print(multiples((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2))

    print(only_vowels("The apple man is sad."))

    random.seed(1)
    print(random_count(10000))

    
if __name__ == "__main__":
    main()