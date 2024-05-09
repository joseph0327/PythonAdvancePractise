


# C:\Users\jvill162\Documents


def main():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jue", "Ven", "Sam"]
    
    #iterate over collection
    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    
    #iterate using sentinel and function
    # with open(r"C:\Users\jvill162\Documents\testread.txt", "r") as fp:
    #     for line in iter(fp.readline, ""):
    #         print(line)

    #use regular iterators
    # for m in range(len(days)):
    #     print(m+1, days[m])

    #using enurate reduces code and provides a counter
    # for i, m in enumerate(days, start=1):
    #     print(i, m)

    # use zip to combines consequences
    for i, m in enumerate(zip(days, daysFr), start=1) :
        print(i, m[0], "=" ,  m[1], "in French")

if __name__ == "__main__":
    main()