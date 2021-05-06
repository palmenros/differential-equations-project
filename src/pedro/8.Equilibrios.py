from manim import *

class EDScene(Scene):
    def construct(self):
        title = TextMobject(r"Equilibrios")
        title.scale(1.5)

        self.play(
            Create(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1 / 1.5)
        )

        #Equilibrio de Nash

        tex1 = Tex(r"$\vec{x}^* \in \Delta^p$ es un ", "equilibrio de Nash", " si")
        tex1[1].set_color(RED)
        tex2 = MathTex(r"\vec{x} \cdot A \vec{x}^* \le \vec{x}^* \cdot A \vec{x}^* \, \, \, \, \forall\vec{x} \in \Delta^p")

        VGroup(tex1, tex2).arrange(DOWN).center().shift(0.7*UP)
        brace = BraceLabel(tex2, r"Si no varía $\vec{x}^*$, cualquier otra proporción \\ es peor que $\vec{x}^*$ contra él mismo", DOWN, label_constructor=Tex, color=BLUE)
        brace.label.set_color(BLUE)

        self.play(
            Create(tex1),
            Create(tex2),
            Create(brace)
        )

        self.wait(4)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not title]
        )

        center = Tex(r"Si $\vec{x}^*$ es un equilibrio de Nash, \\ es un equilibrio de la ecuación del replicador")

        self.play(
            Create(center)
        )

        self.wait(4)

        self.play(
            FadeOut(center)
        )

        #Estado evolutivamente estable
        tex1 = Tex(r"$\vec{x}^* \in \Delta^p$ es un ", "estado evolutivamente estable", " si")
        tex1[1].set_color(RED)
        tex2 = MathTex(
            r"\vec{x}^* \cdot A \vec{x} > \vec{x}^* \cdot A \vec{x} \, \, \, \, \forall\vec{x} \neq \vec{x}^* \, \, \textrm{en un entorno de } \vec{x}^*")

        VGroup(tex1, tex2).arrange(DOWN).center().shift(0.7 * UP)
        brace = BraceLabel(tex2,
                           r"$\vec{x}^*$ es el mejor estado en algún entorno suyo",
                           DOWN, label_constructor=Tex, color=BLUE)
        brace.label.set_color(BLUE)

        self.play(
            Create(tex1),
            Create(tex2),
            Create(brace)
        )

        self.wait(4)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not title]
        )

        center = Tex(r"Si $\vec{x}^*$ es un estado evolutivamente estable, \\ es un equilibrio estable de la ecuación del replicador")

        self.play(
            Create(center)
        )

        self.wait(4)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )