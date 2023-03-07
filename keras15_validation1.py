# 성능 향상에 좋음 (훈련할 때 모의고사 보는 너낌)
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import numpy as np

#1. 데이터
x_train = np.array(range(1, 11))    # 스칼라 10개짜리 벡터 1개
y_train = np.array(range(1, 11))
x_val = np.array([14, 15, 16])
y_val = np.array([14, 15, 16])
x_test = np.array([11, 12, 13])
y_test = np.array([11, 12, 13])


#2. 모델구성
model = Sequential()
model.add(Dense(5, activation='linear', input_dim = 1))
model.add(Dense(2))
model.add(Dense(3))
model.add(Dense(1))


#3. 컴파일, 훈련
model.compile(loss = 'mse', optimizer= 'adam')
model.fit(x_train, y_train, epochs = 20, batch_size= 2,
          validation_data= (x_val, y_val))          # 훈련하고 검증하고 훈련하고 검증하고 ...(반복)

#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss', loss)

result = model.predict([17])
print('17의 예측값 : ', result)
