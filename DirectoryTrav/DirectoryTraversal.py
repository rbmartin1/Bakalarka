import os
from flask import Flask, request, send_from_directory, abort

app = Flask(__name__)
# vytvorenie cesty
BASE_DIR = os.path.abspath(os.path.join("DirectoryTrav", "app_files"))
print("Serving files from:", BASE_DIR)

@app.route('/download')
def download():
    filename = request.args.get('filename')

    secure_filename = os.path.normpath(os.path.join(BASE_DIR, filename))

    if not secure_filename.startswith(BASE_DIR):
        abort(403)  # Forbidden access 
    if not os.path.exists(secure_filename):
        print("File does not exist:", secure_filename)
        abort(404)  # File not found
    print('Downloading...')
    return send_from_directory(BASE_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)




# http://127.0.0.1:5000/download?filename=example.txt
# Downloading...
# 127.0.0.1 - - [22/Apr/2024 20:25:19] "GET /download?filename=example.txt HTTP/1.1" 304 -

# http://127.0.0.1:5000/download?filename=../../../etc/passwd
# pri snahe použiť symlink dostaneme 403 - zabezpečenie funguje
# 127.0.0.1 - - [22/Apr/2024 18:33:06] "GET /download?filename=../../../etc/passwd HTTP/1.1" 403 -
