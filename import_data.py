import numpy as np
import os

def import_dataset(name: str) -> np.ndarray:
    """
    Import timeseries bitrate from given directory

    Args:
        name (str): name of directory where  all dataset is stored

    Returns:
        np.ndarray: Array with 2 shapes. First represents data for each day and second one represents many probes from one day
    """ 

    days_series = os.listdir(name)
    X = []

    for i in days_series:
        if i.endswith(".txt"):
            X.append(np.loadtxt(f"{name}/{i}"))
        elif i.endswith(".csv"):
            X.append(np.genfromtxt(f"{name}/{i}", delimiter=",", skip_header=1, usecols=1))
        else:
            print("Skip due incorrect format")

    return np.array(X)