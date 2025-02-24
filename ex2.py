import argparse
import numpy as np
import pandas as pd
import requests as rq

def load_csv(file):
    return pd.read_csv(file)

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = rq.get(url)
    return response.json()

def employee_bonus_calc(df):
    # If Experience >= 10, bonus is 10% of Salary, else 8% of Salary
    bonus_np = np.where(df['Experience'] >= 10, df['Salary'] * 0.10, df['Salary'] * 0.08)
    bonus_pd = df['Salary'] * df['Experience'].apply(lambda x: 0.10 if x >= 10 else 0.08)
    senior_employees = df[df['Experience'] >= 10]
    junior_employees = df[df['Experience'] < 10]
    print(f"Senior Employees: {len(senior_employees)}")
    print(senior_employees)
    print(f"Junior Employees: {len(junior_employees)}")
    print(junior_employees)
    return bonus_pd

def main():
    parser = argparse.ArgumentParser(description="Load a CSV file")
    parser.add_argument("file", help="Read the employees.csv file")
    args = parser.parse_args()

    users = get_users()
    df_employees = pd.read_csv(args.file)
    df = pd.DataFrame(users)

    df['Name'] = df['name']
    # Adding the columns from the employees.csv file
    df['Age'] = df_employees['Age']
    df['Salary'] = df_employees['Salary']
    df['Experience'] = df_employees['Experience']
    df['Dept'] = df_employees['Dept']

    bonus = employee_bonus_calc(df)
    df['Bonus'] = bonus

    # Removing 'id' and name column if exists
    df = df.drop(columns=['id', 'name'], errors='ignore')

    # Reordering the columns to match the original file
    column_order = ['Name', 'Age', 'Salary', 'Experience', 'Dept', 'Bonus'] + list(df.columns[:-6])
    df = df[column_order]

    # Capitiliazing the first letter of the column names
    df.columns = df.columns.str.capitalize()

    df.to_csv(".data/employees_bonus.csv", index=False)
    print(df)



if __name__ == "__main__":
    main()