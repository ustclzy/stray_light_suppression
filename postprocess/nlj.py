import numpy as np
import pandas as pd
import os

def get_mean(txt_file):
    """read avg result from txt_file

    Args:
        txt_file (str): txt_file_path
    Returns:
        avg (float): avg result
    """
    skip_rows = 37
    delimiter = "\s+"
    header = None
    usecols = [0, 1]
    nrows = 300

    df = pd.read_csv(txt_file, skiprows=skip_rows, sep=delimiter, header=header, usecols=usecols, nrows=nrows)
    df.columns = ["Timestamp", "Channel(A)"]
    # get mean value of channel A
    channel_A = df["Channel(A)"].values
    avg = np.mean(channel_A)
    return avg


def read_data(nlj_path):
    nlj_result= {}
    for _file in os.listdir(nlj_path):
        filepath = os.path.join(nlj_path,_file)
        index_num = int(_file.split(".")[0].split("_")[1])
        nlj_result[str(index_num)] = get_mean(filepath)
    # print(nlj_result)
    return nlj_result
if __name__ == '__main__':
    df = read_data(r"C:\Users\duan'we'hua\Desktop\stray_light_suppression\data\0526-nengliangji\3058255_03.txt")
    print(df)