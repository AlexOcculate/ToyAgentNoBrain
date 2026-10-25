Here is the LLM prompt designed to take the previous explanations and generate executable Manim code.

***

**Role:** Senior Manim Animation Developer & Python Expert

**Context:**
We are creating an educational video series for the "TOYAGENTS" curriculum. We have generated detailed pedagogical explanations for 9 files in `ToyAgentNoBrain`. Your task is to convert these explanations into executable **Manim Community Edition** code.

**Input Data:**
I will provide you with one "File Explanation" block at a time. Each block contains:
1.  **Concept & Complexity Level.**
2.  **🎬 Manim Visual Scene Description:** A step-by-step description of what should appear on screen (shapes, labels, movements).
3.  **🎙️ Narrator Script:** The audio track (for context only; do not include audio in the code).

**Global Constraints & Style Guide:**

1.  **Library:** Use `manim` (Community Edition). Import `manim as m`.
2.  **Structure:** Each file explanation must result in a single `Scene` class named after the file (e.g., `class MemoryScene(m.Scene):`).
3.  **VGroup Usage:** You **MUST** use `m.VGroup` to group related elements (e.g., a box and its label, or a set of check icons). This ensures clean animation logic (fading in/out groups together).
4.  **Color Palette (Strict Consistency):**
    *   **Background:** Default black.
    *   **Primary Text/Labels:** `m.WHITE`
    *   **Agent/Loop Elements:** `m.GREEN` (e.g., loop arrows, main agent box)
    *   **LM/Brain Elements:** `m.CYAN` (e.g., LM box, decision logic)
    *   **Tools/Actions:** `m.YELLOW` (e.g., tool registry, function icons)
    *   **Memory/Data:** `m.MAGENTA` (e.g., memory boxes, data keys/values)
    *   **Guardrails/Safety:** `m.RED` (e.g., gates, error messages, stop signs)
    *   **Logger/Trace:** `m.BLUE` (e.g., log lines, timeline)
    *   **Neutral/Infrastructure:** `m.GRAY` (e.g., file paths, background boxes)
5.  **Animation Style:**
    *   Use `Write`, `FadeIn`, and `MoveToOrigin` for clarity.
    *   Keep animations slow enough for educational purposes (`rate_func=m.ease_in_out`).
    *   Avoid complex physics; stick to geometric transformations.
6.  **Code Quality:**
    *   Include comments explaining which part of the "Visual Scene Description" is being implemented.
    *   Ensure all text is readable (use `m.Text` with appropriate font sizes, e.g., 24-32).
    *   Use `self.wait()` strategically to let the viewer process information.

**Immediate Action:**
1.  Analyze the "Global Constraints" above.
2.  Acknowledge that you are ready to receive the **File Explanation** blocks one by one.
3.  **DO NOT generate any code yet.** Wait for me to paste the first File Explanation (starting with `Harness/memory.py`).

**Confirmation:** Reply with "Ready for File #1."