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


class File7_MainScene(Scene):
    def construct(self):
        self.camera.background_color = POPO.BG_COLOR

        # 1. Title Card
        title = Text("main.py", color=POPO.TEXT_MAIN, font_size=48).to_edge(
            UP, buff=0.5
        )
        subtitle = Text("The Stage Door", font_size=24, color=POPO.ACCENT_BLUE).next_to(
            title, DOWN, buff=0.3
        )

        self.play(FadeIn(title), FadeIn(subtitle))
        self.wait(1)

        # 2. The Empty Stage
        stage_text = Text(
            "The system is built, but it’s asleep.", font_size=20
        ).move_to(ORIGIN)
        self.play(FadeIn(stage_text))
        self.wait(2)
        self.play(FadeOut(stage_text))

        # 3. Instantiation
        # Blueprint (Dashed box)
        blueprint = VGroup(
            Rectangle(
                width=3,
                height=2,
                color=POPO.TEXT_MAIN,
                stroke_width=2,
                stroke_opacity=0.5,
            ),
            Text("Agent Class", font_size=16).move_to(ORIGIN),
        ).to_edge(LEFT, buff=2)

        # Concrete Instance (Solid box)
        instance = VGroup(
            Rectangle(
                width=3,
                height=2,
                color=POPO.LOOP_GREEN,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("agent_instance", font_size=16).move_to(ORIGIN),
        ).next_to(blueprint, RIGHT, buff=1)

        code_line = Text(
            "agent = Agent(max_iterations=5)", font_size=14, color=POPO.TEXT_MAIN
        ).next_to(instance, DOWN, buff=0.5)

        self.play(FadeIn(blueprint))
        self.wait(0.5)
        self.play(Transform(blueprint, instance), Write(code_line))
        self.wait(1)

        # 4. The Prompt
        user_prompt = Text('"Please add 10 and 20"', font_size=14).to_edge(
            RIGHT, buff=2
        )
        self.play(FadeIn(user_prompt))
        self.wait(0.5)

        arrow_prompt = Arrow(
            user_prompt.get_left(), instance.get_right(), color=POPO.TEXT_MAIN, buff=0.2
        )
        self.play(GrowArrow(arrow_prompt))
        self.wait(0.5)

        # Move prompt into box
        self.play(
            user_prompt.animate.move_to(instance.get_center()), FadeOut(arrow_prompt)
        )
        self.wait(0.5)

        # 5. The Execution (Glow & Progress)
        glow = Circle(
            radius=1.8, color=POPO.LOOP_GREEN, stroke_width=2, fill_opacity=0.2
        ).move_to(instance.get_center())

        progress_bar_bg = Rectangle(
            width=2, height=0.3, color=POPO.TEXT_MAIN, stroke_width=1, fill_opacity=0.2
        ).next_to(instance, DOWN, buff=0.5)

        # Start with a small visible rectangle
        progress_start = Rectangle(
            width=0.2, height=0.3, color=POPO.LOOP_GREEN, fill_opacity=0.8
        ).move_to(progress_bar_bg.get_left() + RIGHT * 0.1)

        # End state: Full width of the background (minus small padding)
        progress_end = Rectangle(
            width=1.8, height=0.3, color=POPO.LOOP_GREEN, fill_opacity=0.8
        ).move_to(progress_bar_bg.get_left() + RIGHT * 0.9)

        self.play(FadeIn(glow), Create(progress_bar_bg), FadeIn(progress_start))

        # Use Transform for stability instead of scale
        self.play(Transform(progress_start, progress_end))
        self.wait(1)

        self.play(FadeOut(glow), FadeOut(user_prompt))

        # 6. The Output
        result_screen = VGroup(
            Rectangle(
                width=4,
                height=1.5,
                color=POPO.TEXT_MAIN,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("FINAL RESULT", font_size=14).to_edge(UP, buff=0.2),
        ).next_to(instance, RIGHT, buff=1)

        result_text = Text('"I don\'t know how to handle that."', font_size=12).move_to(
            result_screen.get_center()
        )

        self.play(FadeIn(result_screen), Write(result_text))
        self.wait(2)

        # 7. The Report (Log Scroll)
        # Ensure texts are properly positioned within the VGroup
        log_line_1 = Text("[LOOP] Starting...", font_size=10, color=POPO.LOOP_GREEN)
        log_line_2 = Text("[LM] Calling add...", font_size=10, color=POPO.LM_CYAN)
        log_line_3 = Text("[TOOLS] Executing...", font_size=10, color=POPO.TOOLS_YELLOW)

        log_content = VGroup(log_line_1, log_line_2, log_line_3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.2
        )

        log_scroll = VGroup(
            Rectangle(
                width=5,
                height=2,
                color=POPO.TEXT_MAIN,
                stroke_width=1,
                fill_opacity=0.1,
            ),
            log_content.move_to(ORIGIN),
        ).to_edge(DOWN, buff=1)

        self.play(FadeIn(log_scroll))

        completion_text = Text("Run complete. Log generated.", font_size=14).next_to(
            log_scroll, UP, buff=0.2
        )
        self.play(Write(completion_text))
        self.wait(2)
