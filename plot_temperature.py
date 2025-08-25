import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('temperature_dataset.csv')

df = df.sort_values(['date','time'], ascending=True).reset_index(drop=True)
plt.figure(figsize=(10,5))
plt.plot(df.index, df['temperature_C'], label='Temperature (°C)')
plt.xlabel('Observation (hour)')
plt.ylabel('Temperature (°C)')
plt.title('Room temperature variation (1–7 Aug 2025)')
plt.legend()
plt.tight_layout()
plt.show()

