# Day 1 project

def GenerateBandName(location, name):
    return (location + " " + name)

if __name__ == "__main__":
    print("Welcome to the Band Name Generator.")
    location = input("Where did you grow up?\n")
    name = input("What was your first pet's name?\n")
    print(GenerateBandName(location, name))