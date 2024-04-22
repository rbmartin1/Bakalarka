import os
from flask import Flask, request, send_from_directory, abort

app = Flask(__name__)
# Here we append 'DirectoryTrav' to the base directory path
BASE_DIR = os.path.abspath(os.path.join("DirectoryTrav", "app_files"))
print("Serving files from:", BASE_DIR)

@app.route('/download')
def download():
    filename = request.args.get('filename')

    secure_filename = os.path.normpath(os.path.join(BASE_DIR, filename))
    print("Attempting to serve:", secure_filename)  # Print the absolute path to the file
    if not secure_filename.startswith(BASE_DIR):
        abort(403)  # Forbidden access if trying to access files outside of BASE_DIR
    if not os.path.exists(secure_filename):
        print("File does not exist:", secure_filename)
        abort(404)  # File not found
    print('Downloading...')
    return send_from_directory(BASE_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)




# http://127.0.0.1:5000/download?filename=example.txt


# http://127.0.0.1:5000/download?filename=../../../etc/passwd
# pri snahe použiť symlink dostaneme 403 - zabezpečenie funguje
# 127.0.0.1 - - [22/Apr/2024 18:33:06] "GET /download?filename=../../../etc/passwd HTTP/1.1" 403 -