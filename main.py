import DecisionTree
import Node
import NaiveBayes
<<<<<<< HEAD
import SVM
=======
#import SVM
>>>>>>> origin/master
from numpy import *

TrainingDataNum = 28000
TestDataNum = 2000
Target = 'income'
<<<<<<< HEAD


def predicitions():
    """
    Decision Tree:
    """
=======
def predicitions():

    """
    Decision Tree:
    """
>>>>>>> origin/master
    data, attributes = DecisionTree.readCVS('AdultCensus_cleaned.csv')
    trainingdata, testdata = DecisionTree.splitData(data, TrainingDataNum, TestDataNum)
    tree = DecisionTree.makeTree(trainingdata, attributes, Target, 0)
    print "generated decision tree"
    DecisionTree.predictions(testdata, tree, attributes)
<<<<<<< HEAD

    table, decisions, testData = NaiveBayes.training('AdultCensus_cleaned.csv', Target, TrainingDataNum, TestDataNum)
    print "generate naive bayes table"
    NaiveBayes.predictions(table, testData, decisions)

 #   print "generated SVM"
 #   SVM.classify()


=======

    table, decisions, testData = NaiveBayes.training('AdultCensus_cleaned.csv', Target, TrainingDataNum, TestDataNum)
    print "generate naive bayes table"
    NaiveBayes.predictions(table, testData, decisions)




"""
    # SVM learning
    print "generated SVM"

    ## step 1: load data
    print "step 1: load data..."
    dataSet = []
    labels = []
    fileIn = open('AdultCensus_cleaned SVM.csv')
    for line in fileIn.readlines():
        lineArr = line.strip().split('\t')
        feature = []
        feature.extend([float(lineArr[0][0]), float(lineArr[0][2])])
        if (lineArr[0][5] == "," ):
            feature.extend([float(lineArr[0][4])])
            feature.extend([float(lineArr[0][6])])
            if (lineArr[0][9] == "," ):
                feature.extend([float(lineArr[0][8])])
                feature.extend([float(lineArr[0][10]),float(lineArr[0][12]),
                               float(lineArr[0][14]),float(lineArr[0][16]),
                               float(lineArr[0][18]),float(lineArr[0][20])])

                dataSet.append(feature)
                labels.append(float(lineArr[0][22]))
            else:
                feature.extend([float(lineArr[0][8]) * 10 +
                                float(lineArr[0][9])])
                feature.extend([float(lineArr[0][11]),float(lineArr[0][13]),
                               float(lineArr[0][15]),float(lineArr[0][17]),
                               float(lineArr[0][19]),float(lineArr[0][21])])

                dataSet.append(feature)
                labels.append(float(lineArr[0][23]))
        else :
            feature.extend([float(lineArr[0][4]) * 10 + float(lineArr[0][5])])
            feature.extend([float(lineArr[0][7])])
            if (lineArr[0][10] == "," ):
                feature.extend([float(lineArr[0][9])])
                feature.extend([float(lineArr[0][11]),float(lineArr[0][13]),
                               float(lineArr[0][15]),float(lineArr[0][17]),
                               float(lineArr[0][19]),float(lineArr[0][21])])
                dataSet.append(feature)
                labels.append(float(lineArr[0][23]))
            else:
                feature.extend([float(lineArr[0][9]) * 10 +
                                float(lineArr[0][10])])
                feature.extend([float(lineArr[0][12]),float(lineArr[0][14]),
                               float(lineArr[0][16]),float(lineArr[0][18]),
                               float(lineArr[0][20]),float(lineArr[0][22])])
                dataSet.append(feature)

                labels.append(float(lineArr[0][24]))

    dataSet = mat(dataSet)
    labels = mat(labels).T
    train_x = dataSet[:10000, :]
    train_y = labels[:10000, :]
    test_x = dataSet[10100:10200, :]
    test_y = labels[10100:10200, :]

    print  dataSet[:10000, :]
    print  labels[:10000, :]

    ## step 2: training...
    print "step 2: training..."
    C = 0.6
    toler = 0.1
    maxIter = 5
    svmClassifier = SVM.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption=('linear', 0))

    ## step 3: testing
    print "step 3: testing..."
    accuracy = SVM.testSVM(svmClassifier, test_x, test_y)

    ## step 4: show the result
    print "step 4: show the result..."
    print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
#    SVM.showSVM(svmClassifier)
"""
>>>>>>> origin/master

import FPTreeBuilder
import FPTreeMiner


def associationAnalysis():
<<<<<<< HEAD
    transactions = [[]]
    formedTransactions = [[]]
=======
	transactions = [[]]
	formedTransactions = [[]]
	
	# customized training data
	file = open('AdultCensus_cleaned.csv')	
 	for line in file:
 	  	line = line.strip("\r\n")
 	  	transactions.append(line.split(',')[1:])
 	transactions.remove([])
 	headerList = transactions[0]
	for transaction in transactions:
		trans = []
		for i in range(len(transaction)):
			item = transaction[i]
			attributeName = headerList[i]
			trans.append(attributeName + ':' + item)
		formedTransactions.append(trans)
	formedTransactions = formedTransactions[2:]
				
	# since we got approximate 30,000 transaction, min support num can't be two small
	min_sup = 150
	headerTable = {}
	counts = []
  	
	targetItem1 = 'income:<=50K'
	targetItem2 = 'income:>50K'
  	
  	print('Using FP-Growth algorithm to find the frequent pattern in given census:')
	fpTreeBuilder = FPTreeBuilder.FPTreeBuilder(formedTransactions, min_sup, counts, headerTable)
	FPTreeMiner.FPTreeMiner(targetItem1, targetItem2, fpTreeBuilder.tree, min_sup, headerTable)
>>>>>>> origin/master

    # customized training data
    file = open('AdultCensus_cleaned.csv')
    for line in file:
        line = line.strip("\r\n")
        transactions.append(line.split(',')[1:])
    transactions.remove([])
    headerList = transactions[0]
    for transaction in transactions:
        trans = []
        for i in range(len(transaction)):
            item = transaction[i]
            attributeName = headerList[i]
            trans.append(attributeName + ':' + item)
        formedTransactions.append(trans)
    formedTransactions = formedTransactions[2:]

    # since we got approximate 30,000 transaction, min support num can't be two small
    min_sup = 150
    headerTable = {}
    counts = []

<<<<<<< HEAD
    targetItem1 = 'income:<=50K'
    targetItem2 = 'income:>50K'
=======
if __name__ == '__main__':
    predicitions()
    associationAnalysis()
>>>>>>> origin/master

    print('Using FP-Growth algorithm to find the frequent pattern in given census:')
    fpTreeBuilder = FPTreeBuilder.FPTreeBuilder(formedTransactions, min_sup, counts, headerTable)
    FPTreeMiner.FPTreeMiner(targetItem1, targetItem2, fpTreeBuilder.tree, min_sup, headerTable)




if __name__ == '__main__':
    predicitions()
    associationAnalysis()