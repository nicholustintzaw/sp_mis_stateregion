#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 07:55:42 2019

@author: nicholustintzaw
"""


####################################################################################################
'''
project tite    :           social pension database - national level
purpose         :           quaterly data combine and check - combined all new quarter datasheet
developed by    :           Nicholus Tint Zaw             
modified date   :           7th Dec 2019

follow-up action:
    
'''
####################################################################################################
####################################################################################################

print('Now, the spyder is preparing for youre state and region combined report, please wait for a few minutes')

## STEP 1: EXPORT ALL NEW QUARTER SHEETS IN ONE EXCEL FILE ##

#sheet = ['01_new_register', '02_moved_in', '03_false_death_in', '04_death', '05_moved_out', '06_false_register']

    
writer = pd.ExcelWriter(report + region + '_' + qrt + 'combined_updated_report.xlsx', engine = 'xlsxwriter')

df_newreg.to_excel(writer, sheet_name = '01_new_register')

df_movein.to_excel(writer, sheet_name = '02_moved_in')

df_falsed.to_excel(writer, sheet_name = '03_false_death_in')

df_death.to_excel(writer, sheet_name = '04_death')

df_moveout.to_excel(writer, sheet_name = '05_moved_out')

df_falsereg.to_excel(writer, sheet_name = '06_false_register')
    
writer.save()
writer.close()
    



####################################################################################################
####################################################################################################

print('Woow, just finished all the steps involved in data quality check and please check the result in outputs folder and combined folder')



