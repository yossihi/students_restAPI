from flask import Flask, current_app, jsonify, request, send_from_directory, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import re
import os

app = Flask(__name__)
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mj47TWMJ@localhost/students'  # Replace with your MySQL credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
app.config['UPLOAD_FOLDER'] = '/static/images'


db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addres = db.Column(db.String(200))
    photo = db.Column(db.String(500))

    def __init__(self, name, city, addres, photo):
        self.name = name
        self.city = city
        self.addres = addres
        self.photo = photo

#routes
@app.route('/static/images/<filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route("/")
def main():
    stud = [{"id":student.id,
              "name":student.name,
                "city":student.city,
                  "addres":student.addres,
                  "photo": url_for('get_image', filename= student.photo)}
                    for student in Students.query.all()]
    print(stud)
    return jsonify(stud)

@app.route("/add", methods=['POST'])
def add_stud():
    name = request.form['name']
    city = request.form['city']
    addres = request.form['addres']
    
    if 'image' in request.files:
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)

            image.save(os.path.join(current_app.root_path, 'static/images', filename))
            new_stud = Students(
                name=name,
                city=city,
                addres=addres,
                photo=filename
            )
            db.session.add(new_stud)
            db.session.commit()
            return jsonify({'msg': "student added succefuly"})


@app.route("/delete/<int:studID>", methods=['DELETE'])
def del_stud(studID):
    student = Students.query.get_or_404(studID)

    # Delete the student from the database
    db.session.delete(student)
    db.session.commit()

    return {'msg': 'Student deleted successfully'}


@app.route("/update/<int:studID>", methods=['POST'])
def upd_stud(studID):
    student = Students.query.get_or_404(studID)

    student.name = request.form['name']
    student.city = request.form['city']
    student.addres = request.form['addres']
    
    if 'image' in request.files:
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)

            image.save(os.path.join(current_app.root_path, 'static/images', filename))
            student.photo = filename

    db.session.commit()

    return {'msg': 'Student updated successfully'}


def is_legal_name(name):
    # Check length
    if not (2 <= len(name) <= 30):
        return False

    # Check if it contains only allowed characters
    if not re.match(r'^[a-zA-Z\- ]+$', name):
        return False

    # Check if it starts or ends with a space or hyphen
    if name.startswith(' ') or name.endswith(' ') or name.startswith('-') or name.endswith('-'):
        return False

    return True

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)