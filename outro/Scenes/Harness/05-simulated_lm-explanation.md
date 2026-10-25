Here is the proposed explanation for **File #5: `Harness/simulated_lm.py`**.

### File 5/9: `Harness/simulated_lm.py`

**Concept:** The "Brain" & Decision Engine
**Complexity Level:** 4/10 (Pattern Matching & Logic)

---

#### 🎬 Manim Visual Scene Description

1.  **Title Card:** Title fades in: `simulated_lm.py`. Subtitle: *"The Simulated Brain."*
2.  **The Black Box:**
    *   A complex, glowing neural network graphic appears but is immediately replaced by a simple, transparent box labeled `SimulatedLM`.
    *   Text appears: *"No Magic. Just Rules."*
3.  **The Input Stream:**
    *   A text stream enters the box from the left: `"Please add 10 and 20"`.
4.  **The Keyword Scanner:**
    *   Inside the box, a scanner light sweeps across the text.
    *   It highlights the word **"add"** in bright yellow.
    *   A second scanner highlights the numbers **10** and **20**.
5.  **The Decision Tree:**
    *   A flowchart appears inside the box:
        *   `IF "add" in text AND numbers found` -> `ACTION: Call Tool 'add'`
        *   `ELSE IF "store" in text` -> `ACTION: Call Tool 'memory_store'`
        *   `ELSE` -> `ACTION: Return Default Text`
    *   The path for `"add"` lights up green.
6.  **The Output:**
    *   A structured JSON object exits the box to the right.
    *   It contains: `"tool_calls": [{"name": "add", "arguments": {"a": 10, "b": 20}}]`.
    *   The text `Calling add(10.0, 20.0)...` appears next to it.

---

#### 🎙️ Narrator Script

> "This is the heart of our toy agent: the `SimulatedLM`.
>
> In a real production system, this would be an API call to a massive neural network like GPT-4. It would take your prompt, process it through billions of parameters, and return a response. That process is opaque—it’s a 'black box.'
>
> For our curriculum, we want to see *inside* the black box. So, we replace the neural network with simple Python logic: keyword matching.
>
> This class has one main method: `generate`. It takes the conversation history and looks at the last user message.
>
> Here is how it 'thinks':
> 1. **Scan for Keywords:** It checks if the word "add" is in the message. If yes, it scans the entire string to extract any numbers it finds (like 10 and 20).
> 2. **Construct the Action:** If it finds two numbers, it constructs a specific JSON structure that says: 'I want to call the tool named `add` with these arguments.'
> 3. **Fallback:** If no keywords match, or if the parsing fails, it returns a generic text response like 'I don't know how to handle that.'
>
> Notice that this file does *not* do the math. It doesn’t know that 10+20=30. It only knows that if you say 'add' and give me numbers, I should ask my tools to do it. This separation of **decision** (LM) and **execution** (Tools) is the core principle of Agentic AI."
