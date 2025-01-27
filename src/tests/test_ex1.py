import sys
import os
import unittest
import pandas as pd
from io import StringIO

# Añadir la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercises.ex1 import df_info

class TestEx1(unittest.TestCase):

    def setUp(self):
        # Datos simulados para pruebas
        self.test_csv = """dorsal;biker;club;time
1;John Doe;Independiente;02:30:45
2;Jane Smith;Cycling Club;03:00:15
3;Emily Johnson;Independiente;01:45:30
"""
        self.file_path = "test_dataset.csv"

        # Crear archivo CSV simulado
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(self.test_csv)

    def tearDown(self):
        # Eliminar archivo temporal después de las pruebas
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_df_info_structure(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        # Ejecutar la función
        df = df_info(self.file_path)

        # Restaurar la salida estándar
        sys.stdout = sys.__stdout__

        # Verificar el tipo del DataFrame
        self.assertIsInstance(df, pd.DataFrame)

        # Verificar las columnas del DataFrame
        expected_columns = ["dorsal", "biker", "club", "time"]
        self.assertListEqual(df.columns.tolist(), expected_columns)

        # Verificar la longitud del DataFrame
        self.assertEqual(len(df), 3)

    def test_df_info_output(self):
        # Redirigir la salida estándar
        captured_output = StringIO()
        sys.stdout = captured_output

        # Ejecutar la función
        df_info(self.file_path)

        # Restaurar la salida estándar
        sys.stdout = sys.__stdout__

        # Verificar que el contenido esperado está en la salida
        output = captured_output.getvalue()
        self.assertIn("El dataset importado es de tipo <class 'pandas.core.frame.DataFrame'>", output)
        self.assertIn("Los cinco primeros valores del dataset son:", output)
        self.assertIn("Han participado un total de 3 ciclistas", output)
        self.assertIn("El dataframe tiene las columnas: ['dorsal', 'biker', 'club', 'time']", output)

if __name__ == "__main__":
    unittest.main()
