# Importiere benötigte Bibliotheken
import sklearn.datasets as skl_data
import sklearn.neural_network as skl_nn
import pickle
import matplotlib.pyplot as plt
from skimage import io
import numpy as np

data = np.random.rand(150,1)
print(data.shape)
#quit()
label=np.random.randint(0,3,150)
for i in range(0,150):
    if(label[i]==0):
        sub_1=lambda e:e-1
        vectorized_sub_1=np.vectorize(sub_1)
        data[i] =vectorized_sub_1(data[i])
    if(label[i]==2):
        add_1=lambda a:a+1
        vectorized_add_1=np.vectorize(add_1)
        data[i] =vectorized_add_1(data[i])
        

data_train = data[0:135]
labels_train = label[0:135]
data_test = data[136:]
labels_test = label[136:]
#data_train = np.ndarray()
plt.scatter(data[:,0],label)
plt.show()
#test_digit = data_test.iloc[0].to_numpy()

# Save example test image to disk
# io.imsave('img/8.png', data_test.iloc[1].to_numpy().reshape(28,28))

# Instantiiere MLP Classifier
mlp = skl_nn.MLPClassifier(hidden_layer_sizes=(50,), max_iter=500, verbose=1, random_state=1)

# Training
mlp.fit(data_train,labels_train)
print("Training set score", mlp.score(data_train, labels_train))
print("Testing set score", mlp.score(data_test, labels_test))

# Speichere Netzwerk auf der Platte
pickle.dump(mlp, open("MLP_classifier0", 'wb'))

