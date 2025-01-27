"""
This module contains a function to read and analyze a CSV dataset,
as a response to exercise 1
"""

import pandas as pd


def df_info(file_path, show_msg: bool = True):
    """
    Reads a CSV file, displays dataset information,
    and returns the dataset as a DataFrame

    This function:
    1. Reads the dataset from the given file path using pandas
    2. Prints the type of the dataset
    3. Displays the first five rows of the dataset
    4. Prints the total number of records (rows) in the dataset
    5. Lists the column names of the dataset

    Parameters:
        file_path (str): The file path of the CSV file to read
        show_msg (bool): Whether or not to display the results.
                         Defaults to True
    Returns:
        pandas.DataFrame: The dataset loaded from the file
    """
    # Leemos el dataset usando pandas
    dataset = pd.read_csv(file_path, encoding='utf-8', sep=";")
    if show_msg:
        print(f"\na) El dataset importado es de tipo {type(dataset)}")

        # Por defecto, head() nos devuelve
        # los 5 primeros registros
        print("\nb) Los cinco primeros valores del dataset son: ")
        print(dataset.head())

        # La longitud del dataset nos dirá
        # la cantidad de registros (inscripciones)
        print(f"\nc) Han participado un total de {len(dataset)} ciclistas")

    # El atributo 'columns' nos devuelve
    # las columnas del dataframe,
    # que convertimos a lista para simplificar
    # el output
    cols = dataset.columns.tolist()
    if show_msg:
        print(f"\nd) El dataframe tiene las columnas: {cols}")

    return dataset
