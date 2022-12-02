
def part_one():
    with open("Day1/input", "r") as input_file:
        current_calories = 0
        most_calories = 0
        for line in input_file:
            if line == "\n":
                most_calories = max(most_calories, current_calories)
                current_calories = 0
            else:
                current_calories += int(line)
    
    print("The most calories one Elf is carrying is " + str(most_calories))

def part_two():
    calorie_list = []
    with open("Day1/input", "r") as input_file:
        current_calories = 0
        for line in input_file:
            if line == "\n":
                calorie_list.append(current_calories)
                current_calories = 0
            else:
                current_calories += int(line)
    
    calorie_list.sort(reverse=True)
    print("The three Elves carrying the most calories are carrying " + 
        str(calorie_list[0] + calorie_list[1] + calorie_list[2]) + " in total.")

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
