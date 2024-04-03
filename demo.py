# coding:utf-8
from datetime import datetime
from mondrian import mondrian
from utils.read_file import read_csv

ATT_NAME = ["encounter_id", "patient_nbr","race","gender","age","weight","admission_type_id","discharge_disposition_id","admission_source_id",
            "time_in_hospital","payer_code","medical_specialty","num_lab_procedures","num_procedures",
            "num_medications", "number_outpatient","number_emergency","number_inpatient","diag_1","diag_2",
            "diag_3","number_diagnoses","max_glu_serum","A1Cresult","metformin","repaglinide","nateglinide",
            "chlorpropamide","glimepiride","acetohexamide","glipizide","glyburide","tolbutamide","pioglitazone",
            "rosiglitazone","acarbose","miglitol","troglitazone","tolazamide","examide","citoglipton","insulin",
            "glyburide-metformin","glipizide-metformin","glimepiride-pioglitazone","metformin-rosiglitazone",
            "metformin-pioglitazone","change","diabetesMed","readmitted"]

QI_INDEX = [0,1,2]
IS_CAT = [False, False, True]
IS_DATETIM = [False, False, False]
SA_INDEX = 11
DATA, INTUITIVE_ORDER = read_csv(file_path="diabetic_data.csv",QI_INDEX=QI_INDEX, IS_CAT=IS_CAT, IS_DATETIME= IS_DATETIM, SA_INDEX=SA_INDEX, header=True)
result, eval_result = mondrian(DATA, 40, False)
print(result)
