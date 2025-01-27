import sys
import os

# Añadir la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
from exercises.ex2 import name_surname, remove_non_participants

class TestEx2(unittest.TestCase):

    def setUp(self):
        # Datos simulados para pruebas
        self.test_data = {
            'dorsal': [1, 2, 3, 4],
            'biker': ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown'],
            'club': ['Independiente', 'Cycling Club', 'Independiente', 'Cycling Club'],
            'time': ['02:30:45', '00:00:00', '01:45:30', '03:00:15']
        }
        self.df = pd.DataFrame(self.test_data)

    def test_name_surname(self):
        # Probar la anonimización
        df_anonimized = name_surname(self.df, seed=42)

        # Verificar que los nombres hayan cambiado
        self.assertNotEqual(list(self.df['biker']), ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown'])
        
        # Verificar que los nombres sean cadenas no vacías
        for name in df_anonimized['biker']:
            self.assertIsInstance(name, str)
            self.assertGreater(len(name), 0)

    def test_remove_non_participants(self):
        # Probar la eliminación de no participantes
        df_cleaned = remove_non_participants(self.df)

        # Verificar que solo quedan filas donde 'time' no sea '00:00:00'
        self.assertNotIn('00:00:00', df_cleaned['time'].values)

        # Verificar que el número de filas sea el correcto
        self.assertEqual(len(df_cleaned), 3)

if __name__ == "__main__":
    unittest.main()