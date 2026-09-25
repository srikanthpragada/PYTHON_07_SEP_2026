def largest_name(*names):
    largest = ""
    for name in names:
        if len(name) > len(largest):
            largest = name

    return largest


print( largest_name('Li', 'Martin', 'James', 'Kevin','Jammey'))
