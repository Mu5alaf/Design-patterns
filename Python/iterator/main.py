def count_to(count):
    number_in_german = ["eins","zwei","drei","vier","funf"]
    #our built in iterator
    iterator = zip(range(count),number_in_german)
    
    for  position, number in iterator:
        # returns a generator contining numbers in german
        yield number

for num in count_to(1):
    print ("{}".format(num))

for num in count_to(5):
    print ("{}".format(num))