import acquire_mall as acq_mall
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler


def get_upper_outliers(s, k):
    '''
    Given a series and a cutoff value, k, returns the upper outliers for the series.\
    The values returned will be either 0 (if the point is not an outlier), or a\
    number that indicates how far away from the upper bound the observation is.\
    '''
    q1, q3 = s.quantile([.25, .75])
    iqr = q3 - q1
    upper_bound = q3 + k * iqr
    return s.apply(lambda x: max([x - upper_bound, 0]))

def add_upper_outlier_columns(df, k):
    '''
    Add a column with the suffix _outliers for all the numeric columns in the given dataframe.\
    '''
    # outlier_cols = {col + '_outliers': get_upper_outliers(df[col], k)
    #                 for col in df.select_dtypes('number')}
    # return df.assign(**outlier_cols)
    for col in df.select_dtypes('number'):
        df[col + '_outliers'] = get_upper_outliers(df[col], k)
    return df

def outlier_peek(df):
    outlier_cols = [col for col in df if col.endswith('_outliers')]
    for col in outlier_cols:
        print('~~~\n' + col)
        data = df[col][df[col] > 0]
        print(data.describe())

def dumb_df(df):
    pd.get_dummies(df)
    return df
    
def prep_mall_data(df):
    return df.pipe(get_upper_outliers)\
    .pipe(add_upper_outlier_columns)\
    .pipe(outlier_peek)\
    .pipe(dumb_df)

def peekatdata(df):
    print("HEAD:")
    print(df.head(5))

    print('\n \n TAIL:' )
    print(df.tail(5))

    print("\n \n SHAPE:")
    print(df.shape)

    print("\n \n DESCRIBE:")
    print(df.describe())

    print("\n \n INFO")
    print(df.info())

    print("\n \n Missing Values:")
    missing_vals = df.columns[df.isnull().any()]
    print(df.isnull().sum())