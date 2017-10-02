# Deep-Convolutional-Neural-Networks-Stock-Market
Deep Convolutional Neural Networks to predict stock market data.

## Usage
- Grabbing historical data
'''bash
python get_data.py --ticker SPY
'''
or using list in file
'''bash
python get_data.py --tickerfile etflist
'''

- Do prediction
'''bash
python stock_model.py --ticker ETF
'''

## Result
| Dataset | Acc on testing set |
|---|:---:|
|ETF|0.513|
|AADR|0.622024|
|BIB|0.642857|
