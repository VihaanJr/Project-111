from asyncore import read
import csv
from cv2 import line
import pandas as pd
import statistics
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

read = df['reading_time'].tolist()

mean = statistics.mean(read)
standard_deviation = statistics.stdev(read)

print('The population mean is ', mean)
print('The population standard deviation is ', standard_deviation)

def random_set_means(counter):

    sample_list = []

    for i in range(0,counter):
        random_index = random.randint(0,len(read)-1)
        value = read[random_index]
        sample_list.append(value)
    
    sample_mean = statistics.mean(sample_list)
    return sample_mean

mean_list = []

for i in range(0,100):
    mean = random_set_means(30)
    mean_list.append(mean)

sampling_stdev = statistics.stdev(mean_list)
sampling_mean = statistics.mean(mean_list)

print('The sampling mean is' , sampling_mean)
print('The sampling standard deviation' , sampling_stdev)

first_stdev_start , first_stdev_end = sampling_mean - 1 * sampling_stdev , sampling_mean + 1 * sampling_stdev
second_stdev_start , second_stdev_end = sampling_mean - 2 * sampling_stdev , sampling_mean + 2 * sampling_stdev
third_stdev_start , third_stdev_end = sampling_mean - 3 * sampling_stdev , sampling_mean + 3 * sampling_stdev

fig = ff.create_distplot([mean_list] , ['Sampling Distribution'] , show_hist=False)
fig.add_trace(go.Scatter(x = [sampling_mean,sampling_mean]  , y = [0 , 0.8]  , mode = 'lines' , name='Sampling Mean'))
fig.add_trace(go.Scatter(x = [first_stdev_start,first_stdev_start]  , y = [0 , 0.8]  , mode = 'lines' , name='stdev 1 start'))
fig.add_trace(go.Scatter(x = [first_stdev_end,first_stdev_end]  , y = [0 , 0.8]  , mode = 'lines' , name='stdev 1 end'))
fig.add_trace(go.Scatter(x = [second_stdev_start,second_stdev_start]  , y = [0 , 0.8]  , mode = 'lines' , name='stdev 2 start'))
fig.add_trace(go.Scatter(x = [second_stdev_end,second_stdev_end]  , y = [0 , 0.8]  , mode = 'lines' , name='stdev 2 end'))
fig.add_trace(go.Scatter(x = [third_stdev_start,third_stdev_start]  , y = [0 , 0.8]  , mode = 'lines' , name='stdev 3 start'))
fig.add_trace(go.Scatter(x = [third_stdev_end,third_stdev_end]  , y = [0 , 0.8]  , mode = 'lines' , name='stdev 3 end'))
fig.show()

z = (mean - sampling_mean)/sampling_stdev
print('The z score is' , z)

