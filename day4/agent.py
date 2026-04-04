import re
from tools import calculate_average, summarize

def extract_numbers(query):
    numbers = re.findall(r'\d+', query)
    return list(map(int, numbers))

def main():

    query = input("Enter task: ")

    print("\nStep 1: Extracting numbers...")
    numbers = extract_numbers(query)
    print("Numbers:", numbers)

    print("\nStep 2: Calculating average...")
    avg = calculate_average(numbers)
    print("Average:", avg)

    print("\nStep 3: Summarizing...")
    summary = summarize(f"The average is {avg}")
    print(summary)

if __name__ == "__main__":
    main()