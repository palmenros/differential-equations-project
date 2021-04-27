from manim import *


class GScene(GraphScene):

    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_axis_label="$x_1$",
            x_axis_label="$x_2$",
            graph_origin=3 * DOWN + 4 * LEFT,
            y_labeled_nums=[0, 1],
            x_labeled_nums=[0, 1, 2],
            exclude_zero_label=False,
            y_min=0,
            y_max=1.5,
            x_min=0,
            x_max=2.25,
            y_axis_config={"tick_frequency": 0.5},
            x_axis_config={"tick_frequency": 0.5},
            include_tip=True,
            **kwargs
        )

    def construct(self):

        def update_S(slabel):
            slabel.next_to(dS, RIGHT + UP, buff=SMALL_BUFF)

        def update_dot(dot):
            val = tracker.get_value()
            dot.move_to(self.coords_to_point(val, 1-val))

        def update_n1(n):
            n.set_value(1-tracker.get_value())

        def update_n2(n):
            n.set_value(tracker.get_value())

        n = 2
        n_var = Variable(n, "n", var_type=Integer).to_edge(UP+RIGHT)
        rect = SurroundingRectangle(n_var, color=WHITE, stroke_width=2)

        self.add(n_var)
        self.add(rect)

        self.setup_axes(animate=True)

        dS1 = Dot(self.coords_to_point(0, 1), color=RED, radius=0.11)
        dS2 = Dot(self.coords_to_point(1, 0), color=BLUE, radius=0.11)

        l = Line(dS1, dS2).set_color("#eeeeee")

        self.play(
            Create(dS1),
            Create(dS2),
            Create(l)
        )

        S1 = MathTex("S_1", color=RED).next_to(dS1, RIGHT + UP, buff=SMALL_BUFF)
        S2 = MathTex("S_2", color=BLUE).next_to(dS2, UP + RIGHT, buff=SMALL_BUFF)

        self.play(
            Write(S1),
            Write(S2)
        )

        self.wait(1)

        dS = Dot(self.coords_to_point(0.5, 0.5), color=GREEN, radius=0.11)
        S = MathTex("S", color=GREEN).next_to(dS, RIGHT + UP, buff=SMALL_BUFF)

        self.play(
            Create(dS),
            Create(S)
        )

        self.wait(1)


        n1 = DecimalNumber(0.5)
        n2 = DecimalNumber(0.5)

        ts = MathTex("S", "=")
        ts[0].set_color(GREEN)

        ts1 = MathTex("\cdot", "S_1", "+")
        ts1[1].set_color(RED)

        ts2 = MathTex("\cdot", "S_2")
        ts2[1].set_color(BLUE)

        g = VGroup(ts, n1, ts1, n2, ts2).arrange(RIGHT, buff=0.11).move_to(ORIGIN + 2*RIGHT + UP)
        self.play(
            *[Write(mob) for mob in g.submobjects]
        )

        S.add_updater(update_S)
        tracker = ValueTracker(0.5)
        dS.add_updater(update_dot)
        n1.add_updater(update_n1)
        n2.add_updater(update_n2)

        self.play(
            tracker.animate.set_value(0.8),
            run_time=2
        )

        self.play(
            tracker.animate.set_value(0.15),
            run_time=2
        )

        self.play(
            tracker.animate.set_value(0.7),
            run_time=2
        )

        self.wait(2)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        n = 3
        n_var = Variable(n, "n", var_type=Integer).center()

        self.play(
            Write(n_var)
        )

        self.wait(2)
        self.play(
            n_var.animate.to_edge(UP + RIGHT)
        )

        rect = SurroundingRectangle(n_var, color=WHITE, stroke_width=2)
        self.play(
            Create(rect)
        )