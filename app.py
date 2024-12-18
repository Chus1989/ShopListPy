from flask import Flask, render_template, request, redirect, url_for
from DAO.DAOFactory import DAOfactory
from DB.connectionSQL import DatabaseConnection

jsonDao = DAOfactory().get_dao("json_dao")
sqlDAO = DAOfactory().get_dao("sqlalchemy_dao")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', items=sqlDAO.show_products())

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        purchased ='purchased' in  request.form
        number = request.form['number']
        jsonDao.create_product(id,name,purchased,number)
        sqlDAO.create_product(id = id,name = name, purchased = purchased, number = number)
        return redirect(url_for('index'))
    return render_template('add_item.html')

@app.route('/delete/<int:item_id>', methods = ['GET','POST'])
def delete_item(item_id):
    
    sqlDAO.delete_product(item_id)
    jsonDao.delete_product(item_id)
    return redirect(url_for('index'))
@app.route('/update/<int:item_id>',methods= ['POST'])
def update_item(item_id):
    name_update = request.form.get('name')
    number_update = request.form.get('number')
    purchased_update = request.form.get('purchased') == 'True'
    if name_update:
        sqlDAO.modify_product(item_id,'name',name_update)
        jsonDao.modify_product(item_id,'name',name_update)
        
    if number_update:
        sqlDAO.modify_product(item_id,'number',number_update)
        jsonDao.modify_product(item_id,'number',number_update)
        
    if purchased_update:
        sqlDAO.modify_product(item_id,'purchased',purchased_update)
        jsonDao.modify_product(item_id,'purchased',purchased_update)
        
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    
    app.run(debug=True)
    