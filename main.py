def main():
    with open('books/Frankenstein.txt') as f:
        frankenstein = f.read()
        print(frankenstein)
        words = frankenstein.split()
        print(len(words))
        lowered_string = frankenstein.lower()
        from collections import Counter
        print(Counter(lowered_string))
        
        # count = {'a':,'b':,'c':,'d':,'e':,'f':,'g':,'h':,'i':,'j':,'k':,'l':,'m':,'n':,'o':,'p':,'q':,'r':,'s':,'t':,'u':,'v':,'w':,'x':,'y':,'z':}
    

main()