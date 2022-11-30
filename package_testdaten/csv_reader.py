import csv
import random

complete_content = []

data_train = []
labels_train = []

data_test = []
labels_test = []

with open('samples_labels.csv', newline='') as csvfile:
	complete_csv = csv.reader(csvfile, delimiter=',')
	for row in complete_csv:
		complete_content.append([ [float(row[1])], row[2] ])

	random.shuffle(complete_content)
	no_samples=len(complete_content)
	ninety_percent=no_samples*0.9
	i = 0

	while i < ninety_percent:
		data_train.append(complete_content[i][0])
		labels_train.append(complete_content[i][1])
		i=i+1

	while i < no_samples:
		data_test.append(complete_content[i][0])
		labels_test.append(complete_content[i][1])
		i=i+1


print("Train Ergebnis: Daten")
print(data_train)
print("Train Ergebnis: labels")
print(labels_train)

print("Test Ergebnis: Daten")
print(data_test)
print("Test Ergebnis: labels")
print(labels_test)
