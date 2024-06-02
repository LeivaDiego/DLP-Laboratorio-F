from models.slr1 import *
from models.grammar import *
from utils.path_cleaner import *
from yapar_processing.parser_yapar import *

def main():
	try:
		yalex_path = input("Enter the path to the YALEX file: ")
		yalex_path = replace_slash_with_backslash(yalex_path)
		# yalp_path = input("Enter the path to the YAPAR file: ")
		# yalp_path = replace_slash_with_backslash(yalp_path)
		# input_text = input("Enter the text to parse: ")
		# print()
		# _, productions = parse_yalp(yalp_path)
		# grammar_str = dict_to_grammar_str(productions)
		# grammar = Grammar(grammar_str)
		# slr_parser = SLRParser(grammar)
		# slr_parser.print_info()
		# results = slr_parser.LR_parser(input_text)
		# slr_parser.print_LR_parser(results)

	except Exception as e:
			print(f"ERROR: {e}")
        
        

if __name__ == "__main__":
    main()