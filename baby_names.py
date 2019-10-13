from metaphone import doublemetaphone
import pandas as pd
from fuzzywuzzy import fuzz

#get name file
babyNamesRaw = pd.read_csv("C:\\Users\\jenni\\Downloads\\Popular_Baby_Names.csv")
babyNames = df_no_repeats(babyNamesRaw)

#get user input
entered_name = doublemetaphone(input())
gender = input('Female or Male? ').upper()

#functions to get rid of repeats
def df_no_repeats(df):
    dupes = df.duplicated()
    df2 = df[~dupes]
    return df2

def list_no_repeats(li):
    final_list = []
    for i in li:
        if i.capitalize() not in final_list:
            final_list.append(i.capitalize())
    return final_list

#getting the names
babyNames_gender = babyNames[babyNames.Gender == gender]
babyNames_gender = df_no_repeats(babyNames_gender)

print_names = []
for i in babyNames_gender["Child's First Name"]:
    ratio = fuzz.ratio(doublemetaphone(entered_name), doublemetaphone(match_name))
    if ratio >= 80:
        print_names.append(i)

final_list = list_no_repeats(print_names)
print (final_list)




