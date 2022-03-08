#Template inheritance, CSS exercise
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__, template_folder='template')

#For Workbench use 'localhost' 
#For editor.computing use 'student.computing.dcu.ie'
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='aliceinwonderlanD1!'
app.config['MYSQL_DATABASE_DB']='mealtime'

mysql = MySQL(app)

#This function will retrieve all data from database
@app.route('/Recipes', methods=['GET', 'POST'])
def recipes():
    
    cur = mysql.get_db().cursor()
    query1 = "SELECT * FROM mealtime.recipe"
    cur.execute(query1)
    output = cur.fetchall()
    mysql.get_db().commit()
    cur.close()
    
    return render_template('recipes.html', person = output)

@app.route('/Search', methods=['GET', 'POST'])
def search():
    
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        cur = mysql.get_db().cursor()
        query1 = "SELECT * FROM mealtime.recipe WHERE recipe_ingredient=%s"
        cur.execute(query1, (recipe_ingredients,))
        output = cur.fetchall()
        mysql.get_db().commit()
        cur.close()
        return render_template('filter_result.html', recipe_ingredient = output)
    
    return render_template('Search.html', recipe_ingredient = output)
    

#This function will add a new person data (except photo)
@app.route('/socials', methods=['GET', 'POST'])
def socials():
    
    if request.method == 'POST':
        name = request.form['namef']
        ingredient = request.form['ingredientf']
        instructions = request.form['instructionsf']
        cur = mysql.get_db().cursor()
        query1 = "INSERT INTO mealtime.e8_table (recipename, recipeingredient, recipeinstructions, recipetime, recipeimage) VALUES (%s, %s, %s,%s, %s)" 
        cur.execute(query1, (recipe_name, recipe_ingredient, recipe_description, recipe_image, recipe_time)
        mysql.get_db().commit()
        cur.close()
        return "Successfully added, thank you."
    
    return render_template('socials.html', tag="socials")

#Use if in localhost environment
if __name__=='__main__':
    app.run(debug=True)

#Use in editor.computing.dcu.ie environment
#if __name__=='__main__':   
#    app.run(host='0.0.0.0', port='8080', debug=True)
