import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ecl2df import EclFiles, grid

case_params = {
    "2DHOM1": (1.6, 0.5, 1.8),
    "2DHOM2": (0.8, 0.5, 1.8),
    "2DHOM3": (0.4, 0.5, 1.8),
    "2DHOM4": (0.2, 0.5, 1.8),
    "2DHOM5": (0.1, 0.5, 1.8),
}


linestyles = {
    "2DHOM1": '-',
    "2DHOM2": '--',
    "2DHOM3": '-.',
    "2DHOM4": ':',
    "2DHOM5": '-',
}


combined_times = {}
combined_depths = {}


for case_name, (depth_step, min_rs_value, max_rs_value) in case_params.items():
    eclfiles = EclFiles(f"{case_name}.DATA")
    df = grid.df(eclfiles, rstdates="all")

    t_steps = set(col.split("RS@")[1] for col in df.columns if "RS@" in col)
    t_steps_sorted = sorted(t_steps)
    str_t_steps = [str(step) for step in t_steps_sorted]

    deepest_depths = []
    times = []


    for t_step in str_t_steps:
        rs_data = df[f"RS@{t_step}"].to_numpy()
        depth_data = df["DEPTH"].to_numpy()

        valid_indices = np.where((min_rs_value <= rs_data) & (rs_data <= max_rs_value))

        if valid_indices[0].size > 0:
            deepest_index = valid_indices[0][np.argmax(depth_data[valid_indices])]
            times.append(t_step)
            deepest_depths.append(depth_data[deepest_index])


            if depth_data[deepest_index] >= 1012.2:
                break
        else:
            times.append(t_step)
            deepest_depths.append(1001.0)


    combined_times[case_name] = times
    combined_depths[case_name] = deepest_depths


plt.figure(figsize=(20, 12))

for case_name, (depth_step, min_rs_value, max_rs_value) in case_params.items():
    label = f"{case_name}, Grid Cell Size = {depth_step} m"
    plt.plot(combined_times[case_name], combined_depths[case_name], linestyle=linestyles[case_name], label=label)

plt.xlabel("Time Steps")
plt.ylabel("Finger Front - Depth (meters)")
plt.title("Growing Finger Front In Depth Over Time")
plt.grid(True)
plt.legend()

plt.xticks(rotation=90)
plt.savefig('Finger_Front_Growing_HOM1.png')