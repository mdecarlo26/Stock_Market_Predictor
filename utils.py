import numpy as np
from tensorflow import keras
from IPython.display import clear_output
import matplotlib.pyplot as plt 

def create_sequences(data, seq_length):
    sequences = []
    targets = []
    for i in range(len(data) - seq_length):
        sequences.append(data[i:i+seq_length])
        targets.append(data[i+1:i+seq_length+1])
    return np.array(sequences), np.array(targets)

def buildTimeFeatures(data,MAX_SEQ_LENGTH,test_percent):
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(data)

    input_sequences, target_sequences = create_sequences(scaled_data, MAX_SEQ_LENGTH)

    split_index = int((1-test_percent) * len(input_sequences))

    train_input = input_sequences[:split_index]
    train_target = target_sequences[:split_index]
    test_input = input_sequences[split_index:]
    test_target = target_sequences[split_index:]
    return train_input,train_target,test_input,test_target,scaler

class PlotLearning(keras.callbacks.Callback):
    """
    Callback to plot the learning curves of the model during training.
    """
    def on_train_begin(self, logs={}):
        self.metrics = {}
        for metric in logs:
            self.metrics[metric] = []
            

    def on_epoch_end(self, epoch, logs={}):
        # Storing metrics
        for metric in logs:
            if metric in self.metrics:
                self.metrics[metric].append(logs.get(metric))
            else:
                self.metrics[metric] = [logs.get(metric)]
        
        # Plotting
        metrics = [x for x in logs if 'val' not in x]
        
        f, axs = plt.subplots(1, len(metrics), figsize=(15,5))
        clear_output(wait=True)
        if len(metrics) == 1:
            axs = [axs]
        for i, metric in enumerate(metrics):
            axs[i].plot(range(1, epoch + 2), 
                        self.metrics[metric], 
                        label=metric)
            if logs['val_' + metric]:
                axs[i].plot(range(1, epoch + 2), 
                            self.metrics['val_' + metric], 
                            label='val_' + metric)
                
            axs[i].legend()
            axs[i].grid()

        plt.tight_layout()
        plt.show()