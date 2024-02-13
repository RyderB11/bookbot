def main():
    with open('books/Frankenstein.txt') as f:
        frakenstein = f.read()
        print(frakenstein)
        words = frakenstein.split()
        print(len(words))

main()