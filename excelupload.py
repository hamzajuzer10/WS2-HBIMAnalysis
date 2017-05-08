from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import constants
import sys


#write to excel file
def writeDataCols(AppHBIMMap, HBIMRawData):
    """write data to excel file"""

    print 'writing to output workbook...'
    rb = open_workbook(constants.app_workbook_name, formatting_info=True)
    wb = copy(rb)  # a writable copy (I can't read values out of this, only write to it)
    classification_sheet = wb.get_sheet(0)  # sheet with classification results

    col_index = constants.app_start_col
    classification_sheet.write(0, col_index, "Possible HBIM Data Elements")

    for i in range(0,len(AppHBIMMap)):

        row_index = constants.app_start_row + i

        k=0
        for j in AppHBIMMap[i]:

            col_index = constants.app_start_col + k

            k = k + 1

            classification_sheet.write(row_index, col_index,HBIMRawData[j]['Name'])

    wb.save(constants.output_workbook_name)

    print 'completed writing to output workbook...'