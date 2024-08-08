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

   Follow the steps on the [https://opm-project.org/?page_id=245) or watch videos provided by Carl Fredrik Berg to easily set up OPM Flow on your Linux system.

2. **Windows systems:**

   To install the OPM Flow simulator on Windows systems, you can use either a Virtual Machine or Windows Subsystem for Linux (WSL).

   **Virtual Machine:**

   Although you can find the complete instructions on the webpage provided by Allan Katende, generally you should follow these steps:

   a) Download and install a VM platform like VirtualBox or VMware.

   b) Download a Linux ISO of your preferred distribution (e.g., Ubuntu).

   c) Create a new VM and follow the prompts to install the Linux OS using the ISO file.

   d) Once installed, follow the instructions in the video provided by Carl Fredrik Berg.

   **Windows Subsystem for Linux (WSL):**

   If you want to use WSL, follow these steps:

   a) Enable WSL via PowerShell (as Administrator): 
      ```sh
      wsl --install
      ```

   b) Follow the prompts to restart your computer if necessary.

   c) Install a Linux distribution from the Microsoft Store (e.g., Ubuntu).

   d) Once installed, follow the instructions in the video provided by Carl Fredrik Berg.

### ResInsight

To visualize the simulation results, you need to install ResInsight. Follow the instructions on the [ResInsight website](https://resinsight.org/getting-started/download-and-install/windows-installation/) to download and install the software.

### Python

Ensure Python is installed on your system. You can download it from [Python.org](https://www.python.org/downloads/). Additionally, install the necessary Python libraries using the following command:
```sh
pip install -r requirements.txt
