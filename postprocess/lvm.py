import os
import numpy as np
import matplotlib.pyplot as plt
def read_data(data_dir,plot=False):
    """Reads the peak values from each lvm file in the subdirectories of the data directory.
    For each subdirectory, calculates average peak value over all lvm files and returns a dictionary.
    定义一个函数 get_peak_value，用于计算给定的 lvm 文件中的峰值，峰值被定义为其中最大的计数值。
    定义一个函数 read_data，用于读取 data 目录下的所有子文件夹，对于每个子文件夹，遍历其中的所有 lvm 文件
    计算它们的峰值，并计算这些峰值的平均值，作为该子文件夹的平均峰值。
    最后将计算结果存放在一个字典中，并返回该字典。
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
                if plot:
                    plot_lvm(file_path,save_path=os.path.join(data_dir, dir_name, file_name.replace(".lvm", ".png")))
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
