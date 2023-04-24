from flask import Flask, jsonify, request
import pickle

# Instanciamos la clase Flask
app = Flask(__name__)

# Urilizamos decoradores para definir las rutas de nuestro servidor web
# Definimos la ruta principal y el método HTTP que va a escuchar
@app.route('/', methods=['GET'])
def home():
    return """
    <h1>APP para calcular MPG</h1>
    APP para testear flask y Railway    
    """

# Definimos la ruta para el endpoint /api/v1/predictions
@app.route('/api/v1/predictions', methods=['GET'])
def predictions():
    # Obtenemos los datos de la URL
    cylinders = request.args['cylinders']
    displacement = request.args['displacement']
    horsepower = request.args['horsepower']
    weight = request.args['weight']
    acceleration = request.args['acceleration']
    model_year = request.args['model_year']

    map_origin = {'usa':1, 'europe':2, 'japan':3}
    origin = request.args['origin']
    origin = map_origin[origin]

    # Cargamos el modelo
    loaded_model = pickle.load(open('model.pkl', 'rb'))

    # El orden de los datos debe ser el mismo que el del modelo
    new_data = [cylinders, 
                displacement, 
                horsepower, 
                weight, 
                acceleration, 
                model_year, 
                origin]

    # Realizamos la predicción
    prediction = loaded_model.predict([new_data])
    # Retornamos la predicción en formato JSON    
    return jsonify({'prediction is': prediction[0]})

# __name__ es una variable que contiene el nombre del módulo
# Si el módulo se ejecuta directamente, Python asigna el nombre __main__ al módulo
# Si el módulo se importa, el nombre del módulo será el nombre del archivo .py
# debug=True activa el modo debug para la aplicación, esto permite que se reinicie automáticamente el servidor cuando se realicen cambios en el código.
if __name__ == '__main__':
    app.run(debug=False)
