import env
import pandas as pd

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_mall_data():
    '''gets mall customer data from mall_customers sql dbase'''
    return pd.read_sql('''SELECT *\
    FROM customers''', get_connection('mall_customers'))

def write_mall_csv(df):
    '''creates csv of mall customer info'''
    df.to_csv('mall_customers.csv')
