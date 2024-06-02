from scanner_generator.analyzers.lexical_generator import LexicalAnalizerGenerator

yalex_path = "C:/Users/diego/Documents/UVG/7mo Semestre/Diseño de Lenguajes de Programacion/Laboratorio-F/src/files/yalex_files/conflicto.yal"

print("Generating scanner...")
LexicalAnalizerGenerator(yalex_path, "scan")