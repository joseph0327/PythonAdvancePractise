from string import Template

def main():

    #template 
    str1 = [1,2,3,0,4,5]
    #using any it will return true if one is true 
    print(any(str1))
    
    #using all will return true if all is true
    print(all(str1))

    #using max
    print("max: ", max(str1))

    #using min
    print("min: ", min(str1))
   
   #sum
    print("sum: ", sum(str1))


if __name__ == "__main__":
    main()