# Line 1:  Import the Agent class from the Harness package.
from Harness.agent import Agent


# Line 2:  Define the main entry point function.
def main():
    # Line 3:  Create an instance of the Agent with default settings.
    agent = Agent(max_iterations=5)

    # Line 4:  Define a sample user prompt to test the agent.
    test_prompt = "Please add 10 and 20"

    # Line 5:  Run the agent with the test prompt.
    result = agent.run(test_prompt)

    # Line 6:  Print the final result to the console.
    print(f"\nFINAL RESULT: {result}")

    # Line 7:  Generate and print the full trace report for visibility.
    agent.logger.report()


# Line 9:  Standard Python entry point check.
if __name__ == "__main__":
    # Line 10:  Call the main function when script is executed directly.
    main()
