from flask import request, jsonify, render_template
from .health import doctor, treatments, mealplan, fitness, research, network, keyword
from app import app

@app.route('/api/doctor', methods=['POST'])
def api_doctor():
    content = request.json
    result = doctor(content['prompt'])
    return render_template('index.html')


@app.route('/api/treatments', methods=['POST'])
def api_treatments():
    content = request.json
    result = treatments(content['prompt'])
    return jsonify(result=result)


@app.route('/api/mealplan', methods=['POST'])
def api_mealplan():
    content = request.json
    result = mealplan(content['prompt'])
    return jsonify(result=result)


@app.route('/api/fitness', methods=['POST'])
def api_fitness():
    prompt = request.json['prompt']
    response = fitness(prompt)
    return jsonify({'response': response})


@app.route('/api/research', methods=['POST'])
def api_research():
    content = request.json
    result = research(content['prompt'])
    return jsonify(result=result)

@app.route('/api/network', methods=['POST'])
def api_network():
    content = request.json
    result = network(content['prompt'])
    return jsonify(result=result)

@app.route('/api/keyword', methods=['POST'])
def api_keyword():
    content = request.json
    result = keyword(content['prompt'])
    return jsonify(result=result)
