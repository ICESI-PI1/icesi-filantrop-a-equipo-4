import pandas as pd

def readExcel(fileName):

    info_df = pd.read_excel(fileName, header=0)

    info_list = info_df.to_dict(orient='index')

    return info_list
