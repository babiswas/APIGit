from model import db
from sqlalchemy.dialects.postgresql import JSON

class Primedata:
   __tablename__="primedata"
   id=db.Column(db.String(100),primary_key=True,nullable=False,unique=True)
   primedata=db.Column(JSON)


   def __init__(self,id,data):
       self.id=id
       self.primedata=data

   def __str__(self):
       return f"{self.id}"

