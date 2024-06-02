def parse_yalex_tokens(file_path):
    try:
        # Leer todo el contenido del archivo en una cadena
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")

    # Eliminar comentarios delimitados por (* y *)
    while '(*' in content and '*)' in content:
        start_comment = content.index('(*')
        end_comment = content.index('*)', start_comment) + 2
        content = content[:start_comment] + content[end_comment:]

    # Encontrar la sección que empieza con "rule"
    rule_keyword = "rule"
    rule_start = content.find(rule_keyword)
    if rule_start == -1:
        raise ValueError(f"No se encontró la palabra clave 'rule' en el archivo: {file_path}")

    # Extraer la sección desde "rule" hasta el final
    rule_content = content[rule_start:]

    # Definir variables para encontrar tokens
    tokens = set()
    current_index = 0

    # Buscar cada "return" y extraer el token
    while "return" in rule_content[current_index:]:
        return_index = rule_content.index("return", current_index)
        # Encontrar el inicio del token (la primera letra mayúscula después de "return")
        token_start = return_index + len("return")
        while token_start < len(rule_content) and not (rule_content[token_start].isupper() or rule_content[token_start] == '_'):
            token_start += 1
        # Encontrar el final del token
        token_end = token_start
        while token_end < len(rule_content) and (rule_content[token_end].isupper() or rule_content[token_end] == '_' or rule_content[token_end].isdigit()):
            token_end += 1
        # Extraer el token y crear la tupla
        token = rule_content[token_start:token_end].strip()
        if token:  # Validar que el token no esté vacío
            tokens.add((f"return {token}", token))
        # Mover el índice actual más allá del token encontrado
        current_index = token_end

    if not tokens:
        raise ValueError(f"No se encontraron tokens en el archivo: {file_path}")

    return tokens