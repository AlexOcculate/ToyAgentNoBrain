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


class File3_TraceLoggerScene(Scene):
    def construct(self):
        self.camera.background_color = POPO.BG_COLOR

        # 1. Title Card
        title = Text("trace_logger.py", color=POPO.TEXT_MAIN, font_size=48).to_edge(
            UP, buff=0.5
        )
        subtitle = Text(
            "The Agent's Black Box Recorder", font_size=24, color=POPO.ACCENT_BLUE
        ).next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(title), FadeIn(subtitle))
        self.wait(1)

        # 2. The Problem: Chaos
        chaos_lines = VGroup()
        for i in range(15):
            line = Line(
                LEFT * 4
                + RIGHT * np.random.uniform(-1, 1)
                + UP * np.random.uniform(-3, 3),
                RIGHT * 4
                + LEFT * np.random.uniform(-1, 1)
                + DOWN * np.random.uniform(-3, 3),
                color=POPO.TEXT_MAIN,
                stroke_width=1,
                stroke_opacity=0.5,
            )
            chaos_lines.add(line)

        question_text = Text(
            "How do we know what the agent is thinking?", font_size=20
        ).to_edge(DOWN, buff=1)

        self.play(FadeIn(chaos_lines), FadeIn(question_text))
        self.wait(2)

        # 3. The Solution: Logger & Components
        self.play(FadeOut(chaos_lines), FadeOut(question_text))

        # Timeline (Left)
        timeline_box = VGroup(
            Rectangle(
                width=4,
                height=5,
                color=POPO.TEXT_MAIN,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("Trace Log", font_size=18).to_edge(UP, buff=0.3),
        ).to_edge(LEFT, buff=1.5)

        # Components (Right)
        loop_box = (
            VGroup(
                Rectangle(
                    width=2,
                    height=1,
                    color=POPO.LOOP_GREEN,
                    stroke_width=2,
                    fill_opacity=0.1,
                ),
                Text("[LOOP]", font_size=14).move_to(ORIGIN),
            )
            .to_edge(RIGHT, buff=1.5)
            .shift(UP * 2)
        )

        lm_box = VGroup(
            Rectangle(
                width=2, height=1, color=POPO.LM_CYAN, stroke_width=2, fill_opacity=0.1
            ),
            Text("[LM]", font_size=14).move_to(ORIGIN),
        ).to_edge(RIGHT, buff=1.5)

        tools_box = (
            VGroup(
                Rectangle(
                    width=2,
                    height=1,
                    color=POPO.TOOLS_YELLOW,
                    stroke_width=2,
                    fill_opacity=0.1,
                ),
                Text("[TOOLS]", font_size=14).move_to(ORIGIN),
            )
            .to_edge(RIGHT, buff=1.5)
            .shift(DOWN * 2)
        )

        # Camera Icon (Fixed: Using Circle and Line instead of Triangle with unsupported args)
        camera_body = Circle(radius=0.3, color=POPO.TEXT_MAIN, stroke_width=2)
        camera_lens = Line(
            ORIGIN + RIGHT * 0.3,
            ORIGIN + RIGHT * 0.5,
            color=POPO.TEXT_MAIN,
            stroke_width=4,
        )
        camera_icon = VGroup(camera_body, camera_lens).move_to(RIGHT * 3 + UP * 1)

        self.play(Create(timeline_box))
        self.play(FadeIn(loop_box), FadeIn(lm_box), FadeIn(tools_box))
        self.play(FadeIn(camera_icon))
        self.wait(1)

        # 4. The Logging Action
        # Log Entry 1: Loop
        log_line_1 = (
            Text("10:00:01 [LOOP] Starting...", font_size=12, color=POPO.LOOP_GREEN)
            .to_edge(LEFT, buff=2)
            .shift(UP * 1.5)
        )

        # Pulse from Loop box
        pulse_1 = Circle(radius=0.2, color=POPO.LOOP_GREEN, fill_opacity=0.5).move_to(
            loop_box.get_center()
        )
        self.play(GrowFromCenter(pulse_1), Write(log_line_1))
        self.wait(0.5)
        self.play(FadeOut(pulse_1))

        # Log Entry 2: LM
        log_line_2 = Text(
            "10:00:02 [LM] Calling add...", font_size=12, color=POPO.LM_CYAN
        ).to_edge(LEFT, buff=2)

        pulse_2 = Circle(radius=0.2, color=POPO.LM_CYAN, fill_opacity=0.5).move_to(
            lm_box.get_center()
        )
        self.play(GrowFromCenter(pulse_2), Write(log_line_2))
        self.wait(0.5)
        self.play(FadeOut(pulse_2))

        # Log Entry 3: Tools
        log_line_3 = (
            Text("10:00:03 [TOOLS] Executing...", font_size=12, color=POPO.TOOLS_YELLOW)
            .to_edge(LEFT, buff=2)
            .shift(DOWN * 1.5)
        )

        pulse_3 = Circle(radius=0.2, color=POPO.TOOLS_YELLOW, fill_opacity=0.5).move_to(
            tools_box.get_center()
        )
        self.play(GrowFromCenter(pulse_3), Write(log_line_3))
        self.wait(0.5)
        self.play(FadeOut(pulse_3))

        # 5. Color Coding Legend
        legend_title = (
            Text("Color Coding", font_size=16).to_edge(RIGHT, buff=1.5).shift(DOWN * 4)
        )

        # Fixed: Use side_length for Square
        legend_items = (
            VGroup(
                VGroup(
                    Square(side_length=0.2, color=POPO.LOOP_GREEN),
                    Text("Loop Control", font_size=10),
                ),
                VGroup(
                    Square(side_length=0.2, color=POPO.LM_CYAN),
                    Text("Brain (LM)", font_size=10),
                ),
                VGroup(
                    Square(side_length=0.2, color=POPO.TOOLS_YELLOW),
                    Text("Tools", font_size=10),
                ),
                VGroup(
                    Square(side_length=0.2, color=POPO.GUARDRAILS_RED),
                    Text("Safety", font_size=10),
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(legend_title, DOWN, buff=0.5)
        )

        self.play(FadeIn(legend_title), FadeIn(legend_items))
        self.wait(2)

        # 6. The Report
        proof_text = Text(
            "This log is our proof of what happened.", font_size=18
        ).to_edge(DOWN, buff=1)

        # Scroll effect simulation (just fade in more lines rapidly)
        extra_logs = (
            VGroup(
                Text("10:00:04 [LM] Response...", font_size=12, color=POPO.LM_CYAN),
                Text("10:00:05 [LOOP] Finished", font_size=12, color=POPO.LOOP_GREEN),
            )
            .arrange(DOWN)
            .next_to(log_line_3, DOWN, buff=0.2)
        )

        self.play(Write(extra_logs[0]), Write(extra_logs[1]))
        self.play(FadeIn(proof_text))
        self.wait(2)
