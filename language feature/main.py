from string import Template

def main():
    b = bytes([0x41,0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)
    #combine the 2
    print(str(b)+s)

    #decode - you have to decode the byte to convert to string
    s2 = b.decode('utf-8')
    print(s+s2)

    #encode to utf-32
    b2 = s.encode('utf-32')
    print("this is the encoded value: ", b2)


    

if __name__ == "__main__":
    main()