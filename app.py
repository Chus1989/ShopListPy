from flask import Flask, render_template, request, redirect, url_for
from model import ShoppingList


app = Flask(__name__)
shopping_list = ShoppingList()

@app.route('/')
def index():
    return render_template('index.html', items=shopping_list.getItem())

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item = request.form['item']
        shopping_list.addItem(item)
        return redirect(url_for('index'))
    return render_template('add_item.html')

if __name__ == '__main__':
    app.run(debug=True)
    