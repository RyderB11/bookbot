from collections import Counter

def main():
    with open('books/Frankenstein.txt') as f:
        frankenstein = f.read()
        print(frankenstein)

        words = frankenstein.split()
        print(len(words))

        lowered_string = frankenstein.lower()
        # print(Counter(lowered_string)) this was a counter i used but counted everything to include special characters, i'd rather have just letters for now and practice 
        
        counter = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        for char in lowered_string:
            if char.isalpha():
                counter[char] += 1
        print(counter)
    

main()