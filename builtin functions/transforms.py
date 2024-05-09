def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def filterLower(x):
    if x.isupper():
        return False
    return True

def sqaureFunc(x):
    return x**2

def gradeFunc(x):
    if x >= 90:
        return "A"
    elif x < 90 and x >= 85:
        return "B"
    elif x < 85 and x >= 80:
        return "C"
    elif x < 80 and x >= 70:
        return "D"
    return "F"

def main():

    #samples 
    nums = (1,5,7,4,4,8,23,65,4,56,2,4,5)
    chars = "anHkLKuOjYkHPUTeEWHKLjkB"
    grades = (80, 87, 81,95,93,76,56,55,89,95,61)

    #print all the ods
    odds = list(filter(filterFunc, nums))
    print(odds)

    #print all lower letter
    lowers = list(filter(filterLower, chars))
    print(lowers)

    #to square or create new values use map
    squares = list(map(sqaureFunc, nums))
    print(squares)


    # sorted and map
    sorted_items = sorted(grades)
    print(sorted_items)
    results = list(map(gradeFunc, sorted_items))
    print(results)

if __name__ == "__main__":
    main()