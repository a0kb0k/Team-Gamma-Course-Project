EN.535.610 Computational Methods of Analysis

Course Project: Thermal Simulation of PCBs and Heatsinks
    
Created By: David Baltazar and Diego Ortiz
Credits To: Daniel Silva for the 'heatrapy' module that helped to run this script. (https://github.com/djsilva99/heatrapy/wiki)

The main purpose of this script is to be able to conduct a thermal analysis on a PCB by seeing the cooling effects that different heat sinks have on a PCB with actively powered components on board. The script calculates the heat fluxes and temperature distributions of the heatsinks, calculates effective PCB material properties, models the heat flux that different electrical components apply to the board, then generates a temeprature plot of the PCB to calculate thermal margins. More information on each of these topics are described in the markdowns of the Jupyter script called 'Team_Gamma_Course_Project'.

Please note that the main script for running Team Gamma's Course Project is inside of the another repository called 'heatrapy' (credited and mentioned in the report, as well) in order to run the program. There were some difficulties installing the 'heatrapy' module on our computers, and the easiest way for us to import the library into our code was by creating the script inside of the actual directory itself. 
