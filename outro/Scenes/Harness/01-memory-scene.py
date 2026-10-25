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


class File1_MemoryScene(Scene):
    def construct(self):
        self.camera.background_color = POPO.BG_COLOR

        # 1. Title Card
        title = Text("memory.py", color=POPO.TEXT_MAIN, font_size=48).to_edge(
            UP, buff=0.5
        )
        subtitle = Text(
            "The Agent's Long-Term Memory", font_size=24, color=POPO.ACCENT_BLUE
        ).next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(title), FadeIn(subtitle))
        self.wait(1)

        # 2. The Black Box (Memory Container)
        memory_box = VGroup(
            Rectangle(
                width=4,
                height=3,
                color=POPO.MEMORY_MAGENTA,
                stroke_width=2,
                fill_opacity=0.1,
            ),
            Text(POPO.LABEL_MEMORY, color=POPO.MEMORY_MAGENTA, font_size=24).to_edge(
                UP, buff=0.5
            ),
        ).move_to(ORIGIN)

        # Fixed: Use Text with monospace style instead of Code to avoid file path interpretation errors
        store_text = Text(
            "_store = {}", font_size=24, color=POPO.TEXT_MAIN, font="monospace"
        ).move_to(memory_box[0])

        self.play(Create(memory_box), Write(store_text))
        self.wait(1)

        # 3. The Store Action
        store_arrow = Arrow(
            LEFT * 5, memory_box.get_left(), color=POPO.MEMORY_MAGENTA, buff=0.2
        )
        store_label = Text(
            "store(key, value)", color=POPO.TEXT_MAIN, font_size=18
        ).next_to(store_arrow, LEFT, buff=0.2)

        key_block = VGroup(
            Rectangle(
                width=1.5, height=0.6, color=POPO.MEMORY_MAGENTA, fill_opacity=0.3
            ),
            Text('key: "last_item"', font_size=14).move_to(ORIGIN),
        ).next_to(store_arrow.get_start(), DOWN, buff=0.5)

        val_block = VGroup(
            Rectangle(
                width=1.5, height=0.6, color=POPO.MEMORY_MAGENTA, fill_opacity=0.3
            ),
            Text('value: "42"', font_size=14).move_to(ORIGIN),
        ).next_to(key_block, DOWN, buff=0.2)

        self.play(
            GrowArrow(store_arrow),
            FadeIn(store_label),
            FadeIn(key_block),
            FadeIn(val_block),
        )
        self.wait(1)

        # Animate blocks moving into box
        merged_entry = Text(
            '{"last_item": "42"}', font_size=20, color=POPO.TEXT_MAIN, font="monospace"
        ).move_to(memory_box[0])

        self.play(
            key_block.animate.shift(memory_box.get_center() - key_block.get_center()),
            val_block.animate.shift(memory_box.get_center() - val_block.get_center()),
            FadeOut(store_arrow),
            FadeOut(store_label),
        )

        # Transform the text to show the updated dictionary state
        self.play(Transform(store_text, merged_entry))
        self.wait(1)

        # 4. The Recall Action
        recall_arrow = Arrow(
            LEFT * 5, memory_box.get_left(), color=POPO.ACCENT_BLUE, buff=0.2
        )
        recall_label = Text("recall(key)", color=POPO.TEXT_MAIN, font_size=18).next_to(
            recall_arrow, LEFT, buff=0.2
        )

        self.play(GrowArrow(recall_arrow), FadeIn(recall_label))
        self.wait(0.5)

        # Magnifying glass effect (simulated with a circle and line)
        magnifier = VGroup(
            Circle(radius=0.4, color=POPO.ACCENT_BLUE, stroke_width=3),
            Line(
                ORIGIN + DR * 0.3,
                ORIGIN + DR * 0.7,
                color=POPO.ACCENT_BLUE,
                stroke_width=3,
            ),
        ).move_to(memory_box.get_center())

        self.play(FadeIn(magnifier))
        self.wait(1)

        # Value floats out
        result_text = Text('"42"', font_size=24, color=POPO.LOOP_GREEN).next_to(
            memory_box, RIGHT, buff=0.5
        )

        self.play(
            FadeOut(magnifier),
            FadeOut(recall_arrow),
            FadeOut(recall_label),
            Write(result_text),
        )
        self.wait(1)
        self.play(FadeOut(result_text))

        # 5. The List Action
        list_arrow = Arrow(
            LEFT * 5, memory_box.get_left(), color=POPO.TOOLS_YELLOW, buff=0.2
        )
        list_label = Text("list_keys()", color=POPO.TEXT_MAIN, font_size=18).next_to(
            list_arrow, LEFT, buff=0.2
        )

        self.play(GrowArrow(list_arrow), FadeIn(list_label))
        self.wait(0.5)

        list_icon = VGroup(
            Line(
                ORIGIN + UL * 0.3,
                ORIGIN + DR * 0.3,
                color=POPO.TOOLS_YELLOW,
                stroke_width=2,
            ),
            Text('• "last_item"', font_size=14, color=POPO.TEXT_MAIN).next_to(
                list_arrow.get_start(), RIGHT, buff=0.5
            ),
        )

        self.play(FadeIn(list_icon))
        self.wait(1)

        self.play(FadeOut(list_arrow), FadeOut(list_label), FadeOut(list_icon))

        # 6. Summary
        summary_text = Text(
            "Persistent State Container", font_size=20, color=POPO.TEXT_MAIN
        ).to_edge(DOWN, buff=1)
        self.play(FadeIn(summary_text))
        self.wait(2)
