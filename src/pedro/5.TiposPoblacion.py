from manim import *


class EDScene(Scene):
    def construct(self):

        def update_rect1(rect1):
            rect1.stretch_to_fit_width(8 * tracker.get_value())
            group.arrange(RIGHT, buff=0)

        def update_rect2(rect2):
            rect2.stretch_to_fit_width(8 * (1-tracker.get_value()))
            group.arrange(RIGHT, buff=0)

        def update_number(numb):
            numb.set_value(tracker.get_value())
            numb.next_to(rect1, RIGHT + DOWN )
            numb.shift(LEFT * 0.7)

        def update_brace1(b):
            temp = Brace(rect1, UP, color=RED)
            b.replace(temp)
            label1.next_to(b, UP)

        def update_brace2(b):
            temp = Brace(rect2, UP, color=GREEN)
            b.replace(temp)
            label2.next_to(b, UP)

        title = TextMobject("Modelo del replicador")
        title.scale(1.5)

        self.play(
            Create(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1 / 1.5)
        )

        l = BulletedList(
            "La población está dividida en $p$ tipos con distintas estrategias",
            "La evolución de cada tipo depende de los resultados del juego",
            "La población es grande y las generaciones se mezclan"
        )

        sup = Tex("Suposiciones:", color=BLUE).next_to(l, UP).shift(UP * 0.2)
        self.play(
            Write(sup)
        )


        self.play(
            Write(l[0])
        )

        self.wait(3)
        self.play(
            Write(l[1])
        )

        self.wait(3)
        self.play(
            Write(l[2])
        )

        self.wait(3)

        self.play(
            FadeOut(sup),
            FadeOut(l)
        )

        rect1 = Rectangle(color=RED, height=1.2, width=4).set_fill(RED, 1)
        rect2 = Rectangle(color=GREEN, height=1.2, width=4).set_fill(GREEN, 1)
        group = VGroup(rect1, rect2).arrange(RIGHT, buff=0)
        tracker = ValueTracker(0.5)

        text0 = MathTex("0").next_to(group, DOWN + LEFT)
        text1 = MathTex("1").next_to(group, DOWN + RIGHT)
        number = DecimalNumber(0.5, tracker=tracker)
        number.next_to(rect1, RIGHT + DOWN)
        number.shift(LEFT * 0.7)
        update_number(number)

        self.play(
            FadeInFrom(rect1, UP),
            FadeInFrom(rect2, UP),
            Write(text0),
            Write(text1),
            Write(number)
        )

        self.wait(1)

        brace1 = Brace(rect1, UP, color=RED)
        label1 = MathTex("x_1", color=RED).next_to(brace1, UP)
        brace2 = Brace(rect2, UP, color=GREEN)
        label2 = MathTex("x_2", color=GREEN).next_to(brace2, UP)

        self.play(
            Write(brace1),
            Write(label1),
            Write(brace2),
            Write(label2)
        )

        explanation = MathTex(r"x_1 + x_2 = 1 \Rightarrow \vec{x} = (", "x_1", ", ", "x_2", ") \in \Delta^{2}").shift(2 * DOWN)
        explanation[1].set_color(RED)
        explanation[3].set_color(GREEN)

        self.play(
            Write(explanation)
        )

        brace1.add_updater(update_brace1)
        brace2.add_updater(update_brace2)
        rect1.add_updater(update_rect1)
        rect2.add_updater(update_rect2)
        number.add_updater(update_number)

        self.play(
            tracker.animate.set_value(0.7),
            run_time=2
        )

        self.play(
            tracker.animate.set_value(0.3),
            run_time = 2
        )

        self.play(
            tracker.animate.set_value(0.6),
            run_time = 2
        )

        self.wait(2)

        rect1.remove_updater(update_rect1)
        rect2.remove_updater(update_rect2)

        generalized_explanation = MathTex(r"x_1 + \dots + x_p = 1 \Rightarrow \vec{x} = (x_1, \dots, x_p) \in \Delta^{p}").shift(2 * DOWN)

        self.play(
            Transform(
                explanation,
                generalized_explanation
            )
        )

        self.wait(5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not title]
        )