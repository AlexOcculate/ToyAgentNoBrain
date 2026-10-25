# Line 1:  Import json module for parsing and generating structured tool calls.
import json


# Line 2:  Define the SimulatedLM class which acts as the "brain" of the agent.
class SimulatedLM:
    # Line 3:  Constructor that initializes the simulated language model.
    def __init__(self):
        # Line 4:  Store a reference to this instance for potential state tracking.
        self.name = "SimulatedLM-v1"

    # Line 5:  Main method that generates a response based on input context.
    def generate(self, messages: list) -> dict:
        # Line 6:  Extract the last user message from the conversation history.
        last_message = messages[-1]["content"] if messages else ""

        # Line 7:  Convert message to lowercase for case-insensitive keyword matching.
        msg_lower = last_message.lower()

        # Line 8:  Initialize default response structure (no tool call).
        response = {
            "role": "assistant",
            "content": "I don't know how to handle that.",
            "tool_calls": [],
        }

        # Line 9:  Rule 1: If user asks to add numbers, simulate a tool call.
        if "add" in msg_lower:
            # Line 10:  Extract all numeric tokens from the entire message using a simple loop.
            numbers = []
            current_num = ""
            for char in last_message:
                # Line 12:  If character is a digit or dot, append to current number string.
                if char.isdigit() or char == ".":
                    current_num += char
                else:
                    # Line 14:  If character is not part of a number, try to convert current buffer.
                    if current_num:
                        try:
                            # Line 16:  Convert buffer to float and add to numbers list.
                            numbers.append(float(current_num))
                        except ValueError:
                            pass
                        # Line 19:  Reset buffer for next potential number.
                        current_num = ""
            # Line 21:  Check if there is a last number being built at the end of the string.
            if current_num:
                try:
                    numbers.append(float(current_num))
                except ValueError:
                    pass

            # Line 25:  If we found at least two numbers, construct the tool call.
            if len(numbers) >= 2:
                # Line 26:  Take the first two numbers found in the text.
                num1 = numbers[0]
                num2 = numbers[1]

                # Line 29:  Construct the tool call JSON structure.
                response["tool_calls"] = [
                    {
                        "id": "call_add_001",
                        "type": "function",
                        "function": {
                            "name": "add",
                            "arguments": json.dumps({"a": num1, "b": num2}),
                        },
                    }
                ]
                # Line 38:  Set assistant content to indicate tool usage.
                response["content"] = f"Calling add({num1}, {num2})..."
            else:
                # Line 40:  Fallback if "add" is mentioned but no valid numbers found.
                response["content"] = "I couldn't parse the numbers for addition."

        # Line 42:  Rule 2: If user asks to store in memory.
        elif "store" in msg_lower or "remember" in msg_lower:
            # Line 43:  Extract the value to store (everything after "store" or "remember").
            key_part = (
                last_message.split("store", 1)[-1]
                if "store" in msg_lower
                else last_message.split("remember", 1)[-1]
            )
            value = key_part.strip().strip('"').strip("'")

            # Line 46:  If value is empty, default to a placeholder.
            if not value:
                value = "empty_value"

            # Line 49:  Construct tool call for memory_store.
            response["tool_calls"] = [
                {
                    "id": "call_mem_001",
                    "type": "function",
                    "function": {
                        "name": "memory_store",
                        "arguments": json.dumps({"key": "last_item", "value": value}),
                    },
                }
            ]
            # Line 58:  Set assistant content.
            response["content"] = f"Storing '{value}' in memory."

        # Line 60:  Rule 3: If user asks to recall from memory.
        elif "recall" in msg_lower or "remembered" in msg_lower:
            # Line 61:  Construct tool call for memory_recall.
            response["tool_calls"] = [
                {
                    "id": "call_mem_002",
                    "type": "function",
                    "function": {
                        "name": "memory_recall",
                        "arguments": json.dumps({"key": "last_item"}),
                    },
                }
            ]
            # Line 70:  Set assistant content.
            response["content"] = "Recalling from memory..."

        # Line 72:  Rule 4: If user asks to list memory.
        elif "list" in msg_lower and "memory" in msg_lower:
            # Line 73:  Construct tool call for memory_list.
            response["tool_calls"] = [
                {
                    "id": "call_mem_003",
                    "type": "function",
                    "function": {"name": "memory_list", "arguments": json.dumps({})},
                }
            ]
            # Line 82:  Set assistant content.
            response["content"] = "Listing memory contents..."

        # Line 84:  Return the structured response.
        return response
