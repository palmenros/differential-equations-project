from manim import *


class EDScene(Scene):

    def construct(self):
        title = Tex("Sección 3: Relación con\\\\Lotka-Volterra. Otros modelos")
        title.scale(1.5)
        title.set_color(BLUE)
        title.move_to([0, 0, 0])

        self.play(
            Write(title)
        )

        self.wait(3)

        self.play(
            title.animate.to_edge(UP).scale(1/1.5)
        )

        l = BulletedList("Ecuaciones generalizadas de Lotka-Volterra", "Cambio de variables. Órbitas", "Introducción a modelos más generales", "Soluciones no explícitas,\\\\no obstante existen invariantes").shift(DOWN)

        self.play(
            Write(l[0])
        )

        self.wait(3)
        self.play(
            Write(l[1])
        )

        self.wait(3)
        self.play(
            Write(l[2])
        )
        l[3].set_color("#BBFFBB")
        self.wait(3)
        self.play(
            Write(l[3])
        )
        self.wait(9)
        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )