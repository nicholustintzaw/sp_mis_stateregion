#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 07:55:42 2019

@author: nicholustintzaw
"""


####################################################################################################
'''
project tite    :           social pension database - national level
purpose         :           quaterly data combine and check - new registration
developed by    :           Nicholus Tint Zaw             
modified date   :           7th Dec 2019

follow-up action:
    
'''
####################################################################################################
####################################################################################################

print('Now, the spyder is working on New Register Sheet, please wait for a few minutes')

## STEP 2: APPLICATION PACKAGE SETTING ##
## package setting ##

import pandas as pd
import numpy as np


####################################################################################################

# columns name assignment

col_na = ['State/Region Name', 'District Name', 'Township Name', 'Benef: Name',
       'Benef: Gender']

'''
['geo_state_region', 'cal_region', 'state_region_code',
       'geo_district', 'cal_district', 'Township Name', 'cal_dist_town',
       'cal_town', 'township_code', 'Rural or Urban',
       'Beneficiaries Reg. No.', 'benef_id']
'''


col_names = ['No.', 'State/Region Name', 'District Name', 'Township Name',
       'Rural or Urban', 'Ward', 'Village Tract', 'Village',
       'Address Detail', 'Beneficiaries Reg. No.',
       'benef_id', 'eao_yesno', 'eao_name', 'Benef: Name',
       'Benef: Gender', 'DOB Type', 'Benef: DOB Myanmar', 'Cal_DOB_MM_ENG',
       'Correct Calculation', 'Correct DOB MM to ENG', 'Benef: DOB Day',
       'Benef: DOB Month', 'Benef: DOB Year', 'Benef: DOB',
       'Enrollment End: Day', 'Enrollment End: Month', 'Enrollment End: Year',
       'Enrollment End Date', 'Age in Years', 'Age Verification Doc',
       'NRC Format', 'NRC old - Text', 'NRC old - Digits', 'NRC Old',
       'NRC - Region Code', 'cal_nrc_region', 'NRC - Township Code',
       'NRC Status', 'NRC - Digits', 'NRC New', 'Benef: Father Name']


col_person = ['Benef: Name', 'Benef: Gender', 'Age in Years', 'Benef: Father Name']


'''
['sr_no', 'geo_state_region', 'cal_region', 'state_region_code',
       'geo_district', 'cal_district', 'Township Name', 'cal_dist_town',
       'cal_town', 'township_code', 'Rural or Urban', 'Ward', 'Village Tract',
       'geo_village', 'Address Detail',
       'Beneficiaries Reg. No.', 'benef_id', 'eao_yesno', 'eao_name',
       'benef_name', 'benef_gender', 'Day', 'Month', 'Year', 'DR', 'DR29S',
       'MR', 'MRS', 'YS', 'DOB1TAGU', 'benef_dob_mm', 'Cal_DOB_MM_ENG',
       'benef_age', 'Age Verification Doc', 'NRC Format', 'NRC old - Text',
       'NRC old - Digits', 'NRC Old', 'NRC - Region Code', 'cal_nrc_region',
       'NRC - Township Code', 'NRC Status', 'NRC - Digits', 'NRC New',
       'benef_father_name']

'''

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
        
        dta = pd.read_excel(raw  + xlsx, sheet_name = '01_new_register', \
                            skiprows = 3, header = None, index_col = False, usecols="A:AO", names = col_names)
        
        
        # drop na from selected main variables
        dta = dta.dropna(how = 'all', subset = col_na)
        
        #dta['geo_township'] = geo_township
        dta.sort_values('Township Name')
        
        source = xlsx
        dta['source'] = source
        
    
        df = df.append(dta)
        
        i = 1 + i

df_newreg = df

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
    
    
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].astype(str)
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('ဝ', '၀')
      
    # english numeric to Myanmar numeric convertion
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('0', '၀')
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('1', '၁')
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('2', '၂')
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('3', '၃')
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('4', '၄')
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('5', '၅')
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('6', '၆')
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('7', '၇')
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('8', '၈')
    df_test['Beneficiaries Reg. No.'] = df_test['Beneficiaries Reg. No.'].str.replace('9', '၉')

     # myanmar fount zero and wa lone replacement
    df_test['NRC - Digits'] = df_test['NRC - Digits'].astype(str)
    
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('ဝ', '၀')
    
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].astype(str)
    
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('ဝ', '၀')
    
    
    # english numeric to Myanmar numeric convertion
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('0', '၀')
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('1', '၁')
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('2', '၂')
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('3', '၃')
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('4', '၄')
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('5', '၅')
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('6', '၆')
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('7', '၇')
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('8', '၈')
    df_test['NRC - Digits'] = df_test['NRC - Digits'].str.replace('9', '၉')
    
    
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('0', '၀')
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('1', '၁')
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('2', '၂')
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('3', '၃')
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('4', '၄')
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('5', '၅')
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('6', '၆')
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('7', '၇')
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('8', '၈')
    df_test['NRC old - Digits'] = df_test['NRC old - Digits'].str.replace('9', '၉')
   
    # Male Burmese fount Standartization
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('ကျား ', 'ကျား')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('ကျား\xa0', 'ကျား')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('ကျား', 'ကျား')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('ကျးာ', 'ကျား')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('က', 'ကျား')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('ကျားျား', 'ကျား')
    
    
    # Female Burmese fount Standartization  
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('မ ', 'မ')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('မ\xa0', 'မ')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('မ', 'မ')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('\u200bမ', 'မ')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('မ ', 'မ')
       
    
    
    # to apply loop function to generate stat figure at district level
    states = df_test['District Name'].unique() 
    
    i = 1
    sum_state = pd.DataFrame()
    
    j = 1
    sum_town = pd.DataFrame()
    
    regions = df_test['State/Region Name'].unique() 
        
    for region in regions : 
                
        for state in states :
            
            # keep one state/region
            df_state = df_test.loc[df_test['District Name'] == state]
            
            # count the number of obs
            tot = len(df_state.index)
            xx = df_state['Benef: Gender'] == 'ကျား'
            xy = df_state['Benef: Gender'] == 'မ'

            
            xx = df_state.loc[xx == True]
            xy = df_state.loc[xy == True]
            
            male = len(xx.index)
            female = len(xy.index)
            
            d_i = {'District Name': [state], 'Total New Register': [tot], 'Male': [male], 'Female': [female]}
            
            dta_i = pd.DataFrame(d_i)
            sum_state = sum_state.append(dta_i)
            
            # prepare for the township level figure
            towns = df_state['Township Name'].unique() 
            
        
            
            for town in towns :
                
                # keep one township
                df_town = df_state.loc[df_state['Township Name'] == town]
                
                # count the number of obs
                tot = len(df_town.index)
                
                xx = df_town['Benef: Gender'] == 'ကျား'
                xy = df_town['Benef: Gender'] == 'မ'

                xx = df_town.loc[xx == True]
                xy = df_town.loc[xy == True]
                
                tmale = len(xx.index)
                tfemale = len(xy.index)
                
                            
                d_j = {'District Name': [state], 'Township Name': [town],'Total New Register': [tot],  'Male': [tmale], 'Female': [tfemale]}
                
                dta_j = pd.DataFrame(d_j)
                sum_town = sum_town.append(dta_j)
                    
    
    
    ## STEP 5: DATA QUALITY CHECK ##
    
    ## Age Criteria Check
    age = df_test['Age in Years'] < 85
    age = df_test.loc[age == True]
    
    # age not meet
    obs = len(age)
    if obs > 0 :    
        
        i = 1
        age_state = pd.DataFrame()
        
        j = 1
        age_town = pd.DataFrame() 
            
        for state in states :
            
            # keep one state/region
            df_state = age.loc[age['District Name'] == state]
            
            # count the number of obs
            tot = len(df_state.index)
            
            d_i = {'District Name': [state], 'Total < 85 years old': [tot]}
            
            dta_i = pd.DataFrame(d_i)
            age_state = age_state.append(dta_i)
            
            # prepare for the township level figure
            towns = df_state['Township Name'].unique() 
            
        
            
            for town in towns :
                
                # keep one township
                df_town = df_state.loc[df_state['Township Name'] == town]
                
                # count the number of obs
                tot = len(df_town.index)
                
                d_j = {'District Name': [state], 'Township Name': [town],'otal < 85 years old': [tot]}
                
                dta_j = pd.DataFrame(d_j)
                age_town = age_town.append(dta_j)
    
    
    
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
        
        j = 1
        dup_town = pd.DataFrame() 
            
        for state in states :
            
            # keep one state/region
            df_state = dup_resp.loc[dup_resp['District Name'] == state]
            
            # count the number of obs
            tot = len(df_state.index)
            
            d_i = {'District Name': [state], 'Total Person Duplicate': [tot]}
            
            dta_i = pd.DataFrame(d_i)
            dup_state = dup_state.append(dta_i)
            
            # prepare for the township level figure
            towns = df_state['Township Name'].unique() 
            
        
            
            for town in towns :
                
                # keep one township
                df_town = df_state.loc[df_state['Township Name'] == town]
                
                # count the number of obs
                tot = len(df_town.index)
                
                d_j = {'District Name': [state], 'Township Name': [town],'Total Person Duplicate': [tot]}
                
                dta_j = pd.DataFrame(d_j)
                dup_town = dup_town.append(dta_j)
        
    # dup benef id
    obsid = len(dup_id)
    if obsid > 0 :    
        
        i = 1
        dupid_state = pd.DataFrame()
        
        j = 1
        dupid_town = pd.DataFrame() 
            
        for state in states :
            
            # keep one state/region
            df_state = dup_id.loc[dup_id['District Name'] == state]
            
            # count the number of obs
            tot = len(df_state.index)
            
            d_i = {'District Name': [state], 'Total ID Duplicate': [tot]}
            
            dta_i = pd.DataFrame(d_i)
            dupid_state = dupid_state.append(dta_i)
            
            # prepare for the township level figure
            towns = df_state['Township Name'].unique() 
            
        
            
            for town in towns :
                
                # keep one township
                df_town = df_state.loc[df_state['Township Name'] == town]
                
                # count the number of obs
                tot = len(df_town.index)
                
                d_j = {'District Name': [state], 'Township Name': [town],'Total ID Duplicate': [tot]}
                
                dta_j = pd.DataFrame(d_j)
                dupid_town = dupid_town.append(dta_j)
        
           
    # export as summary statistic figures for all combined data migration files 
    #dup_resp.to_excel(output + qrt + '_dup_person.xlsx', index = False)
    
    writer = pd.ExcelWriter(output + region + '_' + qrt + '_newregister_check.xlsx', engine = 'xlsxwriter')
    sum_state.to_excel(writer, sheet_name = 'District')
    sum_town.to_excel(writer, sheet_name = 'Townships')
    
    obs = len(age)
    if obs > 0 : 
        age_state.to_excel(writer, sheet_name = 'age_issue_district')
        age_town.to_excel(writer, sheet_name = 'age_issue_township')
        age.to_excel(writer, sheet_name = 'age_issue_list')
    
    obs = len(dup_resp)
    if obs > 0 : 
        dup_state.to_excel(writer, sheet_name = 'dupli_person_district')
        dup_town.to_excel(writer, sheet_name = 'dupli_person_township')
        dup_resp.to_excel(writer, sheet_name = 'dupli_person_list')
    
    obsid = len(dup_id)
    if obsid > 0 : 
        dupid_state.to_excel(writer, sheet_name = 'dupli_id_district')
        dupid_town.to_excel(writer, sheet_name = 'dupli_id_township')
        dup_id.to_excel(writer, sheet_name = 'dupli_id_list')
    writer.save()
    writer.close()




####################################################################################################
####################################################################################################

print('Woow, just finished the New Register Sheet checking, please check your outputs folder for result excel files')



