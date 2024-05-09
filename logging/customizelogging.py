# Demonstrate how to customize logging output



# formatting token 
# %(asctime)s
# %(filename)s
# %(funcName)s
# %(levelname)s
# %(levelno)d
# %(lineno)d
# %(message)s
# %(module)s

# date token
# "%m/
# %d/
# %Y 
# %I:
# %M:
# %S 
# %p"




import logging

# TODO: add another function to log from


extData = {"user" : "user@gmail.com"}

def anotherfunc():
    logging.debug("this is debug log message : ", extra=extData)

def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    datestr = "%m/%d/%Y %I:%M:%S %p"
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=fmtstr,
                        datefmt=datestr)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherfunc()

if __name__ == "__main__":
    main()
