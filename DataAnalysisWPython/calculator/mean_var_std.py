import numpy as np

def calculate(list):

    if(len(list) != 9):
        raise ValueError("List must contain nine numbers.")#raise an error if the list does not contain 9 numbers

    list2 = np.array(list).reshape(3, 3) 
    calculations = {}
    operations = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }

    for name, func in operations.items():
        #have to convert to types accrding to the test cases
        axis0 = func(list2, axis=0).tolist()
        axis1 = func(list2, axis=1).tolist()
        flatten = func(list2)
        axis0 = [float(x) if "deviation" in name or "mean" in name or "variance" in name else int(x) for x in axis0]
        axis1 = [float(x) if "deviation" in name or "mean" in name or "variance" in name else int(x) for x in axis1]
        flatten = float(flatten) if "deviation" in name or "mean" in name or "variance" in name else int(flatten) # whew this works 
        calculations[name] = [axis0, axis1, flatten]
    return calculations

# this was my first attempt but it was too long and not efficient so I retried


    # list2 = np.array(lst).reshape(3, 3)# reshape the list into a 3x3 matrix
    # if list2.shape != (3, 3):
    #     raise ValueError("List must contain nine numbers.")
    # axis1 = list2# get the first axis (rows)
    # axis2 = list2.T# get the second axis (columns)
    # flatten = list2.flatten()# flatten the list into a 1D array
    # #for mean
    # axis1mean = list(np.mean(axis1, axis=0))
    # axis1mean = [float(i) for i in axis1mean]
    # axis2mean = list(np.mean(axis2, axis=0))
    # axis2mean = [float(i) for i in axis2mean]
    # flattenmean = float(np.mean(flatten))
    # #for variance
    # axis1var = list(np.var(axis1, axis=0))
    # axis1var = [float(i) for i in axis1var]
    # axis2var = list(np.var(axis2, axis=0))
    # axis2var = [float(i) for i in axis2var]
    # flattenvar = float(np.var(flatten))
    # #for standard deviation
    # axis1std = list(np.std(axis1, axis=0))
    # axis1std = [float(i) for i in axis1std]
    # axis2std = list(np.std(axis2, axis=0))
    # axis2std = [float(i) for i in axis2std]
    # flattenstd = float(np.std(flatten))
    # #for max
    # axis1max = list(np.max(axis1, axis=0))
    # axis1max = [int(i) for i in axis1max]
    # axis2max = list(np.max(axis2, axis=0))
    # axis2max = [int(i) for i in axis2max]
    # flattenmax = int(np.max(flatten))
    # #for min
    # axis1min = list(np.min(axis1, axis=0))
    # axis1min = [int(i) for i in axis1min]
    # axis2min = list(np.min(axis2, axis=0))
    # axis2min = [int(i) for i in axis2min]
    # flattenmin = int(np.min(flatten))
    # #for sum
    # axis1sum = list(np.sum(axis1, axis=0))
    # axis1sum = [int(i) for i in axis1sum]
    # axis2sum = list(np.sum(axis2, axis=0))
    # axis2sum = [int(i) for i in axis2sum]
    # flattensum = int(np.sum(flatten))
    # #final calculations
    # # create a dictionary to hold the results
    # calculations = {
    #     "mean":[axis1mean, axis2mean, flattenmean],
    #     "variance":[axis1var, axis2var, flattenvar],
    #     "standard deviation":[axis1std, axis2std, flattenstd],
    #     "max":[axis1max, axis2max, flattenmax],
    #     "min":[axis1min, axis2min, flattenmin],
    #     "sum":[axis1sum, axis2sum, flattensum]
    # }