import time

######## Function
def say_hello():
    print('hello world')

################ MAIN ################
while __name__ == '__main__':
    try:
        say_hello()
        time.sleep(3)
    except:
        time.sleep(3)
        say_hello()