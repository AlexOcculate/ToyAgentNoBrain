Here is the proposed explanation for **File #9: `test_adversarial.py`**.

### File 9/9: `test_adversarial.py`

**Concept:** The Stress Test & Robustness Proof
**Complexity Level:** 5/10 (System Integration & Failure Modes)

---

#### 🎬 Manim Visual Scene Description

1.  **Title Card:** Title fades in: `test_adversarial.py`. Subtitle: *"Breaking the System on Purpose."*
2.  **The Setup:**
    *   The full Agent system (from File #6) is shown intact and stable.
    *   A red "Chaos Monkey" icon appears, holding a hammer labeled `Test Cases`.
3.  **Test 1: The Broken Brain:**
    *   The Chaos Monkey hits the `SimulatedLM` box with a wrench.
    *   The LM starts spitting out garbage symbols (`@#$%`).
    *   The Agent loop catches it, logs `[LM] MALFORMED`, and stops gracefully without crashing. A green shield icon appears: *"System Survived."*
4.  **Test 2: The Hostile Input:**
    *   A giant block of text (1000 chars) is thrown at the `Guardrails` gate.
    *   The gate slams shut immediately.
    *   Text appears: `"Input too long"`.
    *   The Agent never even starts its loop. Green shield: *"Blocked."*
5.  **Test 3: The Failing Tool:**
    *   The Chaos Monkey replaces the `add` tool with a bomb icon.
    *   When the Agent tries to use it, the bomb explodes (throws an exception).
    *   The `ToolRegistry` catches the explosion and returns an error string instead of crashing.
    *   The loop continues or stops gracefully. Green shield: *"Error Handled."*
6.  **Test 4: The Infinite Loop:**
    *   The Chaos Monkey forces the LM to always say "Call Tool."
    *   The Agent loop spins rapidly: `1... 2... 3...`.
    *   A counter hits `5/5`.
    *   A red stop sign appears. The loop halts. Green shield: *"Limit Enforced."*
7.  **Summary:**
    *   All four green shields align in a row.
    *   Text appears: *"The Harness is Robust."*

---

#### 🎙️ Narrator Script

> "We have built the agent, we’ve seen how it works, and we’ve seen how to run it. But does it work when things go wrong? In production, 'things' always go wrong. APIs fail, users send garbage, and models hallucinate.
>
> This file is our proof of robustness. It’s a suite of adversarial tests designed to break the system on purpose. If the system survives these tests, we can trust it.
>
> Let’s look at the four main failure modes we test:
>
> 1. **Broken LM:** What if the 'brain' returns garbage data? We mock the LM to return invalid JSON or missing keys. The Agent must catch this and stop gracefully with an error message, rather than crashing with a Python traceback.
> 2. **Hostile Input:** What if a user sends a massive text file or malicious code? The Guardrails must block it before it even reaches the brain. We test with oversized inputs to ensure the system doesn’t waste resources on bad data.
> 3. **Tool Failure:** What if a tool crashes? For example, if our `add` function suddenly throws an exception. The Tool Registry must catch this error and return it as a string result. The agent should handle this error message, not crash.
> 4. **Infinite Loop:** What if the LM gets stuck in a loop, always asking for more tools? The Agent’s iteration counter (`max_iterations`) must kick in and force-stop the process. This prevents runaway costs and frozen programs.
>
> This file doesn’t add new features; it verifies that the guardrails we built in previous files actually work under pressure. It is the final quality check before we consider the module complete."
