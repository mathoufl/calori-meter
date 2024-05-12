import os 
import shutil

def restorebd(filepath, version) :
    if not os.path.exists('/backup-store' + filepath + ''):
        print("backup doesn't for this file or the version is incorect")
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

def getLatestVersion(filepath):
    print('tbd')
    