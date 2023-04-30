import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('table_data.txt', delimiter='\t', parse_dates=[0], header=None, names=['DateTime', 'V1', 'V2', 'V3', 'V4'])



plt.plot(data['V2'])

plt.xlabel('Time')

plt.ylabel('Amplitude')

plt.show()