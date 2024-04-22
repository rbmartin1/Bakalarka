from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Base directory from where the Flask app starts looking for files
    base_dir = 'FileInclus'

    # Get the 'file' parameter from the URL, if not found use 'data/default.txt' as the default
    file_name = request.args.get('file', 'data/default.txt')

    # Create the full file path
    file_path = os.path.join(base_dir, file_name)

    if 'default.txt' not in file_path and 'hidden.txt' not in file_path:
        return "Access denied."

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if content == "":
                print(f"The file {file_path} is empty.")
            else:
                print(f"Content of {file_path}: '{content}'")  # Print content to the console for debugging
    except FileNotFoundError:
        content = f"File not found. Tried accessing: {file_path}"
        print(content)
    except Exception as e:
        content = f"An error occurred: {str(e)}"
        print(content)

    # Explicitly create a response object with the correct content type
    response = Response(content, mimetype='text/plain; charset=utf-8')
    return response



if __name__ == '__main__':
    print(f"Current working directory: {os.getcwd()}")
    app.run(debug=True)
