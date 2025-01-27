import sys
import os

# Añadir la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
from exercises.ex3 import minutes_002040, add_time_grouped_column, group_by_time_grouped, plot_histogram


class TestEx3(unittest.TestCase):

    def setUp(self):
        # Datos inventados para las pruebas
        self.test_data = {
            'dorsal': [1, 2, 3, 4],
            'biker': ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown'],
            'club': ['Independiente', 'Cycling Club', 'Independiente', 'Cycling Club'],
            'time': ['02:15:45', '02:25:30', '02:45:00', '02:55:15']
        }
        self.df = pd.DataFrame(self.test_data)

    def test_minutes_002040(self):
        # Pruebas para la función minutes_002040
        self.assertEqual(minutes_002040('02:15:48'), '02:00')
        self.assertEqual(minutes_002040('02:25:30'), '02:20')
        self.assertEqual(minutes_002040('02:45:00'), '02:40')
        self.assertEqual(minutes_002040('02:55:15'), '02:40')

    def test_add_time_grouped_column(self):
        # Probamos la función add_time_grouped_column
        updated_df = add_time_grouped_column(self.df, 'time')
        self.assertIn('time_grouped', updated_df.columns)
        expected_values = ['02:00', '02:20', '02:40', '02:40']
        self.assertListEqual(updated_df['time_grouped'].tolist(), expected_values)

    def test_group_by_time_grouped(self):
        # Probamos la función group_by_time_grouped
        updated_df = add_time_grouped_column(self.df, 'time')
        grouped_df = group_by_time_grouped(updated_df)

        # Creamos el DataFrame esperado con el nombre correcto de la columna
        expected_data = {
            'time_grouped': ['02:00', '02:20', '02:40'],
            'cyclist_count': [1, 1, 2]
        }
        expected_df = pd.DataFrame(expected_data)

        # Verificamops que los DataFrames sean iguales
        pd.testing.assert_frame_equal(grouped_df, expected_df)

    def test_plot_histogram(self):
        # Probamos la función plot_histogram
        updated_df = add_time_grouped_column(self.df, 'time')
        grouped_df = group_by_time_grouped(updated_df)

        output_path = 'test_histogram.png'
        plot_histogram(grouped_df, output_path)

        # Comprobamos que el archivo se ha creado
        self.assertTrue(os.path.exists(output_path))

        # Eliminar el archivo tras el test
        if os.path.exists(output_path):
            os.remove(output_path)

if __name__ == "__main__":
    unittest.main()
