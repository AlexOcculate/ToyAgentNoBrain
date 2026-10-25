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


class File2_GuardrailsScene(Scene):
    def construct(self):
        self.camera.background_color = POPO.BG_COLOR

        # 1. Title Card
        title = Text("guardrails.py", color=POPO.TEXT_MAIN, font_size=48).to_edge(
            UP, buff=0.5
        )
        subtitle = Text(
            "The Safety Gate", font_size=24, color=POPO.GUARDRAILS_RED
        ).next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(title), FadeIn(subtitle))
        self.wait(1)

        # 2. The Gateway Setup
        # User Input Box (Left)
        input_box = (
            VGroup(
                Rectangle(
                    width=4,
                    height=1.5,
                    color=POPO.TEXT_MAIN,
                    stroke_width=2,
                    fill_opacity=0.1,
                ),
                Text("User Input", font_size=16).to_edge(UP, buff=0.2),
            )
            .to_edge(LEFT, buff=1.5)
            .shift(DOWN * 0.5)
        )

        input_text = Text('"Hello, please add 5 and 5"', font_size=14).move_to(
            input_box
        )

        # Guardrails Gate (Center)
        gate_box = VGroup(
            Rectangle(
                width=3,
                height=4,
                color=POPO.GUARDRAILS_RED,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text(POPO.LABEL_GUARDRAILS, font_size=20).to_edge(UP, buff=0.3),
        ).move_to(ORIGIN)

        # Safe Zone (Right)
        safe_zone = (
            VGroup(
                Rectangle(
                    width=4,
                    height=1.5,
                    color=POPO.LOOP_GREEN,
                    stroke_width=2,
                    fill_opacity=0.1,
                ),
                Text("Safe Zone", font_size=16).to_edge(UP, buff=0.2),
            )
            .to_edge(RIGHT, buff=1.5)
            .shift(DOWN * 0.5)
        )

        self.play(Create(input_box), Write(input_text))
        self.play(Create(gate_box))
        self.play(Create(safe_zone))
        self.wait(1)

        # 3. The Check Process
        # Move input towards gate
        self.play(
            input_box.animate.shift(RIGHT * 2), input_text.animate.shift(RIGHT * 2)
        )

        # Check 1: Non-Empty
        check1_icon = VGroup(
            Circle(radius=0.3, color=POPO.TEXT_MAIN, stroke_width=2),
            Text("!", font_size=20).move_to(ORIGIN),
        ).next_to(gate_box.get_center(), UP, buff=0.5)

        self.play(FadeIn(check1_icon))
        self.wait(0.5)
        # Pass: Turn Green
        self.play(check1_icon.animate.set_color(POPO.LOOP_GREEN))
        self.wait(0.5)

        # Check 2: Length (Fixed: Avoid self-reference in VGroup init)
        ruler_rect = Rectangle(
            width=0.6, height=0.3, color=POPO.TEXT_MAIN, stroke_width=2
        )
        ruler_label = Text("Ruler", font_size=10).next_to(ruler_rect, RIGHT, buff=0.1)
        check2_icon = VGroup(ruler_rect, ruler_label).next_to(
            gate_box.get_center(), DOWN, buff=0.5
        )

        self.play(FadeIn(check2_icon))
        self.wait(0.5)
        # Pass: Turn Green
        self.play(check2_icon.animate.set_color(POPO.LOOP_GREEN))
        self.wait(0.5)

        # Check 3: Forbidden Patterns (Fixed: Replaced Shield with Circle + Diagonal Line)
        shield_circle = Circle(radius=0.3, color=POPO.TEXT_MAIN, stroke_width=2)
        diagonal_line = Line(
            shield_circle.get_left() + UL * 0.15,
            shield_circle.get_right() + DR * 0.15,
            color=POPO.TEXT_MAIN,
            stroke_width=2,
        )
        check3_icon = VGroup(shield_circle, diagonal_line).next_to(
            gate_box.get_center(), DOWN * 1.5, buff=0.5
        )

        self.play(FadeIn(check3_icon))
        self.wait(0.5)
        # Pass: Turn Green
        self.play(check3_icon.animate.set_color(POPO.LOOP_GREEN))
        self.wait(0.5)

        # 4. The Decision (Pass)
        valid_tag = Text("valid=True", font_size=14, color=POPO.LOOP_GREEN).next_to(
            input_box, RIGHT, buff=0.2
        )

        self.play(
            input_box.animate.shift(RIGHT * 3),
            input_text.animate.shift(RIGHT * 3),
            Write(valid_tag),
        )
        self.wait(1)

        # 5. The Failure Scenario
        # Fade out current state
        self.play(
            FadeOut(input_box),
            FadeOut(input_text),
            FadeOut(valid_tag),
            FadeOut(check1_icon),
            FadeOut(check2_icon),
            FadeOut(check3_icon),
        )

        # New Input: Long String
        long_input_text = Text("A" * 50, font_size=14).move_to(input_box.get_center())
        new_input_box = (
            VGroup(
                Rectangle(
                    width=4,
                    height=1.5,
                    color=POPO.TEXT_MAIN,
                    stroke_width=2,
                    fill_opacity=0.1,
                ),
                Text("User Input", font_size=16).to_edge(UP, buff=0.2),
            )
            .to_edge(LEFT, buff=1.5)
            .shift(DOWN * 0.5)
        )

        self.play(FadeIn(new_input_box), Write(long_input_text))

        # Move towards gate
        self.play(
            new_input_box.animate.shift(RIGHT * 2),
            long_input_text.animate.shift(RIGHT * 2),
        )

        # Length Check Fails (Fixed: Avoid self-reference in VGroup init)
        fail_ruler_rect = Rectangle(
            width=0.6, height=0.3, color=POPO.GUARDRAILS_RED, stroke_width=2
        )
        fail_ruler_label = Text("Ruler", font_size=10).next_to(
            fail_ruler_rect, RIGHT, buff=0.1
        )
        fail_check_icon = VGroup(fail_ruler_rect, fail_ruler_label).next_to(
            gate_box.get_center(), DOWN, buff=0.5
        )

        self.play(FadeIn(fail_check_icon))
        self.wait(0.5)

        # Gate Slams Shut / Error
        invalid_tag = Text(
            "valid=False", font_size=14, color=POPO.GUARDRAILS_RED
        ).next_to(new_input_box, RIGHT, buff=0.2)
        error_bubble = VGroup(
            RoundedRectangle(
                corner_radius=0.2,
                width=2,
                height=0.8,
                color=POPO.GUARDRAILS_RED,
                fill_opacity=0.3,
            ),
            Text("Input too long", font_size=12).move_to(ORIGIN),
        ).next_to(gate_box, UP, buff=0.5)

        self.play(
            new_input_box.animate.shift(LEFT * 1),  # Bounce back
            long_input_text.animate.shift(LEFT * 1),
            Write(invalid_tag),
            FadeIn(error_bubble),
        )
        self.wait(2)

        # 6. Summary
        summary_text = Text(
            "Sits Before Brain & Tools", font_size=20, color=POPO.TEXT_MAIN
        ).to_edge(DOWN, buff=1)
        self.play(FadeIn(summary_text))
        self.wait(2)
