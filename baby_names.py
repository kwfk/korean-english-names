from metaphone import doublemetaphone
import pandas as pd
from fuzzywuzzy import fuzz

#functions to get rid of repeats
def df_no_repeats(df):
    dupes = df.duplicated()
    df2 = df[~dupes]
    return df2

def find_names(name, gender):
    #get name file
    babyNamesRaw = pd.read_csv("Popular_Baby_Names.csv")
    babyNames = df_no_repeats(babyNamesRaw)

    entered_name = doublemetaphone(name)

    #getting the names
    babyNames_gender = babyNames[babyNames.Gender == gender.upper()]
    babyNames_gender = df_no_repeats(babyNames_gender)

    close_names = set()
    for match_name in babyNames_gender["Child's First Name"]:
        ratio = fuzz.ratio(entered_name, doublemetaphone(match_name))
        if ratio >= 80:
            close_names.add(match_name.capitalize())

    result = list(close_names)
    result.sort()
    return result
