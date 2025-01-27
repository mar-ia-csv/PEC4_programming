"""
This module provides functions for cleaning club names and analyzing cyclist participation by clubs.
It includes utilities to standardize club names, count participants per club, and merge these counts 
with the original data for its analysis

Functions:
- clean_club: Cleans and standardizes a given club name based on predefined rules
- create_club_participants_df: Creates a DataFrame with the number of participants per club
- create_full_club_participants_df: Merges the participant counts with the original DataFrame
"""

import re


def clean_club(club_name: str):
    """
    Cleans the name of a given club, by a set of rules

    Parameters:
        club (str): club name to be cleaned

    Returns:
        str: clean club name
    """
    # Comprobamos valores no válidos
    if club_name is None or not isinstance(club_name, str) or club_name.strip() == "":
        return "INDEPENDIENTE"

    # Convertimos a mayúsculas
    club_name = club_name.upper()

    # Reemplazamos valores completos
    replace_full = [
        'PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ',
        'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ', 'CLUB CICLISTA ', 'CLUB '
    ]
    for term in replace_full:
        club_name = club_name.replace(term, '')

    # Reemplazamos valores al principio
    replace_start = [
        'C.C. ', 'C.C ', 'CC ', 'C.D. ', 'C.D ', 'CD ', 'A.C. ', 'A.C ', 'AC ',
        'A.D. ', 'A.D ', 'AD ', 'A.E. ', 'A.E ', 'AE ', 'E.C. ', 'E.C ', 'EC ',
        'S.C. ', 'S.C ', 'SC ', 'S.D. ', 'S.D ', 'SD '
    ]
    for term in replace_start:
        club_name = re.sub(f'^{re.escape(term)}', '', club_name)

    # Reemplazamos valores al final
    replace_end = [
        ' T.T.', ' T.T', ' TT', ' T.E.', ' T.E', ' TE', ' C.C.', ' C.C', ' CC',
        ' C.D.', ' C.D', ' CD', ' A.D.', ' A.D', ' AD', ' A.C.', ' A.C', ' AC'
    ]
    for term in replace_end:
        club_name = re.sub(f'{re.escape(term)}$', '', club_name)

    # Eliminamos espacios en blanco al principio y al final
    club_name = club_name.strip()

    # Si queda vacío, se considera "Independiente"
    return club_name if club_name else "Independiente"


def create_club_participants_df(df):
    """
    Creates a DataFrame grouped by clubs and counts the number of cyclists per club,
    sorted in descending order by the number of participants.
    - Note: auxiliary function, not used in final project response

    Parameters:
        df (pd.DataFrame): Original DataFrame containing the 'club_clean' column

    Returns:
        pd.DataFrame: DataFrame with two columns:
                      - 'club_clean': Name of the club
                      - 'participant_count': Number of cyclists in the club
    """

    # Se agrupa por 'club_clean' y contar participantes
    club_participants_df = df.groupby('club_clean').size().reset_index(name='participant_count')

    # Ordenamos por número de participantes en orden descendente
    club_participants_df = club_participants_df.sort_values(by='participant_count', ascending=False)

    # Reiniciamos el índice para un formato limpio
    club_participants_df.reset_index(drop=True, inplace=True)

    return club_participants_df


def create_full_club_participants_df(df):
    """
    Creates a new DataFrame with the original data and a count of participants per club,
    sorted by the number of participants in descending order

    Parameters:
        df (pd.DataFrame): Original DataFrame containing cyclist data, including 'club_clean'

    Returns:
        pd.DataFrame: DataFrame with all original columns and an additional
        'participant_count' column
    """
    # Contar participantes por club
    club_counts = (
        df.groupby('club_clean')
        .size()
        .reset_index(name='participant_count')
    )

    # Mergear los conteos con el DataFrame original
    df = df.merge(club_counts, on='club_clean', how='left')

    # Ordenar por el número de participantes por club en orden descendente
    # y reiniciar el índice para un formato limpio
    df = df.sort_values(by='participant_count', ascending=False)
    df.reset_index(drop=True, inplace=True)

    return df
