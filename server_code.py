from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_base import Base, Items

app = Flask(__name__)

engine = create_engine('sqlite:///item_list.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/items/')
def show_items():
        item_list = session.query(Items).all()
        return render_template('homepage.html',items=item_list)

@app.route('/items/new')
def newItem():
    return "page to create a new menu item. Task 1 complete!"

@app.route('/items/edit')
def editItem():
    return "page to edit a menu item. Task 2 complete!"

@app.route('/items/delete')
def deleteItem():
    return "page to delete a menu item. Task 3 complete!"

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)