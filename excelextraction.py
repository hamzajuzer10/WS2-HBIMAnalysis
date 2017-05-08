from xlrd import open_workbook
import constants
import sys


def openAppWorkbook():
    """Open application specification excel book """
    print 'opening Application Specification Workbook...(this can take a while)'
    try:
        book = open_workbook(constants.app_workbook_name)
    except:
        print 'unable to find or open app workbook...'
        print 'program is exiting...'
        sys.exit(0)

    print 'extracting data from Application Specification Workbook...'

    #Extract data from the Excel Spreadsheet
    #Open excel sheet
    sheet = book.sheet_by_name(constants.app_sheet_name)

    #Read header values into the list
    keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

    #Add values to dictionary and append to list
    dict_list = []
    for row_index in xrange(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value
             for col_index in xrange(sheet.ncols)}
        dict_list.append(d)

    return dict_list


def openHBIMWorkbook():
    """Open HBIM excel book """
    print 'opening HBIM Model Workbook...(this can take a while)'
    try:
        book = open_workbook(constants.HBIM_workbook_name)
    except:
        print 'unable to find or open HBIM workbook...'
        print 'program is exiting...'
        sys.exit(0)

    print 'extracting data from HBIM Model Workbook...'

    #Extract data from the Excel Spreadsheet
    #Open excel sheet
    sheet = book.sheet_by_name(constants.HBIM_sheet_name)

    #Read header values into the list
    keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

    #Add values to dictionary and append to list
    dict_list = []
    for row_index in xrange(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value
             for col_index in xrange(sheet.ncols)}
        dict_list.append(d)

    return dict_list