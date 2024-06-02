from models.slr1 import *
from models.grammar import *
from utils.path_cleaner import *
from yapar.parser import *

def main():


        yalp_path = input("Enter the path to the YALP file: ")
        yalp_path = replace_slash_with_backslash(yalp_path)
        yalp_name = extract_file_name(yalp_path)
        input_str = input("Enter the string to parse: ")

        tokens, productions = parse_yalp(yalp_path)
        grammar_str = dict_to_grammar_str(productions)
        print(grammar_str)
        grammar = Grammar(grammar_str)
        slr_parser = SLRParser(grammar)
        slr_parser.generate_automaton(yalp_name)
        slr_parser.print_info()
        
        

if __name__ == "__main__":
    main()