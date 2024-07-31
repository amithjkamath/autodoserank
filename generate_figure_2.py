import pandas as pd
import itertools as iterT
import random

# Inspired by https://stackoverflow.com/questions/64939016/python-function-for-calculating-ndpm-normalized-distance-based-performance-me

def calculate_ndpm(df, col_sysRank, col_userRank, user_id, ItemsPerUser):
    #     df : Dataframe
    #     col_sysRank: system predicted Rank on a recipe for a user
    #     col_userRank : rank of a recipe for user rank
    #     user_id : identifier for user
    #     ItemsPerUser : how many item per user

    combinations = [i for i in range(0, ItemsPerUser)]  # create a list of indexes { 0 to ItemsPerUser-1}

    listofCombination = list(
        iterT.combinations(combinations, 2))  # creating combination for every items in RecList for a user

    listOfSuccessRankPrediction = []  # list for storing number of successful relative rank for each user

    for j in list(set(df[user_id].tolist())):  # loop to calculate PDM for each user
        smallerslice = df[df[user_id] == j].reset_index()  # extract reclist for each user
        #
        s = 0  # initiate counter
        for i in list(listofCombination):  # compare for every recipe pair in  a reclist for a user
            if (smallerslice.loc[i[0]][col_sysRank] > smallerslice.loc[i[1]][col_sysRank]) == (
                    smallerslice.loc[i[0]][col_userRank] > smallerslice.loc[i[1]][col_userRank]):
                s = s + 1  # increment if successful
        listOfSuccessRankPrediction.append(s)

    NDPM = sum(listOfSuccessRankPrediction) / (len(list(set(df[user_id].tolist()))) * 21)
    return NDPM

if __name__ == "__main__":

    # Test calculate_ndpm:
    df_list = {'user_id': [i for i in ['U_01', 'U_02'] for j in range(0, 7)],
               'SysRank': [random.randint(0, 6) for i in range(0, 7 * len(['U_01', 'U_02']))],
               'userRate_basedRank': [random.randint(0, 6) for i in range(0, 7 * len(['U_01', 'U_02']))]}
    df = pd.DataFrame(df_list)

    print(calculate_ndpm(df, 'SysRank', 'userRate_basedRank', 'user_id', 7))