from manim import *

class EDScene(Scene):
    def construct(self):
        title = TextMobject(r"Ejemplo")
        title.scale(1.5)

        self.play(
            Create(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1 / 1.5)
        )

        tex = Tex(r"Supondremos que los tipos corresponden  \\ a las estrategias del juego: \\ $n = p = 2$ \\  $\vec{p}_1 = S_1 = (1, 0)$ \\ $\vec{p}_2 = S_2 = (0, 1)$").center()

        self.play(
            Create(tex)
        )

        self.wait(4)

        ecuacion = MathTex(r"x_i' = x_i \left[ \left( A\vec{x} \right)_i - \vec{x} \cdot A \vec{x} \right] ", color=BLUE).next_to(title, DOWN)
        ecuacion.shift([-ecuacion.get_center()[0], 0, 0])
        rect = SurroundingRectangle(ecuacion, buff=MED_SMALL_BUFF, stroke_width=1)

        self.play(
            FadeOut(tex),
            Create(ecuacion),
            Create(rect)
        )

        mat1 = MathTex(r"\vec{x} \cdot A \vec{x} = (x, 1-x) \cdot \left( {\left(A \vec{x} \right)}_1, {\left(A \vec{x} \right)}_2 \right)")

        self.play(
            Create(mat1)
        )

        self.wait(3)

        mat2 = MathTex( r"\vec{x} \cdot A \vec{x} = x {\left(A \vec{x} \right)}_1 + (1-x) {\left(A \vec{x} \right)}_2")

        self.play(
            ReplacementTransform(mat1, mat2)
        )

        self.wait(3)

        mat3 = MathTex(r"\Rightarrow x'")
        mat4 = MathTex(r"=")
        mat5 = MathTex(r"x \left[ \left( A\vec{x} \right)_1 - x \left( A\vec{x} \right)_1 - (1-x) \left( A\vec{x} \right)_2 \right]")

        group = VGroup(mat3, mat4, mat5).arrange(RIGHT).center().shift(0.3 * DOWN)

        self.play(
            mat2.animate.shift(UP),
            Create(mat3),
            Create(mat4),
            Create(mat5)
        )

        self.wait(1)

        mat6 = MathTex(r"x \left[ (1-x) \left( A\vec{x} \right)_1 - (1-x) \left( A\vec{x} \right)_2 \right]").move_to(mat5)

        self.play(
            ReplacementTransform(mat5, mat6)
        )

        self.wait(1)

        mat7 = MathTex(r"x (1-x) \left[ \left( A\vec{x} \right)_1 - \left( A\vec{x} \right)_2 \right]").move_to(mat6)

        self.play(
            ReplacementTransform(mat6, mat7),
        )

        self.play(
            VGroup(mat3, mat4, mat7).animate.arrange(RIGHT)
        )

        new_ec = MathTex(r"x' = x (1-x) \left[ \left( A\vec{x} \right)_1 - \left( A\vec{x} \right)_2 \right]", color=BLUE).copy().move_to(ecuacion)
        rect2 = SurroundingRectangle(new_ec, buff=MED_SMALL_BUFF, stroke_width=1)

        self.play(
            FadeOut(ecuacion),
            FadeOut(mat2),
            FadeOut(mat3),
            FadeOut(mat4),
            Transform(mat7, new_ec),
            ReplacementTransform(ecuacion, new_ec),
            ReplacementTransform(rect, rect2)
        )

        tex = Tex("Usamos la matriz de payoff de Halcones y Palomas")
        mat = MathTex(r"""
        A = \begin{pmatrix}
          \frac{G-C}{2} & G\\
          0 & \frac{G}{2}
        \end{pmatrix}""")

        mat2 = MathTex(r"""
        A\vec{x} = \begin{pmatrix}
          \frac{G-C}{2} & G\\
          0 & \frac{G}{2}
        \end{pmatrix}\begin{pmatrix}
          x\\
          1-x
        \end{pmatrix} = \begin{pmatrix}
          \frac{G-C}{2}x+(1-x)G \\
          \frac{G}{2}(1-x)
        \end{pmatrix} """).move_to(mat)

        VGroup(tex, mat).arrange(DOWN).center()
        self.play(
            Create(tex),
            Create(mat)
        )

        self.wait(3)

        mat2.shift(0.5*DOWN)

        self.play(
            ReplacementTransform(mat, mat2)
        )

        self.wait(3)

        mat3 = MathTex(r"\Rightarrow \left(A\vec{x}\right)_1-\left(A\vec{x}\right)_2")
        mat4 = MathTex(r"=")
        mat5 = MathTex(r"\frac{G-C}{2}x + (1-x)G- \frac{G}{2}(1-x)")

        VGroup(mat3, mat4, mat5).arrange(RIGHT).next_to(mat2, DOWN, buff=MED_LARGE_BUFF)

        self.play(
            Create(mat3),
            Create(mat4),
            Create(mat5)
        )

        self.wait(2)

        mat6 = MathTex(r"\frac{G-C}{2}x+(1-x)\frac{G}{2}").move_to(mat5)
        self.play(
            ReplacementTransform(mat5, mat6)
        )

        self.wait(1)
        self.remove(mat7)

        mat7 = MathTex(r"-\frac{C}{2}x + \frac{G}{2}").move_to(mat6)
        self.play(
            ReplacementTransform(mat6, mat7)
        )

        self.play(
            VGroup(mat3, mat4, mat7).animate.arrange(RIGHT).next_to(mat2, DOWN, buff=MED_LARGE_BUFF)
        )

        self.wait(3)

        ec_final = MathTex(r"x' = x (1-x) (G-Cx) / 2", color=BLUE)
        rect3 = SurroundingRectangle(ec_final, buff=MED_SMALL_BUFF, stroke_width=1)

        self.remove(ecuacion)

        self.play(
            ReplacementTransform(new_ec, ec_final),
            ReplacementTransform(rect2, rect3),
            ReplacementTransform(mat7, ec_final),
            FadeOut(mat3),
            FadeOut(mat4),
            FadeOut(mat2),
            FadeOut(tex)
        )

        self.remove(new_ec)

        self.wait(3)

        tex = Tex(r"Equilibrio estable atractor global en $x^{*} = \frac{G}{C}$").next_to(ec_final, UP, buff=MED_LARGE_BUFF)
        self.play(
            Create(tex)
        )

        self.wait(3)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )