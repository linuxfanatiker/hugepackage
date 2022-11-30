# Importiere benötigte Bibliotheken
import sklearn.datasets as skl_data
import sklearn.neural_network as skl_nn
import pickle
import matplotlib.pyplot as plt
from skimage import io


# INFERENZ auf RASPBERRY
# Trainiertes Netzwerk wieder einlesen
mlp = pickle.load(open("MLP_classifier", 'rb'))

# Inferenz mit MLP Modell
#print('Versuchen wir es mit einem der Testdaten')
#test_digit = io.imread('img/8.png')
#test_digit_prediction = mlp.predict(test_digit.reshape(1,784))
#print("Predicted value",test_digit_prediction)

#fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 7))
#ax.imshow(test_digit.reshape(28,28), cmap='gray')
#ax.axis('off')
#plt.show()
for i in range(1,9):
    #print('Bild verarbeiten '+str(i))
    test_digit = io.imread('./28px_zahlen/'+str(i)+'.png')
    test_digit_prediction = mlp.predict(test_digit.reshape(1,784))
    print("Predicted value of image " +str(i),test_digit_prediction)
    #fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 7))
    #ax.imshow(test_digit.reshape(28,28), cmap='gray')
    #ax.axis('off')
    #plt.show()
