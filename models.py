import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'Publisher'
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    
    def get_publisher(self):
        return self.id, self.name
    
    
class Book(Base):
    __tablename__ = 'Book'
    
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('Publisher.id'), nullable=False)
    
    publisher = relationship(Publisher, backref='Book')
    
    def get_book(self):
        return self.id, self.title, self.publisher_id
    
    
class Shop(Base):
    __tablename__ = 'Shop'
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    
    def get_shop(self):
        return self.id, self.name
    
    
class Stock(Base):
    __tablename__ = 'Stock'
    
    id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey('Book.id'), nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey('Shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    
    book = relationship(Book, backref='Stock')
    shop = relationship(Shop, backref='Stock')
    
    def get_stock(self):
        return self.id, self.book_id, self.shop_id, self.count
    
class Sale(Base):
    __tablename__ = 'Sale'
    
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=True)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('Stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    
    stock = relationship(Stock, backref='Sale')
    
    def get_sale(self):
        return self.id, self.price, self.stock_id, self.count
    
def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)