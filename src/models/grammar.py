class Grammar:
    def __init__(self, grammar_str):
        self.grammar_str = '\n'.join(filter(None, grammar_str.splitlines()))
        self.grammar = {}
        self.start = None
        self.terminals = set()
        self.nonterminals = set()

        for production in list(filter(None, grammar_str.splitlines())):
            head, _, bodies = production.partition(' -> ')

            if head.isupper():
                raise ValueError(
                    f'\'{head} -> {bodies}\': Head \'{head}\' is capitalized to be treated as a nonterminal.')

            if not self.start:
                self.start = head

            self.grammar.setdefault(head, set())
            self.nonterminals.add(head)
            bodies = {tuple(body.split()) for body in ' '.join(bodies.split()).split('|')}

            for body in bodies:
                if '^' in body and body != ('^',):
                    raise ValueError(f'\'{head} -> {" ".join(body)}\': Null symbol \'^\' is not allowed here.')

                self.grammar[head].add(body)

                for symbol in body:
                    if symbol.islower() and symbol != '^':
                        self.nonterminals.add(symbol)
                    else:
                        self.terminals.add(symbol)

        self.symbols = self.terminals | self.nonterminals


def dict_to_grammar_str(productions):
    grammar_lines = []
    for nonterminal, expression in productions.items():
        # Convert each production line to the expected format "nonterminal -> production1 | production2"
        formatted_production = f"{nonterminal} -> {expression}"
        grammar_lines.append(formatted_production)
    return "\n".join(grammar_lines)
