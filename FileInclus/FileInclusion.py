from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/')
def index():
    # zakladny priecinok
    base_dir = 'FileInclus\\data'

    # ziskanie file_name z url ak nie tak 'data/default.txt'
    file_name = request.args.get('file', 'data/default.txt')

    # vytvorenie cesty
    file_path = os.path.join(base_dir, file_name)

    #jednoduchy white list pre jedine 2 dovolene subory
    if 'default.txt' not in file_path and 'hidden.txt' not in file_path:
        return "Access denied."

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if content == "":
                print(f"The file {file_path} is empty.")
            else:
                print(f"Content of {file_path}: '{content}'")
    except FileNotFoundError:
        content = f"File not found. Tried accessing: {file_path}"
        print(content)
    except Exception as e:
        content = f"An error occurred: {str(e)}"
        print(content)

    # Explicitné vytvorenie odpovede so správnym typom
    response = Response(content, mimetype='text/plain; charset=utf-8')
    return response



if __name__ == '__main__':
    print(f"Current working directory: {os.getcwd()}")
    app.run(debug=True)


#http://127.0.0.1:5000/?file=default.txt
#Content of FileInclus\data/default.txt: 'This is a safe file.'
#http://127.0.0.1:5000/?file=hidden.txt
#Content of FileInclus\data/hidden.txt: 'You have accessed the hidden file.'

#http://127.0.0.1:5000/?file=../secret.txt
#Acess denied 




