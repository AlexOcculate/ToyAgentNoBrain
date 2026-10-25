from manim import *


class POPO:
    # Colors
    BG_COLOR = "#1E1E2E"
    TEXT_MAIN = "#CDD6F4"
    LOOP_GREEN = "#A6E3A1"
    LM_CYAN = "#89DCEB"
    TOOLS_YELLOW = "#F9E2AF"
    GUARDRAILS_RED = "#F38BA8"
    MEMORY_MAGENTA = "#CBA6F7"
    ACCENT_BLUE = "#89B4FA"

    # Labels
    LABEL_MEMORY = "Memory"
    LABEL_LM = "SimulatedLM"
    LABEL_TOOLS = "ToolRegistry"
    LABEL_GUARDRAILS = "Guardrails"
    LABEL_LOOP = "Agent Loop"


class File6_AgentScene(Scene):
    def construct(self):
        self.camera.background_color = POPO.BG_COLOR

        # 1. Title Card
        title = Text("agent.py", color=POPO.TEXT_MAIN, font_size=48).to_edge(
            UP, buff=0.5
        )
        subtitle = Text("The Conductor", font_size=24, color=POPO.LOOP_GREEN).next_to(
            title, DOWN, buff=0.3
        )

        self.play(FadeIn(title), FadeIn(subtitle))
        self.wait(1)

        # 2. The Assembly Line (Components around Center)
        # Central Agent Box
        agent_box = VGroup(
            Circle(radius=1, color=POPO.LOOP_GREEN, stroke_width=3, fill_opacity=0.1),
            Text("Agent", font_size=20).move_to(ORIGIN),
        ).move_to(ORIGIN)

        # Top: LM
        lm_box = VGroup(
            Rectangle(
                width=2, height=1, color=POPO.LM_CYAN, stroke_width=2, fill_opacity=0.1
            ),
            Text("LM", font_size=16).move_to(ORIGIN),
        ).next_to(agent_box, UP, buff=1.5)

        # Right: Tools
        tools_box = VGroup(
            Rectangle(
                width=2,
                height=1,
                color=POPO.TOOLS_YELLOW,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("Tools", font_size=16).move_to(ORIGIN),
        ).next_to(agent_box, RIGHT, buff=1.5)

        # Bottom: Memory
        memory_box = VGroup(
            Rectangle(
                width=2,
                height=1,
                color=POPO.MEMORY_MAGENTA,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("Memory", font_size=16).move_to(ORIGIN),
        ).next_to(agent_box, DOWN, buff=1.5)

        # Left: Guardrails
        guardrails_box = VGroup(
            Rectangle(
                width=2,
                height=1,
                color=POPO.GUARDRAILS_RED,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("Guardrails", font_size=14).move_to(ORIGIN),
        ).next_to(agent_box, LEFT, buff=1.5)

        self.play(Create(agent_box))
        self.play(
            FadeIn(lm_box),
            FadeIn(tools_box),
            FadeIn(memory_box),
            FadeIn(guardrails_box),
        )

        # Connect with lines
        conn_lm = Line(
            agent_box.get_top(),
            lm_box.get_bottom(),
            color=POPO.TEXT_MAIN,
            stroke_width=1,
        )
        conn_tools = Line(
            agent_box.get_right(),
            tools_box.get_left(),
            color=POPO.TEXT_MAIN,
            stroke_width=1,
        )
        conn_mem = Line(
            agent_box.get_bottom(),
            memory_box.get_top(),
            color=POPO.TEXT_MAIN,
            stroke_width=1,
        )
        conn_guard = Line(
            agent_box.get_left(),
            guardrails_box.get_right(),
            color=POPO.TEXT_MAIN,
            stroke_width=1,
        )

        self.play(
            Create(conn_lm), Create(conn_tools), Create(conn_mem), Create(conn_guard)
        )
        self.wait(1)

        # 3. The Loop Visualization
        # Circular Arrow Path
        loop_path = Arc(
            radius=2.5,
            start_angle=PI / 4,
            angle=TAU - PI / 2,
            color=POPO.LOOP_GREEN,
            stroke_width=3,
        )
        loop_label = Text(
            "The Agent Loop", font_size=16, color=POPO.LOOP_GREEN
        ).next_to(loop_path, RIGHT, buff=0.5)

        self.play(Create(loop_path), FadeIn(loop_label))
        self.wait(1)

        # Step 1: Input -> Guardrails
        input_text = Text("User Input", font_size=14).to_edge(LEFT, buff=1)
        arrow_input = Arrow(
            input_text.get_right(),
            guardrails_box.get_left(),
            color=POPO.TEXT_MAIN,
            buff=0.2,
        )

        self.play(FadeIn(input_text), GrowArrow(arrow_input))
        self.wait(0.5)

        # Valid? Move to Agent
        arrow_guard_to_agent = Arrow(
            guardrails_box.get_right(),
            agent_box.get_left(),
            color=POPO.LOOP_GREEN,
            buff=0.2,
        )
        self.play(GrowArrow(arrow_guard_to_agent))
        self.wait(0.5)

        # Step 2: Think (Agent -> LM)
        arrow_agent_lm = Arrow(
            agent_box.get_top(), lm_box.get_bottom(), color=POPO.LM_CYAN, buff=0.2
        )
        think_label = Text("Think", font_size=12).next_to(
            arrow_agent_lm, RIGHT, buff=0.2
        )

        self.play(GrowArrow(arrow_agent_lm), FadeIn(think_label))
        self.wait(0.5)

        # Step 3: Act (Agent -> Tools)
        arrow_agent_tools = Arrow(
            agent_box.get_right(),
            tools_box.get_left(),
            color=POPO.TOOLS_YELLOW,
            buff=0.2,
        )
        act_label = Text("Act", font_size=12).next_to(arrow_agent_tools, UP, buff=0.2)

        self.play(GrowArrow(arrow_agent_tools), FadeIn(act_label))
        self.wait(0.5)

        # Step 4: Update (Memory)
        arrow_agent_mem = Arrow(
            agent_box.get_bottom(),
            memory_box.get_top(),
            color=POPO.MEMORY_MAGENTA,
            buff=0.2,
        )
        update_label = Text("Update Context", font_size=12).next_to(
            arrow_agent_mem, RIGHT, buff=0.2
        )

        self.play(GrowArrow(arrow_agent_mem), FadeIn(update_label))
        self.wait(0.5)

        # Step 5: Repeat/Stop Check
        check_circle = Circle(radius=0.3, color=POPO.TEXT_MAIN, stroke_width=2).next_to(
            agent_box, UP, buff=0.5
        )
        stop_text = Text("Stop?", font_size=10).move_to(check_circle)

        self.play(FadeIn(check_circle), FadeIn(stop_text))
        self.wait(1)

        # 4. The Safety Net (Iteration Counter)
        counter_text = Text(
            "Iteration: 1/5", font_size=14, color=POPO.TEXT_MAIN
        ).to_corner(UR, buff=0.5)

        self.play(FadeIn(counter_text))
        self.wait(0.5)

        # Simulate loop running (change counter to 5/5)
        counter_5 = Text(
            "Iteration: 5/5", font_size=14, color=POPO.GUARDRAILS_RED
        ).move_to(counter_text.get_center())

        self.play(Transform(counter_text, counter_5))
        self.wait(0.5)

        # Stop Sign
        stop_sign = VGroup(
            Circle(radius=0.3, color=POPO.GUARDRAILS_RED, fill_opacity=0.8),
            Text("STOP", font_size=10, color=WHITE).move_to(ORIGIN),
        ).next_to(counter_text, DOWN, buff=0.2)

        self.play(FadeIn(stop_sign))
        self.wait(2)

        # Summary
        summary_text = Text(
            "Stateful Loop & Orchestration", font_size=18, color=POPO.TEXT_MAIN
        ).to_edge(DOWN, buff=1)
        self.play(FadeIn(summary_text))
        self.wait(2)
