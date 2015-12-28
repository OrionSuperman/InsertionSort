import random
def insertionSort(alist):
	newList = alist

	for sortPos in range(1, len(newList)):

		currentNumber = newList[sortPos]
		insertPos = sortPos

		while newList[insertPos-1] > currentNumber and insertPos > 0:
			newList[insertPos] = newList[insertPos-1]
			insertPos = insertPos-1

		newList[insertPos] = currentNumber
	return newList

test = []
for var in range(1, 100):
	number = random.randint(0, 10000)
	test.append(number)
toPrint = insertionSort(test)

print toPrint
