# y Equilibrios de Nash
from manim import *
import requests


class EDScene(Scene):

    def construct(self):
        title0 = TextMobject("Equilibrio de Nash")
        title0.scale(1.5)

        self.play(Create(title0))
        self.wait(22)

        Road = SVGMobject("Road.svg", height=2, width=4)
        Road.init_colors(self)
        Road.set_x(0)
        Road.set_y(0)

        self.play(
          title0.animate.to_edge(UP).scale(1)
        )

        self.play(
          FadeIn(Road)
        )

        self.wait(10)

        title = TextMobject("Dilema del Prisionero")
        title.scale(1.5)

        self.play(
          FadeOut(title0),
          FadeOut(Road)
        )

        self.play(
            Create(title)
        )

        self.wait(2)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1/1.5)
        )

        Men1 = SVGMobject("Men.svg", height=1, width=2)
        Men1.init_colors(self);
        Men1.set_x(-1)
        Men1.set_y(-1)

        Men2 = SVGMobject("Men.svg", height=1, width=2)
        Men2.init_colors(self);
        Men2.set_x(1)
        Men2.set_y(-1)

        self.play(
          FadeIn(Men1),
          FadeIn(Men2)
        )

        self.wait(2)

        Men1.generate_target()
        Men1.target.move_to((-3,-1,0))
        Men2.generate_target()
        Men2.target.move_to((3,-1,0))

        self.play(
          MoveToTarget(Men1),
          MoveToTarget(Men2)
        )

        self.wait(2)

        Men1.generate_target()
        Men1.target.move_to((0,-1,0))
        Men2.generate_target()
        Men2.target.move_to((0,-1,0))

        self.play(
          MoveToTarget(Men1),
          MoveToTarget(Men2)
        )

        self.play(
          FadeOut(Men2)
        )

        self.wait(2)

        Cooperar = SVGMobject("Cooperar.svg", height=1.5, width=2.8)
        Cooperar.init_colors(self)
        Cooperar.set_x(0)
        Cooperar.set_y(-1)

        Cooperartit = TextMobject("Cooperar")
        Cooperartit.scale(1.5)
        Cooperartit.set_color(BLUE_C)
        Cooperartit.set_x(0.5)
        Cooperartit.set_y(-3.5)

        self.play(
          Transform(Men1, Cooperar),
          FadeIn(Cooperartit)
        )

        self.wait(5)

        Men1.generate_target()
        Men1.target.move_to((-2,-1,0))
        Cooperartit.generate_target()
        Cooperartit.target.move_to((-2,-3.5,0))
        self.play(
           MoveToTarget(Men1),
           MoveToTarget(Cooperartit)
        )

        Traicionar = SVGMobject("Traicionar.svg", height=1.5, width=2.8)
        Traicionar.init_colors(self)
        Traicionar.set_x(2)
        Traicionar.set_y(-1)

        Traicionartit = TextMobject("Traicionar")
        Traicionartit.scale(1.5)
        Traicionartit.set_color(BLUE_C)
        Traicionartit.set_x(2)
        Traicionartit.set_y(-3.5)

        self.play(
          FadeIn(Traicionar),
          FadeIn(Traicionartit)
        )

        self.wait(20)

        self.play(
          FadeOut(Men1),
          FadeOut(Cooperartit),
          FadeOut(Traicionar),
          FadeOut(Traicionartit)
        )

        table = Tex(r"""
                \begin{table}[]
                \begin{tabular}{c|c|c}
                & \textbf{Cooperar} & \textbf{Traicionar} \\ \hline
                & &  \\
                 \textbf{Cooperar} & 4 & 0 \\
                 & & \\
                 \textbf{Traicionar} & 5 & 3 \\
                 & &
                \end{tabular}
                \end{table}""").scale(1.5)

        self.play(
          FadeIn(table)
        )

        self.wait(6)

        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )
