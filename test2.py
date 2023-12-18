import pandas as pd

def calculate_demographic_data(file_path):
    # Read the data into a DataFrame
    data = pd.read_csv(file_path)

    # How many people of each race are represented in this dataset?
    race_count = data['race'].value_counts()

    # What is the average age of men?
    average_age_men = data[data['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (data['education'] == 'Bachelors').mean() * 100

    # What percentage of people with advanced education make more than 50K?
    higher_education = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = data[higher_education & (data['salary'] == '>50K')].shape[0] / data[higher_education].shape[0] * 100

    # What percentage of people without advanced education make more than 50K?
    lower_education = ~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_rich = data[lower_education & (data['salary'] == '>50K')].shape[0] / data[lower_education].shape[0] * 100

    # What is the minimum number of hours a person works per week?
    min_work_hours = data['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = data[data['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    highest_earning_country = (data[data['salary'] == '>50K']['native-country'].value_counts() / data['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (data[data['salary'] == '>50K']['native-country'].value_counts() / data['native-country'].value_counts()).max() * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Return a dictionary with all the results
    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }
