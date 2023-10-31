import unittest
from io import StringIO
from mainClick import create_contact, search_contact

class TestContactManagement(unittest.TestCase):
    def setUp(self):
        # Configura una salida estándar temporal para capturar la salida de la función
        self.output_buffer = StringIO()
        self.original_output = click.get_text_stream()
        click.set_text_stream('stdout', self.output_buffer)

    def tearDown(self):
        # Restablece la salida estándar original
        click.set_text_stream('stdout', self.original_output)
        self.output_buffer.close()

    def test_create_contact(self):
        # Simula la entrada del usuario
        user_input = ['John', 'Doe', 'john@example.com', '123-456-7890\n']
        input_function = lambda _: user_input.pop(0)

        # Ejecuta la función create_contact
        with unittest.mock.patch('builtins.input', input_function):
            create_contact()

        # Captura la salida y verifica si se creó el contacto
        output = self.output_buffer.getvalue()
        self.assertIn("Contacto creado con éxito.", output)

    def test_search_contact(self):
        # Simula la entrada del usuario
        user_input = ['John\n']
        input_function = lambda _: user_input.pop(0)

        # Ejecuta la función search_contact
        with unittest.mock.patch('builtins.input', input_function):
            search_contact("John")

        # Captura la salida y verifica si se encuentra el contacto
        output = self.output_buffer.getvalue()
        self.assertIn("Resultados de búsqueda:", output)
        self.assertIn("John", output)

if __name__ == '__main__':
    unittest.main()
