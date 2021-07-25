# FTX FUTURES plugin for Jesse

This is the initial release of the FTX Futures driver for Jesse.
At the moment:
* it is only meant for importing candles and running backtests
* it supports only Perpetual futures (*-PERP)


## Installation 
Install by running:

```sh
pip install jesse-ftx-futures
```

### Register your driver
Now you need to tell Jesse where to find this driver. We do that by adding it as a driver for importing candles in `plugins.py` file that exists in the root of Jesse projects. Here is an example where I register a driver for the FTX FUTURES exchange:

```py
from jesse.modes.import_candles_mode.drivers.binance import Binance
from jesse.modes.import_candles_mode.drivers.binance_futures import BinanceFutures
from jesse.modes.import_candles_mode.drivers.binance_inverse_futures import BinanceInverseFutures
from jesse.modes.import_candles_mode.drivers.bitfinex import Bitfinex
from jesse.modes.import_candles_mode.drivers.coinbase import Coinbase
from jesse.modes.import_candles_mode.drivers.testnet_binance_futures import TestnetBinanceFutures

from jesse_ftx_futures import FTXFutures

import_candles_drivers = {
    'Binance': Binance,
    'Binance Futures': BinanceFutures,
    'Binance Inverse Futures': BinanceInverseFutures,
    'Testnet Binance Futures': TestnetBinanceFutures,
    'Bitfinex': Bitfinex,
    'Coinbase': Coinbase,
    'FTX Futures': FTXFutures
}
```

Now I should be able to run import candles from FTX (in this example for Perpetual):

```sh
jesse import-candles 'FTX Futures' 'BTC-USDT' '2012-06-04'
```

In this example for an expiring future (*it won't work on baktesting for now*):

```sh
jesse import-candles 'FTX Futures' 'BTC-0924' '2012-06-04'
```


### Add new config values for running backtests
Usually the reason for importing candles in the first place is to run backtests on them. So we need to tell Jesse where to find the config values for our newly added exchange in order for it run backtests on it. 

We can do that by opening `config.py` and coping and pasting values from an existing exchange such as `Binance Futures` and changing the values according to our needs for out exchange:
```py
# https://www.ftx.com
'FTX Futures': {
    'fee': 0.0006,

    # backtest mode only: accepted are 'spot' and 'futures'
    'type': 'futures',

    # futures mode only
    'settlement_currency': 'USDT',
    # accepted values are: 'cross' and 'isolated'
    'futures_leverage_mode': 'isolated',
    # 1x, 2x, 10x, 50x, etc. Enter as integers
    'futures_leverage': 3,

    # used for spot exchange only
    'assets': [
        {'asset': 'USDT', 'balance': 10_000},
    ],
},
```