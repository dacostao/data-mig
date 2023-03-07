from flask import Flask, request, jsonify
from sqlalchemy.exc import IntegrityError
from app.etl.load.Load import Load

app = Flask(__name__)
loader = Load()

@app.route('/api/department', methods=['POST'])
def create_department():
    data = request.json
    try:
        loader.load_deparment([data])
        return jsonify({'message': 'Department created successfully'}), 201
    except IntegrityError:
        loader.session.rollback()
        return jsonify({'error': 'Department already exists'}), 400
    except Exception as e:
        loader.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/job', methods=['POST'])
def create_job():
    data = request.json
    try:
        loader.load_job([data])
        return jsonify({'message': 'Job created successfully'}), 201
    except IntegrityError:
        loader.session.rollback()
        return jsonify({'error': 'Job already exists'}), 400
    except Exception as e:
        loader.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/hiredemployee', methods=['POST'])
def create_hired_employee():
    data = request.json
    try:
        loader.load_hired_employee([data])
        return jsonify({'message': 'HiredEmployee created successfully'}), 201
    except IntegrityError:
        loader.session.rollback()
        return jsonify({'error': 'HiredEmployee already exists'}), 400
    except Exception as e:
        loader.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


