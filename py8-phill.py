# Finds the larget product of 13 adjacent digits in this 1000 digit number.

file_name = "input_files/adjSumInput.txt"

def adjac(num_of_ints, big_num):
    productList = []
    lengthOfBigNum = len(big_num)
    factors = num_of_ints
    position = 0
    while position <= lengthOfBigNum - factors:
        dummy = 1
        for i in big_num[position : position + factors]:
            dummy = dummy * int(i)
            productList.append(dummy)
        position += 1
    return productList

digitList = []

with open(file_name) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        else:
            digitList.append(c)

print(max(adjac(13, digitList)))
