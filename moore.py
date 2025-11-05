def process_moore_machine(input_string, initial_state='AA'):
    # State transition table: (Current State) -> {Input bit: Next State}
    TRANSITIONS = {
        'AA': {'0': 'AA', '1': 'BB'},
        'BB': {'0': 'CA', '1': 'DB'},
        'CA': {'0': 'DC', '1': 'BB'},
        'CC': {'0': 'DC', '1': 'BB'},
        'DB': {'0': 'BB', '1': 'CC'},
        'DC': {'0': 'BB', '1': 'CC'},
        'EC': {'0': 'DC', '1': 'EC'}  # E is an unreachable state from initial A, but included for completeness
    }

    # State output map: (State) -> Output
    OUTPUTS = {
        'AA': 'A', 'BB': 'B', 'CA': 'A', 'CC': 'C',
        'DB': 'B', 'DC': 'C', 'EC': 'C'
    }

    current_state = initial_state
    output_chars = []

    # 1. Output the initial state's output before the first input
    output_chars.append(OUTPUTS[current_state])

    for bit in input_string:
        try:
            # Move to the next state
            next_state = TRANSITIONS[current_state][bit]

            # Update the current state
            current_state = next_state

            # Output the new state's output
            output_chars.append(OUTPUTS[current_state])

            # Optional: Print step-by-step for tracing
            # print(f"Input '{bit}' -> New State: {current_state} (Output: {OUTPUTS[current_state]})")

        except KeyError as e:
            # This shouldn't happen with the correct table, but it's good practice
            print(f"Error: Invalid transition from state {current_state} on input {bit}. {e}")
            return "ERROR"

    return "".join(output_chars)


# --- Required Inputs ---
inputs = ["00110", "11001", "1010110", "1011111"]

# Process all inputs and print the results
results = {}
for i in inputs:
    results[i] = process_moore_machine(i)

# --- Display Final Results ---
print("\n" + "=" * 40)
print("FINAL MOORE MACHINE OUTPUTS")
print("=" * 40)

# Display the results in a formatted table
print(f"{'Input':<10} | {'Output (Start State A)':<25}")
print("-" * 40)
for input_str, output_str in results.items():
    print(f"{input_str:<10} | {output_str:<25}")
print("-" * 40)

# The outputs match the manual calculation:
# 00110: A A A B B B
# 11001: A B B B A B
# 1010110: A B A B A B B B
# 1011111: A B A B B C B B