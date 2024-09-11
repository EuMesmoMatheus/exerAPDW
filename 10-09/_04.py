livros = []

# Adiciona livros iniciais
livros_iniciais = ["Duna", "Neuromancer", "Fundação", "Hyperion"]
livros.extend(livros_iniciais)

def adicionar_livro(titulo):
    global livros
    if titulo not in livros:
        livros.append(titulo)

def listar_livros():
    return livros
te