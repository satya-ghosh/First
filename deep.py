import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def install_deepface():
    try:
        # Run pip install command with --no-deps
        result = subprocess.run(
            ['pip', 'install', 'deepface==0.0.78', '--no-deps'],
            capture_output=True,
            text=True,
            check=True
        )
        return f"DeepFace installed successfully: {result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e.stderr}"

if __name__ == '__main__':
    app.run()
