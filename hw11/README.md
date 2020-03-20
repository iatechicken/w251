# W251 HW11 Richard Ryu

## What

We are training a Lunar Lander on OpenAI Gym's platform powered by our Jetson TX-2. Goal is to land the Lunar Lander on the moon safely as much as possible

## How

Use Reinforcement Learning and tweak the parameters of our models to improve upon the baseline model.

#### Baseline Model

Below is the configuration for our baseline model

```def nnmodel(input_dim):
    model = Sequential()
    model.add(Dense(32, input_dim=input_dim, activation='relu'))
    model.add(Dense(16, activation='sigmoid'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model

...
    model = nnmodel(10)

...
    training_thr = 3000
    total_itrs = 50000
...
        if steps > training_thr and steps %1000 ==0:
            # re-train a model
            print("training model model")
            modelTrained = True
            model.fit(np.array(X_train),np.array(y_train).reshape(len(y_train),1), epochs = 10, batch_size=20)
...
```

##### Baseline Model Results

Not too bad, we can observe that our baseline model had 10 input parameters with 32 neurons as the first hidden layer and a second hidden layer with 16 neurons, which all ends up with a single ouput parameter. The model is using Mean Squared Error for its loss function and Adam optimizer. The training stops at 50,000 steps and the model was able to land the pod 76 times. 

![baseline_model](frame50000.gif)

[video download link](https://cos-week11.s3.us-east.cloud-object-storage.appdomain.cloud/frame50000.mp4)


#### Second Model

In an attempt to improve our baseline results, I went ahead and added an extra hidden layer with 64 neurons as the first hidden layer and relied on ReLu activation function for all three hidden layers. Below is the configuration:

```def nnmodel(input_dim):
    model = Sequential()
    model.add(Dense(64, input_dim=input_dim, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model

...
    model = nnmodel(10)

...
    training_thr = 3000
    total_itrs = 50000
...
        if steps > training_thr and steps %1000 ==0:
            # re-train a model
            print("training model model")
            modelTrained = True
            model.fit(np.array(X_train),np.array(y_train).reshape(len(y_train),1), epochs = 10, batch_size=20)
...
```

##### Second Model Results

Blah

![second_model](m2-frame50000.gif)

[video_download_link](https://cos-week11.s3.us-east.cloud-object-storage.appdomain.cloud/m2_frame50000.mp4)


