from database import db_session
from database import init_db
from models import Data
import datetime

init_db()

date  = datetime.datetime.now()

# row = Data(date=date, subscribers=3500, reviews=200)
# print(row)

# db_session.add(row)

row1 = Data(date=date, subscribers=6500, reviews=300)
row2 = Data(date=date, subscribers=1500, reviews=100)

db_session.add(row1, row2)


print(db_session.query(Data).all()[0])



db_session.commit()
