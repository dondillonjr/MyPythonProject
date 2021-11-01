import time

####### Function ######
def say_hello():
    print('hello don')

##### MAIN ######
while __name__ == '__main__':
    try:
        say_hello()
        time.sleep(4)
    except:
        time.sleep(2)
        print('hit exception')
        SystemExit