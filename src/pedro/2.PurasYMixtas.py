from manim import *


class EDScene(Scene):

    def construct(self):

        def update_n1(n):
            n.set_value(1-tracker.get_value())

        def update_n2(n):
            n.set_value(tracker.get_value())

        def update_dot(dot):
            val = tracker.get_value()
            dot.move_to(nb.get_start() * (1-val) + nb.get_end() * val)

        def update_label(l):
            l.next_to(d, UP)

        title = TextMobject("Estrategias puras y mixtas")
        title.scale(1.5)

        self.play(
            Create(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1/1.5)
        )

        s1 = MathTex("S_1")
        s1.set_color(RED)

        s2 = MathTex("S_2")
        s2.set_color(BLUE)

        nb = UnitInterval(include_numbers=True, numbers_to_show=[0, 1])

        s1.next_to(nb, LEFT)
        s2.next_to(nb, RIGHT)
        s1.shift(UP * 0.15)
        s2.shift(UP * 0.15)

        self.play(
            Create(nb),
            Write(s1),
            Write(s2)
        )

        n1 = DecimalNumber(1)
        n2 = DecimalNumber(0)

        ts = MathTex("S", "=")
        ts[0].set_color(GREEN)

        ts1 = MathTex("\cdot", "S_1", "+")
        ts1[1].set_color(RED)

        ts2 = MathTex("\cdot", "S_2")
        ts2[1].set_color(BLUE)

        d = Dot(nb.get_start(), radius=0.11, color=GREEN)

        label = MathTex("S", color=GREEN)
        label.next_to(d, UP)
        label.add_updater(update_label)

        g = VGroup(ts, n1, ts1, n2, ts2).arrange(RIGHT, buff=0.11).next_to(nb, DOWN)

        self.play(
            Create(g),
            Create(d),
            Create(label)
        )

        tracker = ValueTracker(0)

        n1.add_updater(update_n1)
        n2.add_updater(update_n2)
        d.add_updater(update_dot)

        self.wait(3)

        self.play(
            tracker.animate.set_value(1)
        )

        self.wait(3)

        self.play(
            tracker.animate.set_value(0.3),
            run_time=2
        )

        self.play(
            tracker.animate.set_value(0.8),
            run_time=2
        )

        n1.remove_updater(update_n1)
        n2.remove_updater(update_n2)
        d.remove_updater(update_dot)

        val = tracker.get_value()
        brace1 = BraceLabel(Line(nb.get_start(), nb.get_start() * (1-val) + nb.get_end() * val), brace_direction=UP, text="x_1", buff=1)
        brace2 = BraceLabel(Line(nb.get_start() * (1-val) + nb.get_end() * val, nb.get_end()), brace_direction=UP, text="x_2", buff=1)

        x1 = MathTex("x_1").move_to(n1).shift(DOWN*0.07)
        x2 = MathTex("x_2").move_to(n2).shift(DOWN*0.07)

        self.play(
            FadeOut(label),
            Create(brace1),
            Create(brace2),
            Transform(n1, x1),
            Transform(n2, x2)
        )

        self.play(
            g.animate.arrange(RIGHT, buff=0.11).next_to(nb, DOWN),
            run_time=0.5
        )

        self.play(
            n1.animate.shift(DOWN*0.07),
            n2.animate.shift(DOWN*0.07),
            run_time=0.5
        )

        explain_text = Tex("con $x_1 + x_2 = 1$")
        explain_text.next_to(g, DOWN)

        self.play(
            Write(explain_text)
        )

        self.wait(4)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        # Dibujar el símplex en dos dimensiones

        n = 2
        n_var = Variable(n, "n", var_type=Integer).center()

        self.play(
            Write(n_var)
        )

        self.wait(2)
        self.play(
            n_var.animate.to_edge(UP+RIGHT)
        )

        rect = SurroundingRectangle(n_var, color=WHITE, stroke_width=2)
        self.play(
            Create(rect)
        )