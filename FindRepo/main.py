from argpars.parser import parser
from reader.reader import read_file
from search.search import find
from split.split import Split

def main():
    args = parser.parse_args()
    
    # if args.file is None:

    text, ftype = read_file(args.file)

    # if ftype in []

    split_class = Split()

    splited_text = split_class.split_code(text)

    for t in splited_text:
        print(find(t))
    

if __name__ == "__main__":
    main()
