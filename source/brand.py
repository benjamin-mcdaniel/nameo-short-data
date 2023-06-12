

def brand_main(prompt, marketplaces):
    market_results = {}
    for market in marketplaces:
        # fix this to actually search the marketplaces
        market_search = 3 if prompt == prompt else 0
        market_results[market] = market_search

    return market_results