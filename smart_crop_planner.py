def suggest_crops_and_remedies(ph_value):
    if 0 <= ph_value < 4.0:
        soil_type = "Highly Acidic Soil"
        suggested_crops = ["Difficult to Cultivate crops"]
        remedies = ["Incorporate well-decomposed organic matter like compost or farmyard manure.",
                    "Avoid Acidifying Fertilizers which are high in ammonium and sulphur.",
                    "Apply agricultural lime or dolomite lime to raise the pH gradually."]
    elif 4.0 <= ph_value <= 5.5:
        soil_type = "Acidic Soil"
        suggested_crops = ["Tea", "Coffee", "Turmeric", "Pineapple", "Oranges"]
        remedies = ["Incorporate well-decomposed organic matter like compost or farmyard manure.",
                    "Apply agricultural lime or dolomite lime to raise the pH gradually."]
    elif 5.5 < ph_value <= 6.5:
        soil_type = "Slightly Acidic to Neutral Soil"
        suggested_crops = ["Rice", "Wheat", "Maize", "Potatoes", "Sugarcane", "Mangoes"]
        remedies = ["Maintain soil fertility through regular addition of organic matter.",
                    "Use wood ash in moderation to raise pH levels.",
                    "Apply lime or dolomite lime if necessary to adjust the pH towards neutral."]
    elif 6.5 < ph_value <= 7.5:
        soil_type = "Neutral Soil"
        suggested_crops = ["Most vegetables", "Bananas", "Grapes", "Pomegranates", "Papayas", "Guavas", "Citrus"]
        remedies = ["Focus on maintaining soil health through organic practices and balanced nutrient management.",
                    "Regularly test the soil and apply appropriate organic fertilizers based on crop requirements."]
    elif 7.5 < ph_value <= 9.0:
        soil_type = "Alkaline Soil"
        suggested_crops = ["Barley", "Mustard", "Sesame", "Millets", "Okra", "Cluster Beans"]
        remedies = ["Use organic amendments such as compost or farmyard manure.",
                    "Apply elemental sulfur or gypsum to lower the pH gradually."]
    elif 9.0 < ph_value <= 14.0:
        soil_type = "Highly Alkaline Soil"
        suggested_crops = ["Difficult to Cultivate crops"]
        remedies = ["Use organic amendments such as compost or farmyard manure.",
                    "Apply elemental sulfur or gypsum to lower the pH gradually."]
    else:
        soil_type = "Invalid pH value"
        suggested_crops = []
        remedies = []

    return soil_type, suggested_crops, remedies


valid_ph_value = False

while not valid_ph_value:
    ph_value_input = input("Enter the soil pH value: ")

    try:
        ph_value = float(ph_value_input)
        valid_ph_value = True
    except ValueError:
        print("Please enter a valid pH value.")

# Obtaining the suggestions
soil_type, suggested_crops, remedies = suggest_crops_and_remedies(ph_value)

# Displaying the results
print()
print("Soil Type:", soil_type)
print()
print("Suggested Crops:")
print()
for crop in suggested_crops:
    print("-", crop)
print()
print("Remedies:")
for remedy in remedies:
    print("-", remedy)
input()

