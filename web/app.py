from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)

@app.route('/document', methods=['GET'])

def document():
    return render_template('document.html')


@app.route('/document_detail', methods=['POST'])
def document_detail():
    Id_book = request.form['Id_book']
    title = request.form['title']
    number_pages = request.form['number_pages']
    category = request.form['category']
    author = request.form['author']
    q = Document1(Id_book=Id_book, title=title, number_pages=number_pages, category=category, author=author)
    model.append(q)
    return render_template('document_detail.html', value=q)


@app.route('/Document1')
def Document1():
    dato = [(i.Id_book, i.title, i.number_pages, i.category, i.author) for i in model]
    print(dato)
    return render_template('Document1.html', value=dato)



if __name__ == '__main__':
    app.run()