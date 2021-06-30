from manim import *


class EDScene(Scene):

    def construct(self):
        title = Tex("Invarianza en Lotka-Volterra")
        title.scale(1.4)
        
        self.play(
            Write(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP).scale(1/1.4)
        )

        l = BulletedList("Hay constantes de movimiento apropiadas en cualquier\\\\ecuación de Lotka-Volterra", "\\[ x\' = \\alpha x - \\beta x y,y\' = \\delta x y - \\gamma y\\]", "Separación de variables", "\\[\\frac{\\beta y - \\alpha}{y} y\' + \\frac{\\delta x - \\gamma}{x} x\' = 0\\]", "\\[H = \\delta x - \\gamma \\ln(x) + \\beta y - \\alpha \\ln(y)\\]").shift(0.5*DOWN)

        self.play(
            Write(l[0]),Write(l[1])
        )
        self.wait(7)
        self.play(Write(l[2]),Write(l[3]),Write(l[4]))
        self.wait(7)
        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )
