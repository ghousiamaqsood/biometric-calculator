def calculate_bmi(weight, height):
  """Calculates BMI using weight (kg) and height (m)."""
  bmi = weight / (height ** 2)
  return bmi

def interpret_bmi(bmi):
  """Interprets BMI based on standard categories."""
  if bmi < 18.5:
    return "Underweight"
  elif 18.5 <= bmi < 25:
    return "Normal weight"
  elif 25 <= bmi < 30:
    return "Overweight"
  else:
    return "Obese"

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate and interpret BMI
bmi = calculate_bmi(weight, height)
category = interpret_bmi(bmi)

# Display results
print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as: {category}")