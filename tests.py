import unittest

def nome_valido(nome):
    return bool(nome) and all(c.isalpha() or c.isspace() for c in nome)

class TestNomeValido(unittest.TestCase):
    def test_nome_apenas_letras(self):
        """Verifica se um nome com apenas letras é válido"""
        self.assertTrue(nome_valido("Carlos"))

    def test_nome_com_espaco(self):
        """Verifica se um nome com espaço é válido"""
        self.assertTrue(nome_valido("Carlos Silva"))

    def test_nome_letras_espacos(self):
        """Verifica se um nome com letras e espaços é válido"""
        self.assertTrue(nome_valido("Carlos Silva Junior"))

    def test_nome_com_numeros(self):
        """Verifica se um nome com números é inválido"""
        self.assertFalse(nome_valido("Carlos123"))

    def test_nome_com_caracteres_especiais(self):
        """Verifica se um nome com caracteres especiais é inválido"""
        self.assertFalse(nome_valido("Carlos@Silva"))

    def test_nome_vazio(self):
        """Verifica se um nome vazio é inválido"""
        self.assertFalse(nome_valido(""))

if __name__ == '__main__':
    unittest.main()