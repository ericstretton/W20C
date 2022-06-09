from flask import Flask, jsonify, request, redirect


app = Flask(__name__)


animals = [
            "giraffe",
            "elephant",
            "lion",
            "tiger",
            "jaguar",
            "bear"
]

add_animal = "baboon"
remove_animal = "lion"

@app.route('/')
def homepage():
    return "Hello Animals"



@app.get('/api/animals')
def animals_get():
    args = request.args
    
    animal_Id = args.get('animalId')
    if animal_Id == None:
        return jsonify(animals), 200
    else:
        return jsonify(animals[animal_Id]), 200


@app.post('/api/animals')
def animals_post():
    animals = request.args
    
    animals.add(add_animal)
    return redirect('/api/animals')
    
@app.patch('/api/animals')
def animals_patch():
    animals = request.args
    
    animals.pop('jaguar', 'black-jaguar')
    return redirect('/api/animals')
    
@app.delete('/api/animals')
def animals_delete():
    animals = request.args
    
    animals.remove(remove_animal)
    return redirect('/api/animals')