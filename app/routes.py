from flask import Blueprint, request, jsonify
from .models import Result
from . import db

bp = Blueprint('api', __name__)


@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'ok'})


@bp.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    if not data or 'name' not in data or 'score' not in data:
        return jsonify({'error': 'Invalid payload'}), 400

    new_result = Result(name=data['name'], score=data['score'])
    db.session.add(new_result)
    db.session.commit()

    return jsonify({'message': 'Result added'}), 201


@bp.route('/results', methods=['GET'])
def results():
    results = Result.query.order_by(Result.id.asc()).all()
    out = []

    for r in results:
        out.append({
            'id': r.id,
            'name': r.name,
            'score': r.score,
            'timestamp': r.timestamp.isoformat()
        })

    return jsonify(out)