from manim import *


class GScene(ThreeDScene):

    def __init__(self, **kwargs):
        ThreeDScene.__init__(
            self,
            **kwargs
        )

    def construct(self):

        def calc_pos(x1, x2, x3):
            return x1 * axes.coords_to_point(2, 0, 0) + x2 * axes.coords_to_point(0, 2, 0) + x3 * axes.coords_to_point(0, 0, 2)

        def update_dS(d):
            ds.move_to(calc_pos(x1.get_value(), x2.get_value(), 1-x1.get_value()-x2.get_value()))

        def update_n1(n):
            n.set_value(x1.get_value())
            self.remove(n)
            self.add_fixed_in_frame_mobjects(n)

        def update_n2(n):
            n.set_value(x2.get_value())
            self.remove(n)
            self.add_fixed_in_frame_mobjects(n)

        def update_n3(n):
            n.set_value(1 - x1.get_value() - x2.get_value())
            self.remove(n)
            self.add_fixed_in_frame_mobjects(n)

        l1 = MathTex("n=3").to_edge(UP + RIGHT)
        rect = SurroundingRectangle(l1, color=WHITE, stroke_width=2)

        self.add_fixed_in_frame_mobjects(l1, rect)

        axes = ThreeDAxes()

        #TODO: Replace with commented
        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES)

        # TODO: Uncomment (for performance reasons I'm adding instead of creating)
        # self.add(axes)
        self.play(
            Write(axes)
        )
        #simplex = Polygon(axes.coords_to_point(2, 0, 0), axes.coords_to_point(0, 2, 0), axes.coords_to_point(0, 0, 2), color="#194e67", fill_opacity=0.75, fill_color=BLUE)

        simplex = ParametricSurface(lambda u, v: np.array([
            2*np.sin(u)*np.sin(u) * np.cos(v) * np.cos(v),
            2*np.sin(u) * np.sin(u) * np.sin(v) * np.sin(v),
            2*np.cos(u) * np.cos(u)
        ]), 0, np.pi/2, 0, np.pi/2, stroke_width=1, stroke_color=DARK_BLUE, fill_opacity=0.7, checkerboard_colors=None, fill_color=BLUE)

        #TODO: Create instead of add
        #self.add(simplex)

        self.play(
            Create(simplex)
        )

        ds1 = Dot3D(color=RED, radius=0.1).move_to(axes.coords_to_point(2, 0, 0))
        ds2 = Dot3D(color=BLUE, radius=0.1).move_to(axes.coords_to_point(0, 2, 0))
        ds3 = Dot3D(color=PURPLE, radius=0.1).move_to(axes.coords_to_point(0, 0, 2))

        ds = Dot3D(color=GREEN, radius=0.1).move_to(calc_pos(1/3, 1/3, 1/3))

        self.play(
            Create(ds1),
            Create(ds2),
            Create(ds3),
            Create(ds)
        )

        # self.add(ds1)
        # self.add(ds2)
        # self.add(ds3)
        # self.add(ds)

        self.move_camera(phi=75*DEGREES, theta=45*DEGREES)
        self.begin_3dillusion_camera_rotation(rate=1.5, origin_phi=75*DEGREES, origin_theta=45*DEGREES)
        self.wait(4)
        self.stop_3dillusion_camera_rotation()
        self.move_camera(phi=75*DEGREES, theta=45*DEGREES)

        S1 = MathTex("S_1", color=RED).shift(1.5 * LEFT + 0.82 * DOWN)
        S2 = MathTex("S_2", color=BLUE).shift(1.5 * RIGHT + 0.82 * DOWN)
        S3 = MathTex("S_3", color=PURPLE).shift(2*UP + 0.5 * RIGHT)

        self.add_fixed_in_frame_mobjects(S1)
        self.add_fixed_in_frame_mobjects(S2)
        self.add_fixed_in_frame_mobjects(S3)

        self.remove(S1)
        self.remove(S2)
        self.remove(S3)

        self.play(
            Write(S1),
            Write(S2),
            Write(S3)
        )

        text = MathTex("S", "=", "x_1", "S_1", "+", "x_2" , "S_2", "+", "x_3" , "S_3")
        text[0].set_color(GREEN)
        text[3].set_color(RED)
        text[6].set_color(BLUE)
        text[9].set_color(PURPLE)

        text2 = Tex("con $x_1+x_2+x_3=1$")

        self.add_fixed_in_frame_mobjects(text)
        self.add_fixed_in_frame_mobjects(text2)
        self.remove(text)
        self.remove(text2)

        g = VGroup(text, text2).arrange(DOWN)

        g.to_edge(UP + LEFT)
        self.play(
            Write(text),
            Write(text2)
        )

        n1 = DecimalNumber(1/3)
        n2 = DecimalNumber(1/3)
        n3 = DecimalNumber(1/3)

        ts = MathTex("S", "=")
        ts[0].set_color(GREEN)

        ts1 = MathTex("S_1", "+")
        ts1[0].set_color(RED)

        ts2 = MathTex("S_2", "+")
        ts2[0].set_color(BLUE)

        ts3 = MathTex("S_3", color=PURPLE)

        g = VGroup(ts, n1, ts1, n2, ts2, n3, ts3).arrange(RIGHT, buff=0.11).move_to(ORIGIN + 2 * RIGHT + UP)

        self.add_fixed_in_frame_mobjects(ts, n1, ts1, n2, ts2, n3, ts3)
        self.remove(ts, n1, ts1, n2, ts2, n3, ts3)

        g.to_edge(DOWN + LEFT)

        self.play(
            *[Write(mob) for mob in g.submobjects]
        )

        #ds1.get_center()

        x1 = ValueTracker(1/3)
        x2 = ValueTracker(1/3)
        ds.add_updater(update_dS)

        self.wait(2)
        n1.add_updater(update_n1)
        n2.add_updater(update_n2)
        n3.add_updater(update_n3)

        self.play(
            x1.animate.set_value(0),
            x2.animate.set_value(1),
            run_time=3
        )

        self.play(
            x1.animate.set_value(1/2),
            x2.animate.set_value(1/4),
            run_time=3
        )

        self.play(
            x1.animate.set_value(1 / 3),
            x2.animate.set_value(1 / 4),
            run_time=3
        )

        self.play(
            x1.animate.set_value(1 / 5),
            x2.animate.set_value(3 / 4),
            run_time=3
        )

        self.wait(3)

        n1.remove_updater(update_n1)
        n2.remove_updater(update_n2)
        n3.remove_updater(update_n3)
        ds.remove_updater(update_dS)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )