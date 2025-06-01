import matplotlib.pyplot as plt
from statsmodels.datasets import co2
import pandas as pd
import seaborn as sns
co2_data = co2.load_pandas().data
co2_filtered = co2_data[(co2_data.index >= '1958-01-01') & (co2_data.index <= '1980-12-31')]
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(12, 6), dpi=120)
plt.plot(co2_filtered.index, co2_filtered['co2'],linewidth=2, color='#2e7d32', label='Концентрация CO2')
plt.title('Динамика концентрации CO2 в атмосфере (1958-1980)',fontsize=14, pad=20)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Концентрация CO2 (ppm)', fontsize=12)
plt.legend(fontsize=12)
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
plt.fill_between(co2_filtered.index,co2_filtered['co2'], color='#a5d6a7',  alpha=0.3)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
