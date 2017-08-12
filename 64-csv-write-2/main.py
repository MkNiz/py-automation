import csv

myCSV = open('a_better.csv', 'w', newline='')
myWriter = csv.writer(myCSV, delimiter='~', lineterminator='\n\n\n')

myWriter.writerow(['good', 'bad', 'hungy'])
myWriter.writerow(['decent', 'horrendous', 'hungy'])
myWriter.writerow(['I', 'Like', "Apples"])
myWriter.writerow([2, 69, 420.024])

myCSV.close()
print("File created.")