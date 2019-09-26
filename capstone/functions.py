
# Performs cleaning tasks
def cleaning_task(df):
    """ 
    cleaning_task functions receives dataframe as an input and then
    1) drops any duplicate rows
    2) drops any missing values
    3) prints out what percentage of the dataframe rows are missing
  
    Parameters: 
    df : Pandas dataframe
  
    Returns: 
    df: Returns pandas dataframe 
  
    """
    df.drop_duplicates(inplace = True) 
    df.dropna(inplace=True)
    print (df.isnull().sum()/len(df) )
    return df



# Performs quality check
def quality_check(df):
    """ 
    quality_check functions receives dataframe as an input and then
    1) checks if dataframe is empty
    2) if not empty, it prints out data type information on the dataframe columns as well as the size of data. 
  
    Parameters: 
    df : Pandas dataframe
  
    Returns: 
    df: prints the state of pandas dataframe 
  
    """
    if df.empty:
        print('DataFrame is empty!')
    else:    
        print (df.info() )
        print ('done')
