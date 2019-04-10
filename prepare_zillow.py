import acquire_zillow as acq
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def get_full_zillow():
    '''pulls in the entire 2016-2017 zillow master set'''
    df = pd.read_csv('zillow.csv')
    return df

def singles_only(df):
    '''looks at single units only'''
    singles = ['Single Family Residential']
    # singles = ['Cluster Home', 'Condominium', 'Cooperative', 'Manufactured, Modular, Prefabricated Homes', 'Mobile Home', 'Residential General', 'Single Family Residential', 'Townhouse']
    df = df[df.propertylandusedesc.isin(singles)] 
    return df

def nums_to_obj(df):
    df[['parcelid', 'buildingqualitytypeid', 'fips', 'rawcensustractandblock', 'regionidcity', 'regionidcounty', 'regionidzip', 'yearbuilt', 'assessmentyear', 'censustractandblock']] = df[['parcelid', 'buildingqualitytypeid', 'fips', 'rawcensustractandblock', 'regionidcity', 'regionidcounty', 'regionidzip', 'yearbuilt', 'assessmentyear', 'censustractandblock']].astype(str)
    return df

def remove_columns(df, cols_to_remove):  
    df = df.drop(columns=cols_to_remove)
    return df

def handle_missing_values(df, prop_required_column = .75, prop_required_row = .75):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

# def fill_unitcnt(df):
#     df['unitcnt'] = df['unitcnt'].fillna(value=0, inplace = True)
#     return df

# def fill_all_others(df):
#     df = df.fillna(value=0, inplace = True)
#     return df

def drop_remaining_missing(df):
    df = df.dropna()
    return df

def data_prep(df, cols_to_remove=['calculatedbathnbr','finishedsquarefeet12','assessmentyear','roomcnt','landtaxvaluedollarcnt','structuretaxvaluedollarcnt','rawcensustractandblock','heatingorsystemdesc','lotsizesquarefeet','propertyzoningdesc','fullbathcnt'], prop_required_column=.75, prop_required_row=.75):
    df = nums_to_obj(df)
    df = singles_only(df)
    df = remove_columns(df, cols_to_remove)
    df = handle_missing_values(df, prop_required_column, prop_required_row)
    # df = fill_unitcnt(df)
    # df = fill_all_others(df)
    df = drop_remaining_missing(df)
    return df

def peekatdata(df):
    print("\n \n SHAPE:")
    print(df.shape)

    print("\n \n COLS:")
    print(df.columns)

    print("\n \n INFO:")
    print(df.info())

    print("\n \n Missing Values:")
    missing_vals = df.columns[df.isnull().any()]
    print(df.isnull().sum())

    print("\n \n DESCRIBE:")
    print(df.describe())

    print('\n \n HEAD:')
    print(df.head(5))

    print('\n \n TAIL:' )
    print(df.tail(5))
