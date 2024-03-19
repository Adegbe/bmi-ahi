# -*- coding: utf-8 -*-
"""BMI AHI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AlXzxfItulxLf5MZQzwoNjUA2TfFFFZi
"""

def calculate_bmi(weight_kg, height_cm):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
    weight_kg (float): Weight of the individual in kilograms.
    height_cm (float): Height of the individual in centimeters.

    Returns:
    float: BMI value.
    """
    height_m = height_cm / 100  # Convert height to meters
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    """
    Determine the BMI category.

    Parameters:
    bmi (float): BMI value.

    Returns:
    str: BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# User inputs
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
gender = input("Enter your gender (male/female/other): ")
weight_kg = float(input("Enter your weight in kilograms: "))
height_cm = float(input("Enter your height in centimeters: "))

# Calculate BMI
bmi_value = calculate_bmi(weight_kg, height_cm)

# Determine BMI category
category = bmi_category(bmi_value)

# Output results
print(f"\nAge: {age}")
print(f"Nationality: {nationality}")
print(f"Gender: {gender}")
print(f"Your BMI is: {bmi_value:.2f}")
print(f"BMI Category: {category}")

