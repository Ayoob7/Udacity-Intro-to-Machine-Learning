#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    tempStore = []

    for element in zip(predictions,ages,net_worths):
        error = element[0][0] - element[2][0]
        strnb = element[1][0],element[2][0],error
        tempStore.append(strnb)

    sortList = []
    for e in sorted(tempStore, key=lambda line: line[2]):
        sortList.append(e)
    for i in sortList:
        print i

    cleaned_data = sortList[0:80]

    ### your code goes here

    
    return cleaned_data

