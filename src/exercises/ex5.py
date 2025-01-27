"""
This module provides functionality to analyze cyclist data from a DataFrame, focusing
on the UCSC club. It includes a function to filter and analyze the performance of UCSC cyclists,
determine the best cyclist within the club, their position in the overall ranking, and their
percentage ranking relative to the total number of cyclists

Function:
- analyze_ucsc: Performs an analysis of UCSC cyclists, including their best cyclist
and their ranking
"""

import pandas as pd

def analyze_ucsc(df):
    """
    Analyzes the UCSC club cyclists, finding the cyclists, the one with the best time,
    their position in the overall ranking, and the percentage over the total

    Parameters:
        df (pd.DataFrame): DataFrame containing cyclist data, including 'club_clean' and 'time'

    Returns:
        dict: Results of the analysis with the following keys:
              - 'cyclists': List of UCSC cyclists.
              - 'best_time_cyclist': Name of the cyclist with the best time
              - 'best_time_position': Position of the best cyclist in the overall ranking
              - 'best_time_percentage': Percentage of the position over the total
    """
    # Filtrar ciclistas del club UCSC
    ucsc_cyclists = df[df['club_clean'] == 'UCSC'].copy()

    if ucsc_cyclists.empty:
        return {
            "cyclists": [],
            "best_time_cyclist": None,
            "best_time_position": None,
            "best_time_percentage": None
        }

    # Lista de ciclistas de UCSC
    cyclists = ucsc_cyclists['biker'].tolist()

    # Calcular el tiempo en segundos, manejando valores nulos
    def calc_time(time_str):
        # Si es nulo, devuelve un valor muy grande
        if pd.isna(time_str):
            return float('inf')
        return sum(
            int(t) * 60 ** i
            for i, t in enumerate(reversed(time_str.split(':')))
        )

    df['time_seconds'] = df['time'].apply(calc_time)
    ucsc_cyclists['time_seconds'] = ucsc_cyclists['time'].apply(calc_time)

    # Encontrar el ciclista de UCSC con el mejor tiempo
    best_time_row = ucsc_cyclists.loc[ucsc_cyclists['time_seconds'].idxmin()]
    best_time_cyclist = best_time_row['biker']

    # Posición del mejor ciclista sobre el total
    df = df.sort_values(by='time_seconds').reset_index(drop=True)
    best_time_position = df[df['biker'] == best_time_cyclist].index[0] + 1

    # Calcular el porcentaje sobre el total
    total_cyclists = len(df)
    best_time_percentage = (best_time_position / total_cyclists) * 100

    return {
        "cyclists": cyclists,
        "best_time_cyclist": best_time_cyclist,
        "best_time_position": best_time_position,
        "best_time_percentage": best_time_percentage
    }
