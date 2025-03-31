import json
import pickle
import os

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations

def load_saved_artifacts():
    print('locading saved artifacts... start')
    global __data_columns
    global __locations

    with open('artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = json.load(f)[3:]

    with open('artifacts/banglore_home_prices_model.pickle','rb') as f:
        __model = pickle.load(f)
    
    print('loading saved artifacts... done')


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())