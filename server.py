
from flask import Flask, render_template, request, redirect


from user import User

app = Flask(__name__)

@app.route("/")
def users():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", all_users = users)
            

@app.route("/create", methods=['GET'])
def create():
    return render_template ("create.html")



@app.route('/create_user', methods=["POST"])
def create_user():

    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }

    new_userid = User.save(data) 
    return redirect(f'/user/show/{new_userid}')


@app.route('/user/edit/<int:id>/')
def edit(id):
    data = {
        'id': id
    }
    return render_template('edit_user.html', user = User.get_one(data))

@app.route('/user/show/<int:id>/')
def show(id):
    data = {
        'id': id
    }
    return render_template('show_user.html', user = User.get_one(data))

    
@app.route('/user/update', methods=['POST'])
def update():
    print(request.form['id'])
    User.update(request.form)
    return redirect(f'/user/show/{request.form["id"]}')

@app.route('/user/delete/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/')

    
if __name__ == "__main__":
    app.run(debug=True)

