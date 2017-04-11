# -*- coding: utf-8 -*-
"""
Project 2
Author: Keenen Francois-King
-See README for more information.
"""

import matplotlib.pyplot as plt


f = open('hour_test_1.txt')

text = f.readlines()

sat = []
sat_id = []
time = []
sig_strength = []
azimuth = []
elevation = []
date = []

#go through file and return all possible GPS id numbers
for line in text:
    check_line = line.split(',')
    if check_line[0] == '$GPGSV':
        try:
            sat.append([check_line[4]])
        except (ValueError, IndexError):
            continue
    else: 
        continue

#delete recurring satellite id numbers in sat and contain each unique number in a list
for i in sat:
    if i not in sat_id:
        sat_id.append(i)
    else:
        continue

#go through file and put each measurement of GPGSV in a list that
#contains SNR val, time, and satellite id

current_time = None

for line in text:
    check_line = line.split(',')
    
    #$GPGGA gives the current timestamp and after it comes the $GPGSV which contains
    #the SNR value.  Store the timestamp as current_time so that SNR can later be 
    #plotted against time
    
    if check_line[0] == '$GPGGA':
        current_time = float(check_line[1])
    
    #append 2-item long lists containing time and SNR value to corresponding satellite's list
    elif check_line[0] == '$GPGSV':
        for j in sat_id:
            #check satellite ID so we can put the SNR and time list into that satellite's list
            if int(j[0]) == int(check_line[4]):
                try:
                    j.append([current_time, int(check_line[7])])
                except (ValueError, IndexError):
                    continue
            else:
                continue
    else:
        continue

#timestamps for a satellite  
x_vals = []
#SNR vals for a satellite
y_vals = []

#look at the list for one satellite
for x in sat_id:  
    #split data for one satellite into time (x-axis) and SNR (y-axis)
    for y in x[1:]:
        try:
            x_vals.append(y[0])
            y_vals.append(y[1])
        except (ValueError, IndexError):
            continue
        
    #plot data for one satellite. Greater than zero so that satellites with no SNR vals aren't plotted
    if (len(x_vals) > 0) and (len(y_vals) > 0):
        plt.figure(figsize = (10,5))
        #I saved the first item in each list in sat_id as the ID for that satellite.
        plt.title('Satellite ' + x[0], fontsize=15, fontweight='bold')
        plt.ylabel('SNR (C/N0)', fontsize=10)
        plt.xlabel('Time [UTC] (hhmmss)', fontsize=10)
        
        plt.ylim([(min(y_vals)-1),(max(y_vals)+1)])
        
        #plot the times and SNR vals that were taken from the sat_id list for a 
        #given satellite
        plt.scatter(x_vals[:], y_vals[:], s=.5) 
        
        locs,labels = plt.xticks()
        plt.xticks(locs, map(lambda x: "%.1f" % x, locs))
        plt.show()

        #empty x_vals and y_vals so the next satellite data can be plotted
        x_vals = []
        y_vals = []

    else:
        continue
