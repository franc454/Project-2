# Project-2
SNR values from GPS readings recorded in a CSV File and then plotted.

Using the Ultimate GPS by Adafruit and a datalogger by Eltima Software, CSV files 
containing the output data from the GPS could be saved.  These files contain (but aren't
limited to) data such as the time, satellite ID and SNR (C/N0) value received.  The 
SNR value is a measure of signal strength that can be compared above and below a 
snowpack in order to determine the snow water equivalent of that snowpack.  Here, 
I read the CSV file generated over a given period of time for one Ultimate GPS.  I 
find all of the satellite Ids for the satellites that are recorded and separate each 
into their times and corresponding SNR values.  These are then plotted against
eachother in a separate plot for each satellite.

There are 2 CSV files included.  They are hour_test_1.csv and hour_test_2.csv.  Let me 
know if you would like more uploaded.

Author: Keenen Francois-King
