import json
import pickle
import os
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts... start')
    global __data_columns, __locations, __model
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.join(script_dir, 'artifacts')
    
    # Construct full paths
    columns_path = os.path.join(artifacts_dir, 'columns.json')
    model_path = os.path.join(artifacts_dir, 'banglore_home_prices_model.pickle')
    
    with open(columns_path, 'r') as f:
        data = json.load(f)
        __data_columns = data['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    
    with open(model_path, 'rb') as f:
        __model = pickle.load(f)
    
    print('loading saved artifacts... done')

if __name__ == '__main__':
    load_saved_artifacts()