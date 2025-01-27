import sys
import os

# Añadir la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
from exercises.ex5 import analyze_ucsc

class TestEx5(unittest.TestCase):

    def setUp(self):
        """
        Set up test DataFrame for multiple scenarios
        """
        # DataFrame con datos de prueba
        self.df = pd.DataFrame({
            'biker': [
                'Cyclist 1', 'Cyclist 2', 'Cyclist 3', 'Cyclist 4', 'Cyclist 5',
                'Cyclist 6', 'Cyclist 7', 'Cyclist 8'
            ],
            'club_clean': [
                'UCSC', 'UCSC', 'OTHER', 'UCSC', 'OTHER',
                'OTHER', 'UCSC', 'OTHER'
            ],
            'time': [
                '01:10:30', '01:12:45', '01:15:00', '01:08:20', '01:20:10',
                '01:25:30', '01:05:40', '01:18:25'
            ]
        })

    def test_no_ucsc_cyclists(self):
        """
        Tests the case when there are no UCSC cyclists
        """
        # Prueba el caso en que no hay ciclistas del club UCSC
        df_no_ucsc = self.df[self.df['club_clean'] != 'UCSC']
        result = analyze_ucsc(df_no_ucsc)
        expected = {
            "cyclists": [],
            "best_time_cyclist": None,
            "best_time_position": None,
            "best_time_percentage": None
        }
        self.assertEqual(result, expected)

    def test_with_ucsc_cyclists(self):
        """
        Test case with UCSC cyclists and valid data
        """
        # Prueba el caso con ciclistas del club UCSC y datos válidos
        result = analyze_ucsc(self.df)

        # Verifica que la lista de ciclistas UCSC sea correcta
        expected_cyclists = ['Cyclist 1', 'Cyclist 2', 'Cyclist 4', 'Cyclist 7']
        self.assertEqual(result['cyclists'], expected_cyclists)

        # Verifica el ciclista con mejor tiempo y su posición
        self.assertEqual(result['best_time_cyclist'], 'Cyclist 7')  # Mejor tiempo
        self.assertEqual(result['best_time_position'], 1)  # Mejor posición

        # Verifica el porcentaje del mejor ciclista respecto al total
        total_cyclists = len(self.df)
        expected_percentage = (1 / total_cyclists) * 100
        self.assertAlmostEqual(result['best_time_percentage'], expected_percentage, places=2)

    def test_missing_time_data(self):
        """
        Test case when some cyclists have missing time data
        """
        # Prueba el caso en que algunos ciclistas tienen datos de tiempo faltantes
        df_missing_time = self.df.copy()
        df_missing_time.loc[0, 'time'] = None  # El ciclista 1 no tiene tiempo
        result = analyze_ucsc(df_missing_time)

        # Verifica que el ciclista 7 siga teniendo el mejor tiempo
        self.assertEqual(result['best_time_cyclist'], 'Cyclist 7')
        self.assertEqual(result['best_time_position'], 1)

        # Verifica el porcentaje del mejor ciclista respecto al total
        total_cyclists = len(df_missing_time)
        expected_percentage = (1 / total_cyclists) * 100
        self.assertAlmostEqual(result['best_time_percentage'], expected_percentage, places=2)

if __name__ == '__main__':
    unittest.main()
