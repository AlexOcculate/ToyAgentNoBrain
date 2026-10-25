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


class File5_SimulatedLMScene(Scene):
    def construct(self):
        self.camera.background_color = POPO.BG_COLOR

        # 1. Title Card
        title = Text("simulated_lm.py", color=POPO.TEXT_MAIN, font_size=48).to_edge(
            UP, buff=0.5
        )
        subtitle = Text(
            "The Simulated Brain", font_size=24, color=POPO.LM_CYAN
        ).next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(title), FadeIn(subtitle))
        self.wait(1)

        # 2. The Black Box (Transition from Neural Net to Rules)
        # Simple representation of "Neural Network" (dots and lines)
        neural_net = VGroup()
        for i in range(5):
            dot = Dot(radius=0.1, color=POPO.ACCENT_BLUE).shift(
                LEFT * 2
                + RIGHT * np.random.uniform(-1, 1)
                + UP * np.random.uniform(-1, 1)
            )
            neural_net.add(dot)
        for i in range(len(neural_net)):
            if i > 0:
                line = Line(
                    neural_net[i - 1].get_center(),
                    neural_net[i].get_center(),
                    color=POPO.ACCENT_BLUE,
                    stroke_width=1,
                )
                neural_net.add(line)

        self.play(FadeIn(neural_net))
        self.wait(1)

        # Replace with Simple Box
        lm_box = VGroup(
            Rectangle(
                width=4, height=3, color=POPO.LM_CYAN, stroke_width=2, fill_opacity=0.1
            ),
            Text(POPO.LABEL_LM, font_size=20).to_edge(UP, buff=0.3),
        ).move_to(ORIGIN)

        no_magic_text = Text(
            "No Magic. Just Rules.", font_size=18, color=POPO.TEXT_MAIN
        ).next_to(lm_box, DOWN, buff=0.5)

        self.play(FadeOut(neural_net), Create(lm_box), Write(no_magic_text))
        self.wait(1)

        # 3. The Input Stream
        input_text = Text(
            '"Please add 10 and 20"', font_size=16, color=POPO.TEXT_MAIN
        ).to_edge(LEFT, buff=1.5)

        self.play(FadeIn(input_text))
        self.wait(0.5)

        # Move into box
        self.play(input_text.animate.move_to(lm_box.get_center()))
        self.wait(0.5)

        # 4. The Keyword Scanner
        # Highlight "add"
        scanner_bg = Rectangle(
            width=0.8, height=0.4, color=POPO.TOOLS_YELLOW, fill_opacity=0.3
        ).move_to(input_text.get_center() + LEFT * 1.2)

        self.play(FadeIn(scanner_bg))
        self.wait(0.5)

        # Highlight numbers 10 and 20
        num_10_bg = Rectangle(
            width=0.4, height=0.4, color=POPO.ACCENT_BLUE, fill_opacity=0.3
        ).move_to(input_text.get_center() + RIGHT * 0.5)
        num_20_bg = Rectangle(
            width=0.4, height=0.4, color=POPO.ACCENT_BLUE, fill_opacity=0.3
        ).move_to(input_text.get_center() + RIGHT * 1.8)

        self.play(FadeIn(num_10_bg), FadeIn(num_20_bg))
        self.wait(1)

        # 5. The Decision Tree (Simplified Flowchart)
        # Clear input text to make room for logic
        self.play(
            FadeOut(input_text),
            FadeOut(scanner_bg),
            FadeOut(num_10_bg),
            FadeOut(num_20_bg),
        )

        # Fixed: Use a rotated Square instead of Diamond
        decision_shape = Square(
            side_length=1.5, color=POPO.TEXT_MAIN, stroke_width=2, fill_opacity=0.1
        ).rotate(PI / 4)
        decision_text = Text('"add" in text?', font_size=12).move_to(
            decision_shape.get_center()
        )
        decision_node = VGroup(decision_shape, decision_text).move_to(
            lm_box.get_center()
        )

        action_node = VGroup(
            Rectangle(
                width=2,
                height=0.8,
                color=POPO.LOOP_GREEN,
                stroke_width=2,
                fill_opacity=0.2,
            ),
            Text("Call Tool 'add'", font_size=12).move_to(ORIGIN),
        ).next_to(decision_node, DOWN, buff=0.5)

        arrow = Arrow(
            decision_node.get_bottom(),
            action_node.get_top(),
            color=POPO.LOOP_GREEN,
            buff=0.2,
        )

        self.play(FadeIn(decision_node), GrowArrow(arrow), FadeIn(action_node))
        self.wait(1)

        # 6. The Output
        # Clear decision tree
        self.play(FadeOut(decision_node), FadeOut(arrow), FadeOut(action_node))

        output_json = Text(
            '{"tool_calls": [\n  {"name": "add",\n   "args": {"a": 10, "b": 20}}\n]}',
            font_size=14,
            color=POPO.TEXT_MAIN,
        ).next_to(lm_box, RIGHT, buff=0.5)

        status_text = Text(
            "Calling add(10.0, 20.0)...", font_size=14, color=POPO.LOOP_GREEN
        ).next_to(output_json, DOWN, buff=0.3)

        self.play(FadeIn(output_json), Write(status_text))
        self.wait(2)

        # Summary
        summary_text = Text(
            "Separation of Decision & Execution", font_size=18, color=POPO.TEXT_MAIN
        ).to_edge(DOWN, buff=1)
        self.play(FadeIn(summary_text))
        self.wait(2)
