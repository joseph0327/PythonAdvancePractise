
import collections

def main():
   #create a point namedTuple
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10,20)
    p2 = Point(30, 40) 

    print(p1,p2)
    print(p1.x, p2.x)
    print(p1.y, p2.y)


    #replace function, replacing a fields with a new value
    print("========================")
    p1 = p1._replace(x=100)
    print(p1,p2)


if __name__ == "__main__":
    main()