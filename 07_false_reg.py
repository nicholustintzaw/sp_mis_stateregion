#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 07:55:42 2019

@author: nicholustintzaw
"""


####################################################################################################
'''
project tite    :           social pension database - national level
purpose         :           quaterly data combine and check - false register
developed by    :           Nicholus Tint Zaw             
modified date   :           7th Dec 2019

follow-up action:
    
'''
####################################################################################################
####################################################################################################

print('Now, the spyder is working on False Register Sheet, please wait for a few minutes')


## STEP 2: APPLICATION PACKAGE SETTING ##
## package setting ##

import pandas as pd
import numpy as np


####################################################################################################

# columns name assignment

col_na = ['benef_id']


col_names = ['No.', 'benef_id', 'Benef: Name']


col_person = ['Benef: Name']


#sheet = ['01_new_register', '02_moved_in', '03_false_death_in', '04_death', '05_moved_out', '06_false_register']




####################################################################################################
####################################################################################################

## STEP 3: COMBINED ALL COMPLETED DATA MIGRATION FIELS ##
## Combined data from each office

df = pd.DataFrame()  

i = 1

files = os.listdir(raw)
 

for xlsx in files :
    if xlsx.endswith(".xlsx"):
        print(i)
        print("now working in " + xlsx)

            
        dta = pd.read_excel(raw  + xlsx, sheet_name = '06_false_register', \
                            skiprows = 3, header = None, index_col = False, usecols="A:C", names = col_names)
        
        
        # drop na from selected main variables
        dta = dta.dropna(how = 'all', subset = col_na)
        
        #dta['geo_township'] = geo_township
        dta.sort_values('benef_id')
        
        source = xlsx
        dta['source'] = source
        
    
        df = df.append(dta)
        
        i = 1 + i

df_falsereg = df

####################################################################################################
####################################################################################################

## STEP 4: SUMMARY STATISTIC FOR DATA MIGRATION FILES ##

# use as different dataset name for summary stat figures
df_test = df

obs = len(df_test.index)
if obs > 0 :

    
    # myanmar fount zero and wa lone replacement
    df_test['benef_id'] = df_test['benef_id'].astype(str)
    
    df_test['benef_id'] = df_test['benef_id'].str.replace('ဝ', '၀')
      
    # english numeric to Myanmar numeric convertion
    df_test['benef_id'] = df_test['benef_id'].str.replace('0', '၀')
    df_test['benef_id'] = df_test['benef_id'].str.replace('1', '၁')
    df_test['benef_id'] = df_test['benef_id'].str.replace('2', '၂')
    df_test['benef_id'] = df_test['benef_id'].str.replace('3', '၃')
    df_test['benef_id'] = df_test['benef_id'].str.replace('4', '၄')
    df_test['benef_id'] = df_test['benef_id'].str.replace('5', '၅')
    df_test['benef_id'] = df_test['benef_id'].str.replace('6', '၆')
    df_test['benef_id'] = df_test['benef_id'].str.replace('7', '၇')
    df_test['benef_id'] = df_test['benef_id'].str.replace('8', '၈')
    df_test['benef_id'] = df_test['benef_id'].str.replace('9', '၉')

           
    # keep one state/region
    df_state = df_test
    
    # count the number of obs
    tot = len(df_state.index)
    
    d_i = {'Total False REgister': [tot]}
    
    dta_i = pd.DataFrame(d_i)
    sum_state = dta_i
    
    
    ## STEP 5: DATA QUALITY CHECK ##
    
    ## Duplicated Observation 
    
    # duplicate by beneficiares info - booleen var + ID
    dup_resp = df_test.duplicated(subset = col_person, keep = False)
    dup_id = df_test.duplicated(subset = 'benef_id', keep = False)
    
    # duplciate by id and beneficiares info dataset + ID duplicate
    dup_resp = df_test.loc[dup_resp == True]
    dup_id = df_test.loc[dup_id == True]
    
    
    # dup respondent info
    obs = len(dup_resp)
    if obs > 0 :    
        
        i = 1
        dup_state = pd.DataFrame()

            
        for state in states :

            
            # count the number of obs
            tot = len(dup_resp.index)
            
            d_i = {'Total Person Duplicate': [tot]}
            
            dta_i = pd.DataFrame(d_i)
            dup_state = dta_i
            

        
    # dup benef id
    obsid = len(dup_id)
    if obsid > 0 :    
        
        i = 1
        dupid_state = pd.DataFrame()
        
            
        for state in states :
   
            # count the number of obs
            tot = len(dup_id.index)
            
            d_i = {'Total ID Duplicate': [tot]}
            
            dta_i = pd.DataFrame(d_i)
            dupid_state = dta_i
            

                 
    # export as summary statistic figures for all combined data migration files 
    #dup_resp.to_excel(output + qrt + '_dup_person.xlsx', index = False)
    
    writer = pd.ExcelWriter(output + region + '_' + qrt + '_false_register_check.xlsx', engine = 'xlsxwriter')
    sum_state.to_excel(writer, sheet_name = 'District')
    
    obs = len(dup_resp)
    if obs > 0 : 
        dup_state.to_excel(writer, sheet_name = 'dupli_person_stateregion')
        dup_resp.to_excel(writer, sheet_name = 'dupli_person_list')
    
    obsid = len(dup_id)
    if obsid > 0 : 
        dupid_state.to_excel(writer, sheet_name = 'dupli_id_stateregion')
        dup_id.to_excel(writer, sheet_name = 'dupli_id_list')
    writer.save()
    writer.close()
    



####################################################################################################
####################################################################################################


print('Woow, just finished the False Register Sheet checking, please check your outputs folder for result excel files')


