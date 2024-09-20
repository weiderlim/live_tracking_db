from db_func.funcs import add_txn, get_byPic, get_all
from db_func import app
from exchanges_func.binance_spot_hist import collect_history
from exchanges_func.utils import save_to_json

acc_owners = ['A'] # Debug
#acc_owners = ['J', 'JM2', 'VKEE', 'KS']

@app.route("/collect_bin_spot_full", methods=["GET"])
def bin_spot_full():

    for owner in acc_owners:
        owner_hist = collect_history(owner, 'Full')
        save_to_json(owner_hist, 'hist.json')

        for hist in owner_hist:
            date = hist.get('date')
            position = hist.get('position')
            tx_type = hist.get('action')
            pic = hist.get('PIC')
            exchange = hist.get('exchange')
            token_amt = hist.get('exec_qty')
            token_price = hist.get('exec_price')
            usd_value = hist.get('usd_value')

            add_txn(date, position, tx_type, pic, exchange, token_amt, token_price, usd_value)    

    return "Data stored to database"

@app.route("/get_all_transactions", methods=["GET"])
def get_all_transactions():
    
    database_contents = get_all() 

    return database_contents