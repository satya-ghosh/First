from flask import Flask, request, render_template
from deepface import DeepFace
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare_faces', methods=['POST'])
def compare_faces():
    # Retrieve the uploaded images
    image1 = request.files['image1']
    image2 = request.files['image2']
    
    # Convert uploaded images to OpenCV format
    img1 = cv2.imdecode(np.frombuffer(image1.read(), np.uint8), cv2.IMREAD_COLOR)
    img2 = cv2.imdecode(np.frombuffer(image2.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Compare faces with DeepFace
    result = DeepFace.verify(img1, img2, model_name='OpenFace')
    message = "Faces match!" if result['verified'] else "Faces do not match!"
    
    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
