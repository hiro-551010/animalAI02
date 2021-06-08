from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

classes = ["boar", "crow", "monkey"]
num_classes = len(classes)
image_size = 50

# 画像の読み込み
X = []
Y = []
for index, classlabel in enumerate(classes):
    photos_dir = os.path.join(os.path.dirname(__file__)) + '/animal/{}'.format(classlabel)
    files = glob.glob(photos_dir + "/*.jpg")
    print(photos_dir)
    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

# train_test_splitメゾットで3:1で画像を振り分け
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save('./animal.npy', xy)


