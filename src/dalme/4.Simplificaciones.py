from manim import *


class EDScene(Scene):

    def construct(self):
        title = TextMobject("Simplificaciones")
        title.scale(1.5)

        self.play(
            Create(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1/1.5)
        )

        l = BulletedList(r"Los individuos siguen siempre la misma estrategia", "Las estrategias se heredan", "El recurso tiene un valor G y resultar herido un coste C", "C > G", "El payoff mide el éxito reproductivo")

        self.play(
            Write(l[0])
        )

        self.wait(7)
        self.play(
            Write(l[1])
        )

        self.wait(3)
        self.play(
            Write(l[2])
        )

        self.wait(3)

        self.play(
            Write(l[3])
        )
        self.wait(3)

        self.play(
            Write(l[4])
        )

        self.wait(12)

        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )
