import numpy as np
import pandas as pd

inf_mor = pd.read_csv('../data/cleaned/infant_mortality.csv')

def air_data_cleaning(df, year, write_to, df2=inf_mor,):
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
    df.loc['National First Quartile'] = df.quantile(.25)
    df.loc['National Median'] = df.median()
    df.loc['National Third Quartile'] = df.quantile(.75)
    df.insert(loc=0, column='Year', value=year)
    df.to_csv(write_to)

def append_dataframes(df_list, write_to):
    '''
    DOCSTRING
    '''
    df = df_list[0]
    for dataframe in df_list[1:]:
        df = df.append(dataframe)
    df.reset_index(inplace=True, drop=True)
    df.to_csv(write_to, index=False)

def get_data_by_location_then_transpose(df, location, write_to):
    df = df.loc[df['Location'] == location]
    df.set_index('Year', inplace=True)
    df = df.transpose()
    df.drop('Location', inplace=True)
    df.to_csv(write_to)

def add_infant_mortality_row(file_location, other_df, row_name, new_row_name):
    df = pd.read_csv(file_location, index_col='Unnamed: 0')
    df = df.append(other_df.loc[row_name])
    df = df.rename(index={row_name: new_row_name})
    df.to_csv(file_location)

if __name__ == '__main__': 

    #### WRITE CLEANED DATA TO CSV FOR EACH YEAR ####

    # air_1999 = pd.read_csv('../data/conreport1999.csv')
    # air_data_cleaning(air_1999, 1999, '../data/cleaned/air_1999.csv')

    # air_2000 = pd.read_csv('../data/conreport2000.csv')
    # air_data_cleaning(air_2000, 2000, '../data/cleaned/air_2000.csv')
    
    # air_2001 = pd.read_csv('../data/conreport2001.csv')
    # air_data_cleaning(air_2001, 2001, '../data/cleaned/air_2001.csv')

    # air_2002 = pd.read_csv('../data/conreport2002.csv')
    # air_data_cleaning(air_2002, 2002, '../data/cleaned/air_2002.csv')

    # air_2003 = pd.read_csv('../data/conreport2003.csv')
    # air_data_cleaning(air_2003, 2003, '../data/cleaned/air_2003.csv')

    # air_2004 = pd.read_csv('../data/conreport2004.csv')
    # air_data_cleaning(air_2004, 2004, '../data/cleaned/air_2004.csv')

    # air_2005 = pd.read_csv('../data/conreport2005.csv')
    # air_data_cleaning(air_2005, 2005, '../data/cleaned/air_2005.csv')

    # air_2006 = pd.read_csv('../data/conreport2006.csv')
    # air_data_cleaning(air_2006, 2006, '../data/cleaned/air_2006.csv')

    # air_2007 = pd.read_csv('../data/conreport2007.csv')
    # air_data_cleaning(air_2007, 2007, '../data/cleaned/air_2007.csv')

    # air_2008 = pd.read_csv('../data/conreport2008.csv')
    # air_data_cleaning(air_2008, 2008, '../data/cleaned/air_2008.csv')

    # air_2009 = pd.read_csv('../data/conreport2009.csv')
    # air_data_cleaning(air_2009, 2009, '../data/cleaned/air_2009.csv')

    # air_2010 = pd.read_csv('../data/conreport2010.csv')
    # air_data_cleaning(air_2010, 2010, '../data/cleaned/air_2010.csv')

    # air_2011 = pd.read_csv('../data/conreport2011.csv')
    # air_data_cleaning(air_2011, 2011, '../data/cleaned/air_2011.csv')

    # air_2012 = pd.read_csv('../data/conreport2012.csv')
    # air_data_cleaning(air_2012, 2012, '../data/cleaned/air_2012.csv')

    # air_2013 = pd.read_csv('../data/conreport2013.csv')
    # air_data_cleaning(air_2013, 2013, '../data/cleaned/air_2013.csv')

    # air_2014 = pd.read_csv('../data/conreport2014.csv')
    # air_data_cleaning(air_2014, 2014, '../data/cleaned/air_2014.csv')

    # air_2015 = pd.read_csv('../data/conreport2015.csv')
    # air_data_cleaning(air_2015, 2015, '../data/cleaned/air_2015.csv')

    # air_2016 = pd.read_csv('../data/conreport2016.csv')
    # air_data_cleaning(air_2016, 2016, '../data/cleaned/air_2016.csv')

    # air_2017 = pd.read_csv('../data/conreport2017.csv')
    # air_data_cleaning(air_2017, 2017, '../data/cleaned/air_2017.csv')

    # air_2018 = pd.read_csv('../data/conreport2018.csv')
    # air_data_cleaning(air_2018, 2018, '../data/cleaned/air_2018.csv')


    #### READ IN NEW, CLEANED CSV FILES ####

    air_1999 = pd.read_csv('../data/cleaned/air_1999.csv')
    air_2000 = pd.read_csv('../data/cleaned/air_2000.csv')
    air_2001 = pd.read_csv('../data/cleaned/air_2001.csv')
    air_2002 = pd.read_csv('../data/cleaned/air_2002.csv')
    air_2003 = pd.read_csv('../data/cleaned/air_2003.csv')
    air_2004 = pd.read_csv('../data/cleaned/air_2004.csv')
    air_2005 = pd.read_csv('../data/cleaned/air_2005.csv')
    air_2006 = pd.read_csv('../data/cleaned/air_2006.csv')
    air_2007 = pd.read_csv('../data/cleaned/air_2007.csv')
    air_2008 = pd.read_csv('../data/cleaned/air_2008.csv')
    air_2009 = pd.read_csv('../data/cleaned/air_2009.csv')
    air_2010 = pd.read_csv('../data/cleaned/air_2010.csv')
    air_2011 = pd.read_csv('../data/cleaned/air_2011.csv')
    air_2012 = pd.read_csv('../data/cleaned/air_2012.csv')
    air_2013 = pd.read_csv('../data/cleaned/air_2013.csv')
    air_2014 = pd.read_csv('../data/cleaned/air_2014.csv')
    air_2015 = pd.read_csv('../data/cleaned/air_2015.csv')
    air_2016 = pd.read_csv('../data/cleaned/air_2016.csv')
    air_2017 = pd.read_csv('../data/cleaned/air_2017.csv')
    air_2018 = pd.read_csv('../data/cleaned/air_2018.csv')

    # VARIABLES INTO ITERABLE LIST
    dfs = [air_1999, air_2000, air_2001, air_2002, air_2003, air_2004, 
    air_2005, air_2006, air_2007, air_2008, air_2009, air_2010, air_2011, 
    air_2012, air_2013, air_2014, air_2015, air_2016, air_2017, air_2018]

    #### APPEND ALL YEARS AND WRITE TO CSV ####
    # append_dataframes(dfs, '../data/cleaned/air_all_years.csv')

    # READ IN ALL ANNUAL AIR DATA
    all_annual_data = pd.read_csv('../data/cleaned/air_all_years.csv')

    #### SPLIT INTO 'LOCATIONS' OF INTEREST FOR PLOTTING LATER ####
    # get_data_by_location_then_transpose(all_annual_data, 'New York City', '../data/cleaned/new_york.csv')
    # get_data_by_location_then_transpose(all_annual_data, 'National Means', '../data/cleaned/means.csv')
    # get_data_by_location_then_transpose(all_annual_data, 'National First Quartile', '../data/cleaned/q1.csv')
    # get_data_by_location_then_transpose(all_annual_data, 'National Median', '../data/cleaned/median.csv')
    # get_data_by_location_then_transpose(all_annual_data, 'National Third Quartile', '../data/cleaned/q3.csv')
    
    # READ IN INFANT MORTALITY AND ASTHMA DATAFRAMES 
    inf_mor = pd.read_csv('../data/cleaned/infant_mortality.csv', index_col = 'Location')
    asthma_nyc = pd.read_csv('../data/cleaned/asthma_nyc.csv', index_col = 'Unnamed: 0')

    #### ADD INFANT MORTALITY AND ASTHMA ROWS TO NEW YORK DATA ####
    # add_infant_mortality_row('../data/cleaned/new_york.csv', inf_mor, 'New York City', 'Infant Mortality Rate')
    # add_infant_mortality_row('../data/cleaned/new_york.csv', asthma_nyc, 'Asthma Hosp. Rate', 'Asthma Hosp. Rate')
    new_york = pd.read_csv('../data/cleaned/new_york.csv')
    # print(new_york)

    #### ADD INFANT MORTALITY METRICS TO MEAN AND QUARTILE DATA ####
    # add_infant_mortality_row('../data/cleaned/means.csv', inf_mor, 'Infant Mortality Mean', 'Infant Mortality')
    # add_infant_mortality_row('../data/cleaned/q1.csv', inf_mor, 'Infant Mortality First Quartile', 'Infant Mortality')
    # add_infant_mortality_row('../data/cleaned/median.csv', inf_mor, 'Infant Mortality Median', 'Infant Mortality')
    # add_infant_mortality_row('../data/cleaned/q3.csv', inf_mor, 'Infant Mortality Third Quartile', 'Infant Mortality')

