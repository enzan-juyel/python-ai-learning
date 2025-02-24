import argparse
import numpy as np
import pandas as pd

def load_csv(file):
    return pd.read_csv(file)

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
    return bonus_np, bonus_pd

def main():
    parser = argparse.ArgumentParser(description="Load a CSV file")
    parser.add_argument("file", help="Read the employees.csv file")
    args = parser.parse_args()
    df = load_csv(args.file)
    bonus_np, bonus_pd = employee_bonus_calc(df)
    df['Bonus NP'] = bonus_np
    df['Bonus PD'] = bonus_pd
    # Saving the file with the new columns
    df.to_csv(".data/employees_bonus.csv", index=False)
    print(df)

if __name__ == "__main__":
    main()