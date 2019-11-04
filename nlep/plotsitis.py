import os
import pandas as pd
import matplotlib.pyplot as plt

for i in [f for f in os.listdir('.') if f.endswith('.csv')]:
    df = pd.read_csv(i)
    plt.plot(df.si, df.ti, 'o')

plt.legend([os.path.splitext(f)[0] for f in os.listdir('.') if f.endswith('csv')], fontsize=15)
plt.xlabel("Spatial Information", fontsize=15)
plt.ylabel('Temporal Information', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()
