import numpy as np
import pandas as pd

inf_mor = pd.read_csv('../data/cleaned/infant_mortality.csv')


def air_data_cleaning(df, write_to_path, df2=inf_mor):
    '''
    DocString
    '''
    numeric_cols = df.columns[2:]
    df[numeric_cols] = df[numeric_cols].replace('.', np.nan)
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col])
    df['CBSA'] = df['CBSA'].str.replace('Washington-Arlington-Alexandria, DC-VA-MD-WV', 'District of Columbia')
    df['CBSA'] = df['CBSA'].str.replace('New York-Newark-Jersey City, NY-NJ-PA', 'New York City')
    df['CBSA'] = df['CBSA'].str.split(',', expand=True)
    df['CBSA'] = df['CBSA'].str.split('-', expand=True)
    df['CBSA'] = df['CBSA'].str.split('/', expand=True)
    cities_to_keep = df2['Location'].unique()
    df = df.loc[df['CBSA'].isin(cities_to_keep)]
    cbsa_codes_to_drop = [17380, 17420, 17980, 18020, 18060, 27340, 33060, 38860]
    df = df.loc[~(df['CBSA Code'].isin(cbsa_codes_to_drop))]
    df.rename(columns={'CBSA': 'Location'}, inplace=True)
    df.set_index('Location', drop=True, inplace=True)
    df.drop(columns='CBSA Code', inplace = True)
    df.loc['National Means'] = df.mean()
    df.to_csv(write_to_path)



if __name__ == '__main__':
    
    air_1999 = pd.read_csv('../data/conreport1999.csv')
    air_data_cleaning(air_1999, '../data/cleaned/air_1999.csv')

    air_2000 = pd.read_csv('../data/conreport2000.csv')
    air_data_cleaning(air_2000, '../data/cleaned/air_2000.csv')
    
    air_2001 = pd.read_csv('../data/conreport2001.csv')
    air_data_cleaning(air_2001, '../data/cleaned/air_2001.csv')

    air_2002 = pd.read_csv('../data/conreport2002.csv')
    air_data_cleaning(air_2002, '../data/cleaned/air_2002.csv')

    air_2003 = pd.read_csv('../data/conreport2003.csv')
    air_data_cleaning(air_2003, '../data/cleaned/air_2003.csv')

    air_2004 = pd.read_csv('../data/conreport2004.csv')
    air_data_cleaning(air_2004, '../data/cleaned/air_2004.csv')

    air_2005 = pd.read_csv('../data/conreport2005.csv')
    air_data_cleaning(air_2005, '../data/cleaned/air_2005.csv')

    air_2006 = pd.read_csv('../data/conreport2006.csv')
    air_data_cleaning(air_2006, '../data/cleaned/air_2006.csv')

    air_2007 = pd.read_csv('../data/conreport2007.csv')
    air_data_cleaning(air_2007, '../data/cleaned/air_2007.csv')

    air_2008 = pd.read_csv('../data/conreport2008.csv')
    air_data_cleaning(air_2008, '../data/cleaned/air_2008.csv')

    air_2009 = pd.read_csv('../data/conreport2009.csv')
    air_data_cleaning(air_2009, '../data/cleaned/air_2009.csv')

    air_2010 = pd.read_csv('../data/conreport2010.csv')
    air_data_cleaning(air_2010, '../data/cleaned/air_2010.csv')

    air_2011 = pd.read_csv('../data/conreport2011.csv')
    air_data_cleaning(air_2011, '../data/cleaned/air_2011.csv')

    air_2012 = pd.read_csv('../data/conreport2012.csv')
    air_data_cleaning(air_2012, '../data/cleaned/air_2012.csv')

    air_2013 = pd.read_csv('../data/conreport2013.csv')
    air_data_cleaning(air_2013, '../data/cleaned/air_2013.csv')

    air_2014 = pd.read_csv('../data/conreport2014.csv')
    air_data_cleaning(air_2014, '../data/cleaned/air_2014.csv')

    air_2015 = pd.read_csv('../data/conreport2015.csv')
    air_data_cleaning(air_2015, '../data/cleaned/air_2015.csv')

    air_2016 = pd.read_csv('../data/conreport2016.csv')
    air_data_cleaning(air_2016, '../data/cleaned/air_2016.csv')

    air_2017 = pd.read_csv('../data/conreport2017.csv')
    air_data_cleaning(air_2017, '../data/cleaned/air_2017.csv')

    air_2018 = pd.read_csv('../data/conreport2018.csv')
    air_data_cleaning(air_2018, '../data/cleaned/air_2018.csv')