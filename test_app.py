import unittest
from main import criar_usuario, listar_usuarios, buscar_usuario_por_cpf, deletar_usuario, usuarios

class TestUsuarioCRUD(unittest.TestCase):

    def setUp(self):
        usuarios.clear()
        criar_usuario("João", "joao@email.com", "1234", "11111111111")

    def test_criar_usuario(self):
        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0]['nome'], "João")

    def test_listar_todos_os_usuarios(self):
        todos = listar_usuarios()
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]['cpf'], "11111111111")

    def test_buscar_usuario_por_cpf_existente(self):
        usuario = buscar_usuario_por_cpf("11111111111")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario['nome'], "João")

    def test_buscar_usuario_por_cpf_inexistente(self):
        usuario = buscar_usuario_por_cpf("00000000000")
        self.assertIsNone(usuario)

    def test_deletar_usuario_por_cpf(self):
        resultado = deletar_usuario("11111111111")
        self.assertTrue(resultado)
        self.assertEqual(len(usuarios), 0)

    def test_deletar_usuario_cpf_inexistente(self):
        resultado = deletar_usuario("00000000000")
        self.assertFalse(resultado)
        self.assertEqual(len(usuarios), 1)

if __name__ == '__main__':
    unittest.main()
