from manim import *


class EDScene(Scene):
    def construct(self):
        title = TextMobject("Modelo del replicador").to_edge(UP + LEFT)
        self.add(title)

        text = Tex("Cada tipo tiene una estrategia fija $\in \, \Delta^n$ (pura o mixta)", color=BLUE)

        self.play(
            Write(text)
        )

        self.wait(2)

        self.play(
            text.animate.to_edge(UP).shift(DOWN)
        )

        rect1 = Rectangle(color=RED, height=1.2, width=2).set_fill(RED, 1)
        rect2 = Rectangle(color=GREEN, height=1.2, width=3).set_fill(GREEN, 1)

        group = VGroup(rect1, rect2).arrange(RIGHT, buff=0).to_edge(LEFT).shift(1 * DOWN)

        triangle = Triangle().to_edge(RIGHT).set_color(WHITE).scale(1.5).shift(LEFT + 1 * DOWN)

        self.play(
            Create(rect1),
            Create(rect2),
            Create(triangle)
        )

        brace1 = BraceLabel(rect1, "x_1", UP, color=RED)
        brace1.label.set_color(RED)
        brace2 = BraceLabel(rect2, "x_2", UP, color=GREEN)
        brace2.label.set_color(GREEN)

        tex1 = MathTex("p = 2").next_to(group, DOWN)

        vertices = triangle.get_vertices()

        d1 = Dot(vertices[0], color=PURPLE, radius=0.11)
        d2 = Dot(vertices[1], color=YELLOW, radius=0.11)
        d3 = Dot(vertices[2], color=ORANGE, radius=0.11)

        l1 = MathTex("S_1", color=PURPLE).next_to(d1, UP, buff=MED_SMALL_BUFF)
        l2 = MathTex("S_2", color=YELLOW).next_to(d2, LEFT, buff=MED_SMALL_BUFF)
        l3 = MathTex("S_3", color=ORANGE).next_to(d3, RIGHT, buff=MED_SMALL_BUFF)

        tex2 = MathTex("n = 3").next_to(triangle, DOWN)

        arrow = MathTex(r"\longrightarrow").shift(DOWN + 0.8 * RIGHT).scale(1.5)

        table = Tex(r"""
                \begin{table}[]
                \begin{tabular}{c|c}
                \textbf{Población} & \textbf{Estrategia} \\ \hline
                {\color{red}$x_1$} & $\vec{p}_1$ \\
                $x_2$ & $\vec{p}_2$       
                \end{tabular}
                \end{table}""").scale(0.6)

        table.next_to(arrow, UP)

        self.play(
            Write(tex1),
            Write(tex2),
            Create(brace1),
            Create(brace2),
            Create(d1),
            Create(d2),
            Create(d3),
            Create(l1),
            Create(l2),
            Create(l3),
            Create(arrow),
            Create(table)
        )

        p1d = Dot(vertices[1] * 0.25 + vertices[0]*0.5 + vertices[2]*0.25, color=RED)
        p2d = Dot(vertices[1] * 0.7 + vertices[0]*0.15 + vertices[2]*0.15, color=GREEN)

        p1 = MathTex(r"\vec{p}_1", color=RED).next_to(p1d, RIGHT + DOWN, buff=SMALL_BUFF).shift(0.1*UP + 0.1*LEFT)
        p2 = MathTex(r"\vec{p}_2", color=GREEN).next_to(p2d, RIGHT, buff=SMALL_BUFF)

        self.play(
            Create(p1d),
            Create(p2d),
            Write(p1),
            Write(p2)
        )

        self.wait(4)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not title]
        )

        text = Tex(r"La evolución de cada tipo depende de la eficacia de $\vec{p}_i$", color=BLUE)

        self.play(
            Write(text)
        )

        self.wait(3)

        text2 = Tex(r"Llamando $f_i$ al \textit{fitness} de cada tipo podemos", color=BLUE)
        text3 = Tex("expresar el crecimiento relativo con una ecuación diferencial", color=BLUE)

        g = VGroup(text2, text3).arrange(DOWN).center()

        self.play(
            ReplacementTransform(text, text2),
            Write(text3)
        )

        self.wait(3)

        ec_dif = MathTex(r"\frac{x_i'}{x_i} = \mathrm{fitness \, \, de \, \,} i - \mathrm{fitness \, \, media}")

        self.play(
            g.animate.to_edge(UP).shift(DOWN),
            Write(ec_dif)
        )

        self.wait(3)

        ec_dif2 = MathTex(r"x_i' = x_i \left[ f_i(\vec{x}) - \left< f(\vec{x}) \right> \right] ")

        self.play(
            ReplacementTransform(ec_dif, ec_dif2)
        )

        self.wait(3)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )