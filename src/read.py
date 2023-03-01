import pandas as pd

def fanfict():

    data = pd.read_csv('./data/avgRatings_annotated.csv')
    df = data.copy()

    return df

def phon_trans():

    data = pd.read_csv('./data/na_names_phonTrans.csv')
    df = data.copy()
    return df 