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


class File9_TestAdversarialScene(Scene):
    def construct(self):
        self.camera.background_color = POPO.BG_COLOR

        # 1. Title Card
        title = Text("test_adversarial.py", color=POPO.TEXT_MAIN, font_size=48).to_edge(
            UP, buff=0.5
        )
        subtitle = Text(
            "Breaking the System on Purpose", font_size=24, color=POPO.GUARDRAILS_RED
        ).next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(title), FadeIn(subtitle))
        self.wait(1)

        # 2. The Setup: Stable Agent System
        agent_system = VGroup(
            Circle(radius=1, color=POPO.LOOP_GREEN, stroke_width=2, fill_opacity=0.1),
            Text("Agent", font_size=16).move_to(ORIGIN),
        ).move_to(LEFT * 3)

        lm_box = VGroup(
            Rectangle(
                width=1.5,
                height=0.8,
                color=POPO.LM_CYAN,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("LM", font_size=12).move_to(ORIGIN),
        ).next_to(agent_system, UP, buff=1)

        tools_box = VGroup(
            Rectangle(
                width=1.5,
                height=0.8,
                color=POPO.TOOLS_YELLOW,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("Tools", font_size=12).move_to(ORIGIN),
        ).next_to(agent_system, RIGHT, buff=1)

        guard_box = VGroup(
            Rectangle(
                width=1.5,
                height=0.8,
                color=POPO.GUARDRAILS_RED,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("Guard", font_size=12).move_to(ORIGIN),
        ).next_to(agent_system, LEFT, buff=1)

        self.play(
            FadeIn(agent_system), FadeIn(lm_box), FadeIn(tools_box), FadeIn(guard_box)
        )

        # Chaos Monkey (Simple representation: Red Circle with angry eyes? Just a red box for now)
        chaos_monkey = (
            VGroup(
                Circle(radius=0.5, color=POPO.GUARDRAILS_RED, fill_opacity=0.3),
                Text("Chaos", font_size=10).move_to(ORIGIN),
            )
            .to_edge(RIGHT, buff=2)
            .shift(UP * 2)
        )

        self.play(FadeIn(chaos_monkey))
        self.wait(1)

        # Helper for Shield Icon
        def create_shield(text_msg, pos):
            shield = VGroup(
                RoundedRectangle(
                    corner_radius=0.2,
                    width=1.5,
                    height=0.8,
                    color=POPO.LOOP_GREEN,
                    stroke_width=2,
                    fill_opacity=0.2,
                ),
                Text(text_msg, font_size=10).move_to(ORIGIN),
            ).move_to(pos)
            return shield

        shields = VGroup()

        # 3. Test 1: Broken Brain
        test_label_1 = (
            Text("Test 1: Broken LM", font_size=14).to_edge(LEFT, buff=1).shift(UP * 2)
        )
        self.play(FadeIn(test_label_1))

        # Garbage symbols from LM
        garbage = Text("@#$%", font_size=20, color=POPO.GUARDRAILS_RED).next_to(
            lm_box, RIGHT, buff=0.5
        )
        self.play(Write(garbage))
        self.wait(0.5)

        # Agent catches it
        error_log = Text(
            "[LM] MALFORMED", font_size=10, color=POPO.GUARDRAILS_RED
        ).next_to(agent_system, DOWN, buff=0.5)
        self.play(FadeIn(error_log))
        self.wait(0.5)

        shield_1 = create_shield("Survived", RIGHT * 4 + UP * 2)
        self.play(FadeOut(garbage), FadeIn(shield_1))
        shields.add(shield_1)
        self.play(FadeOut(test_label_1), FadeOut(error_log))
        self.wait(0.5)

        # 4. Test 2: Hostile Input
        test_label_2 = (
            Text("Test 2: Hostile Input", font_size=14)
            .to_edge(LEFT, buff=1)
            .shift(UP * 2)
        )
        self.play(FadeIn(test_label_2))

        # Giant text block
        hostile_input = Text("A" * 30, font_size=8).next_to(guard_box, LEFT, buff=0.5)
        self.play(FadeIn(hostile_input))
        self.wait(0.5)

        # Gate slams shut (Visual: Red X over guard box)
        red_x = VGroup(
            Line(
                ORIGIN + UL * 0.3,
                ORIGIN + DR * 0.3,
                color=POPO.GUARDRAILS_RED,
                stroke_width=4,
            ),
            Line(
                ORIGIN + UR * 0.3,
                ORIGIN + DL * 0.3,
                color=POPO.GUARDRAILS_RED,
                stroke_width=4,
            ),
        ).move_to(guard_box.get_center())

        self.play(FadeIn(red_x))
        self.wait(0.5)

        block_msg = Text("Blocked", font_size=12, color=POPO.LOOP_GREEN).next_to(
            guard_box, DOWN, buff=0.3
        )
        shield_2 = create_shield("Blocked", RIGHT * 4 + UP * 0.5)

        self.play(FadeOut(hostile_input), FadeIn(shield_2))
        shields.add(shield_2)
        self.play(FadeOut(test_label_2), FadeOut(red_x), FadeOut(block_msg))
        self.wait(0.5)

        # 5. Test 3: Failing Tool
        test_label_3 = (
            Text("Test 3: Failing Tool", font_size=14)
            .to_edge(LEFT, buff=1)
            .shift(UP * 2)
        )
        self.play(FadeIn(test_label_3))

        # Bomb icon in tools box
        bomb = Circle(radius=0.2, color=POPO.GUARDRAILS_RED, fill_opacity=0.5).move_to(
            tools_box.get_center()
        )
        self.play(FadeIn(bomb))

        # Explosion effect (Flash)
        flash = Circle(
            radius=0.5, color=POPO.TOOLS_YELLOW, stroke_width=2, fill_opacity=0.3
        ).move_to(tools_box.get_center())
        self.play(GrowFromCenter(flash))
        self.wait(0.5)

        # Error handled message
        err_handled = Text(
            "Error Handled", font_size=10, color=POPO.LOOP_GREEN
        ).next_to(tools_box, DOWN, buff=0.3)
        shield_3 = create_shield("Handled", RIGHT * 4 - UP * 0.5)

        self.play(FadeOut(flash), FadeIn(err_handled), FadeIn(shield_3))
        shields.add(shield_3)
        self.play(FadeOut(test_label_3), FadeOut(bomb), FadeOut(err_handled))
        self.wait(0.5)

        # 6. Test 4: Infinite Loop
        test_label_4 = (
            Text("Test 4: Infinite Loop", font_size=14)
            .to_edge(LEFT, buff=1)
            .shift(UP * 2)
        )
        self.play(FadeIn(test_label_4))

        # Spinning loop indicator
        spin_circle = Circle(radius=0.3, color=POPO.LOOP_GREEN, stroke_width=2).move_to(
            agent_system.get_center()
        )
        spin_dot = Dot(radius=0.1, color=POPO.TEXT_MAIN).move_to(spin_circle.get_top())

        self.play(FadeIn(spin_circle), FadeIn(spin_dot))

        # Animate spinning
        self.play(
            Rotate(spin_dot, angle=TAU, about_point=spin_circle.get_center()),
            run_time=1,
        )

        # Stop sign
        stop_sign = VGroup(
            Circle(radius=0.3, color=POPO.GUARDRAILS_RED, fill_opacity=0.8),
            Text("STOP", font_size=8).move_to(ORIGIN),
        ).next_to(agent_system, RIGHT, buff=0.5)

        shield_4 = create_shield("Limit Enforced", RIGHT * 4 - UP * 2)

        self.play(
            FadeOut(spin_circle), FadeOut(spin_dot), FadeIn(stop_sign), FadeIn(shield_4)
        )
        shields.add(shield_4)
        self.play(FadeOut(test_label_4), FadeOut(stop_sign))
        self.wait(1)

        # 7. Summary
        summary_text = Text(
            "The Harness is Robust", font_size=20, color=POPO.LOOP_GREEN
        ).to_edge(DOWN, buff=1)

        # Align shields in a row at the top right
        shields.arrange(RIGHT, buff=0.5).move_to(RIGHT * 3 + UP * 2)

        self.play(FadeIn(summary_text))
        self.wait(2)
