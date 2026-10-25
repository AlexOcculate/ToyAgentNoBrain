# Line 1:  Define ANSI color codes for terminal output without external libraries.
class Colors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    BG_L_GREEN = "\033[102m"
    BG_L_RED = "\033[101m"
    BG_L_YELLOW = "\033[103m"


# Line 8:  Define the TraceLogger class for structured, colored logging.
class TraceLogger:
    # Line 9:  Constructor that initializes an empty log list.
    def __init__(self):
        # Line 10:  List to store all log entries with their metadata.
        self.log_entries = []

    # Line 11:  Method to log a message with specific component and level.
    def log(self, component: str, message: str, level: str = "INFO"):
        # Line 12:  Assign color based on the component type.
        color = {
            "LM": Colors.CYAN,
            "TOOLS": Colors.YELLOW,
            "LOOP": Colors.GREEN,
            "GUARDRAILS": Colors.RED,
            "MEMORY": Colors.MAGENTA,
        }.get(component, Colors.RESET)

        # Line 18:  Format the log entry with timestamp placeholder and color.
        entry = f"{color}[{component}] {message}{Colors.RESET}"

        # Line 19:  Append the formatted entry to the internal log list.
        self.log_entries.append(entry)

        # Line 20:  Print immediately to console for real-time feedback.
        print(entry)

    # Line 21:  Method to print the full trace report after execution.
    def report(self):
        # Line 22:  Print a separator line for visual clarity.
        print("\n" + "=" * 50)
        print("FULL TRACE REPORT")
        print("=" * 50)

        # Line 25:  Iterate through all stored log entries and print them.
        for entry in self.log_entries:
            # Line 26:  Print each log line individually.
            print(entry)

        # Line 27:  Print closing separator.
        print("=" * 50 + "\n")
