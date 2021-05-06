from manim import *
import math
import requests


class EDScene(Scene):

    def construct(self):
        title = TextMobject("Enfrentamientos y Matriz de Payoff")
        title.scale(1.5)

        self.play(
            Create(title)
        )

        self.wait(9)

        self.play(
            title.animate.to_edge(UP + LEFT).scale(1/1.5)
        )

        Hawk1 = SVGMobject("Hawk.svg", height=1, width=2)
        Hawk1.init_colors(self)
        Hawk1.set_x(-1)
        Hawk1.set_y(1)

        Hawk2 = SVGMobject("Hawk.svg", height=1, width=2)
        Hawk2.init_colors(self)
        Hawk2.set_x(1)
        Hawk2.set_y(1)

        self.play(
          FadeInFrom(Hawk1, LEFT),
          FadeInFrom(Hawk2, RIGHT)
        )

        self.wait(23)

        textHawk1 = TextMobject(r"$\frac{G-C}{2}$", height=1, width=2, color=BLUE_D)

        textHawk1.set_x(-4)
        textHawk1.set_y(1)

        textHawk2 = TextMobject(r"$\frac{G-C}{2}$", height=1, width=2, color=BLUE_D)

        textHawk2.set_x(4)
        textHawk2.set_y(1)
        self.play(
          FadeIn(textHawk1),
          FadeIn(textHawk2)
        )

        self.wait(3)

        Hawk3 = SVGMobject("Hawk.svg", height=1, width=2)
        Hawk3.init_colors(self)
        Hawk3.set_x(-1)
        Hawk3.set_y(-1)

        Dove1 = SVGMobject("Dove.svg", height=1, width=2)
        Dove1.init_colors(self)
        Dove1.set_x(1)
        Dove1.set_y(-1)

        self.play(
          FadeInFrom(Hawk3, LEFT),
          FadeInFrom(Dove1, RIGHT)
        )

        self.wait(18)

        textHawk3 = TextMobject(r"$G$", height=1, width=0.5, color=GREEN_E)

        textHawk3.set_x(-4)
        textHawk3.set_y(-1)

        textDove1 = TextMobject(r"$0$", height=1, width=0.4, color=RED_E)

        textDove1.set_x(4)
        textDove1.set_y(-1)
        self.play(
          FadeIn(textHawk3),
          FadeIn(textDove1)
        )

        self.wait(6)

        Dove2 = SVGMobject("Dove.svg", height=1, width=2)
        Dove2.init_colors(self)
        Dove2.set_x(-1)
        Dove2.set_y(-3)

        Dove3 = SVGMobject("Dove.svg", height=1, width=2)
        Dove3.init_colors(self)
        Dove3.set_x(1)
        Dove3.set_y(-3)

        self.play(
          FadeInFrom(Dove2, LEFT),
          FadeInFrom(Dove3, RIGHT)
        )

        self.wait(25)

        textDove2 = TextMobject(r"$\frac{G}{2}$", height=1, width=0.5, color=PURPLE_E)

        textDove2.set_x(-4)
        textDove2.set_y(-3)

        textDove3 = TextMobject(r"$\frac{G}{2}$", height=1, width=0.5, color=PURPLE_E)

        textDove3.set_x(4)
        textDove3.set_y(-3)
        self.play(
          FadeIn(textDove2),
          FadeIn(textDove3)
        )

        self.wait(4)

        textHawk1.generate_target()
        textHawk1.target.move_to((0,0,0))

        textHawk2.generate_target()
        textHawk2.target.move_to((0,0,0))

        textHawk3.generate_target()
        textHawk3.target.move_to((3.8,0,0))

        textDove1.generate_target()
        textDove1.target.move_to((0,-2,0))

        textDove2.generate_target()
        textDove2.target.move_to((3.8,-2,0))

        textDove3.generate_target()
        textDove3.target.move_to((3.8, -2, 0))

        self.play(
          FadeOut(Dove1),
          FadeOut(Dove2),
          FadeOut(Dove3),
          FadeOut(Hawk1),
          FadeOut(Hawk2),
          FadeOut(Hawk3),
          MoveToTarget(textHawk1),
          MoveToTarget(textHawk2),
          MoveToTarget(textHawk3),
          MoveToTarget(textDove1),
          MoveToTarget(textDove2),
          MoveToTarget(textDove3)
        )

        self.wait(1)

        table = Tex(r"""
                \begin{table}[]
                \begin{tabular}{c|c|c}
                & \textbf{Halcón} & \textbf{Paloma} \\ \hline
                & & \\
                 \textbf{Halcón} & & \\
                 & & \\
                 \textbf{Paloma} & \\
                 & &
                \end{tabular}
                \end{table}""").scale(1.5)
        table.set_x(0)
        table.set_y(-0.5)

        self.play(
          FadeIn(table)
        )

        self.wait(19)

        arrow = MathTex(r"\longrightarrow").shift(DOWN + 0.8 * RIGHT).scale(1.5)
        arrow.rotate(math.pi / 2)
        arrow.next_to(textDove1, DOWN)

        # other arrrows: https://talkingphysics.wordpress.com/2018/06/12/more-shapes-manim-series-part-3/
        self.play(
          FadeIn(arrow),
          ScaleInPlace(textDove1, 1.4)
        )

        self.play(
          ScaleInPlace(textDove1, 0.7142)
        )

        self.play(
          ScaleInPlace(textDove1, 1.4)
        )

        self.play(
          ScaleInPlace(textDove1, 0.7142)
        )

        self.wait(22)

        self.play(
          FadeOut(arrow)
        )

#        matriz = Tex(r"""
 #               $\begin{pmatrix}
 #               & &
 #               \end{pmatrix}$""").scale(6)
 #       matriz.set_x(1.5)
 #       matriz.set_y(-0.5)

        matriz = Tex(r"""
                $\begin{pmatrix}
                & \frac{G-C}{2} & G \\
                & 0 & \frac{G}{2}
                \end{pmatrix}$""").scale(2)
        matriz.set_x(0)
        matriz.set_y(0)

        self.play(
          Transform(table, matriz),
          FadeOut(textDove1),
          FadeOut(textDove2),
          FadeOut(textDove3),
          FadeOut(textHawk1),
          FadeOut(textHawk2),
          FadeOut(textHawk3)
        )

        self.wait(6)

#        Dove = SVGMobject("Dove.svg", height=1, width=2)
#        Dove.init_colors(self);
#        Dove.set_x(-1)
#        Dove.set_y(2)

 #       Hawk = SVGMobject("Hawk.svg", height=1, width=2)
 #       Hawk.init_colors(self);

#        self.play(
#          FadeInFrom(Dove, LEFT)
#        )

        #Dove.generate_target()
        #Dove.target.shift(3*LEFT)
        #self.play(
        #  MoveToTarget(Dove)
        #)

#        Hawk.set_x(1)
#        Hawk.set_y(2)


#        self.play(
#          FadeIn(Hawk)
#        )

#        self.wait(3)

#        Dove.generate_target()
#        Dove.target.shift(LEFT)
        #Dove.shift(3*RIGHT)

#        Hawk.save_state()

#        self.play(
#          MoveToTarget(Dove),
          #ScaleInPlace(Dove, 2),
#          FadeOut(Hawk)
#        )

#        self.play(ScaleInPlace(Dove,2))

#        self.wait(2)

#        self.play(ScaleInPlace(Dove, 0.5),
#        Transform(Dove, Hawk))

#        self.play(ScaleInPlace(Hawk, 2))

#        self.wait(3)

#        self.play(
#          ScaleInPlace(Hawk, 0.5)
#        )

        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )
