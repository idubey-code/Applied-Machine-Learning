import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    
    utowns = pd.read_csv("university_towns.txt",sep="delimiter",header=None,engine='python',encoding='utf-8')
    utowns.columns=['RegionName']
    utowns.insert(0,'State',None)
    count=0
    for value in utowns.loc[:,'RegionName']:
        if value.find('[edit]')!=-1:
            i=utowns.index[utowns['RegionName']==value][0]
            utowns['State'][i-count:]=value[:value.index('[')]
            utowns.drop(i,inplace=True)
            count+=1
        elif value.find('(')!=-1:
            utowns['RegionName'].replace({value:value[:value.index('(')-1]},inplace=True)
    utowns.reset_index(inplace=True)
    utowns.drop('index',axis=1,inplace=True)
    
    return utowns

def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    
    GDP = pd.read_excel('gdplev.xls',skiprows=5).iloc[2:,4:7].drop(columns='GDP in billions of current dollars.1')
    GDP.columns=['Year','GDP']
    index = GDP.index[GDP['Year']=='2000q1'][0]
    GDP = GDP[index-2:]
    GDP.reset_index(inplace=True)
    GDP.drop(columns='index',inplace=True)
    r_duration=[]
    for i in range(1,len(GDP)-1):
        if GDP.iloc[i+1][1] < GDP.iloc[i][1] < GDP.iloc[i-1][1]:
            r_duration.append(GDP.iloc[i][0])
    return r_duration[0]

def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
       
    GDP = pd.read_excel('gdplev.xls',skiprows=5).iloc[2:,4:7].drop(columns='GDP in billions of current dollars.1')
    GDP.columns=['Year','GDP']
    index = GDP.index[GDP['Year']=='2000q1'][0]
    GDP = GDP[index-2:]
    GDP.reset_index(inplace=True)
    GDP.drop(columns='index',inplace=True)
    r_duration=[]
    for i in range(2,len(GDP)-2):
        if GDP.iloc[i-2][1] > GDP.iloc[i-1][1] > GDP.iloc[i][1] and GDP.iloc[i][1] < GDP.iloc[i+1][1] < GDP.iloc[i+2][1] :
            r_duration.append(GDP.iloc[i][0])
    return r_duration[0]
    
def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    
    GDP = pd.read_excel('gdplev.xls',skiprows=5).iloc[2:,4:7].drop(columns='GDP in billions of current dollars.1')
    GDP.columns=['Year','GDP']
    index = GDP.index[GDP['Year']=='2000q1'][0]
    GDP = GDP[index-2:]
    GDP.reset_index(inplace=True)
    GDP.drop(columns='index',inplace=True)
    r_duration={}
    for i in range(1,len(GDP)-1):
        if GDP.iloc[i-2][1] > GDP.iloc[i-1][1] > GDP.iloc[i][1] and GDP.iloc[i][1] < GDP.iloc[i+1][1] < GDP.iloc[i+2][1] :
        #if GDP.iloc[i+1][1] < GDP.iloc[i][1] < GDP.iloc[i-1][1]:
            r_duration[GDP.iloc[i][1]]=GDP.iloc[i][0]
    return r_duration[min(r_duration.keys())]

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    
    columns_to_keep = [str(i)+j for i in range(2000,2017) for j in ['q1','q2','q3','q4'] ]*3
    columns_to_keep.sort()
    columns_to_keep.insert(0,'RegionName')
    columns_to_keep.insert(1,'State')
    columns_to_keep = columns_to_keep[:-4]
    housing = pd.read_csv('City_Zhvi_AllHomes.csv').drop(columns='RegionID')
    housing1 = housing.loc[:,['RegionName','State']]
    housing2 = housing.loc[:,'2000-01':]
    housing = housing1.join(housing2)
    housing['State'].replace(states,inplace=True)
    housing.columns = columns_to_keep
    housing_new = housing[['State','RegionName']]
    i=2
    for column in housing.columns.unique()[2:]:
        housing_new.insert(i,column,np.mean(housing.loc[:,column],axis=1))
        i+=1
    del housing,housing1,housing2,i
    housing_new.set_index(['State','RegionName'],inplace=True)
    housing_new.sort_index(inplace=True)
    return housing_new

def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    
    utowns=get_list_of_university_towns()
    housing=convert_housing_data_to_quarters()
    housing.reset_index(inplace=True)
    df1 = pd.merge(utowns,housing,how='inner',left_on=['State','RegionName'],right_on=['State','RegionName'])
    df1.insert(2,'Price_Ratio',df1['2008q2']/df1['2009q2'])
    df1 = df1.iloc[:,0:3]
    df1.reset_index(inplace=True)
    df1.drop('index',axis=1,inplace=True)
    df2 = pd.merge(utowns,housing,how='outer',left_on=['State','RegionName'],right_on=['State','RegionName'],indicator=True)
    df2 = df2[df2['_merge']=='right_only']
    df2.insert(2,'Price_Ratio',df2['2008q2']/df2['2009q2'])
    df2 = df2.iloc[:,0:3]
    df2.reset_index(inplace=True)
    df2.drop('index',axis=1,inplace=True)
    
    p = ttest_ind(df1['Price_Ratio'],df2['Price_Ratio'],nan_policy='omit')[1]
    
    if p < 0.01:
        return (True,p,'university town')
    else:
        return (False,p,'non-university town')
    

#get_recession_bottom()
#get_recession_end()
#get_recession_start()
#get_list_of_university_towns()
#convert_housing_data_to_quarters()
#run_ttest()