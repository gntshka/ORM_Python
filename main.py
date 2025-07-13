import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:m1re5K%40@localhost:5432/Python_ORM'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher_1 = Publisher(name='Пушкин')
publisher_2 = Publisher(name='Достоевский')

book_1 = Book(title='Евгений Онегин', publisher_id=1)
book_2 = Book(title='Руслан и Людмила', publisher_id=1)
book_3 = Book(title='Преступление и наказание', publisher_id=2)

shop_1 = Shop(name='Someshop')
shop_2 = Shop(name='SomeBook')

stock_1 = Stock(book_id=1, shop_id=1, count=5)
stock_2 = Stock(book_id=2, shop_id=2, count=10)

sale_1 = Sale(price=1000, stock_id=1, count=1)
sale_2 = Sale(price=500, stock_id=2, count=1)

session.add_all([publisher_1, publisher_2, book_1, book_2, book_3, shop_1, shop_2, stock_1, stock_2, sale_1, sale_2])
session.commit()


for i in session.query(Book).join(Book.publisher).filter(Publisher.name == 'Пушкин').all():
    i_1 = i.get_book()
    dict = {'title': i_1[1]}
    
    for j in session.query(Stock).join(Stock.book).filter(Book.id == i_1[0]).all():
        j_1 = j.get_stock()
        
        for k in session.query(Shop).filter(Shop.id == j_1[2]).all():
            k_1 = k.get_shop()
            dict['shop'] = k_1[1]
        
        for l in session.query(Sale).filter(Sale.id == j_1[0]).all():
            l_1 = l.get_sale()
            dict['sale'] = l_1[1] # type: ignore
    print(dict)


session.close()