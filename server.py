from flask import Flask, request, jsonify
from openpyxl import load_workbook
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Salvar o arquivo e processá-lo
    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)

    # Processar o arquivo (exemplo: abrir com openpyxl)
    wb = load_workbook(filepath)
    # ...processar o arquivo...

    return jsonify({'message': 'File processed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
