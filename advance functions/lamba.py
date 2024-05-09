
def celciousToFareheit(temp):
    return (temp*9/5) + 32 
   

def FarenheitToCelcius(temp):
    return (temp - 32 ) * 5/9

def main():
    ctemp = [10, 12, 24, 100]
    ftemp = [32, 65, 100, 212]
    #regular function to convert to temps
    cres = list(map(FarenheitToCelcius, ftemp))
    print(cres)
    fres = list(map(celciousToFareheit, ctemp))
    print(fres)

    #using the lamb
    print(list(map(lambda t:(t - 32 ) * 5/9 , ftemp)))
    print(list(map(lambda t:(t * 9/5) + 32 , ctemp)))
   


if __name__ == "__main__":
    main()