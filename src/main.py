"""
This script is designed to process and analyze cyclist data from a CSV dataset
It provides step-by-step solutions to exercises, including data loading, 
anonymization, grouping, and club-specific analysis

The script is divided into five exercises, each with a corresponding function:
1. answer_ex_1: Loads the dataset and displays basic information
2. answer_ex_2: Anonymizes cyclist names, removes non-participants, and extracts specific data
3. answer_ex_3: Groups cyclist times into intervals, creates a histogram, and updates the dataset
4. answer_ex_4: Cleans club names, groups data by clubs, and counts participants per club
5. answer_ex_5: Analyzes cyclists from the UCSC club, identifying the best cyclist and their ranking

Command-line options:
- Run the script without arguments to execute all exercises sequentially
- Use the `--help` argument to display usage instructions
- Pass a number (1-5) as an argument to execute a specific exercise

Usage:
    python main.py [option]

Options:
    1: Displays exercise 1.
    2: Displays exercise 2.
    3: Displays exercise 3.
    4: Displays exercise 4.
    5: Displays exercise 5.
    --help: Displays this usage message.
"""


import sys
from exercises import ex1, ex2, ex3, ex4, ex5


# Ruta relativa al archivo
FILE_PATH = 'data/dataset.csv'


# Ejercicio 1
def answer_ex_1(show_msg: bool = True, file_path: str = FILE_PATH):
    """
    Loads the dataset and displays basic information

    This function:
    1. Loads the dataset from the specified file path
    2. Prints details about the dataset, including:
        - Its type
        - The first 5 rows
        - The total number of participants
        - The list of column names
    Parameters:
        file_path (str): The path to the dataset file. 
        Default set to the global variable FILE_PATH
        show_msg (bool): Whether or not to display the results.
                         Defaults to True
    Returns:
        pd.DataFrame: The original dataset loaded from the file

    Prints:
        - Dataset type
        - The first 5 records
        - The total number of participants
        - Column names of the dataset
    """

    if show_msg:
        print("\nEjercicio 1:")
    original_dataframe = ex1.df_info(file_path, show_msg)

    return original_dataframe

# Ejercicio 2
def answer_ex_2(show_msg: bool = True, show_prev_msg: bool = False):
    """
    Processes the dataset to anonymize cyclist names, remove non-participants, 
    and extract specific information

    This function:
    1. Retrieves the original dataset from the previous exercise (1)
    2. Anonymizes the 'biker' column in the dataset
    3. Removes participants with a time of '00:00:00'
    4. Extracts information about the cyclist with dorsal number 1000

    Paramaters:
    show_msg (bool): Whether or not to display the results.
                     Defaults to True
    show_prev_msg (bool): Whether or not to display the results from the previous exercise.
                          Defaults to False

    Returns:
        pd.DataFrame: The updated dataset after anonymization and cleaning
    
    Prints:
        - The first 5 anonymized records
        - The number of remaining participants after cleaning
        - The first 5 records of the cleaned dataset
        - Details of the cyclist with dorsal number 1000
    """

    # Extraer el dataframe utilizando
    # la respuesta del ejercico 1
    original_dataframe = answer_ex_1(show_msg=show_prev_msg)
    if show_msg:
        print("\nEjercicio 2:")

    anonimized_df = ex2.name_surname(original_dataframe)
    if show_msg:
        print("\n\tSe ha anonimizado el dataset.")
        print("\n\ta) Los 5 primeros valores con anonimización son:")
        print("\n", anonimized_df.head())

    updated_df = ex2.remove_non_participants(anonimized_df)
    if show_msg:
        print("\n\tSe han eliminado los ciclistas con tiempo 00:00:00.")
        print(f"\n\tb) Ahora, el dataset cuenta con {len(updated_df)} ciclistas")
        print("\n\tc) Los 5 primeros son:")
        print("\n", updated_df.head())

    dorsal_1000 = updated_df[updated_df['dorsal'] == 1000]
    if show_msg:
        print("\n\td) Los datos del ciclista con dorsal número 1000 son:")
        print("\n", dorsal_1000)

    return updated_df

# Ejercicio 3
def answer_ex_3(show_msg: bool = True, show_prev_msg: bool = False):
    """
    Groups cyclist times into intervals, creates a histogram, and updates the dataset

    This function:
    1. Retrieves the cleaned dataset from the previous exercise (2)
    2. Adds a new column, 'time_grouped', to group cyclist times into intervals
       (00, 20, 40 minutes)
    3. Creates a grouped DataFrame that counts the number of cyclists in each time interval
    4. Generates and saves a histogram of the grouped time intervals

    Paramaters:
        show_msg (bool): Whether or not to display the results.
                         Defaults to True
        show_prev_msg (bool): Whether or not to display the results from the previous exercise.
                              Defaults to False.
    Returns:
        pd.DataFrame: The updated dataset with the new 'time_grouped' column
    
    Prints:
        - The first 15 rows of the updated dataset with the 'time_grouped' column
        - The grouped DataFrame with cyclist counts per time interval
        - A message confirming the creation of the histogram
    
    Saves:
        - A histogram image in 'img/histograma.png'
    """

    updated_df = answer_ex_2(show_msg=show_prev_msg)
    if show_msg:
        print("\nEjercicio 3:")
    updated_df = ex3.add_time_grouped_column(updated_df, 'time')

    if show_msg:
        print("Se ha creado la nueva columna 'time_grouped' en el dataframe.")
        print("Los 15 primeros valores son:")
        print("\n", updated_df.head(15))

    grouped_df = ex3.group_by_time_grouped(updated_df)

    if show_msg:
        print("Se ha creado el dataframe agrupado. Sus valores son:")
        print("\n", grouped_df)

    if show_msg:
        print("Se crea el histograma sobre la información anterior.")
        ex3.plot_histogram(grouped_df)
        print("El histograma se ha guardado en 'img/histograma.png'")

    return updated_df

# Ejercicio 4
def answer_ex_4(show_msg: bool = True, show_prev_msg: bool = False):
    """
    Cleans club names, adds a new column, and creates a grouped DataFrame by clubs

    This function:
    1. Retrieves the updated dataset from the previous exercise (3)
    2. Cleans the 'club' column
    3. Adds a new column, 'club_clean', containing the cleaned club names
    4. Creates a new DataFrame grouped by 'club_clean' and counts the number
       of participants in each club
    
    Paramaters:
    show_msg (bool): Whether or not to display the results.
                     Defaults to True
    show_prev_msg (bool): Whether or not to display the results from the previous exercise.
                          Defaults to False
                     
    Returns:
        pd.DataFrame: A grouped DataFrame with the following columns:
                      - 'club_clean': Cleaned club names
                      - 'participant_count': Number of participants per club
    
    Prints:
        - The first 15 rows of the updated dataset with the 'club_clean' column
        - The first 10 rows of the grouped DataFrame showing participant counts per club
    """

    updated_df = answer_ex_3(show_msg=show_prev_msg)

    if show_msg:
        print("\nEjercicio 4:")
        print("\nSe crea la nueva columna 'club_clean'")

    updated_df['club_clean'] = updated_df['club'].apply(ex4.clean_club)

    if show_msg:
        print("\nLos primeros 15 valores del dataframe ahora son:")
        print(updated_df.head(15))

    if show_msg:
        print("\nSe crea el nuevo dataframe con los clubes y participantes de cada club")
    club_participants_df = ex4.create_full_club_participants_df(updated_df)

    if show_msg:
        print("\nLos 10 primeros valores son:")
        print(club_participants_df.head(10))

    return club_participants_df

# Ejericio 5
def answer_ex_5(show_prev_msg: bool = False):
    """
    Analyzes UCSC club cyclists and extracts infromation

    This function:
    1. Retrieves the grouped DataFrame from the previous exercise (4)
    2. Analyzes the cyclists from the UCSC (Unió Ciclista Sant Cugat) club, providing:
        - A list of UCSC cyclists
        - The cyclist with the best time
        - The position of this cyclist in the overall ranking
        - The percentage position of this cyclist in the total ranking
    Parameters:
    show_prev_msg (bool): Whether or not to display the results from the previous exercise.
                          Defaults to False.
    Prints:
        - The list of UCSC cyclists
        - The name of the UCSC cyclist with the best time
        - The position and percentage of the best UCSC cyclist in the total ranking
    """
    club_participants_df = answer_ex_4(show_msg=show_prev_msg)

    print("\nEjercicio 5:")

    result = ex5.analyze_ucsc(club_participants_df)
    print("\nLos ciclistas de la UCSC son:")
    print(result['cyclists'])

    print("\nEl ciclista de la UCSC que ha hecho el mejor tiempo es:")
    print(result['best_time_cyclist'])

    print(
        f"\nEl ciclista {result['best_time_cyclist']} ha quedado en la posición "
        f"{result['best_time_position']}/{len(club_participants_df)}, "
        f"y su porcentaje sobre el total es {result['best_time_percentage']:.2f}%"
    )


if __name__ == "__main__":
    # Mostrar ayuda si se pasa '--help'
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("""
        Uso: python main.py [opcion]

        Opciones:
        1: Responder el ejercicio 1
        2: Responder el ejercicio 2
        3: Responder el ejercicio 3
        4: Responder el ejercicio 4
        5: Responder el ejercicio 5
        Sin parámetros: Se responde toda la PEC
        """)
        sys.exit(0)

    # Leer argumentos de línea de comandos
    if len(sys.argv) > 1:
        try:
            option = int(sys.argv[1])
            if option == 1:
                answer_ex_1()
            elif option == 2:
                answer_ex_2()
            elif option == 3:
                answer_ex_3()
            elif option == 4:
                answer_ex_4()
            elif option == 5:
                answer_ex_5()
            else:
                print("Opción inválida. Por favor, elija un número entre 1 y 5.")
        except ValueError:
            print("Por favor, introduzca un número válido entre 1 y 5.")
    else:
        # Ejecutar toda la PEC por defecto
        answer_ex_1()
        answer_ex_2()
        answer_ex_3()
        answer_ex_4()
        answer_ex_5()
