import time

# Finds the larget product of 13 adjacent digits in this 1000 digit number.

file_name = "input_files/adjSumInput.txt"

def prod(list_to_prod):
    prod = 1
    for i in range(0, len(list_to_prod)):
        prod = prod * list_to_prod[i]
    return prod

def adjac(num_of_ints, big_num):
    product = 0
    productIndex = 0
    print(num_of_ints.__class__)
    for i in range(0, len(big_num)-num_of_ints):
        productCandidate = prod(big_num[i:i+num_of_ints])
        if productCandidate > product:
            product = productCandidate
            productIndex = i

    product = 1
    for i in big_num[productIndex: productIndex + (num_of_ints)]:
        product = product * i

    return product


digitList = []

with open(file_name) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        else:
            digitList.append(int(c))

startTime = time.time()* 1000
print(adjac(13, digitList))
print(str(time.time() * 1000 - startTime))

