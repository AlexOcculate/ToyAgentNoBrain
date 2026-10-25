Here is the proposed explanation for **File #2: `Harness/guardrails.py`**.

### File 2/9: `Harness/guardrails.py`

**Concept:** The Safety Gate & Input Validator
**Complexity Level:** 2/10 (Logic & Validation)

---

#### 🎬 Manim Visual Scene Description

1.  **Title Card:** Title fades in: `guardrails.py`. Subtitle: *"The Safety Gate."*
2.  **The Gateway Setup:**
    *   On the left, a text box appears labeled `User Input`. Inside it, write: `"Hello, please add 5 and 5"`.
    *   In the center, a large, vertical barrier or gate structure appears. Label it `Guardrails`.
    *   On the right, a green light zone is labeled `Safe Zone` (leading to the Agent).
3.  **The Check Process:**
    *   The text box `User Input` moves toward the gate.
    *   Inside the gate, three distinct check icons appear sequentially:
        1.  **Non-Empty Check:** A small "!" icon checks if the string is not empty. It turns green (Pass).
        2.  **Length Check:** A ruler icon measures the length of the text. It shows `500 max`. The current text is short, so it turns green (Pass).
        3.  **Forbidden Patterns:** A shield icon with a "No" sign checks for bad keywords (like `DROP TABLE`). It scans the text, finds nothing, and turns green (Pass).
4.  **The Decision:**
    *   Since all checks passed, the gate opens (or a green light turns on).
    *   The text box passes through to the `Safe Zone`.
    *   A small tag attaches to the text: `valid=True`.
5.  **The Failure Scenario (Flashback/Alt Path):**
    *   The scene resets slightly. A new, very long string of "AAAA..." appears as input.
    *   It hits the gate.
    *   The **Length Check** ruler turns red.
    *   The gate slams shut. A red tag attaches: `valid=False`.
    *   An error message bubble pops up: `"Input too long"`.
6.  **Summary:** The guardrails box remains, emphasizing it sits *before* the brain and tools.

---

#### 🎙️ Narrator Script

> "Now that we have a place to store information, we need to make sure only safe, valid information enters our system. This is where `guardrails.py` comes in.
>
> Think of guardrails as a security checkpoint at the entrance of an airport. Not everyone who walks up to the counter is allowed into the terminal; they must pass through security checks first.
>
> In our agent, this file defines the `Guardrails` class. Its job is to inspect user input *before* it ever reaches the 'brain' (the LLM) or the tools. Why? Because bad input can cause crashes, infinite loops, or even security vulnerabilities.
>
> The class has one main method: `validate_input`. It performs three specific checks:
>
> 1. **Existence Check:** Is the input actually a string? Is it empty? If someone sends an empty message, we reject it immediately.
> 2. **Size Check:** We set a maximum length (default 500 characters). Why? Because if a user sends a 10-megabyte text file, our simple Python agent might slow down or crash. We keep it lightweight.
> 3. **Content Check:** We look for 'forbidden patterns.' For example, if the input contains SQL injection attempts like `DROP TABLE` or system commands like `rm -rf`, we block it. This is a basic form of security filtering.
>
> The method returns a tuple: `(is_valid, error_message)`.
> If everything passes, it returns `(True, None)`.
> If something fails, it returns `(False, 'Reason for failure')`.
>
> This file doesn't do any 'thinking.' It just enforces rules. It’s the bodyguard that stands in front of the agent."

