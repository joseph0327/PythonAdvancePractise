from string import Template

def main():

    #template 
    templ = Template("you're watching ${title} by ${author} ")
    s2 = templ.substitute(title="Advance python", author="Joseph Vill")
    print(s2)

    #template using dictonary
    data = {
        "title":"Advance Python",
        "author":"Joseph Vill"
    }

    s3 = templ.substitute(data)
    print(s3)


if __name__ == "__main__":
    main()