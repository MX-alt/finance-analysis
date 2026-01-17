import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2024-01-01", end="2025-01-01")
print(df.head())

plt.plot(df["Close"])
plt.show()
