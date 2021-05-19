# Store country:total_number_of_covid-19_cases pairs into a dictionary
Coronavirus_Rate = {'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
print(Coronavirus_Rate)

# Get the Keys from Coronavirus_Rate dictionary & store in a list
labels = list(Coronavirus_Rate.keys())
# Get the Values from Coronavirus_Rate dictionary & store in a list
values = list(Coronavirus_Rate.values())

# Construct Pie Chart for Coronavirus_Rate using matplotlib
import matplotlib.pyplot as plt
plt.pie(values, labels=labels, autopct=lambda p:f'{p:.2f}%, \n {p*sum(values)/100 :.0f} cases')
plt.title('Total number of Covid-19 cases in 5 different countries')
plt.show()