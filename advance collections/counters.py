from collections import Counter


def main():
    #create a collections
    class1 = ["Bob", "Becky", "CHAD", "James", "Darcy", "Frank", "Hanna","James"]

    class2 = ["Bill", "Barry", "Cindy", "Debbi", "Frank", "Gabby", "Frank"]

    #create a counter
    c1 = Counter(class1)
    c2 = Counter(class2)

    #count the name that has the same name for james
    # print(c1["James"])
    # print(sum(c1.values()) , " - number of students") #count the numbser of students

    # #combine the 2 class
    # # c1.update(c2)
    # # print("combine classes: ", sum(c1.values()))

    # #most commmon and limits to 3 names
    # print(c1.most_common(3))
    # print(c2.most_common(3))

    # #subtract
    # c1.subtract(c2)
    
    # print("subtract c1 to c2 : ", c1.most_common(3))
    # & to print the intersection of both c1 and c2
    print(c1 & c2)
if __name__ == "__main__":
    main()