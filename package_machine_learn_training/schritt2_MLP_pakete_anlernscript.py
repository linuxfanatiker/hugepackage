# Importiere benötigte Bibliotheken
import matplotlib.pyplot as plt
import sklearn.datasets as skl_data
import sklearn.neural_network as skl_nn
import pickle
import numpy as np
import csv
import random
import sys

from skimage import io

# DATENIMPORT ############################################

complete_content = []

data_train = []
labels_train = []

data_test = []
labels_test = []

sample_labels_csv = sys.argv[1]

with open(sample_labels_csv, newline='') as csvfile:
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
with open('sample_labels_rev2.csv', newline='') as csvfile:
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


hidden_neurons=[5,50,60,80,100]        # Anzahl der Neuronen für die verschiedenen Durchläufe
#hidden_neurons=[1,2,3,4,5]        # Anzahl der Neuronen für die verschiedenen Durchläufe
mean_score_train=[]
mean_score_test=[]


# Instantiiere MLP Classifier
cur_neur_no = 0
for current_neurons in hidden_neurons:
    i = 0
    mean_score_train.append(0)
    mean_score_test.append(0)
    while i <10:
        mlp = skl_nn.MLPClassifier(hidden_layer_sizes=(current_neurons,), max_iter=2000, verbose=1, random_state=1)
        mlp.fit(data_train, labels_train)
        current_train_score = mlp.score(data_train, labels_train)
        current_test_score  = mlp.score(data_test, labels_test)
        print("Training set score at "+str(current_neurons)+" Neurons: ", current_train_score)
        print("Testing set score at "+str(current_neurons)+" Neurons: ", current_test_score)
        mean_score_train[cur_neur_no]+=current_train_score
        mean_score_test[cur_neur_no]+=current_test_score
        i+=1
    mean_score_train[cur_neur_no]/=i;
    mean_score_test[cur_neur_no]/=i;
    cur_neur_no+=1

print("Speichere Classifier")
pickle.dump(mlp, open("MLP_classifier_hugepackage", 'wb'))

cur_neur_no = 0
print("Ergebnisse \n");
for current_neurons in hidden_neurons:
    print("Fuer "+str(current_neurons)+" Neuronen\n")
    print("Mean train score (accuracy) = "+str(mean_score_train[cur_neur_no])+"\n")
    print("Mean test score (accuracy) = "+str(mean_score_test[cur_neur_no])+"\n")
    cur_neur_no+=1

# Training
#plt.boxplot(hidden_neurons,mse)
#plt.show()
#pickle.dump(mlp, open("MLP_classifier_test", 'wb'))

# Speichere Netzwerk auf der Platte

