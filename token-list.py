import requests
import time

def get_token_list():
    # Queries Osmosis DEX for list of symbols & prices

    url = "https://api.osmosis.zone/tokens/v2/all/"
    # loop repeats until response is received, as Osmosis fails a lot
    while True:
        try:
            response = requests.get(url, headers={"Content-Type": "application/json"})
        except requests.exceptions.HTTPError as e:
            print("Error getting token list: {}".format(e))
            time.sleep(0.3)
            continue

        if response:
            response_json = response.json()
            symbols = [token["symbol"] for token in response_json]
            prices = [price["price"] for price in response_json]
            for i in range(len(symbols)):
                if symbols[i] == "":
                    symbols[i] = "XXX"
            return symbols, prices

if __name__ == "__main__":
    tokens, prices = get_token_list()
    print("Token | Price")
    print("------- | --------")
    for token in tokens:
        price = prices[tokens.index(token)]
        print("{} | {}".format(token, price))
