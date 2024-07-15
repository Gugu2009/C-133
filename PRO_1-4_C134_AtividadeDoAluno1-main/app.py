from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Obtenha a entrada de texto do requisição POST 
    input_text = request.json.get("text")
    
    if not input_text:
        # Resposta a enviar se o input_text for indefinido
      response = {
         "status": "error",
         "message": "Digite um texto para prever a emoção associada a ele!"
      }
      return jsonify(response)  
    else:      
        predict_emotion, predict_emotion_img_url = predict(input_text)        
        # Resposta a enviar se o input_text não for indefinido
        response = {
           "status": "success",
           "data": { 
              "predict_emotion":predict_emotion,
              "predict_emotion_img_url":predict_emotion_img_url
           }

        }
        # Enviar resposta         
        
       
app.run(debug=True)



    