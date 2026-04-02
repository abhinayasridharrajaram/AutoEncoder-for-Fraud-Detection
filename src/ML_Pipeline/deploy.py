# deploy.py
import pandas as pd
from flask import Flask, request, jsonify
import Preprocess
import Predict
import Utils

app = Flask(__name__)

model_path = "../output/deep-ae-model"
ml_model, columns = Utils.load_model(model_path)

@app.post("/get_fraud_score")
def get_fraud_score():
    # Parse JSON body into Python dict
    items = request.get_json()
    if items is None:
        return jsonify({"error": "No JSON received"}), 400

    # Build dataframe from JSON
    test_df = pd.DataFrame([items])
    processed_df = Preprocess.apply(test_df, is_train=False)
    prediction = Predict.init(processed_df, ml_model, columns)

    # Return JSON response
    return jsonify({"status": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
