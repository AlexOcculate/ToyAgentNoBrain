# Line 1:  Define the Guardrails class for input/output validation.
class Guardrails:
    # Line 2:  Constructor that sets maximum allowed input length.
    def __init__(self, max_input_length=500):
        # Line 3:  Store the maximum allowed character count for inputs.
        self.max_input_length = max_input_length

    # Line 4:  Method to validate user input before processing.
    def validate_input(self, user_input: str) -> tuple:
        # Line 5:  Check if input is empty or None.
        if not user_input or not isinstance(user_input, str):
            # Line 6:  Return False and reason for empty/invalid type.
            return False, "Input must be a non-empty string."

        # Line 7:  Check if input exceeds maximum allowed length.
        if len(user_input) > self.max_input_length:
            # Line 8:  Return False and reason for oversized input.
            return False, f"Input too long (max {self.max_input_length} chars)."

        # Line 9:  Check for forbidden patterns (e.g., injection attempts).
        if "DROP TABLE" in user_input.upper() or "rm -rf" in user_input.lower():
            # Line 10:  Return False and reason for forbidden content.
            return False, "Input contains forbidden patterns."

        # Line 11:  Input passed all checks; return True and no error.
        return True, None
