import excelextraction
import preprocessing
import excelupload
import constants


#Extract Raw data
AppRawData=excelextraction.openAppWorkbook()
HBIMRawData=excelextraction.openHBIMWorkbook()

#Extract Relevant Raw data
AppRelRawData, HBIMRelRawData = preprocessing.extractDataCols(AppRawData,HBIMRawData)

#Concatenate Data
AppConcatRawData, HBIMConcatRawData = preprocessing.concatenateDataCols(AppRelRawData,HBIMRelRawData)

#Replace Special Chars
AppProcData, HBIMProcData = preprocessing.replaceSpecialChars(AppConcatRawData,HBIMConcatRawData)

#Stem, Remove stop words and tokenize
vectAppList, vectHBIMList = preprocessing.stemAndTokenize(AppProcData,HBIMProcData)

#Perform comparison matching
AppHBIMMap = preprocessing.compare(vectAppList,vectHBIMList)

#write results back to excel
excelupload.writeDataCols(AppHBIMMap, HBIMRawData)