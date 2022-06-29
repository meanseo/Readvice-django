from keras.datasets import mnist
import tensorflow as tf
from matplotlib import pyplot as plt

_, (x_test, y_test) = mnist.load_data()
x_test = x_test / 255.0  # 데이터 정규화

model = tf.keras.models.load_model('./save/mnist_model.h5')
# model .summary()
model.evaluate(x_test, y_test, verbose=2)
plt.imshow(x_test[30], cmap="gray")
plt.show()

picks = [30]
y_prob = model.predict(x_test[picks], verbose=0)
predicted = y_prob.argmax(axis=-1)

print("손글씨 예측값:", predicted)