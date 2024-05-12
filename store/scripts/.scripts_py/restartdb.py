import pandas as pd
import backupdb
import os

def restoredb(filepath):
    if not os.path.exists(filepath):
        print(f"File '{filepath}' doesn't exist.")
        return False
    else:
        isBackupOk = backupdb.backupdb(filepath)
        if not isBackupOk :
            print(f"Couldn't complete backup")
            return False
        
        os.remove(filepath)

        df = pd.DataFrame(columns=['date', 'time', 'plateName', 'occasion', 'caloriesSum'])
        df.to_csv(filepath, index=False)
        print(f"File '{filepath}' created with required columns.")
        return True

# Specify the filename
filename = 'eaten-cal.csv'

# Check if the file exists, if not, create it
restoredb(filename)
