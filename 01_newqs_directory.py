#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 07:55:42 2019

@author: nicholustintzaw
"""


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


## STEP 1: DIRECTORY SETTING ##
## directory setting
import getpass
username = getpass.getuser()  # identify the user

print('this program is currently using from username ', username)

raw     =   os.path.join(masterdir,'_raw/')
output  =   os.path.join(masterdir,'_outputs/')
report  =   os.path.join(masterdir,'_combined/')



          
####################################################################################################
####################################################################################################
