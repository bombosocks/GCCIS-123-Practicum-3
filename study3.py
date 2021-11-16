"""
Practicum 3 practice units 8, 9, 10
"""

def make_tuple(a, b, c):
    tup = (a, b, c)
    return tup

def reverse_tuple(sequence):
    new_list = sequence[::-1]
    new_tup = tuple(new_list)
    return new_tup

def main():
    print(reverse_tuple([1, 3, 4, 5, 6, 7]))
    print(reverse_tuple((1, 5, 6, 6, 7)))

if __name__ == "__main__":
    main()