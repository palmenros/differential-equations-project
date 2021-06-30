from manim import *


class EDScene(Scene):

    def construct(self):
        title = Tex("Ejemplo: cambio de variables RPS")
        title.scale(1.4)
        
        self.play(
            Write(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP).scale(1/1.4)
        )

        l = BulletedList("Transformación a Lotka-Volterra", "El tiempo cambia y es más rápido", "\\begin{align*}  y_1\'&=y_1(1+y_1-2y_2) \\\\ y_2\'&=y_2(-1+2y_1-y_2)   \\end{align*}", "\\[H=\\frac{y_1 \\cdot y_2}{(y_1+y_2+1)^3}\\]")

        self.play(
            Write(l[0]),Write(l[1]),Write(l[2]),Write(l[3])
        )
        self.wait(10)
        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )
