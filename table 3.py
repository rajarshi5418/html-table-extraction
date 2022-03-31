# reading all the csv file in directory
import os
from glob import glob

def get_csv_files(dir_path, ext):
    os.chdir(dir_path)
    return list(map(lambda x: os.path.join(dir_path, x), glob(f'*.{ext}')))

print(get_csv_files(r"C:\Users\H&H\PycharmProjects\pythonProject\html table extraction", "csv"))
