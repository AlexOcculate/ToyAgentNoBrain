Here is the proposed explanation for **File #4: `Harness/tools.py`**.

### File 4/9: `Harness/tools.py`

**Concept:** The Agent’s "Hands" & Action Executor
**Complexity Level:** 3/10 (Function Registry & Execution)

---

#### 🎬 Manim Visual Scene Description

1.  **Title Card:** Title fades in: `tools.py`. Subtitle: *"The Agent's Hands."*
2.  **The Tool Shed:**
    *   A large cabinet or "Tool Shed" appears. Label it `ToolRegistry`.
    *   Inside, four distinct slots are visible, labeled: `add`, `memory_store`, `memory_recall`, `memory_list`.
3.  **The Request:**
    *   A message envelope arrives from the left (representing the LM). It contains: `Name: "add"`, `Args: {"a": 10, "b": 20}`.
    *   The envelope flies into the `ToolRegistry`.
4.  **The Lookup & Execution:**
    *   A spotlight shines on the `add` slot.
    *   A small function icon labeled `_tool_add` pops out.
    *   The arguments `10` and `20` are plugged into the function.
    *   The function calculates: `10 + 20 = 30`.
5.  **The Return:**
    *   A result package labeled `"10.0 + 20.0 = 30.0"` is handed back out of the registry.
6.  **The Error Case (Flashback):**
    *   A request for a tool named `fly` arrives.
    *   The registry scans its slots, finds no `fly` slot.
    *   It returns a red error package: `"Error: Unknown tool 'fly'"`.

---

#### 🎙️ Narrator Script

> "Now we have the brain (which decides what to do) and the memory (where it keeps notes). But an agent that can only think is useless. It needs hands to act on the world.
>
> This file defines the `ToolRegistry`. Think of this as a tool shed. The agent doesn’t build tools; it just picks them up, uses them, and puts them back.
>
> The registry maintains a dictionary mapping tool names (like `"add"`) to their actual Python functions (`_tool_add`).
>
> Here is the workflow:
> 1. **The Call:** The LM sends a request: "I want to use the `add` tool with arguments `a=10, b=20`."
> 2. **The Lookup:** The registry checks if `add` exists in its dictionary.
> 3. **The Execution:** If it exists, it parses the JSON arguments and calls the specific function `_tool_add(10, 20)`.
> 4. **The Result:** The function returns a string result, which is passed back to the agent loop.
>
> Notice that `memory_store` and `memory_recall` are also tools here. This means "remembering" is just another action the agent can perform, just like doing math.
>
> Crucially, this file handles errors gracefully. If the LM asks for a tool that doesn’t exist, or sends broken JSON, the registry catches it and returns an error string instead of crashing the whole program. This makes the harness robust."

