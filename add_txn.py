from main import Transaction, db, app

app.app_context().push()

txn_1 = Transaction(
    txn_id = 1,
    txn_date = "1/1/2024",
    exchange = "Binance",
    pic = "Vkee",
    position = "ETHUSDT",
    # buy / sell 
    txn_type = "Buy",
    token_amt = 10,
    usd_amt = 30000
)

txn_2 = Transaction(
    txn_id = 2,
    txn_date = "2/1/2024",
    exchange = "Bybit",
    pic = "Jansen",
    position = "BTCUSDT",
    # buy / sell 
    txn_type = "Sell",
    token_amt = 1,
    usd_amt = 60000
)

db.session.add(txn_1)
db.session.add(txn_2)
db.session.commit()


