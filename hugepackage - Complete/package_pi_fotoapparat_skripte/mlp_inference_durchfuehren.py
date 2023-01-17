# Importiere benötigte Bibliotheken
import sklearn.datasets as skl_data
import sklearn.neural_network as skl_nn
import pickle
import matplotlib.pyplot as plt
from skimage import io
import sys

current_feature = []
#current_feature.append( [float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])] )
current_feature.append( [float(sys.argv[1]),float(sys.argv[2])] )

# INFERENZ auf RASPBERRY
# Trainiertes Netzwerk wieder einlesen
mlp = pickle.load(open("MLP_classifier_hugepackage", 'rb'))

# Inferenz mit MLP Modell
print('PY: Prediction von '+str(current_feature))
prediction = mlp.predict(current_feature)
print("PY: Predicted value "+str(prediction[0]))
sys.exit(int(prediction[0]))
