# CleanTech-AI [[demo video]](https://drive.google.com/file/d/1Scjjys9tNOlCtzlbInaFODc8bpnVcZuC/view?usp=sharing)

## AI-Powered Waste Classification System

CleanTech is an intelligent waste classification system powered by Artificial Intelligence. By employing advanced transfer learning techniques, it classifies waste into categories such as **Biodegradable, Recyclable, and Trash** with high precision.

The project aims to **reduce human error**, **support recycling efforts**, and **promote sustainable waste management practices** across the globe.

## Features

- **Image Upload and Classification**: Upload waste images and get instant classification results with confidence scores.
- **High Accuracy**: Utilizes a pre-trained VGG16 model fine-tuned for waste classification.
- **User-Friendly Web Interface**: Clean, responsive design built with Bootstrap and Flask.
- **Multiple Pages**: Includes About, Uses, Integration, Impact, How It Works, and Contact sections.
- **Flash Messages**: Provides user feedback for form submissions.
- **Secure File Handling**: Supports image uploads with validation.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Automated Setup (Recommended)
1. Clone the repository:
   ```bash
   git clone https://github.com/veera5423/CleanTech-AI.git
   cd CleanTech-AI
   ```

2. Run the setup script to install all prerequisites and set up the environment:
   ```bash
   python setup.py
   ```
   This will:
   - Check Python version compatibility
   - Create a virtual environment
   - Install all required dependencies
   - Verify presence of model and config files

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

### Manual Setup (Alternative)
If you prefer manual installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/veera5423/CleanTech-AI.git
   cd CleanTech-AI
   ```

2. Install the required dependencies:
   ```bash
   pip install flask tensorflow keras numpy pillow
   ```

3. Ensure the model file `waste_classifier.h5` and `class_indices.json` are in the root directory.

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Upload an image of waste using the upload form on the home page.

4. View the classification result, including the predicted category and confidence percentage.

## File Structure

```
CleanTech-AI/
├── app.py                          # Main Flask application
├── waste_classifier.h5             # Pre-trained Keras model
├── class_indices.json              # Class labels mapping
├── README.md                       # Project documentation
├── TODO.md                         # Task list (temporary)
├── .gitignore                      # Git ignore file
├── static/                         # Static assets
│   ├── css/
│   │   ├── style.css
│   │   └── styles2.css
│   ├── js/
│   │   └── script.js
│   └── uploads/                    # Uploaded images storage
├── templates/                      # HTML templates
│   ├── base.html                   # Base template
│   ├── index.html                  # Home page
│   ├── result.html                 # Classification result page
│   ├── about.html                  # About page
│   ├── uses.html                   # Uses page
│   ├── integration.html            # Integration page
│   ├── impact.html                 # Impact page
│   ├── how-it-works.html           # How It Works page
│   └── contact.html                # Contact page
└── .git/                           # Git repository
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **AI/ML**: TensorFlow, Keras (for model loading and prediction)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Data Handling**: NumPy






