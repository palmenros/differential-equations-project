from manim import *

class EDScene(Scene):
    def construct(self):
        title = TextMobject(r"Clasificación de juegos simétricos $2\cross2$")
        title.scale(1.5)

        self.play(
            Create(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1 / 1.5).shift(LEFT)
        )

        tex = Tex(r"La ecuación del replicador es invariante respecto a \\ la suma de una constante a cada columna de la matriz")

        self.play(
            Create(tex)
        )

        self.wait(3)

        self.play(
            tex.animate.next_to(title, DOWN, coor_mask=[0, 1, 1]).shift(DOWN * 0.3)
        )

        mat = MathTex(r"""
        A = \begin{pmatrix}
          a_{11} & a_{12}\\
          a_{21} & a_{22}
        \end{pmatrix}, \, \, \, B = \begin{pmatrix}
          a_{11} + c & a_{12} + d \\
          a_{21} + c & a_{22} + d
        \end{pmatrix}
        """)

        self.play(
            Create(mat)
        )

        self.wait(1)

        mat3 = MathTex(r"x'=x(1-x)\left[ \left(A \vec{x} \right)_1 - \left(A \vec{x} \right)_2 \right]")

        mat3.arrange(RIGHT).next_to(mat, DOWN, buff = MED_LARGE_BUFF)

        self.play(
            Create(mat3)
        )

        mat5 = MathTex(r"x'=x(1-x)\left[ x a_{11} + (a-x) a_{12} - x a_{21} - (1-x) a_{22} \right]").move_to(mat3)
        self.wait(1)

        self.play(
            ReplacementTransform(mat3, mat5)
        )

        mat6 = MathTex(r"x'=x(1-x)\left[ x (",  r"a_{11} - a_{21}", r") - (1-x) (", r"a_{12}-a_{22}", r") \right]").move_to(mat3)
        self.wait(1)

        brace1 = BraceLabel(mat6[1], "Se cancela $c$", brace_direction=DOWN, label_constructor=Tex, color=BLUE)
        brace1.label.set_color(BLUE)

        brace2 = BraceLabel(mat6[3], "Se cancela $d$", brace_direction=DOWN, label_constructor=Tex, color=BLUE)
        brace2.label.set_color(BLUE)


        self.play(
            ReplacementTransform(mat5, mat6),
            Create(brace1),
            Create(brace2)
        )

        self.wait(3)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not title]
        )

        tex = Tex("Basta entonces estudiar los juegos con matriz de payoff diagonal")
        mat = MathTex(r"""
                A = \begin{pmatrix}
                  a_1 & 0\\
                  0 & a_2
                \end{pmatrix}""")

        mat2 = MathTex(r"""
                A\vec{x} = \begin{pmatrix}
                  a_1 & 0\\
                  0 & a_2
                \end{pmatrix}\begin{pmatrix}
                  x\\
                  1-x
                \end{pmatrix} = \begin{pmatrix}
                  a_1 x \\
                  a_2 (1-x)
                \end{pmatrix} """).move_to(mat)

        VGroup(tex, mat).arrange(DOWN).center()
        self.play(
            Create(tex),
            Create(mat)
        )

        self.wait(3)

        mat2.shift(0.5 * DOWN)

        self.play(
            ReplacementTransform(mat, mat2)
        )

        mat3 = MathTex(r"x'=x(1-x)\left[ a_1 x - a_2 (1-x)\right]").next_to(mat2, DOWN, buff=MED_LARGE_BUFF)

        self.play(
            Create(mat3)
        )

        mat4 = MathTex(r"x'=x(1-x)\left[", r"a_1 x_1 - a_2 x_2", r"\right]").move_to(mat3)

        brace = BraceLabel(mat4[1], "Equilibrio interior cuando se anula", label_constructor=Tex, color=BLUE)
        brace.label.set_color(BLUE)

        self.play(
            ReplacementTransform(mat3, mat4),
            Create(brace)
        )

        self.wait(8)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not title]
        )

        tex = Tex(r"$a_1 x_1 - a_2 x_2$ se anula en $(0, 1)$ \\ si $a_1$ y $a_2$ tienen el mismo signo")

        mat = MathTex(r"x_1^{*}", r"= \frac{a_2}{a_1 + a_2}")

        VGroup(tex, mat).arrange(DOWN).center()

        brace = BraceLabel(mat[0], "Equilibrio de Nash", brace_direction=DOWN, label_constructor=Tex, color=BLUE)
        brace.label.set_color(BLUE)

        self.play(
            Create(tex),
            Create(mat),
            Create(brace)
        )

        self.wait(8)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not title]
        )

        tex = MathTex(r"a_1 > 0, a_2 > 0", color=GREEN).to_edge(UP + RIGHT)
        rect = SurroundingRectangle(tex, color=GREEN, stroke_width=1)

        self.play(
            Create(tex),
            Create(rect)
        )

        unitInterval = UnitInterval(include_numbers=True, numbers_to_show=[0, 1])

        name = Tex(r"Coordination Game")
        mat = MathTex(r"""
        \begin{pmatrix}
                  2 & 0\\
                  0 & 1
                \end{pmatrix}
        """)

        group = VGroup(name, mat).arrange(DOWN)
        VGroup(unitInterval, group).arrange(RIGHT, buff=LARGE_BUFF).center()

        self.play(
            Create(name),
            Create(mat),
            Create(unitInterval)
        )

        d = Dot(unitInterval.number_to_point(0.6), radius=0.11, color=RED)
        d1 = Tex(r"Nash", color=RED).next_to(d, UP)
        d2 = MathTex(r"x^{*}", color=RED).next_to(d, DOWN)

        dp0 = Dot(unitInterval.number_to_point(0), radius=0.11, color=RED)
        dp1 = Dot(unitInterval.number_to_point(1), radius=0.11)

        dp0_tex = Tex(r"ESS", color=BLUE).next_to(dp0, UP)
        dp1_tex = Tex(r"ESS", color=BLUE).next_to(dp1, UP)

        length = 0.1
        p = unitInterval.number_to_point(0.45)
        p1 = unitInterval.number_to_point(0.3)

        t = Polygon(p + LEFT * 2 * length, p + UP * length, p + DOWN * length, color=PURPLE, fill_color=PURPLE, fill_opacity=1)
        t1 = Polygon(p1 + LEFT * 2 * length, p1 + UP * length, p1 + DOWN * length, color=PURPLE, fill_color=PURPLE, fill_opacity=1)

        p2 = unitInterval.number_to_point(0.75)
        p3 = unitInterval.number_to_point(0.9)

        t2 = Polygon(p2 - LEFT * 2 * length, p2 + UP * length, p2 + DOWN * length, color=PURPLE, fill_color=PURPLE, fill_opacity=1)
        t3 = Polygon(p3 - LEFT * 2 * length, p3 + UP * length, p3 + DOWN * length, color=PURPLE, fill_color=PURPLE, fill_opacity=1)


        self.play(
            Create(d),
            Create(d1),
            Create(d2),
            Create(dp0_tex),
            Create(dp1_tex),
            Create(t),
            Create(t1),
            Create(t2),
            Create(t3)
        )

        self.play(
            t.animate.shift(LEFT * 0.3),
            t1.animate.shift(LEFT * 0.3),
            t2.animate.shift(RIGHT * 0.3),
            t3.animate.shift(RIGHT * 0.3),
            run_time=6,
            rate_functions=linear
        )

        tex2 = MathTex(r"a_1 < 0, a_2 < 0", color=GREEN).move_to(tex)

        name2 = Tex(r"Halcones y Palomas").move_to(name)
        mat2 = MathTex(r"""
                \begin{pmatrix}
                          \frac{G-C}{2} & 0\\
                          0 & -\frac{G}{2}
                        \end{pmatrix}
                """).move_to(mat)

        self.play(
            Uncreate(t),
            Uncreate(t1),
            Uncreate(t2),
            Uncreate(t3),
            FadeOut(d),
            FadeOut(d1),
            FadeOut(d2),
            FadeOut(dp0_tex),
            FadeOut(dp1_tex),
            ReplacementTransform(tex, tex2),
            ReplacementTransform(name, name2),
            ReplacementTransform(mat, mat2)
        )

        p = unitInterval.number_to_point(0.45)
        p1 = unitInterval.number_to_point(0.3)
        p2 = unitInterval.number_to_point(0.75)
        p3 = unitInterval.number_to_point(0.9)

        t = Polygon(p - LEFT * 2 * length, p + UP * length, p + DOWN * length, color=PURPLE, fill_color=PURPLE,
                    fill_opacity=1)
        t1 = Polygon(p1 - LEFT * 2 * length, p1 + UP * length, p1 + DOWN * length, color=PURPLE, fill_color=PURPLE,
                     fill_opacity=1)
        t2 = Polygon(p2 + LEFT * 2 * length, p2 + UP * length, p2 + DOWN * length, color=PURPLE, fill_color=PURPLE,
                     fill_opacity=1)
        t3 = Polygon(p3 + LEFT * 2 * length, p3 + UP * length, p3 + DOWN * length, color=PURPLE, fill_color=PURPLE,
                     fill_opacity=1)

        dp0_tex.next_to(d1, UP)

        self.play(
            Create(t),
            Create(t1),
            Create(t2),
            Create(t3),
            Create(d),
            Create(d1),
            Create(d2),
            Create(dp0_tex),
           # Create(dp1_tex)
        )

        self.play(
            t.animate.shift(RIGHT * 0.3),
            t1.animate.shift(RIGHT * 0.3),
            t2.animate.shift(LEFT * 0.3),
            t3.animate.shift(LEFT * 0.3),
            run_time=6,
            rate_functions=linear
        )

        tex3 = MathTex(r"a_1 < 0, a_2 > 0", color=GREEN).move_to(tex)

        #Entonces x' < 0

        name3 = Tex(r"Dilema del prisionero").move_to(name)
        mat3 = MathTex(r"""
                        \begin{pmatrix}
                                  -1 & 0\\
                                  0 & 3
                                \end{pmatrix}
                        """).move_to(mat)

        self.play(
            Uncreate(t),
            Uncreate(t1),
            Uncreate(t2),
            Uncreate(t3),
            FadeOut(d),
            FadeOut(d1),
            FadeOut(d2),
            FadeOut(dp0_tex),
           # FadeOut(dp1_tex),
            ReplacementTransform(tex2, tex3),
            ReplacementTransform(name2, name3),
            ReplacementTransform(mat2, mat3)
        )

        dp0_tex.next_to(dp0, UP)

        p = unitInterval.number_to_point(0.7 - 0.15 * 3)
        p1 = unitInterval.number_to_point(0.7 - 0.15 * 2)
        p2 = unitInterval.number_to_point(0.7 - 0.15)
        p3 = unitInterval.number_to_point(0.7)

        t = Polygon(p + LEFT * 2 * length, p + UP * length, p + DOWN * length, color=PURPLE, fill_color=PURPLE,
                    fill_opacity=1)
        t1 = Polygon(p1 + LEFT * 2 * length, p1 + UP * length, p1 + DOWN * length, color=PURPLE, fill_color=PURPLE,
                     fill_opacity=1)
        t2 = Polygon(p2 + LEFT * 2 * length, p2 + UP * length, p2 + DOWN * length, color=PURPLE, fill_color=PURPLE,
                     fill_opacity=1)
        t3 = Polygon(p3 + LEFT * 2 * length, p3 + UP * length, p3 + DOWN * length, color=PURPLE, fill_color=PURPLE,
                     fill_opacity=1)

        d2 = MathTex(r"x^{*}", color=RED).next_to(dp0, DOWN).shift(0.2*DOWN)

        self.play(
            Create(t),
            Create(t1),
            Create(t2),
            Create(t3),
            Create(dp0),
            Create(d2),
            Create(dp0_tex)
        )

        self.play(
            t.animate.shift(LEFT * 0.3),
            t1.animate.shift(LEFT * 0.3),
            t2.animate.shift(LEFT * 0.3),
            t3.animate.shift(LEFT * 0.3),
            run_time=6,
            rate_functions=linear
        )

        tex4 = MathTex(r"a_1 > 0, a_2 < 0", color=GREEN).move_to(tex)

        # Entonces x' > 0

        name4 = Tex(r"Equivalente al \\ caso anterior").move_to(name).shift(0.5 * DOWN)


        self.play(
            Uncreate(t),
            Uncreate(t1),
            Uncreate(t2),
            Uncreate(t3),
        #   FadeOut(d),
        #    FadeOut(d1),
            FadeOut(d2),
            FadeOut(dp0),
            FadeOut(dp0_tex),
        #    FadeOut(dp1_tex),
            ReplacementTransform(tex3, tex4),
            ReplacementTransform(name3, name4),
            Uncreate(mat3)
        )

        p = unitInterval.number_to_point(0.3 + 0.15 * 3)
        p1 = unitInterval.number_to_point(0.3 + 0.15 * 2)
        p2 = unitInterval.number_to_point(0.3 + 0.15)
        p3 = unitInterval.number_to_point(0.3)

        t = Polygon(p - LEFT * 2 * length, p + UP * length, p + DOWN * length, color=PURPLE, fill_color=PURPLE,
                    fill_opacity=1)
        t1 = Polygon(p1 - LEFT * 2 * length, p1 + UP * length, p1 + DOWN * length, color=PURPLE, fill_color=PURPLE,
                     fill_opacity=1)
        t2 = Polygon(p2 - LEFT * 2 * length, p2 + UP * length, p2 + DOWN * length, color=PURPLE, fill_color=PURPLE,
                     fill_opacity=1)
        t3 = Polygon(p3 - LEFT * 2 * length, p3 + UP * length, p3 + DOWN * length, color=PURPLE, fill_color=PURPLE,
                     fill_opacity=1)

        d2 = MathTex(r"x^{*}", color=RED).next_to(dp0, DOWN).shift(0.2 * DOWN)


        dp0.move_to(unitInterval.number_to_point(1))
        d2 = MathTex(r"x^{*}", color=RED).next_to(dp0, DOWN).shift(0.2*DOWN)


        self.play(
            Create(t),
            Create(t1),
            Create(t2),
            Create(t3),
            Create(dp0),
            Create(d2),
            Create(dp1_tex)
        )

        self.play(
            t.animate.shift(RIGHT * 0.3),
            t1.animate.shift(RIGHT * 0.3),
            t2.animate.shift(RIGHT * 0.3),
            t3.animate.shift(RIGHT * 0.3),
            run_time=6,
            rate_functions=linear
        )

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
