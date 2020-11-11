import pandas as pd
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file_estate = os.path.join(THIS_FOLDER,'csv\\Real estate.csv')

def Write_Csv(list_data):
    df = pd.read_csv(my_file_estate)
    file = open(my_file_estate,"a")
    number=df['No'].values[-1]
    number+=1
    file.write(str(number)+",")
    for i in list_data:
        if i != list_data[6]:
            file.write(str(i)+",")
        else :file.write(str(i)+"\n")
    file.close()
    df.reset_index(drop = True,inplace=True)
