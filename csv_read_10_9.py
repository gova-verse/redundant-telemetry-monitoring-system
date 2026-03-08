import pandas as pd

dft = pd.read_csv('tg_7.csv')


def read_time():

    return [dft.iloc[0][0], dft.iloc[0][1]]


def read_chno():

    return [
        dft.iloc[0][3],
        dft.iloc[1][3],
        dft.iloc[2][3],
        dft.iloc[3][3]
    ]


def y_range():

    return [
        dft.iloc[0][4:6],
        dft.iloc[1][4:6],
        dft.iloc[2][4:6],
        dft.iloc[3][4:6]
    ]


dfi = pd.read_csv('info_7.csv')


def title():
    return dfi.columns[0]