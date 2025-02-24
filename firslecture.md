## Installation Guide
1. Install Python from [python.org](https://www.python.org/downloads/) or Microsoft Store.
2. Use a virtual environment for project isolation: **(Important!!!)**
   - **Isolate Project Dependencies**: Each project can have its own set of package versions, avoiding conflicts.
   - **Reproducibility**: Ensure consistent environments across different machines.
   - **Clean System Packages**: Keeps the global Python installation clean.
   - **Easy Management**: Simplifies installing, upgrading, and removing packages for a specific project.
   
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install packages using pip:
   ```sh
   pip install package_name
   ```

4. Install packages from `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```
   Example `requirements.txt`:
   ```
   numpy
   pandas
   requests
   flask
   django
   scipy
   matplotlib
   seaborn
   tensorflow
   scikit-learn
   ```
5. Uninstall packages from `requirements.txt`:
### Linux/macOS
```sh
pip uninstall -r requirements.txt -y
```
### Windows
```sh
Get-Content requirements.txt | ForEach-Object { pip uninstall $_ -y } 
```

6. Choose an Integrated Development Environment (IDE) like **PyCharm** or **VS Code**.
   - **VS Code is very useful**, offering many extensions to enhance development.

## How to Run a Python Script
- Save your script as `script.py`
- Run the script using:
  ```sh
  python script.py
  ```

## Basic Code Template
```python
import argparse

def hoge(input_folder: str):
    print(f"Hello, {input_folder}!")

def main():
    parser = argparse.ArgumentParser(description="A simple Python script.")
    parser.add_argument("input_folder", type=str, help="The name to greet.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()

    hoge(args.input_folder)

    if args.verbose:
        print("Verbose mode enabled.")

if __name__ == "__main__":
    main()
```

## Examples using Pandas and NumPy
### Using Pandas
```python
import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)
```

### Using NumPy
```python
import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)

# Performing mathematical operations
arr_squared = arr ** 2
print("Squared Array:", arr_squared)
```

## Further Learning
- [Python Official Documentation](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)
