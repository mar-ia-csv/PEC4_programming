"""
This module provides utility functions for processing dataframes related to bikers' data.
It includes functionalities for anonymizing names and filtering non-participants.
Solves exercise 2.
"""

from faker import Faker


def name_surname(df, seed: int = 42):
    """
    Given a dataframe, anonimizes the bikers' names,
    found in the 'biker' column
    Parameters:
    - df: dataframe to anonimize
    Reurns:
          anonimized dataframe
    """
    fake = Faker()

    # Establecer la semilla
    # (para reproducibilidad de resultados)
    if seed is not None:
        Faker.seed(seed)

    # Verificamos que la columna existe
    if 'biker' in df.columns:
        df['biker'] = [fake.name() for element in range(len(df))]
    else:
        raise KeyError("The 'biker' column does not exist in the DataFrame.")

    return df

def remove_non_participants(df):
    """
    Given a dataframe, removes the non-participants,
    based on if their time in the 'time' column is
    00:00:00
    Parameters:
    - df: dataframe to modify
    Returns:
          updated dataframe where non-participants
          have been removed
    """

    # Nos quedamos solo con las filas
    # cuyo valor para 'time'
    # NO sea 00:00:00
    df = df[df['time'] != '00:00:00']

    return df
