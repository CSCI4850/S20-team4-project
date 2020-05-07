import sympy as sp
import numpy as np
import keras
X=np.loadtxt('/home/dak3t/Project Stuff/cur.csv', delimiter = ',')
X=X.astype('float32')
Y=np.loadtxt('/home/dak3t/Project Stuff/fin.csv', delimiter = ',')
Y=Y.astype('float32')

x_train = np.zeros((X.shape[0],9,9,1))
for i in range(X.shape[0]):
    x_train[i,:,:,0] = X[i].reshape(9,9)
y_train = Y

def generate_model():
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(18, kernel_size=(6,6),
                                  activation = 'relu',
                                  data_format='channels_last',
                                  input_shape=[x_train.shape[1],
                                              x_train.shape[2],
                                              x_train.shape[3]]))
    model.add(keras.layers.Conv2D(3,(3,3),activation='relu'))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(162,activation='relu'))
    model.add(keras.layers.Dense(81, activation='sigmoid'))

    model.compile(loss=keras.losses.binary_crossentropy,
                  optimizer=keras.optimizers.SGD(lr=0.01),
                  metrics=['accuracy'])
    model.summary()

    model.load_weights("model.h5")
    



from keras.utils.vis_utils import plot_model

def run_preds(grid):
#    min = grid[0];
#    max = grid[0];
#    for i in grid:
#        if grid[i] < min:
#            min = grid[i]
#        if grid[i] > max:
#            max = grid[i]

    preds = model.predict(grid).astype("float32")
    preds = preds.round(decimals=1)
    return preds