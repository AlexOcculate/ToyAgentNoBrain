# Line 1:  Import json for parsing arguments passed to tools.
import json


# Line 2:  Define the ToolRegistry class that holds and executes tools.
class ToolRegistry:
    # Line 3:  Constructor that registers default tools.
    def __init__(self):
        # Line 4:  Dictionary mapping tool names to their execution functions.
        self._tools = {
            "add": self._tool_add,
            "memory_store": self._tool_memory_store,
            "memory_recall": self._tool_memory_recall,
            "memory_list": self._tool_memory_list,
        }
        # Line 5:  Reference to memory instance (injected later).
        self.memory = None

    # Line 6:  Method to inject the memory instance into the registry.
    def set_memory(self, memory_instance):
        # Line 7:  Store the reference for use in memory-related tools.
        self.memory = memory_instance

    # Line 8:  Execute a tool by name with given JSON arguments.
    def execute(self, tool_name: str, arguments_json: str) -> str:
        # Line 9:  Check if the tool exists in the registry.
        if tool_name not in self._tools:
            # Line 10:  Return error message for unknown tools.
            return f"Error: Unknown tool '{tool_name}'"

        # Line 11:  Parse the JSON arguments string into a dictionary.
        try:
            args = json.loads(arguments_json) if arguments_json else {}
        except json.JSONDecodeError:
            # Line 12:  Handle malformed JSON gracefully.
            return "Error: Invalid JSON arguments"

        # Line 13:  Call the specific tool function with parsed arguments.
        try:
            result = self._tools[tool_name](**args)
            # Line 14:  Convert result to string for consistent output format.
            return str(result)
        except Exception as e:
            # Line 15:  Catch any runtime errors during tool execution.
            return f"Error executing {tool_name}: {str(e)}"

    # Line 16:  Internal tool: Add two numbers.
    def _tool_add(self, a: float, b: float) -> str:
        # Line 17:  Perform addition and return formatted result.
        return f"{a} + {b} = {a + b}"

    # Line 18:  Internal tool: Store a value in memory.
    def _tool_memory_store(self, key: str, value: str) -> str:
        # Line 19:  Save the key-value pair to the memory instance.
        self.memory.store(key, value)
        # Line 20:  Return confirmation message.
        return f"Stored '{value}' under key '{key}'."

    # Line 21:  Internal tool: Recall a value from memory.
    def _tool_memory_recall(self, key: str) -> str:
        # Line 22:  Retrieve the value from memory; return default if not found.
        value = self.memory.recall(key)
        # Line 23:  Return the recalled value or a "not found" message.
        return (
            f"Recalled '{key}': {value}"
            if value is not None
            else f"Key '{key}' not found in memory."
        )

    # Line 24:  Internal tool: List all keys in memory.
    def _tool_memory_list(self) -> str:
        # Line 25:  Get list of all keys from memory.
        keys = self.memory.list_keys()
        # Line 26:  Return formatted list of keys.
        return f"Memory contains {len(keys)} items: {keys}"
