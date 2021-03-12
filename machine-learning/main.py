import matplotlib.pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()

# print(digits.images)

plt.imshow(digits.images[1], cmap=plt.cm.gray_r)
plt.show()
