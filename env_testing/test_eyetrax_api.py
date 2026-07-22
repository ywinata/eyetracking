from pprint import pprint

from eyetrax import GazeEstimator

estimator = GazeEstimator()

# print("=" * 80)
# print("TYPE")
# print(type(estimator))

# print("=" * 80)
# print("DIR")
# pprint(dir(estimator))

# print("=" * 80)
# print("__dict__")
# pprint(estimator.__dict__)



# import cv2

# cap = cv2.VideoCapture(0)

# ret, frame = cap.read()

# features = estimator.extract_features(frame)

# print(type(features))
# print(len(features))

# print(type(features[0]))
# print(type(features[1]))

# print(features[0].shape)
# print(features[1])

# cap.release()


# prediction = estimator.predict(features)

# print(type(prediction))
# print(prediction)

# import inspect

# print("TRAIN")
# print(inspect.signature(estimator.train))
# print(inspect.getdoc(estimator.train))

# print("=" * 80)

# print("PREDICT")
# print(inspect.signature(estimator.predict))
# print(inspect.getdoc(estimator.predict))

# print("=" * 80)

# print("SAVE")
# print(inspect.signature(estimator.save_model))
# print(inspect.getdoc(estimator.save_model))

# print("=" * 80)

# print("LOAD")
# print(inspect.signature(estimator.load_model))
# print(inspect.getdoc(estimator.load_model))

# import inspect

# print(inspect.getsource(estimator.train))

# print(inspect.getsource(estimator.predict))

# print(inspect.getsource(estimator.model.__class__))

# print(type(estimator.model))

import inspect

from eyetrax.models.base import BaseModel

print(inspect.getsource(BaseModel))