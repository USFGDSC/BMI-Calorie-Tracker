# Codelab Tutorial: BMI and Calories Calculator using Taipy

In this tutorial, you'll build a BMI and Calories calculator web application using **Taipy**. This app will allow users to input their body metrics and activity level to calculate their BMI and daily caloric needs.

## Prerequisites

Before starting, ensure you have Python installed on your machine, along with the necessary libraries. You'll also need the Taipy library to create the GUI.

### Install required libraries

```bash
pip install taipy pandas
```

---

## Step 1: Project Setup

First, create a new Python script file, for example, `app.py`, and import the following libraries.

```python
from taipy import Gui
from taipy.gui import Markdown
import pandas as pd
```

You'll also need to make sure you know your Python interpreter path. You can find this by pressing `cmd + shift + G` to open `usr/local/bin` and locating your Python interpreter.

---

## Step 2: Create the BMI, BMR, and Calories Calculation Functions

Now, let's define the main functions for BMI, BMR (Basal Metabolic Rate), and daily calorie calculations based on user inputs.

```python
def bmi_calculation(feet, inches, weight):
    bmi = (weight / 2.205) / ((((feet * 12) + inches) * 0.0254)**2)
    return bmi

def bmr_calculation(feet, inches, weight, age, sex):
    height = (feet * 30.48) + (inches * 2.54)  # Converts to cm
    if sex == 'Male':
        bmr = (10 * (weight / 2.205)) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * (weight / 2.205)) + (6.25 * height) - (5 * age) + 161
    return bmr

def calories_calculation(feet, inches, weight, age, sex, activity):
    if activity == "Little or no exercise":
        return round(bmr_calculation(feet, inches, weight, age, sex) * 1.2)
    elif activity == "Exercise 1-3 times/week":
        return round(bmr_calculation(feet, inches, weight, age, sex) * 1.375)
    elif activity == "Exercise 3-5 times/week":
        return round(bmr_calculation(feet, inches, weight, age, sex) * 1.55)
    elif activity == "Exercise 6-7 times/week":
        return round(bmr_calculation(feet, inches, weight, age, sex) * 1.725)
    elif activity == "Very intense exercise or 2x training":
        return round(bmr_calculation(feet, inches, weight, age, sex) * 1.9)
```

These functions handle the calculations based on user input, converting measurements and returning the appropriate results.

---

## Step 3: Setting Up Default Variables

Define preset values to allow testing of the app even before users input their data.

```python
sex = 'Male'
cal = 0
weight = 160
feet = 5
inches = 9
age = 18
activity = 'Little or no exercise'
```

---

## Step 4: Setting Up the Data for BMI Categories

Create a small data table that will display BMI categories and their corresponding descriptions.

```python
bmi_data = pd.DataFrame({
  "BMI": ['< 18.5', '18.5 - 24.9', '25 - 29.9', '> 30'],
  "Categories": ['Underweight', 'Healthy', 'Overweight', 'Obese']
})
```

---

## Step 5: Building the GUI

Now, we'll build the GUI using **Taipy**. This will allow users to input their metrics and view results interactively.

### Main Welcome Page

This page will greet the user and provide navigation options via a navbar.

```python
main = Markdown("""
<|layout|class_name=main|
# Welcome, **Jhoon**{: .name }!
#### BMI = Body Mass Index
<|navbar|>
|>
""")
```

### Metrics Input Page

This page allows the user to input their metrics (age, weight, height, sex, activity level).

```python
metrics_page = Markdown("""
<|layout|class_name=metrics|
<|{sex}|toggle|lov=Male;Female|>
<|{age}|number|label=Age|>
<|{feet}|number|label=Feet|>
<|{inches}|number|label=Inches|>
<|{weight}|number|label=Weight (lbs)|>
<|{activity}|selector|label=Activity level|lov=Little or no exercise;Exercise 1-3 times/week;Exercise 3-5 times/week;Exercise 6-7 times/week;Very intense exercise or 2x training|dropdown|>
|>
""")
```

### BMI Results Page

The BMI calculation will be displayed here. It will update dynamically based on the user's inputs.

```python
bmi_page = Markdown("""
<|layout|class_name=bmi|
**BMI:**{: .name }
<|{bmi_calculation(feet, inches, weight)}|text|format=%.1f|>
<|{bmi_data}|table|>
|>
""")
```

### Calories Calculation Page

This page will display the number of calories needed to maintain weight, as well as different caloric intakes for various weight loss goals.

```python
calories_page = Markdown("""
<|layout|class_name=calories|
#### Maintenance:
<|{calories_calculation(feet, inches, weight, age, sex, activity)}|> cal/day

#### Mild weight loss (0.5 lbs/week):
<|{calories_calculation(feet, inches, weight, age, sex, activity)-250}|> cal/day

#### Weight loss (1 lb/week):
<|{calories_calculation(feet, inches, weight, age, sex, activity)-500}|> cal/day

#### Extreme weight loss (2 lbs/week):
<|{calories_calculation(feet, inches, weight, age, sex, activity)-1000}|> cal/day
|>
""")
```

---

## Step 6: Configuring the Pages and Running the App

Finally, define the different pages the app will navigate through, and then run the app using the **Taipy** GUI.

```python
pages = {
    "/": main,
    "Metrics": metrics_page,
    "BMI": bmi_page,
    "Calories": calories_page
}

Gui(pages=pages, css_file='main.css').run(use_reloader='true', port=5001)
```

Here, we're also linking an external CSS file (`main.css`) for styling.

---

## Step 7: Running the Application

Save your script and run the app with:

```bash
Run Python File

Open your browser and navigate to `http://localhost:5001` to interact with your BMI and Calories Calculator.

---

With this setup, you now have a fully functional BMI and calories calculator app built using **Taipy**!
```
