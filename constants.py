#All configurable settings and constants go here

#Application Specification Workbook
app_workbook_name = 'Data/TabularViewSpecDraft.xls'
app_sheet_name = 'TabularViewSpecDraft'

#Application Specification Workbook - cols to write data to
app_start_row = 1  # 0 based (subtract 1 from excel row number)
app_start_col = 5  # 0 based - corresponds to col X

#Output directory
output_workbook_name = 'Data/output.xls'

#HBIM Model Workbook
HBIM_workbook_name = 'Data/HBIMDataElement.xls'
HBIM_sheet_name = 'Sheet0'

#Labels for each Workbook dataset
AppLabels = ('Data Element','Description','Data Set')
HBIMLabels = ('Name','Definition (No Formatting)','Is Property Of [HBIM Data Concept] > HBIM Data Concept')

minMatchSize = 1 #minimum number of matches
maxOutputSize = 25 #maximum number of results