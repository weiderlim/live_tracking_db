from db_func.funcs import initiate
from db_func import app
from routes import * 

if __name__ == '__main__' : 
    initiate()
    app.run(host="0.0.0.0", port=5001, debug=True)

# add_txn(3, "3/1/2024", "Binance", "Joshua", "BNBUSDT", "Sell", 100, 50000)
# print (get_byPic ("Vkee"))

# TODO
# 1. Learn about SQL-ALCHEMY and FLASK, so i know how to send the database data as json or whatever that needs to be sent
# 2. Is it the right way for the APIs to be the one commencing the actions?
# 3. Migrate the other API endpoints - Asset/PNL Histories