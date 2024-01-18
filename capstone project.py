#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
file_path="project.csv"
df = pd.read_csv(file_path)


# In[2]:


#####3Identify suicide clusters and hotspots based on historical trends and geographic locations.

# Group data by state and calculate the average number of cases per state
statewise_avg_cases = df.groupby('State')['Total'].mean().sort_values(ascending=False)

# Calculate the overall average number of cases
overall_avg = df['Total'].mean()

# Identify states with higher-than-average suicide rates (potential hotspots)
hotspot_states = statewise_avg_cases[statewise_avg_cases > overall_avg]

# Plotting a bar chart for potential suicide hotspots
plt.figure(figsize=(12, 8))
hotspot_states.plot(kind='bar', color='salmon')
plt.axhline(y=overall_avg, color='gray', linestyle='--', label='Overall Average')
plt.title('Potential Suicide Hotspots by State')
plt.xlabel('State')
plt.ylabel('Average Cases')
plt.legend()
plt.show()

# Display the identified hotspot states
print("\nPotential Suicide Hotspot States:")
print(hotspot_states)

statewise_total_cases = df.groupby('State')['Total'].sum().sort_values(ascending=False)

# Identify the state with the fourth-highest total number of cases
fourth_max_state = statewise_total_cases.index[2]
fourth_max_cases = statewise_total_cases.iloc[2]

# Identify the state with the lowest total number of cases
min_state = statewise_total_cases.idxmin()
min_cases = statewise_total_cases.min()

# Print the results
print("State with the Fourth-Highest Total Cases:*****", fourth_max_state, "****Total Cases:", fourth_max_cases)
print("State with the Lowest Total Cases:", min_state, "Total Cases:", min_cases)


# In[3]:


###meaining ful insights from it


# Group data by cause, gender, and age group
cause_gender_age_group = df.groupby(['Type', 'Gender', 'Age_group'])['Total'].sum().reset_index()

# Plotting a bar chart for top causes of death
plt.figure(figsize=(14, 8))
sns.barplot(x='Total', y='Type', hue='Gender', data=cause_gender_age_group.sort_values(by='Total', ascending=False).head(10), palette='viridis')
plt.title('Top 10 Causes of Death by Gender and Age Group')
plt.xlabel('Total Cases')
plt.ylabel('Cause of Death')
plt.show()


# Plotting a pie chart for the distribution of suicides across age groups
plt.figure(figsize=(8, 8))
df['Age_group'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, explode=(0.1, 0, 0, 0, 0, 0), colors=sns.color_palette('pastel'))
plt.title('Distribution of Suicides Across Age Groups')
plt.show()


# Plotting a bar chart for gender-wise comparison
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=df, palette='Set2')
plt.title('Gender-wise Distribution of Suicides')
plt.xlabel('Gender')
plt.ylabel('Total Cases')
plt.show()


# Assuming 'Year' is present in the dataset
# Plotting a line chart for trends over the years
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Total', data=df, estimator='sum', ci=None)
plt.title('Trends in Suicides Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Cases')
plt.show()
# Group data by cause and age group
cause_age_group = df.groupby(['Type', 'Age_group'])['Total'].sum().reset_index()

# Plotting a bar chart for top causes of death by age group
plt.figure(figsize=(14, 8))
sns.barplot(x='Total', y='Type', hue='Age_group', data=cause_age_group.sort_values(by='Total', ascending=False).head(10), palette='muted')
plt.title('Top 10 Causes of Death by Age Group')
plt.xlabel('Total Cases')
plt.ylabel('Cause of Death')
plt.show()


# In[ ]:


import tkinter as tk
from tkinter import ttk

# Define the helpline numbers for different regions
helpline_numbers = {
    'National Suicide Prevention Lifeline': '1-800-273-TALK (8255)',
    'Vandrevala Foundation (for emotional support)': '1860 2662 345 / 1800 2333 330',
    'Roshni (Hyderabad-based helpline)': '040 6620 2000 / 040 6620 2001',
    # Add more helpline numbers as needed
}

class SuicideHelplineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Suicide Helpline Numbers")

        # Create a treeview widget to display regions and helpline numbers
        self.tree = ttk.Treeview(root, columns=('Helpline Number'))
        self.tree.heading('#0', text='Region')
        self.tree.heading('#1', text='Helpline Number')

        # Insert helpline numbers into the treeview
        for region, number in helpline_numbers.items():
            self.tree.insert('', 'end', text=region, values=(number))

        # Pack the treeview into the window
        self.tree.pack(expand=True, fill='both')

def main():
    # Create the main window
    root = tk.Tk()
    app = SuicideHelplineApp(root)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:


### aware ness
# Function to display a message about suicide prevention and provide helpline numbers
def suicide_prevention_message():
    print("********************************************")
    print("**          Suicide Prevention            **")
    print("********************************************\n")

    print("If you or someone you know is in crisis, please seek help immediately.")
    print("You are not alone, and help is available. Reach out to someone you trust or contact one of the helpline numbers below:\n")

    # Helpline numbers
    helpline_numbers = {
        'National Suicide Prevention Lifeline': '1-800-273-TALK (8255)',
        'Vandrevala Foundation (for emotional support)': '1860 2662 345 / 1800 2333 330',
        'Roshni (Hyderabad-based helpline)': '040 6620 2000 / 040 6620 2001',
        # Add more helpline numbers as needed
    }

    for organization, number in helpline_numbers.items():
        print(f"{organization}: {number}")

    print("\nYou matter. Your life matters. Please reach out for support.")
    print("********************************************")

# Call the function to display the message
suicide_prevention_message()


# In[ ]:




