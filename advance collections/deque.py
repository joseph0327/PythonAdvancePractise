# deque objects are like double-ended queues

import collections
import string


def main():
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    u = collections.deque(string.ascii_uppercase)


    # deques support the len() function
    print("Item count: " + str(len(d)))

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")

    # # manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)
    print("======================")
    # # rotate the deque
    print(d)
    d.rotate(10)
    print(d)


if __name__ == "__main__":
    main()
