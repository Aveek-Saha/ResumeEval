import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from flask_cors import CORS

UPLOAD_FOLDER = os.getcwd() + '/uploaded/'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        print("File recieved")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            return redirect(url_for('index'))
    return """
    <!doctype html>
    <title>Uploaded Files</title>
    <h1>Uploaded Files</h1>
    
    <p>%s</p>
    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))

if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)