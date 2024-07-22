import re
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def check_password_strength(password):
    criteria = [
        (len(password) >= 8, "At least 8 characters long"),
        (len(re.findall(r'\d', password)) >= 2, "Contains at least two numbers"),
        (len(re.findall(r'[!@#$%^&*(),.?":{}|<>" "/¬]', password)) >= 2, "Contains at least two special characters"),
        (bool(re.search(r'[A-Z]', password) and re.search(r'[a-z]', password)), "Contains both uppercase and lowercase letters")
    ]

    met_criteria = sum(1 for criterion, _ in criteria if criterion)
    return met_criteria, criteria

def colored_symbol(met):
    return f"{Fore.GREEN}✓{Style.RESET_ALL}" if met else f"{Fore.RED}✗{Style.RESET_ALL}"

def get_strength_rating(met_criteria):
    if met_criteria == 0:
        return f"{Fore.RED}Very Weak{Style.RESET_ALL}"
    elif met_criteria in [1, 2]:
        return f"{Fore.YELLOW}Weak{Style.RESET_ALL}"
    elif met_criteria == 3:
        return f"{Fore.GREEN}Strong{Style.RESET_ALL}"
    else:
        return f"{Fore.BLUE}Very Strong{Style.RESET_ALL}"

def main():
    print("Password Policy:")
    print("- At least 8 characters long")
    print("- Contains at least two numbers")
    print("- Contains at least two special characters")
    print("- Contains both uppercase and lowercase letters")
    print()

    while True:
        password = input("Enter a password to check its strength: ")
        met_criteria, criteria_results = check_password_strength(password)

        print("\nPassword strength check results:")
        for met, description in criteria_results:
            symbol = colored_symbol(met)
            print(f"{symbol} {description}")

        strength_rating = get_strength_rating(met_criteria)
        print(f"\nPassword strength: {strength_rating}")

        if met_criteria == 4:
            print("Congratulations! You have a very strong password.")
            break
        else:
            print("Please try again to create a stronger password.\n")

if __name__ == "__main__":
    main()
