import random
import time


def main():
    input('Let\'s see... you should draw...')
    time.sleep(1)
    getString()
    fixFormat()
    print(''.join(str(x) for x in final))
      

##Obtains string from document##
def getString():
    doc = "./noun.txt"
    global noun
    noun = random.choice(list(open(doc)))
    global mod
    doc = "./mod.txt"
    mod = random.choice(list(open(doc)))

##Put strings on same line##
def fixFormat():
    global final
    final = [noun.replace("\n", " "), mod.replace("\n", " ")]

if __name__ == '__main__':
    main()