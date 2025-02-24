# Python-ai-learning
# Python Programming Language

## What is Python?
Python is a high-level, **interpreted** programming language known for its **simplicity**, **readability**, and **versatility**. It is widely used in web development, data science, artificial intelligence (AI), automation, and more.

## Key Features of Python
1. **Easy to Learn and Read** – Python has a simple syntax similar to English, making it beginner-friendly.
2. **Interpreted Language** – Python runs code line by line, making debugging easier.
3. **Dynamically Typed** – No need to define variable types explicitly.
4. **Cross-Platform** – Works on Windows, macOS, and Linux.
5. **Large Standard Library** – Built-in modules for handling files, databases, networking, and more.
6. **Object-Oriented and Functional** – Supports multiple programming paradigms.
7. **Huge Community Support** – One of the most widely used languages with active support.

## Common Uses of Python
- **Web Development** – Frameworks like Django and Flask
- **Data Science & Machine Learning** – Libraries like Pandas, NumPy, Scikit-Learn, TensorFlow
- **Automation & Scripting** – Writing scripts to automate tasks
- **Game Development** – Using Pygame or Unity with Python scripting
- **Cybersecurity & Ethical Hacking** – Writing security tools and penetration testing
- **Embedded Systems & IoT** – Using MicroPython for hardware programming

## Basic Example of Python Code
```python
# Hello World Program
print("Hello, World!")
```

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

5. Choose an Integrated Development Environment (IDE) like **PyCharm** or **VS Code**.
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

## Further Learning
- [Python Official Documentation](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)
