
#keyword only arguments.

def myFunc(arg1, arg2, * , key=False): # * asterisk is the special keywork on argument list
    pass

def main():
    myFunc(1,2,key=True)


if __name__ == "__main__":
    main()