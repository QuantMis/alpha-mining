import json
f = open("Binance_ETHBTC_30m_1512086400000-1514764800000.json", "r")

data = json.loads(f.read())
for i in data:
    print(i)

