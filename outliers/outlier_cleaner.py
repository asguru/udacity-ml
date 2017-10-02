#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """


    errors = []
    prediction = []
    age = []
    net_worth = []

    for i in range(len(predictions)):
        error = (net_worths[i] - predictions[i]) ** 2
        errors.append(error)
        prediction.append(predictions[i])
        age.append(ages[i])
        net_worth.append(net_worths[i])



    indices = []
    for i in range(int(0.1 * len(predictions))):
        tmp = max(errors)
        tmp2 = errors.index(tmp)
        errors.pop(tmp2)
        prediction.pop(tmp2)
        age.pop(tmp2)
        net_worth.pop(tmp2)


    cleaned_data = []

    for i in range(len(age)):
        cleaned_data.append([age[i], net_worth[i], errors[i]])


    ### your code goes here

    
    return cleaned_data

