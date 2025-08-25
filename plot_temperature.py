import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('temperature_dataset.csv')
plt.figure(figsize=(10,5))
plt.plot(df['time'], df['temperature_C'], label='Temperature (°C)')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title('Room temperature variation (1–7 Aug 2025)')
plt.legend()
plt.tight_layout()
plt.savefig('results/temperature_plot.png')
