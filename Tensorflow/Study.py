import tensorflow as tf
from tensorflow.python import keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_image, test_labels) = fashion_mnist.load_data()

print(len(test_image))
