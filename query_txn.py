from main import Transaction, db, app

app.app_context().push()

# print(Transaction.query.all())
# print(Transaction.query.first())

# filters
txn_test = Transaction.query.filter_by(txn_id = 1).first()
txn_test2 = Transaction.query.filter_by(pic = "Vkee").first()

# get info
# print(txn_test.txn_id)
# print(txn_test.position)

# loop through all queries 
all_queries = Transaction.query.all()

for query in all_queries : 
    print(query)