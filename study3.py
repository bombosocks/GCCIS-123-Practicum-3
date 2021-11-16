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

def make_list(a, b, c):
    return [a, b, c]
    
def nth_list(sequence, n):
    list = []
    for i in sequence:
        if i % n == 0:
            list.append(i)
    return list

def main():
    print(reverse_tuple([1, 3, 4, 5, 6, 7]))
    print(reverse_tuple((1, 5, 6, 6, 7)))

    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nth_list(a_list, 2))

if __name__ == "__main__":
    main()