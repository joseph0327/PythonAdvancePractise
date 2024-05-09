import itertools



def testFunc(x):
    return x < 40

def main():

    #cycle over a collection
    seq1 = ["Joe", "Jonh", "Mike"]
    cycle1 = itertools.cycle(seq1)

    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    
    #creating a simple counter
    # count1 = itertools.count(100,10)
    # print(next(count1)) 
    # print(next(count1)) 
    # print(next(count1)) 

    #accumumulate or counter with stem
    vals= [10, 20, 30, 40, 50, 60, 10, 20, 1]
    # acc = itertools.accumulate(vals, max)
    # print(list(acc))

    #chain command in itertools
    items = itertools.chain('ABCD', vals)
    print(list(items))

    #dropwhile and take while 
    print(list(itertools.dropwhile(testFunc, vals))) #it ill print above 40
    print(list(itertools.takewhile(testFunc, vals))) #it will print below 40 or eqaul to 40
if __name__ == "__main__":
    main()