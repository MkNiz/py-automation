import csv

myCSV = open('a_good.csv', 'w', newline='')
myWriter = csv.writer(myCSV)

myWriter.writerow(['good', 'bad', 'hungy'])
myWriter.writerow(['decent', 'horrendous', 'hungy'])
myWriter.writerow(['I', 'Like', "Apples"])
myWriter.writerow([2, 69, 420.024])

myCSV.close()
print("File created.")