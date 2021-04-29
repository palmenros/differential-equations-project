from manim import *

class EDScene(Scene):
    def construct(self):
        title = TextMobject(r"Cálculo del \textit{fitness}")
        title.scale(1.5)

        self.play(
            Create(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1 / 1.5)
        )

        text = TextMobject(r"Llamemos U a la matriz de payoff").next_to(title, DOWN).shift(0.3*DOWN)
        text.shift([-text.get_center()[0], 0, 0])

        table1 = Tex(r"""
                    \begin{table}[]
            \begin{tabular}{l|ll}
                                & \textbf{Cooperar} & \textbf{Traicionar} \\ \hline
            \textbf{Cooperar}   & {4}                 & 0                   \\
            \textbf{Traicionar} & 5                 & 3                  
            \end{tabular}
            \end{table}
        """)

        table2 = Tex(r"""
                    \begin{table}[]
            \begin{tabular}{l|ll}
                                & \textbf{C} & \textbf{T} \\ \hline
            \textbf{C}   & 4                 & 0                   \\
            \textbf{T} & 5                 & 3                  
            \end{tabular}
            \end{table}
        """)

        self.play(
            Create(text),
            Create(table1),
        )

        mat = Matrix([["4", "0"], ["5", "3"]], left_bracket="\\big(", right_bracket="\\big)").next_to(table2, RIGHT)

        vec = Matrix([["1"], ["0"]], left_bracket="\\big(", right_bracket="\\big)")

        g = VGroup(table2, MathTex(r" \, \, \, \Rightarrow \, \, \, U ="), mat, vec).arrange(RIGHT).center()

        self.wait(2)

        self.play(
            ReplacementTransform(table1, table2),
            *[Create(mob) for mob in g if mob is not table2 and mob is not vec]
        )

        c1, c2 = mat.get_columns()

        rect1 = SurroundingRectangle(c1, color=BLUE)
        rect2 = SurroundingRectangle(c2, color=RED)

        brace1 = BraceLabel(rect1, "Oponente coopera", label_constructor=Tex, brace_direction=DOWN, color=BLUE)
        brace2 = BraceLabel(rect2, "Oponente traiciona", label_constructor=Tex, brace_direction=DOWN, color=RED)

        brace1.label.set_color(BLUE)
        brace2.label.set_color(RED)

        self.wait(3)

        vec.set_color(BLUE)

        self.play(
            Create(rect1),
            Create(vec),
            Create(brace1)
        )

        self.wait(3)

        vec2 = Matrix([["0"], ["1"]], left_bracket="\\big(", right_bracket="\\big)").move_to(vec)
        vec2.set_color(RED)

        self.play(
            Uncreate(rect1),
            ReplacementTransform(brace1, brace2),
            ReplacementTransform(vec, vec2),
            Create(rect2)
        )

        self.wait(5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not title]
        )

        texto = Tex(r"Payoff de la estrategia del tipo $i$ contra el tipo $j$")
        tex = MathTex(r"a_{ij} = \vec{p}_i \cdot U \vec{p}_j ")

        VGroup(texto, tex).arrange(DOWN).center()

        self.play(
            Create(texto),
            Create(tex)
        )

        self.wait(5)

        texto2 = Tex(r"\textit{Fitness} del tipo $i$")
        tex2 = MathTex(r"f_i(\vec{x}) = \sum_{j=1}^{p}{a_{ij}x_j} = \left\{ A\vec{x} \right\}_i ")

        VGroup(texto2, tex2).arrange(DOWN).center()

        self.play(
            ReplacementTransform(texto, texto2),
            ReplacementTransform(tex, tex2)
        )

        self.wait(4)

        texto3 = Tex(r"Ecuación del replicador", color=BLUE)
        ecuacion = MathTex(r"x_i' = x_i \left[ \left( A\vec{x} \right)_i - \vec{x} \cdot A \vec{x} \right] ")

        VGroup(texto3, tex2).arrange(DOWN).center()
        texto3.shift(UP*0.3)

        self.play(
            FadeOut(title),
            ReplacementTransform(texto2, texto3),
            ReplacementTransform(tex2, ecuacion),
            Create(SurroundingRectangle(ecuacion, buff=MED_LARGE_BUFF, stroke_width=1))
        )

        self.wait(4)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

