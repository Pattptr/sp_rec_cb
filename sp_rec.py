from flask import Flask, render_template, request, jsonify
import speech_recognition as sr


app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():

   language = request.args.get('lang', type=str)
      
   if request.method == 'POST':
      f = request.files['file']
      r = sr.Recognizer()
      
      with sr.AudioFile(f) as source:
         audio = r.listen(source)
         text = r.recognize_google(audio, language=language)
      #txtFile = open('text2.txt', 'a')
      #txtFile.writelines(text)
 
      return jsonify({"text":text})

		
if __name__ == '__main__':
   app.run(debug = True)