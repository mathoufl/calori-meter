import pandas as pd
import json
import os



def createdb(filename):

    if os.path.exists(filename):
        print(f"File '{filename}' already exists.")
        return True

    else:
        try :
            dbColumns = loadSchema(filename)

            df = pd.DataFrame(columns=dbColumns)
            df.to_csv(filename, index=False)

            print(f"File '{filename}' created with required columns.")
            return True
        
        except Exception as e :
            return False



def loadSchema(filename):

    try :
        with open('schemadb.json', 'r') as file:
            schema = json.load(file)
        
        keyList = list(schema.keys())
        parsedSchemas = list([schema[k] for k in keyList])
        filterSchema = list(filter(lambda x: x['name']==filename, parsedSchemas))

        if len(filterSchema) < 1 :
            raise Exception("No corresponding schema")
        return filterSchema[0]['columns']
        
    except Exception as e:
        raise print(f"An error occurred while laoding correct schema: {e}")



############## run ###############

filename = 'eatan-cal.csv'
createdb(filename)
