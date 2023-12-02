listOfInputFile = []
listOfNumbers = []

def extract_strings_to_list(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file and strip newline characters
            lines = [line.strip() for line in file.readlines()]
            return lines
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

string_list = extract_strings_to_list("Input.txt")

def stringReplace(line):
    line = line.replace("one", "on1ne")
    line = line.replace("two", "tw2wo")
    line = line.replace("three", "thr3hree")
    line = line.replace("four", "fou4our")
    line = line.replace("five", "fiv5ive")
    line = line.replace("six", "si6ix")
    line = line.replace("seven", "seve7even")
    line = line.replace("eight", "eigh8ight")
    line = line.replace("nine", "nin9ine")
    return line

def extract_numbers_from_list(string_list):
    for line in string_list:
        firstNumberBool, firstNumber, lastNumber = True, "", ""
        
        line = stringReplace(line)
        
        for character in line:
            if character.isdigit() and firstNumberBool == True:
                firstNumberBool, firstNumber = False, character
            elif character.isdigit():
                lastNumber = character

        if lastNumber == "":
            lastNumber = firstNumber

        combinedNumber = firstNumber + lastNumber
        listOfNumbers.append(combinedNumber)
        print(combinedNumber)
    
    return listOfNumbers

def add_numbers_from_list(listOfNumbers):
    total = 0
    for number in listOfNumbers:
        total += int(number)
    print("\nAnswer", total)


listOfNumbers = extract_numbers_from_list(string_list)
add_numbers_from_list(listOfNumbers)