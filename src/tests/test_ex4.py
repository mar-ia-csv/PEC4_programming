import sys
import os

# Añadir la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
from exercises.ex4 import clean_club, create_full_club_participants_df


class TestEx4(unittest.TestCase):

    def test_clean_club(self):
        """
        Tests the function clean_club
        """

        # Caso 1: Entrada None
        self.assertEqual(clean_club(None), "INDEPENDIENTE", 
                         "Si el club es None, debería devolver 'INDEPENDIENTE'")

        # Caso 2: Cadena vacía
        self.assertEqual(clean_club(""), "INDEPENDIENTE", 
                         "Si el club es cadena vacía, debería devolver 'INDEPENDIENTE'")

        # Caso 3: Cadena con espacios vacíos
        self.assertEqual(clean_club("    "), "INDEPENDIENTE", 
                         "Si el club son solo espacios, debería devolver 'INDEPENDIENTE'")

        # Caso 4: Ejemplo simple
        self.assertEqual(clean_club("C.C. Huesca"), "HUESCA", 
                         "C.C. Huesca debería limpiarse como 'HUESCA'")

        # Caso 5: Varias palabras, incluyendo 'Club Ciclista'
        self.assertEqual(clean_club("Club Ciclista Oscense"), "OSCENSE", 
                         "Club Ciclista Oscense debería limpiarse como 'OSCENSE'")

        # Caso 6: Nombre sin prefijos
        self.assertEqual(clean_club("Oscense"), "OSCENSE", 
                         "Oscense debería simplemente convertirse a mayúsculas")

        # Caso 7: Expresiones al final (como TT)
        self.assertEqual(clean_club("AC HUESCA  TT"), "HUESCA", 
                         "AC HUESCA  TT debería limpiarse como 'HUESCA'")

        # Caso 8: Sustitución de 'PEÑA CICLISTA '
        self.assertEqual(clean_club("PEÑA CICLISTA SARIÑENA"), "SARIÑENA", 
                         "PEÑA CICLISTA SARIÑENA debería limpiarse como 'SARIÑENA'")

    def test_create_full_club_participants_df(self):
        """
        Tests the function create_full_club_participants_df
        """
        data = {
            'club': [
                "C.C. Huesca", 
                "PEÑA CICLISTA SARIÑENA", 
                None, 
                "C.D. Algo", 
                "Club Ciclista Oscense", 
                "Oscense", 
                "AC Huesca  TT", 
                ""
            ],
            'nombre': [
                "Ciclista1", 
                "Ciclista2", 
                "Ciclista3", 
                "Ciclista4", 
                "Ciclista5", 
                "Ciclista6", 
                "Ciclista7", 
                "Ciclista8"
            ]
        }
        df = pd.DataFrame(data)

        # Creamos la columna club_clean aplicando clean_club
        df["club_clean"] = df["club"].apply(clean_club)

        # Llamamos a la función que queremos probar
        df_result = create_full_club_participants_df(df)

        # Comprobamos si la columna participant_count está presente
        self.assertIn('participant_count', df_result.columns, 
                      "El DataFrame resultante debe contener la columna 'participant_count'.")

        # Verificamos si el recuento es correcto:
        #   - Esperamos ver que hay 2 'HUESCA' (C.C. Huesca y AC Huesca  TT)
        #   - 1 'SARIÑENA'
        #   - 1 'ALGO'
        #   - 2 'OSCENSE' (Club Ciclista Oscense, Oscense)
        #   - El resto son 'INDEPENDIENTE' (2 casos: None y cadena vacía)
        expected_counts = {
            "HUESCA": 2,
            "SARIÑENA": 1,
            "ALGO": 1,
            "OSCENSE": 2,
            "INDEPENDIENTE": 2
        }

        # Recorremos los clubs existentes y comparamos con el valor esperado
        for _, row in df_result.iterrows():
            club = row['club_clean']
            count = row['participant_count']
            # Si está en el diccionario, comprobamos
            if club in expected_counts:
                self.assertEqual(count, expected_counts[club], 
                                 f"El club '{club}' debería tener {expected_counts[club]} participantes.")
            else:
                # Si no lo esperaba, debe ser un caso sin definir
                self.fail(f"Club inesperado encontrado en el DataFrame: {club}")

        # Por último, comprobamos el orden. Debería ordenarse descendente por 'participant_count'
        # Extraemos la columna 'participant_count' y comprobamos que esté en orden decreciente
        participant_counts = df_result['participant_count'].tolist()
        self.assertEqual(participant_counts, sorted(participant_counts, reverse=True),
                         "Los valores de 'participant_count' deben estar en orden descendente.")

        
if __name__ == '__main__':
    unittest.main()
