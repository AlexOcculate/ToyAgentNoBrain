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


class File4_ToolsScene(Scene):
    def construct(self):
        self.camera.background_color = POPO.BG_COLOR

        # 1. Title Card
        title = Text("tools.py", color=POPO.TEXT_MAIN, font_size=48).to_edge(
            UP, buff=0.5
        )
        subtitle = Text(
            "The Agent's Hands", font_size=24, color=POPO.TOOLS_YELLOW
        ).next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(title), FadeIn(subtitle))
        self.wait(1)

        # 2. The Tool Shed (Registry)
        registry_box = VGroup(
            Rectangle(
                width=5,
                height=4,
                color=POPO.TOOLS_YELLOW,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text(POPO.LABEL_TOOLS, font_size=20).to_edge(UP, buff=0.3),
        ).move_to(ORIGIN)

        # Tool Slots inside the registry
        slot_add = (
            VGroup(
                Rectangle(
                    width=1.5,
                    height=0.8,
                    color=POPO.TEXT_MAIN,
                    stroke_width=1,
                    fill_opacity=0.2,
                ),
                Text("add", font_size=14).move_to(ORIGIN),
            )
            .next_to(registry_box.get_top(), DOWN, buff=0.5)
            .shift(LEFT * 1.5)
        )

        slot_store = VGroup(
            Rectangle(
                width=1.5,
                height=0.8,
                color=POPO.TEXT_MAIN,
                stroke_width=1,
                fill_opacity=0.2,
            ),
            Text("memory_store", font_size=10).move_to(ORIGIN),
        ).next_to(slot_add, RIGHT, buff=0.3)

        slot_recall = VGroup(
            Rectangle(
                width=1.5,
                height=0.8,
                color=POPO.TEXT_MAIN,
                stroke_width=1,
                fill_opacity=0.2,
            ),
            Text("memory_recall", font_size=10).move_to(ORIGIN),
        ).next_to(slot_store, DOWN, buff=0.3)

        slot_list = VGroup(
            Rectangle(
                width=1.5,
                height=0.8,
                color=POPO.TEXT_MAIN,
                stroke_width=1,
                fill_opacity=0.2,
            ),
            Text("memory_list", font_size=10).move_to(ORIGIN),
        ).next_to(slot_add, DOWN, buff=0.3)

        self.play(Create(registry_box))
        self.play(
            FadeIn(slot_add), FadeIn(slot_store), FadeIn(slot_recall), FadeIn(slot_list)
        )
        self.wait(1)

        # 3. The Request (Message Envelope)
        request_envelope = VGroup(
            Rectangle(
                width=2, height=1, color=POPO.LM_CYAN, stroke_width=2, fill_opacity=0.2
            ),
            Text('Name: "add"', font_size=12).shift(UP * 0.2),
            Text('Args: {"a": 10, "b": 20}', font_size=10).shift(DOWN * 0.2),
        ).to_edge(LEFT, buff=1.5)

        self.play(FadeIn(request_envelope))
        self.wait(0.5)

        # Envelope flies into registry
        self.play(request_envelope.animate.move_to(registry_box.get_center()))
        self.wait(0.5)
        self.play(FadeOut(request_envelope))

        # 4. Lookup & Execution
        # Spotlight on 'add' slot
        spotlight = Circle(
            radius=1, color=POPO.ACCENT_BLUE, stroke_width=2, fill_opacity=0.1
        ).move_to(slot_add.get_center())
        self.play(FadeIn(spotlight))

        # Function icon pops out
        func_icon = VGroup(
            RoundedRectangle(
                corner_radius=0.1,
                width=1.5,
                height=0.8,
                color=POPO.LM_CYAN,
                stroke_width=2,
            ),
            Text("_tool_add", font_size=12).move_to(ORIGIN),
        ).next_to(slot_add, RIGHT, buff=0.5)

        self.play(GrowFromCenter(func_icon))
        self.wait(0.5)

        # Arguments plugged in
        arg_1 = Text("10", font_size=16, color=POPO.TEXT_MAIN).next_to(
            func_icon, LEFT, buff=0.2
        )
        arg_2 = Text("20", font_size=16, color=POPO.TEXT_MAIN).next_to(
            arg_1, DOWN, buff=0.2
        )

        self.play(FadeIn(arg_1), FadeIn(arg_2))
        self.play(
            arg_1.animate.move_to(func_icon.get_left() + RIGHT * 0.3),
            arg_2.animate.move_to(func_icon.get_left() + RIGHT * 0.3),
        )
        self.wait(0.5)

        # Calculation
        calc_text = Text("10 + 20 = 30", font_size=18, color=POPO.LOOP_GREEN).next_to(
            func_icon, RIGHT, buff=0.5
        )
        self.play(Write(calc_text))
        self.wait(1)

        # 5. The Return
        result_package = VGroup(
            Rectangle(
                width=2.5,
                height=0.8,
                color=POPO.LOOP_GREEN,
                stroke_width=2,
                fill_opacity=0.2,
            ),
            Text('"10.0 + 20.0 = 30.0"', font_size=12).move_to(ORIGIN),
        ).next_to(registry_box, LEFT, buff=0.5)

        self.play(FadeIn(result_package))
        self.wait(1)

        # Cleanup success scene
        self.play(
            FadeOut(spotlight),
            FadeOut(func_icon),
            FadeOut(arg_1),
            FadeOut(arg_2),
            FadeOut(calc_text),
            FadeOut(result_package),
        )

        # 6. The Error Case
        # New Request: 'fly'
        error_envelope = VGroup(
            Rectangle(
                width=2,
                height=1,
                color=POPO.GUARDRAILS_RED,
                stroke_width=2,
                fill_opacity=0.2,
            ),
            Text('Name: "fly"', font_size=12).move_to(ORIGIN),
        ).to_edge(LEFT, buff=1.5)

        self.play(FadeIn(error_envelope))
        self.wait(0.5)

        # Fly into registry
        self.play(error_envelope.animate.move_to(registry_box.get_center()))
        self.wait(0.5)

        # Scan/No match
        scan_line = Line(
            LEFT * 2, RIGHT * 2, color=POPO.GUARDRAILS_RED, stroke_width=2
        ).move_to(registry_box.get_center())
        self.play(Create(scan_line))
        self.wait(0.5)
        self.play(FadeOut(error_envelope), FadeOut(scan_line))

        # Error Package Returns
        error_package = VGroup(
            Rectangle(
                width=3,
                height=0.8,
                color=POPO.GUARDRAILS_RED,
                stroke_width=2,
                fill_opacity=0.2,
            ),
            Text("\"Error: Unknown tool 'fly'\"", font_size=12).move_to(ORIGIN),
        ).next_to(registry_box, LEFT, buff=0.5)

        self.play(FadeIn(error_package))
        self.wait(2)

        # Summary
        summary_text = Text(
            "Robust Error Handling", font_size=20, color=POPO.TEXT_MAIN
        ).to_edge(DOWN, buff=1)
        self.play(FadeIn(summary_text))
        self.wait(2)
