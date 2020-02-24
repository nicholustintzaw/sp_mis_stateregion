#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:28:44 2019

@author: nicholustintzaw
"""


####################################################################################################
####################################################################################################
'''
project tite    :           social pension database - national level
purpose         :           data migration national social pension data check and summary statistics
developed by    :           Nicholus Tint Zaw             
modified date   :           3rd Dec 2019

follow-up action:
    
'''
####################################################################################################
####################################################################################################


### PLEASE, CHANGE YOUR DIRECTORY BELOW ###
masterdir = r'C:\Users\Age.ing\Dropbox\01_Eligable\_New_QRT_COMBINE_CHECK_Window'


### PLEASE, CHANGE THE CASH TRANSFER BUDGET YEAR QUARTER BELOW ###
qrt = '1st_qrt_2019_2020'




####################################################################################################
####################################################################################################
################ PLEASE, DON'T TOUCH ANY PYTHON CODES BELOW ########################################
####################################################################################################
####################################################################################################




####################################################################################################
### task 1: prepare the directory setting
####################################################################################################

import os
os.chdir(masterdir)

exec(open("01_newqs_directory.py", 'r', encoding="utf8").read())



####################################################################################################
### task 2: combined all completed new quarter files
####################################################################################################

     
## IN

# 02_new_register
exec(open("02_new_register.py", 'r', encoding="utf8").read())

# 03_moved_in
exec(open("03_moved_in.py", 'r', encoding="utf8").read())

# 04_false_death
exec(open("04_false_death.py", 'r', encoding="utf8").read())



# OUT
# 05_death
exec(open("05_death.py", 'r', encoding="utf8").read())

# 06_moved_out
exec(open("06_moved_out.py", 'r', encoding="utf8").read())

# 07_false_reg
exec(open("07_false_reg.py", 'r', encoding="utf8").read())


# COMBINED REPORT
# State and Region level combined
exec(open("08_combined_report.py", 'r', encoding="utf8").read())


####################################################################################################
