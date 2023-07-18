import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.title("MYFIT")




name = st.text_input("Enter your name ")

height = st.number_input("Enter your height (in centimeters)", min_value=1.0, max_value=300.0, step=0.1)
weight = st.number_input("Enter your weight (in kilograms)", min_value=1.0, max_value=500.0, step=0.1)

def calculate_bmi(height, weight):
    bmi = weight / (height / 100) ** 2
    return bmi

st.write("<span style='font-size: 24px;'>Name :",name," </span>", unsafe_allow_html=True)
st.write("<span style='font-size: 24px;'>Height :",height," centimeters </span>", unsafe_allow_html=True)
st.write("<span style='font-size: 24px;'>Weight :",weight," kilograms </span>", unsafe_allow_html=True)

if calculate_bmi(height, weight) < 18.5:
    st.write("<span style='font-size: 24px;'> Your BMI is",calculate_bmi(height, weight),", you are underweight. </span>", unsafe_allow_html=True)
elif 18.5 <= calculate_bmi(height, weight) < 24.9:
    st.write("<span style='font-size: 24px;'> Your BMI is",calculate_bmi(height, weight),", you are in healthy weight range.</span>", unsafe_allow_html=True)
elif 25 <= calculate_bmi(height, weight) < 29.9:
    st.write("<span style='font-size: 24px;'> Your BMI is",calculate_bmi(height, weight),", you are overweight.</span>", unsafe_allow_html=True)
else:
    st.write("<span style='font-size: 24px;'> Your BMI is",calculate_bmi(height, weight),", you are obese.</span>", unsafe_allow_html=True)





fitness_goal = st.selectbox("Select Fitness Goal", ["None","Lose Weight", "Build Muscle(Bulking)", "Stay Active"])

health_conditions = st.selectbox("Select Health Conditions", ["None","High Blood Pressure", "Diabetes", "Asthma"])


wearable_data = st.file_uploader("Upload Data from Wearable Device", type=["csv", "txt"])


if fitness_goal == "None":
    workout_plan = "**Do minimum of 1 hour of workout or cardio exercises or practice yoga regularly. Jogging of minimum 30 mins a day is recommended everyday for better health**"

elif fitness_goal == "Lose Weight":
    workout_plan = """

**Cardiovascular Exercises** : 
Perform these exercises to elevate your heart rate and burn calories.  \n \n

**Frequency**: 4-5 times per week \n
**Duration**: 30-60 minutes per session \n

**Brisk Walking**: A low-impact exercise that's easy to incorporate into your daily routine. \n
**Jogging/Running**: If your fitness level allows, you can incorporate jogging or running into your routine for increased calorie burn. \n
**Cycling**: Either on a stationary bike or outdoors, cycling is an effective way to burn calories. \n
**Swimming**: A full-body workout that is gentle on the joints. \n \n
**Strength Training**:
Building lean muscle mass can help increase your metabolism and support weight loss. Perform these exercises on non-consecutive days to allow for muscle recovery.




"""
elif fitness_goal == "Build Muscle(Bulking)":
    workout_plan = """**Day 1: Upper Body**

Bench Press (Chest) - 4 sets x 6-8 reps \n
Bent-Over Rows (Back) - 4 sets x 8-10 reps \n 
Overhead Press (Shoulders) - 3 sets x 8-10 reps \n 
Bicep Curls (Biceps) - 3 sets x 10-12 reps \n
Tricep Dips (Triceps) - 3 sets x 10-12 reps \n \n

**Day 2: Lower Body** \n

Squats (Quadriceps, Hamstrings, Glutes) - 4 sets x 6-8 reps \n
Deadlifts (Hamstrings, Glutes, Lower Back) - 4 sets x 6-8 reps \n
Leg Press (Quadriceps, Glutes) - 3 sets x 8-10 reps \n
Lunges (Quadriceps, Hamstrings, Glutes) - 3 sets x 10-12 reps per leg \n
Calf Raises (Calves) - 3 sets x 12-15 reps \n

**Day 3: Rest** \n \n

**Day 4: Upper Body** \n \n

Pull-Ups/Assisted Pull-Ups (Back, Biceps) - 4 sets x 6-8 reps \n
Dumbbell Chest Press (Chest) - 4 sets x 8-10 reps \n
Seated Shoulder Press (Shoulders) - 3 sets x 8-10 reps \n
Barbell or Dumbbell Rows (Back) - 3 sets x 10-12 reps \n
Hammer Curls (Biceps) - 3 sets x 10-12 reps \n \n

**Day 5: Lower Body** \n

Romanian Deadlifts (Hamstrings, Glutes) - 4 sets x 6-8 reps \n
Leg Extensions (Quadriceps) - 4 sets x 8-10 reps \n
Glute Bridges (Glutes) - 3 sets x 10-12 reps \n
Leg Curls (Hamstrings) - 3 sets x 10-12 reps \n
Standing Calf Raises (Calves) - 3 sets x 12-15 reps \n

"""

else:
    workout_plan = """

**Cardiovascular Exercises** :
Cardio exercises get your heart rate up and promote cardiovascular health. Choose activities that you enjoy and can easily incorporate into your daily routine. \n

**Frequency**: Aim for at least 150 minutes of moderate-intensity cardio or 75 minutes of vigorous-intensity cardio per week.

**Brisk Walking**: Easy to do and can be done anywhere. \n
**Cycling**: Either outdoors or on a stationary bike. \n
**Dancing**: Join a dance class or dance at home to your favorite music. \n
**Swimming**: A full-body workout that's gentle on the joints. \n
**Jump Rope**: Great for cardiovascular fitness and coordination. \n \n
**Strength Training**:
Strength training helps maintain muscle mass, bone density, and functional strength. It can be done with bodyweight exercises or using resistance bands or weights.


"""
st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.subheader("Personalized Workout Plan")
st.write(workout_plan)

# Dietary Recommendations (Sample Implementation)
if "Diabetes" in health_conditions:
    dietary_recommendations = """

1. **Choose Complex Carbohydrates**: Focus on consuming carbohydrates that have a lower glycemic index (GI) and are high in fiber. These include whole grains (such as brown rice, quinoa, and whole wheat), legumes, fruits, and non-starchy vegetables. These foods can help regulate blood sugar levels and provide sustained energy.

2. **Limit Simple Sugars and Refined Carbohydrates**: Reduce or avoid foods with added sugars and those made with refined grains (white bread, white rice, sugary cereals, pastries, etc.). These can cause rapid spikes in blood sugar levels.

3. **Control Portion Sizes**: Pay attention to portion sizes to manage carbohydrate intake. Eating smaller, frequent meals throughout the day can help control blood sugar levels more effectively.

4. **Include Lean Protein Sources**: Incorporate lean proteins such as skinless poultry, fish, tofu, beans, lentils, and low-fat dairy products. Protein can help slow down the digestion of carbohydrates and prevent sharp rises in blood sugar.

5. **Healthy Fats**: Choose heart-healthy fats like those found in avocados, nuts, seeds, olive oil, and fatty fish (salmon, mackerel, sardines). These fats are beneficial for cardiovascular health and can help manage blood sugar levels.


"""
elif "Asthma" in health_conditions:
    dietary_recommendations = """

1. **Anti-Inflammatory Foods**: Incorporate foods rich in antioxidants and anti-inflammatory properties. These can help reduce inflammation in the airways and may alleviate asthma symptoms. Include fruits and vegetables (especially colorful ones), nuts, seeds, and fatty fish like salmon in your diet.

2. **Omega-3 Fatty Acids**: Increase your intake of omega-3 fatty acids, as they have anti-inflammatory effects. Sources include fatty fish (salmon, mackerel, sardines), flaxseeds, chia seeds, and walnuts.

3. **Avoid Trigger Foods**: Pay attention to any foods that seem to trigger asthma symptoms and try to avoid or limit them. Common trigger foods may include processed foods, sulfite-containing foods (e.g., dried fruits, wine), and foods high in preservatives.

4. **Stay Hydrated**: Drink plenty of water throughout the day to keep your airways hydrated and help reduce the likelihood of mucus buildup in the lungs.

5. **Maintain a Balanced Diet**: Focus on a balanced diet that includes a variety of nutrients. Incorporate lean proteins, whole grains, fruits, vegetables, and healthy fats in your meals to support overall health, which can indirectly benefit asthma management.

"""
elif "High Blood Pressure" in health_conditions:
    dietary_recommendations = """
1. **Reduce Sodium Intake**: Lower your consumption of sodium (salt) as it can contribute to elevated blood pressure. Aim to consume less than 2,300 milligrams (mg) of sodium per day. Avoid processed and packaged foods, as they often contain high levels of sodium. Instead, opt for fresh, whole foods prepared at home, and use herbs and spices to add flavor to your meals.

2. **Increase Potassium-Rich Foods**: Potassium can help counteract the effects of sodium on blood pressure. Include potassium-rich foods such as bananas, oranges, potatoes, spinach, avocados, and sweet potatoes in your diet.

3, **Adopt the DASH Diet** : Consider following the Dietary Approaches to Stop Hypertension (DASH) diet, which emphasizes fruits, vegetables, whole grains, lean proteins, and low-fat dairy products. The DASH diet has been shown to be effective in lowering blood pressure.

4. **Limit Alcohol Consumption** : Excessive alcohol intake can raise blood pressure. If you choose to drink, do so in moderation. For men, moderate drinking means up to two drinks per day, and for women, it's up to one drink per day.

5. **Maintain a Healthy Weight**: Achieving and maintaining a healthy weight can significantly impact blood pressure levels. Incorporate a balanced diet and regular physical activity to help manage weight and support overall health.

"""

elif "None" in health_conditions:
    dietary_recommendations = "**Have a Balanced Diet**"

st.subheader("Dietary Recommendations")
st.write(dietary_recommendations)


st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

def calculate_stats(data):
    mean_value = data.mean()
    std_value = data.std()
    median_value = data.median()
    return mean_value, std_value, median_value

if wearable_data:
    df = pd.read_csv(wearable_data)
    # calculate_stats(df["Steps"])
    # st.write(calculate_stats)
    
    st.subheader("Progress Tracking")

    st.write("Total Steps : ",df["Steps"].sum())
    st.write("Average no. of Steps : ",round(df["Steps"].mean()))
    st.write("Standard deviation of Steps : ",round(df["Steps"].std()))
    st.write("Median of  Steps : ",round(df["Steps"].median()))
    
    st.write(df)


    st.subheader("Charts")
    plt.plot(df["Date"], df["Steps"])
    plt.xlabel("Date")
    plt.ylabel("Steps")
    st.pyplot(plt)

    st.write("Analysing the data we get to know that the user needs to do set daily targets and finish them on regular basis.")


st.subheader("1MS21CI002 - Abhishek M.S")
st.subheader("1MS21CI036 - Parth Bidari")
st.subheader("1MS21CI037 - Prajwal N")
st.subheader("1MS21CI069 - Pawan kr. Reddy")

# st.write("")