import os
import numpy as np
import matplotlib.pyplot as plt
def read_data(data_dir):
    """Reads the peak values from each lvm file in the subdirectories of the data directory.
    For each subdirectory, calculates average peak value over all lvm files and returns a dictionary.

    Args:
        data_dir (str): path to the data directory
    Returns:
        result_dict (dict): dictionary with keys as subdirectory names and values as average peak values
    """
    result_dict = {}
    for dir_name in os.listdir(data_dir):
        if not os.path.isdir(os.path.join(data_dir, dir_name)):
            continue
        max_values = []
        for file_name in os.listdir(os.path.join(data_dir, dir_name)):
            if not file_name.endswith(".lvm"):
                continue
            file_path = os.path.join(data_dir, dir_name, file_name)
            try:
                # plot_lvm(file_path,save_path=os.path.join(data_dir, dir_name, file_name.replace(".lvm", ".png")))
                # 读取file_path保存在一个list中，每行为一个元素，每个元素去除空白符号
                with open(file_path, "r") as f:
                    lines = f.readlines()
                    lines = [float(line.strip()) for line in lines]
                lines = np.array(lines)
                max_value = np.max(lines)
                max_values.append(max_value)
            except Exception as e:
                print(f"Error reading {file_path}: {str(e)}")
        if len(max_values) > 0:
            avg_max_value = np.mean(max_values)
            result_dict[dir_name] = avg_max_value
    return result_dict

def plot_lvm(lvm_filepath,save_path=None,show=False):
    with open(lvm_filepath, "r") as f:
        lines = f.readlines()
        lines = [float(line.strip()) for line in lines]
    lines = np.array(lines)
    # plot lines
    plt.figure()
    plt.plot(lines)
    xlabel = "Time (s)"
    ylabel = "Voltage (V)"
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    title = os.path.basename(lvm_filepath)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()

if __name__ == '__main__':
    data_dir = r"C:\Users\duan'we'hua\Desktop\stray_light_suppression\data\0526"
    result_dict = read_data(data_dir)
    print(result_dict)
    # plot_lvm(r"C:\Users\duan'we'hua\Desktop\stray_light_suppression\data\0526\4\N91.lvm")