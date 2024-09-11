import unittest
from _03 import adicionar_livro, listar_livros

class TestBiblioteca(unittest.TestCase):
    
    def setUp(self):
        """Executado antes de cada teste"""
        # Reinicia a lista de livros para garantir testes independentes
        global livros
        livros = ["Duna", "Neuromancer", "Fundação", "Hyperion"]

    def test_adicionar_livro(self):
        """Testa a função adicionar_livro"""
        adicionar_livro("Neuromancer")  # Já existe
        self.assertIn("Neuromancer", livros)
        adicionar_livro("Neuromancer")  # Deve ignorar duplicados
        self.assertEqual(livros.count("Neuromancer"), 1)
        adicionar_livro("O Jogo do Exterminador")
        self.assertIn("O Jogo do Exterminador", livros)
    
    def test_listar_livros(self):
        """Testa a função listar_livros"""
        livros_listados = listar_livros()
        self.assertEqual(livros_listados, ["Duna", "Neuromancer", "Fundação", "Hyperion"])

if __name__ == "__main__":
    unittest.main()
