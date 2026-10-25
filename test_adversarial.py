# Line 1:  Import sys and os for path setup to ensure local imports work.
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Line 3:  Import the Agent class from the Harness package.
from Harness.agent import Agent


# ──────────────────────────────────────────────
#  TEST 1: Broken / Chaotic LM
#  Proves: the system doesn't crash on malformed output
# ──────────────────────────────────────────────
def test_broken_lm():
    # Line 8:  Create an agent instance.
    agent = Agent()

    # Line 9:  Monkey-patch the LM's generate method to return garbage.
    def broken_generate(messages):
        # Line 10:  Return a malformed dictionary missing required keys.
        return {"invalid_key": "garbage"}

    # Line 12:  Replace the real LM with the broken one.
    agent.lm.generate = broken_generate

    # Line 13:  Run the agent; it should not crash but handle the error gracefully.
    result = agent.run("add 1 and 1")

    # Line 14:  Assert that a string was returned (not an exception).
    assert isinstance(result, str), "Agent must return a string even with broken LM"
    # Line 15:  Assert that the error is explicitly mentioned.
    assert (
        "Malformed" in result or "Error" in result
    ), "Should report malformed response"


# ──────────────────────────────────────────────
#  TEST 2: Invalid / Hostile Input
#  Proves: guardrails block bad input before it reaches the core
# ──────────────────────────────────────────────
def test_hostile_input():
    # Line 20:  Create an agent instance.
    agent = Agent()

    # Line 21:  Try to send an oversized input (exceeds 500 char limit).
    long_input = "A" * 1000

    # Line 22:  Run the agent with hostile input.
    result = agent.run(long_input)

    # Line 23:  Assert that the result contains an error message about length.
    assert "too long" in result.lower(), "Guardrails must block oversized input"


# ──────────────────────────────────────────────
#  TEST 3: Tool Execution Failure
#  Proves: a failing tool doesn't crash the loop; error is handled
# ──────────────────────────────────────────────
def test_tool_failure():
    # Line 29:  Create an agent instance.
    agent = Agent()

    # Line 30:  Monkey-patch a tool to raise an exception.
    def failing_add(a, b):
        # Line 31:  Raise a deliberate error to simulate failure.
        raise ValueError("Simulated calculation error")

    # Line 33:  Replace the add tool with the failing version.
    agent.tools._tools["add"] = failing_add

    # Line 34:  Run the agent requesting addition.
    result = agent.run("add 5 and 5")

    # Line 35:  Assert that the system did not crash and returned a string.
    assert isinstance(result, str), "Agent must survive tool failure"
    # Line 36:  The result might be a generic LM response because SimulatedLM is simple,
    # but it must not be a traceback or exception object.


# ──────────────────────────────────────────────
#  TEST 4: Infinite Loop / Max Iterations
#  Proves: the iteration guardrail stops runaway loops
# ──────────────────────────────────────────────
def test_infinite_loop():
    # Line 41:  Create an agent with a low max iteration limit for speed.
    agent = Agent(max_iterations=3)

    # Line 42:  Monkey-patch LM to always request a tool call (never stops).
    def infinite_generate(messages):
        # Line 43:  Always return a valid tool call structure to force looping.
        return {
            "role": "assistant",
            "content": "Thinking...",
            "tool_calls": [
                {
                    "id": "call_inf_001",
                    "type": "function",
                    "function": {"name": "add", "arguments": '{"a": 1, "b": 1}'},
                }
            ],
        }

    # Line 54:  Replace the real LM with the infinite loop simulator.
    agent.lm.generate = infinite_generate

    # Line 55:  Run the agent; it must stop at max iterations.
    result = agent.run("start")

    # Line 56:  Assert that the max iteration error message is returned.
    assert (
        "max iteration" in result.lower()
    ), "Agent must stop when max iterations are reached"


# ──────────────────────────────────────────────
#  TEST 5: Memory Persistence Across Agent Instances
#  Proves: Memory can be shared or persisted correctly if designed for it
# ──────────────────────────────────────────────
def test_module_specific():
    # Line 62:  Create a first agent instance.
    agent1 = Agent()

    # Line 63:  Store a value in the first agent's memory.
    agent1.memory.store("test_key", "test_value")

    # Line 64:  Verify the value is stored in agent1.
    assert agent1.memory.recall("test_key") == "test_value", "Memory store failed"

    # Line 65:  Create a second agent instance (fresh memory).
    agent2 = Agent()

    # Line 66:  Verify that agent2 has its own isolated memory (default behavior).
    assert (
        agent2.memory.recall("test_key") is None
    ), "Memory should be isolated per instance by default"


# ──────────────────────────────────────────────
#  RUNNER
# ──────────────────────────────────────────────
if __name__ == "__main__":
    # Line 73:  Define list of test functions and their descriptions.
    tests = [
        ("Broken LM / Chaotic output", test_broken_lm),
        ("Hostile / Invalid input", test_hostile_input),
        ("Tool execution failure", test_tool_failure),
        ("Infinite loop / Max iterations", test_infinite_loop),
        ("Memory persistence isolation", test_module_specific),
    ]

    # Line 80:  Initialize counter for passed tests.
    passed = 0

    # Line 81:  Iterate through each test case.
    for name, fn in tests:
        # Line 82:  Try to execute the test function.
        try:
            # Line 83:  Call the test function.
            fn()
            # Line 84:  Print pass message and increment counter.
            print(f"  PASS  {name}")
            passed += 1
        except Exception as e:
            # Line 86:  Catch any exception and print fail message with error details.
            print(f"  FAIL  {name}: {e}")

    # Line 88:  Print summary of test results.
    print(f"\n  {passed}/{len(tests)} tests passed.")

    # Line 89:  Exit with code 1 if any test failed.
    if passed < len(tests):
        # Line 90:  Trigger non-zero exit code for CI/CD integration.
        sys.exit(1)
