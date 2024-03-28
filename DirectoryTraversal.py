from flask import Flask, send_file, request
import os

app = Flask(__name__)

@app.route('/download')
def download_file():
    file_name = request.args.get('file_name')
    file_path = '/path/to/base/directory/' + file_name
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True)

#http://example.com/download?file_name=../../../../../etc/passwd
