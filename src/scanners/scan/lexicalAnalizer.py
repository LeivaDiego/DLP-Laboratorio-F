
import pickle
from scanner_generator.analyzers.lexical_generator import LexicalAutomata
from scanner_generator.classes.automata import Automata



def get_file_name():
    file_name = str(input("Enter the file name: "))
    return file_name


def get_file_content(file_name: str):
    with open(file_name, "r") as file:
        content = file.read()
    return content


def search_tokens(automata: Automata, final_node_precedence: dict, actions: dict, string: str):
    token_stream = []

    while string:
        token = find_token(automata, string)

        if token is None:
            string = string[1:]
        else:
            token_states = token[0]
            token_length = token[1]
            token_string = string[:token_length]

            token_state = min(token_states, key=lambda x: final_node_precedence[x])
            action = actions[token_state]
            token = eval(action)
            string = string[token_length:]
            token_stream.append(token)
            
    return token_stream


def find_token(automata: Automata, word: str):
    index = 0
    longest_match_states = set()
    longest_index = 0
    current = automata.get_initial()
    current = Automata.e_closure(current)

    for char in word:
        current = Automata.e_closure_set(current)
        current = Automata.move(current, char)

        # We check if the current state is empty
        if not current:
            break

        # We check if the current state is a final state
        if any(state in automata.get_final() for state in current):
            longest_match_states = current.intersection(automata.get_final())
            longest_index = index + 1

        index += 1

    if not longest_match_states:
        raise ValueError(f"No token found for the word: {word}")
        return None

    result = (longest_match_states, longest_index)
    return result


def unpickle():
    with open("C:/Users/diego/Documents/UVG/7mo Semestre/Diseño de Lenguajes de Programacion/Laboratorio-F/src/scanners/scan/lexicalAnalizer.pkl", "rb") as file:
        automata = pickle.load(file)
    return automata            

def run(file_path: str):
    lexical_automata: LexicalAutomata = unpickle()
    automata: Automata = lexical_automata.automata
    actions = lexical_automata.actions
    final_node_precedence = lexical_automata.final_node_precedence
    
    content = get_file_content(file_path)

    return search_tokens(automata, final_node_precedence, actions, content)
    
