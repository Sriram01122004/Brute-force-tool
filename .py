from itertools import product

def brute_force_phone_pin():
    # Simulate a phone's lock screen
    correct_pin = "123456789"  # Replace with the actual PIN (for testing purposes)
    max_attempts = 10  # Simulate a limit on attempts
    attempts = 0

    # Generate all possible 4-digit PINs
    digits = "0123456789"
    for pin in product(digits, repeat=4):
        pin_attempt = "".join(pin)
        attempts += 1

        print(f"Trying PIN: {pin_attempt}")

        # Simulate checking the PIN
        if pin_attempt == correct_pin:
            print(f"PIN found: {pin_attempt}")
            return
        elif attempts >= max_attempts:
            print("Maximum attempts reached. Phone is locked.")
            return

    print("PIN not found in the list.")

def main():
    print("Starting brute-force attack on phone PIN...")
    brute_force_phone_pin()

if __name__ == "__main__":
    main()
