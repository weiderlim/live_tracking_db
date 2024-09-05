# starting code to run to initialise the database
from db_func.funcs import add_txn, get_byId, get_byPic, get_all


if __name__ == '__main__' : 
    # add_txn(3, "3/1/2024", "Binance", "Joshua", "BNBUSDT", "Sell", 100, 50000)
    # print (get_byId (3))
    get_all() 
