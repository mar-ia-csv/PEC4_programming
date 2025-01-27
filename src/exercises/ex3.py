"""
This module provides functions to process and analyze data 
from te DataFrame. It includes functionality to group times into intervals,
add new grouped time columns, aggregate data by grouped times, and visualize
the results using a histogram.

Functions:
- minutes_002040: Converts a time string to 'hh:mm' format with 20-minute intervals
- add_time_grouped_column: Adds a new 'time_grouped' column to a DataFrame
- group_by_time_grouped: Aggregates data by grouped time intervals
- plot_histogram: Creates and saves a histogram based on grouped data
"""

import matplotlib.pyplot as plt

def minutes_002040(time_str: str):
    """
        Given a time as hh:mm:ss input format,
        returns the time as hh:mm, while grouping
        minutes as 20 min intervals (00, 20, 40) 
        Parameters:
            time_str (str): time expressed as 'hh:mm:ss'

        Returns:

            formatted_time (str): time in 'hh:mm' fomat, grouped into an interval
    """
    # Dividimos el tiempo en horas, minutos y segundos (no necesarios)
    hours, minutes, _ = map(int, time_str.split(':'))

    # Agrupamos los minutos a la franja más cercana
    # (00, 20, 40)
    if minutes < 20:
        rounded_minutes = 0
    elif minutes < 40:
        rounded_minutes = 20
    else:
        rounded_minutes = 40

    # Tiempo en formato 'hh:mm'
    formatted_time = f"{hours:02d}:{rounded_minutes:02d}"

    return formatted_time


def add_time_grouped_column(df, time_column:str='time'):
    """
    Using the minutes_002040() function, adds a new column
    'time_grouped' to the given DataFrame,
    by grouping the times of an existing time column

    Parameters:
        df (pd.DataFrame): given DataFrame
        time_column (str): column name containing data in 'hh:mm:ss' format

    Returns:
        pd.DataFrame: DataFrame with the new column 'time_grouped'
    """
    df = df.copy()

    df.loc[:, 'time_grouped'] = df[time_column].apply(minutes_002040)

    return df


def group_by_time_grouped(df):
    """
    Groups data by 'time_grouped' column and counts the number of occurrences in each group

    Parameters:
        df (pd.DataFrame): DataFrame containing the 'time_grouped' column

    Returns:
        pd.DataFrame: New DataFrame with two columns:
                      - 'time_grouped': Groups of times
                      - 'cyclist_count': Count of cyclists in each group
    """
    # Agrupamos por 'time_grouped' y contar las ocurrencias
    grouped_df = df.groupby('time_grouped', as_index=False).size()

    # Renombramos las columnas
    grouped_df.rename(
    columns={'time_grouped': 'time_grouped', 'size': 'cyclist_count'},
    inplace=True
    )

    return grouped_df



def plot_histogram(grouped_df, output_path:str='./img/histograma.png'):
    """
    Generates a histogram given the grouped data, and saves it.
    Parameters:
        grouped_df (pd.DataFrame): DataFrame containing the goups and 
                                   no. of occurences per group
        output_path (str): File path to save the histogram image.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(
    grouped_df['time_grouped'],
    grouped_df['cyclist_count'],
    color='blue',
    edgecolor='black'
    )
    plt.title('Histograma de Ciclistas por Tiempos Agrupados', fontsize=14)
    plt.xlabel('Tiempos Agrupados (hh:mm)', fontsize=12)
    plt.ylabel('Número de Ciclistas', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    plt.close()
