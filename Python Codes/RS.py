import ecl2df
import matplotlib.pyplot as plt
import numpy as np
from ecl2df import grid
from ecl2df import EclFiles
import pandas as pd
import re


def process_eclfiles(file_path, grid_range):
    eclfiles = ecl2df.EclFiles(file_path)
    df = grid.df(eclfiles, rstdates='all')
    df = pd.DataFrame(df)

    df_1 = df.iloc[grid_range]
    Rs_col = [col for col in df_1.columns if col.startswith('RS@')]
    Sgas_col = [col for col in df_1.columns if col.startswith('SGAS@')]

    df = df_1[Rs_col + Sgas_col]

    for Sgas_coll in Sgas_col:
        time_step = Sgas_coll.split('@')[1]
        df[f'SOIL@{time_step}'] = 1 - df[Sgas_coll]

    Soil_col = [col for col in df.columns if col.startswith('SOIL@')]
    df = df[Rs_col + Soil_col]
    df['PORV'] = df_1['PORV']

    for Time_step in Rs_col:
        Rs_val_col = f"RS_val{Time_step[-10:]}"
        df[Rs_val_col] = df[Time_step] * df[Soil_col[Rs_col.index(Time_step)]] * df["PORV"]

    df = pd.DataFrame(df)
    Rs_val_col = [col for col in df.columns if col.startswith("RS_val")]
    Rs_f = df[Rs_val_col].sum(axis=0) / (df[Soil_col[Rs_col.index(Time_step)]] * df["PORV"]).sum(axis=0)

    return Rs_f


def main_plot():
    Rs_f_1 = process_eclfiles('2DHOM1.DATA', slice(1, 55))
    Rs_f_2 = process_eclfiles('2DHOM2.DATA', slice(1, 190))
    Rs_f_3 = process_eclfiles('2DHOM3.DATA', slice(1, 700))
    Rs_f_4 = process_eclfiles('2DHOM4.DATA', slice(1, 2680))
    Rs_f_5 = process_eclfiles('2DHOM5.DATA', slice(1, 10480))

    t_steps = [str(step)[-10:] for step in sorted(set(Rs_f_1.index))]

    plt.figure(figsize=(20, 12))

    plt.plot(t_steps, Rs_f_1, label='2DHOM1(Grid_cell_size = 1.6 m)', linestyle='--', color='r')
    plt.plot(t_steps, Rs_f_2, label='2DHOM2(Grid_cell_size = 0.8 m)', linestyle=':', color='g')
    plt.plot(t_steps, Rs_f_3, label='2DHOM3(Grid_cell_size = 0.4 m)', linestyle='-.', color='y')
    plt.plot(t_steps, Rs_f_4, label='2DHOM4(Grid_cell_size = 0.2 m)', linestyle='-', color='b')
    plt.plot(t_steps, Rs_f_5, label='2DHOM5(Grid_cell_size = 0.1 m)', linestyle='-', color='c')

    plt.xlabel("Time")
    plt.ylabel("RS")
    plt.title("RS Vs. Time")
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.savefig('Rs_HOM_2D1.png')

if __name__ == "__main__":
    main_plot()

