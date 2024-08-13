# Upscaling The Dissolution Process of CO2 into Formation Brine Using OPM-flow simulator
This GitHub repository has been established as an additional resource accompanying my Master's thesis conducted in Autumn 2023. The project's primary objective was to scale up the CO2 dissolution process into brine, recognized as one of the most effective chemical trapping mechanisms in CO2 sequestration procedures.

## Abstract

As global reliance on fossil fuels continues, concerns over carbon dioxide (CO2) emission and its role in global warming is intensifying. Carbon capture and storage (CCS) is a widely recognized solution to mitigate CO2 emission, involving the capturing of CO2 from the main sources and its underground sequestration. This method can potentially reduce CO2 emission by up to 20%, contributing significantly to the goal of limiting global temperature rise to 2°C.

This thesis primarily investigates the CO2 dissolution process into brine within aquifers, which is recognized as the most effective long-term chemical trapping mechanism for CO2 sequestration. The study focuses on upscaling the dissolution process and examining the behavior of key factors such as molecular diffusion and convective mixing. For this analysis, the OPM Flow numerical reservoir simulator, ResInsight, and Python programming language are utilized to run simulation files, visualize results, and analyze data from the simulations.

Our findings highlight the significant impact of grid cell size, permeability, and heterogeneity on the CO2 dissolution process. Key conclusions include the influence of permeability in various layers on the rates of molecular diffusion and convective dissolution, and the role of anisotropy in delaying molecular diffusion and reducing its rate.

Our findings highlight the significant impact of grid cell size (utilized in the simulation), permeability heterogeneity, and anisotropy on the dissolution process.

## Installation Instructions

To perform the analysis on the CO2 dissolution process into brine, OPM Flow numerical reservoir simulator, ResInsight, and Python programming language are utilized to run simulation files, visualize results, and analyze data from the simulations.

### Simulation and Visualization

These two important stages of the work require the installation of OPM Flow numerical reservoir simulator and ResInsight visualization tool.

#### OPM Flow Reservoir Simulator

Although all the output files from simulations are provided in this repository, the instructions for installing and running simulations using OPM Flow can be found as follows. OPM Flow is an open-source reservoir simulator and since it is designed for Linux systems, instructions for setting up the simulator on either Linux or Windows systems are provided below:

1. **Linux systems:**

   Follow the steps on the [OPM Project webpage](https://opm-project.org/?page_id=245) or watch [videos (provided by Carl Fredrik Berg)](https://www.youtube.com/watch?v=r1hL1lvwG9c&t=1s) to easily set up OPM Flow on your Linux system.

2. **Windows systems:**

   To install the OPM Flow simulator on Windows systems, you can use either a Virtual Machine or Windows Subsystem for Linux (WSL).

   **Virtual Machine:**

   Although you can find the complete instructions on the webpage provided by Allan Katende, generally you should follow these steps:

   a) Download and install a VM platform like VirtualBox or VMware.

   b) Download a Linux ISO of your preferred distribution (e.g., Ubuntu).

   c) Create a new VM and follow the prompts to install the Linux OS using the ISO file.

   d) Once installed, follow the instructions in the [videos (provided by Carl Fredrik Berg)](https://www.youtube.com/watch?v=r1hL1lvwG9c&t=1s).

   **Windows Subsystem for Linux (WSL):**

   If you want to use WSL, follow these steps:

   a) Enable WSL via PowerShell (as Administrator): 
      ```sh
      wsl --install
      ```

   b) Follow the prompts to restart your computer if necessary.

   c) Install a Linux distribution from the Microsoft Store (e.g., Ubuntu).

   d) Once installed, open Ubuntu and again follow the instructions in the [video (provided by Carl Fredrik Berg)](https://www.youtube.com/watch?v=r1hL1lvwG9c&t=1s).

### ResInsight

To visualize the simulation results, you need to install ResInsight. Follow the instructions on the [ResInsight website](https://resinsight.org/getting-started/download-and-install/windows-installation/) to download and install the newest version of software either for Linux or Windows systems.

### Python

Ensure Python is installed on your system. You can download it from [Python.org](https://www.python.org/downloads/).

To analyze and process the simulation data, the following Python libraries are essential:

- **Numpy**: For numerical computations and array operations.
- **matplotlib**: For plotting and visualizing data.
- **pandas**: For data manipulation and analysis, particularly in tabular form.
- **ecl2df**: A Pandas DataFrame wrapper that incorporates features from opm.io and resdata, which are excellent packages for reading result files from reservoir simulators. ecl2df includes submodules such as summary, grid, pillars, and satfunc, each designed to analyze distinct aspects of the simulation model. This package is provided by Equinor. You can find complete information about the package [here](https://equinor.github.io/res2df/).

You can install these libraries by running the following command:

```sh
pip install numpy matplotlib pandas ecl2df
```
## Usage Instructions

After installing OPM Flow, you'll need a properly configured input file (referred to as a DATA file) to simulate your model. This file includes detailed characterization of the fluid, porous media, and other parameters relevant to your simulation.

Below is a sample input file used in the thesis to simulate the CO2 dissolution process into brine. While this example is specific to one simulation scenario, various input files with different values for certain variables were created to achieve the desired simulation results.

You can find all the input files used in the thesis in the repository. The naming convention for these DATA files indicates the differences between them, which is explained below.

### Naming Convention for Input Files

The general format for the input file names is as follows: `2DHETA11`. Here's how to interpret it:

- **First Two Digits (2D/3D)**: Indicates whether the model is 2D or 3D.
- **Next Three Letters (HOM/HET)**: Specifies if the model is homogeneous (`HOM`) or heterogeneous (`HET`).
- **Next Letter ('A')**: Denotes anisotropic conditions (only applicable in anisotropic models).
- **Last Two Numbers**: Indicate the grid cell size and the heterogeneity condition applied to the model.

**Grid Cell Sizes**:

| Grid Cell Number | Grid Cell Size (m) |
|------------------|--------------------|
| 1                | 1.6                |
| 2                | 0.8                |
| 3                | 0.4                |
| 4                | 0.2                |
| 5                | 0.1                |

**Heterogeneity Conditions**:

| Condition Number | K in Layer 1 (md) | K in Layer 2 (md) | K in Layer 3 (md) |
|------------------|-------------------|-------------------|-------------------|
| 1                | 1000              | 2000              | 1000              |
| 2                | 2000              | 1000              | 2000              |
| 3                | 1000              | 1000              | 2000              |
| 4                | 2000              | 2000              | 1000              |

**Anisotropy Conditions**:

| Direction | Layer 1 | Layer 2 | Layer 3 |
|-----------|---------|---------|---------|
| **x**     | Het. condition | Het. condition | Het. condition |
| **y**     | 500     | 1000    | 500     |
| **z**     | 400     | 300     | 400     |

In 3D models, the structure is similar to 2D models, with consistent changes in heterogeneity and anisotropy. Notably, the grid cell size for the CO2 layer is fixed at 0.1 m in the z-direction in all cases.

### Example Input Deck

Below is an example of an input deck, which is a text file that OPM Flow reads to execute the simulation. This specific example simulates the CO2 dissolution into formation brine:

```plaintext
--This simulation is based on SPE-CASE1 (provided by Statoil-2015)
--and the model utilizes the CO2STORE keyword in OPM-flow (provided by Carl Fredrik Berg)

--Modified by: Reza Mozaffari

RUNSPEC
-- --------------------------------------------------

TITLE
 CO2 Dissolution into Formation Brine

DIMENS    
 1 5 11 /

TABDIMS
 /

--To utilize CO2STORE keyword, DIFFUSE should also be added 
OIL
GAS
DISGAS

DIFFUSE
CO2STORE

--The unit for different input variables
METRIC

START
   1 'JAN' 2023 /

UNIFOUT

GRID
-- --------------------------------------------------

INIT

--Size of grid blocks in different directions
DX
  55*1.6/

DY
  55*1.6/
 
DZ
  15*0.1 40*1.6/

--Depth of top for each grid block
TOPS
  5*1000 /

--Value of porosity 
PORO
2*0.35
1*0.38
5*0.34
1*0.37
3*0.36
2*0.35
1*0.34
40*0.38/
    
--Value of permeability in x-direction (mD)
PERMX
15*2000
20*2000
20*1000/
    
--Value of permeability in y-direction (mD)
PERMY    
15*500
20*1000
20*500/

--Value of permeability in z-direction (mD)
PERMZ
15*400
20*300
20*400/

PROPS
-- -------------------------------------------------

ROCK
-- Rock Compressibility
-- Ref. pressure     Compressibility
-- -------------     ---------------
       10.0          4E-05   /

SGOF
-- Column 1: gas saturation
-- Column 2: gas relative permeability
-- Column 3: oil relative permeability when oil,
-- gas and connate water are present
-- Column 4: oil-gas capillary pressure
0.0 0.0 1.0 0.025
0.1 0.0 0.740 0.026
0.2 0.009 0.528 0.027
0.3 0.030 0.359 0.028
0.4 0.070 0.230 0.030
0.5 0.136 0.136 0.032
0.6 0.230 0.070 0.035
0.7 0.359 0.030 0.038
0.8 0.528 0.009 0.044
0.9 0.740 0.000 0.057 /

SALINITY
0.7/ 35-40g/l -> 35-40g/kg -> 0.63-0.72 mol/g

SOLUTION
-- -------------------------------------------------

EQUIL
-- Datum depth (m) | P @ datum depth (bar) | WOC depth (m) | Oil-water Pc @ WOC (bar) | GOC depth (m) | Gas-oil Pc @ GOC (bar) | RSVD table | RVVD table
  1013.1 140 1020 0 1000.3 0 1 0 0/

RSVD
1000 0
1010 0
1100 0
1128 0/

SUMMARY
-- -------------------------------------------------

-- Print out all commonly used data
ALL

-- Print cumulative CPU usage at different time steps 
TCPU

SCHEDULE
-- -------------------------------------------------

RPTSCHED
  'DENS' /

-- Print out restart files
RPTRST
  BASIC=2 /

DRSDT
  1 ALL/
DRSDTCON
  99.99/

TSTEP
31 28 31 30 31 30 31 31 30 31 30 31 
31 28 31 30 31 30 31 31 30 31 30 31 /

DATES
   1 'JAN' 2025 /
   1 'JAN' 2026 /
   1 'JAN' 2027 /
   1 'JAN' 2028 /
   1 'JAN' 2029 /
   1 'JAN' 2030 /
   1 'JAN' 2031 /
   1 'JAN' 2032 /
   1 'JAN' 2033 /
   1 'JAN' 2034 /
   1 'JAN' 2035 /
   1 'JAN' 2036 /
   1 'JAN' 2037 /
   1 'JAN' 2038 /
   1 'JAN' 2039 /
   1 'JAN' 2040 /
   1 'JAN' 2041 /
   1 'JAN' 2042 /
   1 'JAN' 2043 /
   1 'JAN' 2044 /
   1 'JAN' 2045 /
   1 'JAN' 2046 /
   1 'JAN' 2047 /
   1 'JAN' 2048 /
   1 'JAN' 2049 /
   1 'JAN' 2050 /
   1 'JAN' 2051 /
   1 'JAN' 2052 /
   1 'JAN' 2053 /
   1 'JAN' 2054 /

DATES
   1 'JAN' 2055 /
   1 'JAN' 2059 /
   1 'JAN' 2063 /
   1 'JAN' 2067 /
   1 'JAN' 2072 /
   1 'JAN' 2074 /
   1 'JAN' 2080 /

DATES
   1 'JAN' 2090 /
   1 'JAN' 2100 /
   1 'JAN' 2110 /
   1 'JAN' 2120 /
   1 'JAN' 2130 /
   1 'JAN' 2140 /
   1 'JAN' 2150 /

DATES
   1 'JAN' 2250 /
   1 '

