# Line 1:  Import necessary modules from the Harness package.
from .simulated_lm import SimulatedLM
from .tools import ToolRegistry
from .memory import Memory
from .guardrails import Guardrails
from .trace_logger import TraceLogger


# Line 6:  Define the Agent class that orchestrates the loop.
class Agent:
    # Line 7:  Constructor that initializes all components of the agent harness.
    def __init__(self, max_iterations=5):
        # Line 8:  Initialize the simulated language model (the "brain").
        self.lm = SimulatedLM()

        # Line 9:  Initialize memory storage.
        self.memory = Memory()

        # Line 10:  Initialize tool registry and inject memory reference.
        self.tools = ToolRegistry()
        self.tools.set_memory(self.memory)

        # Line 12:  Initialize guardrails for input validation.
        self.guardrails = Guardrails()

        # Line 13:  Initialize trace logger for visibility.
        self.logger = TraceLogger()

        # Line 14:  Set maximum iterations to prevent infinite loops.
        self.max_iterations = max_iterations

    # Line 15:  Main method to run the agent with a user prompt.
    def run(self, user_input: str) -> str:
        # Line 16:  Log the start of execution.
        self.logger.log("LOOP", f"Starting agent loop for input: '{user_input}'")

        # Line 17:  Validate input using guardrails.
        valid, error_msg = self.guardrails.validate_input(user_input)

        # Line 18:  If input is invalid, log and return error immediately.
        if not valid:
            # Line 19:  Log the validation failure.
            self.logger.log("GUARDRAILS", f"Input blocked: {error_msg}")
            # Line 20:  Return the error message as the final response.
            return f"Error: {error_msg}"

        # Line 21:  Initialize conversation history with system and user messages.
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]

        # Line 24:  Initialize iteration counter for loop control.
        iteration = 0

        # Line 25:  Start the main agent loop.
        while iteration < self.max_iterations:
            # Line 26:  Increment iteration counter at start of each cycle.
            iteration += 1
            # Line 27:  Log the current iteration number.
            self.logger.log("LOOP", f"Iteration {iteration}/{self.max_iterations}")

            # Line 28:  Call the LM to generate a response based on current context.
            try:
                response = self.lm.generate(messages)
            except Exception as e:
                # Line 30:  If the LM itself crashes, catch it and stop gracefully.
                self.logger.log("LM", f"CRITICAL: LM raised an exception: {e}")
                return "Error: LM crashed unexpectedly."

            # Line 32:  Validate that the response is a dictionary with required keys.
            if not isinstance(response, dict) or "content" not in response:
                # Line 33:  If response is malformed, log and stop gracefully.
                self.logger.log(
                    "LM", f"MALFORMED: LM returned invalid structure: {response}"
                )
                return "Error: Malformed response from LM."

            # Line 35:  Log the LM's decision (content or tool call).
            if response.get("tool_calls"):
                # Line 36:  Log that a tool call was requested.
                self.logger.log(
                    "LM",
                    f"Decision: Call tool {response['tool_calls'][0]['function']['name']}",
                )
            else:
                # Line 37:  Log the final text response from LM.
                self.logger.log("LM", f"Response: {response['content']}")

            # Line 38:  Check if LM decided to stop (no tool calls).
            if not response.get("tool_calls"):
                # Line 39:  Log that the agent is finishing.
                self.logger.log("LOOP", "Agent finished: No more tool calls.")
                # Line 40:  Return the final content as the result.
                return response["content"]

            # Line 41:  Execute the requested tool call.
            tool_call = response["tool_calls"][0]

            # Line 42:  Validate that tool_call has required structure.
            if "function" not in tool_call or "name" not in tool_call["function"]:
                # Line 43:  If tool call is malformed, log and stop.
                self.logger.log(
                    "LM", f"MALFORMED: Invalid tool call structure: {tool_call}"
                )
                return "Error: Malformed tool call from LM."

            func_name = tool_call["function"]["name"]
            args_json = tool_call["function"].get("arguments", "{}")

            # Line 47:  Log the tool execution start.
            self.logger.log("TOOLS", f"Executing: {func_name}({args_json})")

            # Line 48:  Execute the tool and get the result.
            try:
                tool_result = self.tools.execute(func_name, args_json)
            except Exception as e:
                # Line 50:  If tool execution crashes unexpectedly (shouldn't happen with registry), catch it.
                self.logger.log("TOOLS", f"CRITICAL: Tool execution crashed: {e}")
                tool_result = f"Error: Unexpected crash in tool {func_name}"

            # Line 53:  Log the tool execution result.
            self.logger.log("TOOLS", f"Result: {tool_result}")

            # Line 54:  Append assistant's tool call decision to history.
            messages.append(
                {
                    "role": "assistant",
                    "content": response["content"],
                    "tool_calls": response["tool_calls"],
                }
            )

            # Line 55:  Append the tool result as a new user/tool message to history.
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.get("id", "unknown"),
                    "content": tool_result,
                }
            )

        # Line 60:  If loop exhausted max iterations, log and return timeout error.
        self.logger.log("LOOP", "STOPPED: Max iterations reached.")
        # Line 61:  Return error message indicating loop limit hit.
        return "Error: Agent stopped due to max iteration limit."
