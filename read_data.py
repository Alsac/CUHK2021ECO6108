
import pandas as pd
import h5py

def read_data(path: str):

    def find_keys(path: str):
        with h5py.File(path, 'r') as f:
            return list(f.keys())

    data_all = pd.DataFrame()
    for code in find_keys(path):
        data = pd.read_hdf(path, key=code)
        data_all = pd.concat([data_all, data], axis=0)

    return data_all

if __name__ == '__main__':
    path = r'/home/wangyanlong/project/project_1min/data_1min_sz50.h5'  # your data path
    data = read_data(path)