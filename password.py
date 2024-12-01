import random
import string

def generate_password():
    print("Welcome to the Password Generator!")

    try:
        # Prompt the user to specify the desired password length
        length = int(input("Enter the desired password length (minimum 6 characters): "))
        if length < 6:
            raise ValueError("Password length must be at least 6 characters.")

        # Options for password complexity
        print("\nChoose the complexity level:")
        print("1. Letters only (lowercase and uppercase)")
        print("2. Letters and numbers")
        print("3. Letters, numbers, and special characters")

        complexity = input("Enter your choice (1/2/3): ")
        if complexity not in ['1', '2', '3']:
            raise ValueError("Invalid complexity choice.")

        # Define character pools based on complexity choice
        if complexity == '1':
            char_pool = string.ascii_letters  # Letters only
        elif complexity == '2':
            char_pool = string.ascii_letters + string.digits  # Letters and numbers
        elif complexity == '3':
            char_pool = string.ascii_letters + string.digits + string.punctuation  # All

        # Generate the password
        password = ''.join(random.choice(char_pool) for _ in range(length))
        print(f"\nYour generated password is: {password}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Option to restart or exit
    again = input("\nWould you like to generate another password? (yes/no): ").strip().lower()
    if again == 'yes':
        generate_password()
    else:
        print("Goodbye! Stay secure.")

# Run the password generator
generate_password()
