
import os
import json
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications.vgg16 import preprocess_input

# Flask app
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.secret_key = "cleantech_secret_key"  # for flash messages


# Load model & class indices
model = load_model("waste_classifier.h5")
with open("class_indices.json") as f:
    class_indices = json.load(f)
class_labels = [class_indices[str(i)] for i in range(len(class_indices))]

# Ensure upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Helper function: predict uploaded image
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    idx = np.argmax(preds[0])
    return class_labels[idx], float(np.max(preds[0]))

# -----------------------
# Routes for Pages
# -----------------------

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("file")
        if file:
           
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            label, confidence = predict_image(filepath)
            return render_template(
                "result.html",
                label=label,
                confidence=round(confidence*100,2),
                filename=filename
            )
    return render_template("index.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/uses")
def uses():
    return render_template("uses.html", title="Uses")

@app.route("/integration")
def integration():
    return render_template("integration.html", title="Integration")

@app.route("/impact")
def impact():
    return render_template("impact.html", title="Impact")

@app.route("/how-it-works")
def how_it_works():
    return render_template("how-it-works.html", title="How It Works")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # You can save to DB or send email here
        flash("Thank you! Your message has been sent successfully.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", title="Contact")

@app.route("/result")
def result():
    # Just in case someone directly visits /result
    return redirect(url_for("home"))

# -----------------------
# Run the App
# -----------------------
if __name__ == "__main__":
    
    # This block is for local development.
    port = int(os.environ.get("PORT", 5000))
    # Use 0.0.0.0 to be accessible from the network, not just localhost.
    app.run(debug=False, host="0.0.0.0", port=port)
