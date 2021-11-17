import pandas as pd

from dateutil.parser import parse
def is_date(string, fuzzy=False):  ## To check if certain column is date or not
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def profile_df(df):
    profile=[]
    ### Converting column datatype to date - if any date column is present - After the import the date colums comes as Object
    for cols in df.columns:
        coltype = df[cols].dtype
        if (coltype == 'object'):
            if (is_date(df.loc[0, cols]) == True):
                df[cols] = pd.to_datetime(df[cols])
            else:
                df[cols] = df[cols].apply(str)

    for cols in df.columns:
        print(cols)
        col_name = cols
        unique_vals = df[cols].unique()
        total_rec = len(df)
        unique_val_count = len(df[cols].unique())
        null_rec_count = len(df[df[cols].isnull()])
        max_value = df[cols].max()
        min_value = df[cols].min()
        max_value_len = df[cols].astype(str).str.len().max()
        min_value_len = df[cols].astype(str).str.len().min()
        col_data_type = df[cols].dtype
        variable_type = 'Categorical' if len(df[cols].unique())<=10 else 'Non-Categorical'
        print(min_value)
        if df[cols].dtype == 'O':
            blank_rec_count = len(df[df[cols].str.strip() == ''])
        else:
            blank_rec_count = 0
        temp = {'col_name': col_name, 'unique_vals': unique_vals, 'total_rec': total_rec,
                'unique_val_count': unique_val_count, 'null_rec_count': null_rec_count,'max_value':max_value,'min_value':min_value,
                'max_value_len':max_value_len, 'min_value_len':min_value_len, 'col_data_type':col_data_type,'variable_type':variable_type
                }
        profile.append(temp)

    profile_df = pd.DataFrame(profile)
    return profile_df



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv('marketing_camp.csv')
    profile = profile_df(df)
    profile.to_csv('profile.csv')
    print(profile.head(3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
