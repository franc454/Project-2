# Project-2
SNR values from GPS readings recorded in a txt document and then plotted in a PDF.

Using the Ultimate GPS by Adafruit and a datalogger by Eltima Software, txt documents 
containing the output data from the GPS could be saved.  These files contain (but aren't
limited to) data such as the time, satellite ID and SNR (C/N0) value received.  The 
SNR value is a measure of signal strength that can be compared above and below a 
snowpack in order to determine the snow water equivalent of that snowpack.  Here, 
I read the txt document generated over a given period of time for one Ultimate GPS.  I 
find all of the satellite IDs for the satellites that are recorded and separate each 
into their times and corresponding SNR values.  These are then plotted against
eachother in a separate plot for each satellite.  The plots are all combined into a PDF
which is saved in the same directory as the python script and txt files.

There are 2 txt documents included.  They are hour_test_1.txt and hour_test_2.txt.  Let me 
know if you would like more uploaded.

Change the 'name' variable at the beginning of the script to what the name of your txt file
is.  The script will then read the file and save a PDF of the plots under the same name.
Example:  if the file I want to read is 'hour_test_1.txt', set name to 'hour_test_1'.  The
          PDF file of the plots will be saved as 'hour_test_1.pdf.

Author: Keenen Francois-King
