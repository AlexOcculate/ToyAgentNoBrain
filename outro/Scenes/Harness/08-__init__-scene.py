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


class File8_InitScene(Scene):
    def construct(self):
        self.camera.background_color = POPO.BG_COLOR

        # 1. Title Card
        title = Text("__init__.py", color=POPO.TEXT_MAIN, font_size=48).to_edge(
            UP, buff=0.5
        )
        subtitle = Text(
            "The Python Package Key", font_size=24, color=POPO.ACCENT_BLUE
        ).next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(title), FadeIn(subtitle))
        self.wait(1)

        # 2. The Directory Structure
        # Folder Icon (Left)
        folder = VGroup(
            Rectangle(
                width=4,
                height=3,
                color=POPO.TEXT_MAIN,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("Harness/", font_size=20).to_edge(UP, buff=0.3),
        ).to_edge(LEFT, buff=2)

        # Files inside (Greyed out initially)
        file_agent = (
            Text("agent.py", font_size=14, color=GREY)
            .next_to(folder.get_bottom(), UP, buff=0.5)
            .shift(RIGHT * 0.5)
        )
        file_memory = Text("memory.py", font_size=14, color=GREY).next_to(
            file_agent, DOWN, buff=0.2
        )
        file_tools = Text("tools.py", font_size=14, color=GREY).next_to(
            file_memory, DOWN, buff=0.2
        )

        self.play(
            FadeIn(folder), FadeIn(file_agent), FadeIn(file_memory), FadeIn(file_tools)
        )
        self.wait(1)

        # 3. The Problem
        main_py = Text("main.py", font_size=16).to_edge(RIGHT, buff=2).shift(UP * 2)

        import_path = Text("from Harness.agent import Agent", font_size=14).next_to(
            main_py, DOWN, buff=0.5
        )

        arrow_import = Arrow(
            main_py.get_bottom(),
            folder.get_right() + UP * 1,
            color=POPO.GUARDRAILS_RED,
            buff=0.2,
        )

        self.play(FadeIn(main_py), Write(import_path), GrowArrow(arrow_import))

        error_text = Text(
            "Python doesn't know this is a package.",
            font_size=14,
            color=POPO.GUARDRAILS_RED,
        ).next_to(arrow_import, UP, buff=0.5)

        self.play(FadeIn(error_text))

        # Red X over import path
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
        ).move_to(import_path.get_center())

        self.play(FadeIn(red_x))
        self.wait(2)

        # 4. The Solution
        # Fade out error state
        self.play(FadeOut(error_text), FadeOut(red_x), FadeOut(arrow_import))

        # __init__.py drops in
        init_file = (
            VGroup(
                Rectangle(
                    width=1.5,
                    height=0.8,
                    color=POPO.LOOP_GREEN,
                    stroke_width=2,
                    fill_opacity=0.2,
                ),
                Text("__init__.py", font_size=12).move_to(ORIGIN),
            )
            .next_to(folder.get_top(), DOWN, buff=0.5)
            .shift(RIGHT * 1)
        )

        self.play(FadeIn(init_file))

        # Folder lights up (Change color to Green)
        folder_lights = VGroup(
            Rectangle(
                width=4,
                height=3,
                color=POPO.LOOP_GREEN,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text("Harness/", font_size=20).to_edge(UP, buff=0.3),
        ).move_to(folder.get_center())

        self.play(Transform(folder, folder_lights))

        # Files become active (Change color to White/Main)
        file_agent_active = Text(
            "agent.py", font_size=14, color=POPO.TEXT_MAIN
        ).move_to(file_agent.get_center())
        file_memory_active = Text(
            "memory.py", font_size=14, color=POPO.TEXT_MAIN
        ).move_to(file_memory.get_center())
        file_tools_active = Text(
            "tools.py", font_size=14, color=POPO.TEXT_MAIN
        ).move_to(file_tools.get_center())

        self.play(
            Transform(file_agent, file_agent_active),
            Transform(file_memory, file_memory_active),
            Transform(file_tools, file_tools_active),
        )
        self.wait(1)

        # 5. The Import Success
        arrow_success = Arrow(
            main_py.get_bottom(),
            folder.get_right() + UP * 1,
            color=POPO.LOOP_GREEN,
            buff=0.2,
        )

        import_path_success = Text(
            "from Harness.agent import Agent", font_size=14, color=POPO.LOOP_GREEN
        ).move_to(import_path.get_center())

        checkmark = VGroup(
            Line(
                ORIGIN + DL * 0.3,
                ORIGIN + DR * 0.1,
                color=POPO.LOOP_GREEN,
                stroke_width=4,
            ),
            Line(
                ORIGIN + DR * 0.1,
                ORIGIN + UR * 0.3,
                color=POPO.LOOP_GREEN,
                stroke_width=4,
            ),
        ).next_to(import_path_success, RIGHT, buff=0.2)

        self.play(
            GrowArrow(arrow_success),
            Transform(import_path, import_path_success),
            FadeIn(checkmark),
        )

        marker_text = Text("It’s just a marker.", font_size=16).to_edge(DOWN, buff=1)
        self.play(FadeIn(marker_text))
        self.wait(2)
