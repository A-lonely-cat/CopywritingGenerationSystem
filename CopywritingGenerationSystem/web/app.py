from flask import Flask, jsonify, request, render_template
import sql


app = Flask(__name__)
app.template_folder = "C:\\Users\\feng\\Desktop\\py\\chat\\web"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route("/")
def index():
    h1_text = "人生只若如初见 何事秋风悲画扇"
    return render_template("index.html", h1_text=h1_text)

@app.route("/generate_text", methods=["POST"])
def generate_text():
    input_text = request.json.get("input")
    python_variable_text = "some text from Python variable"
    generated_text = input_text + python_variable_text
    return jsonify({'generated_text': generated_text})

if __name__ == "__main__":
    app.run(debug=True)