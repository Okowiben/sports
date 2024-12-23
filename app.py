from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sports.components.data_ingest import DataIngestion
from sports.components.data_validation import DataValiadtion
from sports.components.data_transformation import DataTransformation
from sports.components.model import ModelTrainer
from sports.config.configuration import ConfigurationManager

app = Flask(__name__)

config = ConfigurationManager()

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/ingest', methods=['POST'])
def ingest_data():
    """Handle data ingestion."""
    try:
        ingest = DataIngestion(config=config)
        ingest.initiate_data_ingestion()
        return redirect(url_for('index'))
    except Exception as e:
        return str(e)

@app.route('/validate', methods=['POST'])
def validate_data():
    """Handle data validation."""
    try:
        valid = DataValiadtion(config=config)
        valid.validate_all_columns()
        return redirect(url_for('index'))
    except Exception as e:
        return str(e)

@app.route('/transform', methods=['POST'])
def transform_data():
    """Handle data transformation."""
    try:
        trans = DataTransformation(config=config)
        X_train, y_train, X_test, y_test = trans.initiate_data_transformation()
        return redirect(url_for('index'))
    except Exception as e:
        return str(e)

@app.route('/train', methods=['POST'])
def train_model():
    """Handle model training."""
    try:
        trans = DataTransformation(config=config)
        X_train, y_train, X_test, y_test = trans.initiate_data_transformation()
        trainer = ModelTrainer()
        trainer.initiate_model_trainer(X_train, y_train, X_test, y_test)
        return redirect(url_for('index'))
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)