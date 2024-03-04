import numpy as np
import seaborn as sn
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


st.write(
    """
    # Bike Share Dashboard
    """
)

df = pd.read_csv(r'C:\File Alya\environment\all_data.csv')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.header('Bike sharing Dashboard :sparkles:')
st.subheader("Monthly Bike Rental Performance")
df['yr'].replace([0, 1], ['2011', '2012'], inplace=True)
def create_monthly_totals(df): 
  monthly_totals = df.groupby(['mnth', 'yr'])['cnt'].sum().unstack(fill_value=0) 
  return monthly_totals

monthly_totals = create_monthly_totals(df)

colors = sn.color_palette("husl", n_colors=len(monthly_totals.columns))

plt.figure(figsize=(12, 6))

for year_col, color in zip(monthly_totals.columns, colors):
    sn.lineplot(
        x=monthly_totals.index,  
        y=monthly_totals[year_col],  
        label=year_col,  # Menggunakan tahun sebagai label
        color=color  
    )
    
plt.title('Performa Peminjam Sepeda per Bulan') 
plt.xlabel('Bulan') 
plt.ylabel('Jumlah Peminjaman Sepeda') 
plt.legend(title='Tahun')

st.pyplot()

st.subheader("Seasons Rental")
def create_grouped_by_season(df):
    grouped_by_season = df.groupby('season')['cnt'].mean().reset_index()
    return grouped_by_season

grouped_by_season = create_grouped_by_season(df)

colors = ["#a7bed3", "#c6e2e9", "#ffcaaf", "#dab894"]
sn.barplot(
    x='season',
    y='cnt',
    hue='season',
    data=grouped_by_season,
    palette=colors,
)
plt.title('Pengaruh Musim terhadap Rata-rata Peminjaman Sepeda')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Peminjaman Sepeda')

st.pyplot()