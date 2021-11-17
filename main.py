import pandas as pd

def profile_df(df):
    profile=[]
    for cols in df.columns:
        print(cols)
        col_name = cols
        unique_vals = df[cols].unique()
        total_rec = len(df)
        unique_val_count = len(df[cols].unique())
        null_rec_count = len(df[df[cols].isnull()])
        max_value = df[cols].max()
        min_value = df[cols].min()
        print(min_value)
        if df[cols].dtype == 'O':
            blank_rec_count = len(df[df[cols].str.strip() == ''])
        else:
            blank_rec_count = 0
        temp = {'col_name': col_name, 'unique_vals': unique_vals, 'total_rec': total_rec,
                'unique_val_count': unique_val_count, 'null_rec_count': null_rec_count,'max_value':max_value,'min_value':min_value}
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
