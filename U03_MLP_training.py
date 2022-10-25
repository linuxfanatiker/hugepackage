# Importiere benötigte Bibliotheken
import sklearn.datasets as skl_data
import sklearn.neural_network as skl_nn
import pickle
from skimage import io

importfromweb = False
# Datenimport (MNIST Datensatz)
if importfromweb:
    data, labels = skl_data.fetch_openml('mnist_784', version=1, return_X_y=True)
    # Optional: Benutze picle um Daten und Labels auf Platte zu speichern oder zu laden
    pickle.dump(data,open("mnist_data",'wb'))
    pickle.dump(labels,open("mnist_labels",'wb'))
else:
    data = pickle.load(open("mnist_data", 'rb'))
    labels = pickle.load(open("mnist_labels", 'rb'))

# Normalisierung
data = data / 255.0

# Datensplit
data_train = data[0:63000]
labels_train = labels[0:63000]
data_test = data[63001:]
labels_test = labels[63001:]

test_digit = data_test.iloc[0].to_numpy()

# Save example test image to disk
# io.imsave('img/8.png', data_test.iloc[1].to_numpy().reshape(28,28))

# Instantiiere MLP Classifier
mlp = skl_nn.MLPClassifier(hidden_layer_sizes=(50,), max_iter=50, verbose=1, random_state=1)

# Training
mlp.fit(data_train.values,labels_train)
print("Training set score", mlp.score(data_train, labels_train))
print("Testing set score", mlp.score(data_test, labels_test))

# Speichere Netzwerk auf der Platte
pickle.dump(mlp, open("MLP_classifier", 'wb'))
