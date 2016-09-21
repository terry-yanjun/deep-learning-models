from flask import Flask
from resnet50 import ResNet50
from keras.preprocessing import image
from imagenet_utils import preprocess_input, decode_predictions
import numpy as np
import sys

model = ResNet50(weights='imagenet')

#img_path = str(sys.argv[1])
#img_path="elephant.jpg"

img_path = '/var/www/coolgink-up/img/tt.jpg'
base = '/var/www/coolgink-up/img/'





app = Flask(__name__)

@app.route("/<filename>")
def hello(filename):
#    img = image.load_img(img_path, target_size=(224, 224))
    img = image.load_img(base+filename, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    print('Predicted:', decode_predictions(preds))
    gg=decode_predictions(preds)
#    return filename
    return gg[0][1]
#    return "Hello World!"


if __name__ == "__main__":
    app.run()
