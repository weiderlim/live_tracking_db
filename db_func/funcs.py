from db_func.models import Transaction
from db_func import db 

# creating the DB, if you want to restart the database just delete the site.db file and run this. 
def initiate () : 
    db.create_all()


def add_txn (txn_id_in, txn_date_in, exchange_in, pic_in, position_in, txn_type_in, token_amt_in, usd_amt_in) : 
    trans = Transaction(
        txn_id = txn_id_in,
        txn_date = txn_date_in,
        exchange = exchange_in,
        pic = pic_in,
        position = position_in,
        # buy / sell 
        txn_type = txn_type_in,
        token_amt = token_amt_in,
        usd_amt = usd_amt_in
    ) 

    db.session.add(trans)
    db.session.commit()


def get_all () : 
    # loop through all rows 
    all_queries = Transaction.query.all()

    for query in all_queries : 
        print(query)


def get_byId (txn_id_in) : 
    return Transaction.query.filter_by(txn_id = txn_id_in).first()
    

def get_byPic (pic_in) : 
    txn_test2 = Transaction.query.filter_by(pic = pic_in).first()

