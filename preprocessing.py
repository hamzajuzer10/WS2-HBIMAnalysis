import excelextraction
import constants
import re
import nltk
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

stemmer = PorterStemmer()

def extractDataCols(RawDataDictApp,RawDataDictHBIM):
    """Extract relevant data columns"""

    print 'extracting relevant data columns for App and HBIM data...'

    dataApp = []
    for item in RawDataDictApp:
        temp = []

        for label in constants.AppLabels:
            temp.append(item[label])

        dataApp.append(temp)

    dataHBIM = []
    for item in RawDataDictHBIM:
        temp = []

        for label in constants.HBIMLabels:
            temp.append(item[label])

        dataHBIM.append(temp)

    return dataApp, dataHBIM

def concatenateDataCols(RawDataDictApp,RawDataDictHBIM):
    """Concatenate data in lists"""

    print 'concatenating relevant App and HBIM data...'

    dataApp = []
    for item in RawDataDictApp:
        dataApp.append(' '.join(item))

    dataHBIM = []
    for item in RawDataDictHBIM:
        dataHBIM.append(' '.join(item))

    return dataApp, dataHBIM

def replaceSpecialChars(RawDataDictApp,RawDataDictHBIM):
    """Replace all special characters"""

    print 'replacing special characters in App and HBIM data with' + " ' '..."

    dataApp = []
    for original_string in RawDataDictApp:
        new_string = re.sub('[^a-zA-Z0-9\n\.]', ' ', original_string)
        dataApp.append(new_string.lower())

    dataHBIM = []
    for original_string in RawDataDictHBIM:
        new_string = re.sub('[^a-zA-Z0-9\n\.]', ' ', original_string)
        dataHBIM.append(new_string.lower())

    return dataApp, dataHBIM

# based on http://www.cs.duke.edu/courses/spring14/compsci290/assignments/lab02.html
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems


def stemAndTokenize(RawDataDictAppList,RawDataDictHBIMList):
    """Remove all stop words, stem the words and tokenize"""

    print 'stemming and tokenizing App and HBIM data...'
    #nltk.download()

    vectAppList = []
    for item in RawDataDictAppList:
        vectApp = CountVectorizer(tokenizer=tokenize, stop_words='english')

        #process App Raw Data
        vectApp.fit([item])
        vectAppList.append(vectApp)
        #print('Vocabulary: %s' %vectApp.get_feature_names())

    vectHBIMList = []
    for item in RawDataDictHBIMList:
        vectHBIM = CountVectorizer(tokenizer=tokenize, stop_words='english')

        # process HBIM Raw Data
        vectHBIM.fit([item])
        vectHBIMList.append(vectHBIM)
        #print('Vocabulary: %s' % vectHBIM.get_feature_names())

    return vectAppList, vectHBIMList

def compare(vectAppList,vectHBIMList):
    """compare the app and HBIM vocab list"""

    print 'comparing datasets...'
    AppHBIMMap = []

    for Appitem in vectAppList:

        Appset = set(Appitem.get_feature_names())

        mappinglist = []
        orderlist = []

        for i in range(len(vectHBIMList)):

            HBIMset = set(vectHBIMList[i].get_feature_names())

            intersection = len(Appset & HBIMset)

            if intersection>=constants.minMatchSize:

                mappinglist.append(i)
                orderlist.append(intersection)

        if mappinglist and orderlist:
            orderlistNew, mappinglistNew = zip(*sorted(zip(orderlist, mappinglist), reverse=True))
            AppHBIMMap.append(mappinglistNew[:constants.maxOutputSize])

        else:
            AppHBIMMap.append(mappinglist[:constants.maxOutputSize])

    #re-order elements

    return AppHBIMMap