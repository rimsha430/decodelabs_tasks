import string
import secrets

def get_password_length():
    """Phase 1: Input validation"""
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                print("For security, please choose a length of at least 8.")
                continue
            return length
        except ValueError:
            print("Please enter a valid whole number.")

def generate_password(length):
    """Phase 2: Backend transformation engine"""
    # Build the character pool
    characters = string.ascii_letters + string.digits

    # Use secrets.choice() instead of random.choice() for cryptographic security
    password_chars = [secrets.choice(characters) for _ in range(length)]

    # Use .join() instead of += for O(N) efficiency instead of O(N^2)
    password = ''.join(password_chars)
    return password

def calculate_entropy(length, pool_size=62):
    """Phase 3: Mathematical proof of strength (E = L * log2(R))"""
    import math
    return length * math.log2(pool_size)

def main():
    print("=== DecodeLabs Secure Password Generator ===")
    length = get_password_length()
    password = generate_password(length)
    entropy = calculate_entropy(length)

    print(f"\nGenerated Password: {password}")
    print(f"Entropy: {entropy:.2f} bits")

if __name__ == "__main__":
    main()