# Importiere benötigte Bibliotheken
import sklearn.datasets as skl_data
import sklearn.neural_network as skl_nn
import pickle
import matplotlib.pyplot as plt
from skimage import io

# INFERENZ auf RASPBERRY
# Trainiertes Netzwerk wieder einlesen
mlp = pickle.load(open("MLP_classifier0", 'rb'))
test_digit = [1.3],[1]
test_digit_prediction = mlp.predict(test_digit)
print("Predicted value of image ",test_digit_prediction[0])
#fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 7))
#ax.imshow(test_digit.reshape(28,28), cmap='gray')
#ax.axis('off')
#plt.show()

