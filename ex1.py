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