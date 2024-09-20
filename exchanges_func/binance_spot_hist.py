from exchanges_func import *
from exchanges_func.utils import *

def get_binance_trade_history(bin_api_key, bin_secret_key, start_time, end_time, symbol):

    base_url = 'https://api.binance.com'
    limit = 1000

    timestamp = int(time.time() * 1000)
    params = f'timestamp={timestamp}&limit={limit}&startTime={start_time}&endTime={end_time}&symbol={symbol}'
    signature = hmac.new(bin_secret_key.encode('utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest()

    headers = {
        'X-MBX-APIKEY': bin_api_key
    }

    url = f"{base_url}/api/v3/myTrades?{params}&signature={signature}"
        
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data is None:
            data = []  
        return data
    else:
        print(f"Error: Received status code {response.status_code} for symbol {symbol} with start_time {start_time} and end_time {end_time}")
        print(response.text)
        return []  

def loop_get_binance_history(bin_api_key, bin_secret_key, start_date, end_date, binance_symbols):
    
    # Handling dates 
    unix_start = convert_to_unix(start_date)
    unix_end = convert_to_unix(end_date)

    print(f"Binance: Full unix range {unix_start} to {unix_end}")

    # Another Loop to collect more than 7 days data
    current_start_time = start_date # Current start time for the loop
    trade_history_full = []

    while current_start_time < end_date:
    
        current_end_time = min(current_start_time + timedelta(days=1), end_date)

        unix_start = convert_to_unix(current_start_time)
        unix_end = convert_to_unix(current_end_time)
        trade_history_in_range = []

        print(f"Starting at {unix_start}, ending at {unix_end}")

        # Define a makeshift binance_symbols list for debugging
        binance_symbols = [
            {"symbol": "MEMEUSDT"},
            {"symbol": "RONINUSDT"},
        ]

        for symbol_item in binance_symbols:
            symbol = symbol_item.get('symbol')
            
            print(f"Current Symbol: {symbol}")
            raw_history = get_binance_trade_history(bin_api_key, bin_secret_key, unix_start, unix_end, symbol)
            print(raw_history)
            trade_history_in_range.extend(raw_history)

            # Spot Limit - 6000, Limit 300 Calls Per Minute
            time.sleep(0.4)  
        
        # Save info and update time
        trade_history_full.extend(trade_history_in_range)
        current_start_time = current_end_time 

    return trade_history_full

# Trade History
def parse_binance_hist(binance_trade_history, owner):
    
    binance_orders = []

    for trade in binance_trade_history:
        
        price = trade.get('price') # Reconfirm if execPrice or execValue will give in USD terms
        quantity = trade.get('qty')
        usd_value = float(price) * float(quantity)
        isBuyer = trade.get('isBuyer')
        action = ''

        # Decide buy or sell
        if isBuyer is False:
            action = "Sell"
        elif isBuyer is True:
            action = "Buy"

        order = {
            'date': convert_timestamp_to_date(trade.get('time')),
            'position': trade.get('symbol'),
            'action': action, 
            'PIC': owner,
            'exchange': 'binance-spot',
            'exec_qty': quantity,
            'exec_price': price,
            'usd_value': usd_value
        }
    
        binance_orders.append(order)
    
    df_binance_orders = pd.DataFrame(binance_orders)
    return df_binance_orders

def get_bin_history(mode, bin_api_key, bin_secret_key, owner):
    current_time_exact = datetime.now()

    # Convert the date back to a datetime object at midnight (00:00:00)
    current_date = datetime.combine(current_time_exact, datetime.min.time())

    end_date = current_date 

    # 2 Modes
    if mode == 'Full': 
        print('Getting data from current date to 2 years ago')
        start_date = end_date - timedelta(days=730)  # 2 years = 730 days
        
    elif mode == 'Weekly':
        print('Getting data from current date to 1 week ago')
        start_date = end_date - timedelta(weeks=1)

    binance_symbols = get_binance_symbols()
    raw_result = loop_get_binance_history(bin_api_key, bin_secret_key, start_date, end_date, binance_symbols)
    df_parsed_hist = parse_binance_hist(raw_result, owner)

    return df_parsed_hist

# Main
def collect_history(owner, mode):

    owner_data = process_owners(owner)
    df_owner_hist = get_bin_history(mode, owner_data['bin_api_key'], owner_data['bin_secret_key'], owner_data['pic'])

    json_hist = df_owner_hist.to_dict(orient='records') # Convert to JSON
    
    return json_hist

