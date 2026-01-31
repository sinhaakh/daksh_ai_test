#!/usr/bin/env python3
import sys
import threading
import time

def input_with_timeout(prompt, reminder_timeout, exit_timeout):
    """Get input with timeout and reminder functionality."""
    result = [None]
    reminder_sent = [False]
    reminder_time = [None]
    
    def get_input():
        try:
            result[0] = input(prompt)
        except EOFError:
            result[0] = None
    
    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()
    
    start_time = time.time()
    
    while input_thread.is_alive():
        elapsed = time.time() - start_time
        
        # Check for reminder timeout (15 seconds)
        if elapsed >= reminder_timeout and not reminder_sent[0]:
            print("\nPlease enter a number (you have 30 more seconds)...")
            reminder_sent[0] = True
            reminder_time[0] = time.time()
        
        # Check for exit timeout (30 seconds after reminder)
        if reminder_sent[0]:
            time_since_reminder = time.time() - reminder_time[0]
            if time_since_reminder >= exit_timeout:
                print("\nNo input received. Exiting...")
                sys.exit(0)
        
        time.sleep(0.1)
    
    input_thread.join()
    return result[0]

def is_number(value):
    """Check if the input is a valid number."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def main():
    while True:
        user_input = input_with_timeout("Enter a number: ", reminder_timeout=15, exit_timeout=30)
        
        if user_input is None:
            print("\nNo input received. Exiting...")
            sys.exit(0)
        
        user_input = user_input.strip()
        
        if not user_input:
            print("Please enter a number.")
            continue
        
        if not is_number(user_input):
            print("Please enter a valid number.")
            continue
        
        number = float(user_input)
        double = number * 2
        print(f"The double of {number} is {double}\n")

if __name__ == "__main__":
    main()
