from collections import defaultdict

def main():
    #collections
    fruits  = ["apple", "pear", "orange", "banana",
            "apple", "grape", "orange", "banana", "banana"]

    #empty dict
    # fruitCounter = {}
    # fruitCounter = defaultdict(int) #int is default object.
    #you can use a lamda to start your dict to specific value
    fruitCounter = defaultdict(lambda: 100)

    #count the element on the list
    # for fruit in fruits:
    #     if fruit in fruitCounter.keys():
    #         fruitCounter[fruit] +=1
    #     else:
    #         fruitCounter[fruit] = 1

    # for k,v in fruitCounter.items():
    #     print("fruit ", k, " - value: ", v)

    #using the default dict
    for fruit in fruits:
        fruitCounter[fruit] +=1

    for k,v in fruitCounter.items():
        print("fruit ", k, " - value: ", v)

if __name__ == "__main__":
    main()