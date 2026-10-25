#!/bin/bash

# chmod +x create_folders.s

touch main.py                      # Entry point: instantiates and runs the agent
touch test_adversarial.py          # Adversarial tests for harness robustness
touch README.md                    # Documentation and curriculum context
mkdir -p Harness/
touch Harness/__init__.py          # Package marker
touch Harness/agent.py             # Main agent loop logic
touch Harness/simulated_lm.py      # The "Brain": keyword-based rule engine
touch Harness/tools.py             # Tool definitions and execution logic
touch Harness/memory.py            # Persistent memory storage (dict-based)
touch Harness/guardrails.py        # Input/Output validation and safety checks
touch Harness/trace_logger.py      # Colored console logging for visibility
