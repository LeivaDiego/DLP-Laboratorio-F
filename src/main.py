from models.slr1 import *
from models.grammar import *
from yapar_processing.parser_yapar import *
from yalex_processing.parser_yalex import *
from scanners.scan.lexicalAnalizer import run as run_scanner

def main():
	try:
		# Procesamiento yalex
		input_path = "C:/Users/diego/Documents/UVG/7mo Semestre/Diseño de Lenguajes de Programacion/Laboratorio-F/src/files/input_texts/text.txt"
		tokens = run_scanner(input_path)
        
		# # Procesamiento yapar
		yalp_path = "C:/Users/diego/Documents/UVG/7mo Semestre/Diseño de Lenguajes de Programacion/Laboratorio-F/src/files/yapar_files/slr-1.yalp"
		yapar_tokens, productions, ignored = parse_yalp(yalp_path)
		clean_tokens = []
		for token in tokens:
			if token not in ignored:
				clean_tokens.append(token)
		input_text = " ".join(clean_tokens)

		# Crear la gramática y el parser SLR1
		grammar_str = dict_to_grammar_str(productions)
		grammar = Grammar(grammar_str)
		slr_parser = SLRParser(grammar)

		# # Ejecutar el parser SLR1
		slr_parser.print_info()
		results = slr_parser.LR_parser(input_text)
		slr_parser.print_LR_parser(results)

	except Exception as e:
			print(f"ERROR: {e}")
        
        

if __name__ == "__main__":
    main()