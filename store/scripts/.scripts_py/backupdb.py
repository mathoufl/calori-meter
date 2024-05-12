import os
import shutil

def backupdb(filepath) :
    if not os.path.exists(filepath):
        print(f"File '{filepath}' doesn't exist.")
        return False
    else : 
        try :
            shutil.copy(filepath, '/backup-store')
            return True
        except Exception as e:
            print(f"An error occurred while processing '{filepath}': {e}")
            return False
    
filename = 'eatean-cal.csv'
backupdb(filename)