from db_func import db 

class Transaction (db.Model) :
    txn_id = db.Column(db.Integer, primary_key=True)
    txn_date = db.Column(db.String, nullable=False)
    exchange = db.Column(db.String, nullable=False)
    pic = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    # buy / sell 
    txn_type = db.Column(db.String, nullable=False)
    token_amt = db.Column(db.Integer, nullable=False)
    usd_amt = db.Column(db.Integer, nullable=False)

    # what do you want to show when you print the Transaction instance
    def __repr__(self) -> str:
        return f"Transaction ID : {self.txn_id}, txn_date : {self.txn_date}, exchange : {self.exchange}, pic : {self.pic} \
        , position : {self.position}, txn_type : {self.txn_type}, token_amt : {self.token_amt}, usd_amt : {self.usd_amt}"
