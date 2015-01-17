#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    pred_errors = abs(predictions - net_worths)
    import heapq
    worst_9 = heapq.nlargest(9,pred_errors)[-1][0]

    
    cleaned_data = []

    ### your code goes here
    for ind in range(0,len(predictions)):
        if pred_errors[ind] < worst_9:
            cleaned_data.append([ages[ind][0],net_worths[ind][0],pred_errors[ind][0]])       
    
    return cleaned_data

