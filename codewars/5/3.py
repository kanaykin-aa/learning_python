import pandas as pd
from moexalgo import Ticker
# 1. Захват всей истории SBER (дневки)
sber=Ticker('SBER')
df=sber.candles(start='2000-01-01',end='2026-02-09',period='1D')
#2.Описание паттерна (например: Закрытие выше High вчерашнего дня)
df['pattern']=(df['close']>df['high'].shift(1))
#3.Проверка винрейта (Сработало ли на следующий день?)
df['win'] = (df['close'].shift(-1) > df['close'])
#4.Финальный расчет винрейта для этого паттерна
pattern_found=df[df['pattern'] == True]
winrate = pattern_found['win'].mean() * 100
print(f"Паттерн найден {len(pattern_found)} раз. Винрейт: {winrate:.2f}%")
