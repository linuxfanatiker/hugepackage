# Importiere benötigte Bibliotheken
import matplotlib.pyplot as plt
import sklearn.datasets as skl_data
import sklearn.neural_network as skl_nn
import pickle
import numpy as np
from skimage import io

# Datenimport (MNIST Datensatz)
data = pickle.load(open("dataarray", 'rb'))
labels = pickle.load(open("testdaten\\M\\labels.csv", 'rb'))

# Datensplit
data_train = data[0:150]
labels_train = labels[0:150]
data_test = data[150:]
labels_test = labels[150:]

test_digit = data_test.iloc[0].to_numpy()
setp={1,5,10,25,50}
# Save example test image to disk
# io.imsave('img/8.png', data_test.iloc[1].to_numpy().reshape(28,28))
mse=[]
# Instantiiere MLP Classifier
for e in range(0,4):
    for i in range(0,11):
        mlp = skl_nn.MLPClassifier(hidden_layer_sizes=(steps[e],), max_iter=200, verbose=1, random_state=1)
        mse.append(sklearn.metrics.mean_squared_error, steps[e])

# Training
plt.boxplot(step,mse)
plt.show()
mlp.fit(data_train.values, labels_train)
pickle.dump(mlp, open("MLP_classifier_gelb", 'wb'))
print("Training set score", mlp.score(data_train, labels_train))
print("Testing set score", mlp.score(data_test, labels_test))

# Speichere Netzwerk auf der Platte

