from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

@app.route('/bmi', methods=['GET'])
def get_bmi():
    # Extracting query parameters
    age = request.args.get('age', type=int)
    nationality = request.args.get('nationality', default='', type=str)
    gender = request.args.get('gender', default='', type=str)
    weight_kg = request.args.get('weight', type=float)
    height_cm = request.args.get('height', type=float)

    if not all([age, nationality, gender, weight_kg, height_cm]):
        return jsonify({"error": "Missing data"}), 400

    bmi_value = calculate_bmi(weight_kg, height_cm)
    category = bmi_category(bmi_value)

    return jsonify({
        "Age": age,
        "Nationality": nationality,
        "Gender": gender,
        "BMI": round(bmi_value, 2),
        "BMI Category": category
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080)
