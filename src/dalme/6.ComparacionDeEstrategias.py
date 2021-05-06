from manim import *
import requests


class EDScene(Scene):

    def construct(self):
#        title = TextMobject("Halcones y Palomas")
#        title.scale(1.5)

#        self.play(
#            Create(title)
#        )

        array_hawk = [ ]
        array_dove = [ ]
        for i in range(10):
          array_hawk.append(SVGMobject("Hawk.svg", height=1, width=2))
          array_hawk[i].init_colors(self)
          array_hawk[i].set_color(BLUE_C)

          array_dove.append(SVGMobject("Dove.svg", height=1, width=2))
          array_dove[i].init_colors(self)
          array_dove[i].set_color(PURPLE_D)
          if i <= 4:
            array_dove[i].set_x(-4+i*2)
            array_dove[i].set_y(2.8)
            array_hawk[i].set_x(-4+i*2)
            array_hawk[i].set_y(2.8)
          else:
            array_dove[i].set_x(-4+(i-5)*2)
            array_dove[i].set_y(0)
            array_hawk[i].set_x(-4+(i-5)*2)
            array_hawk[i].set_y(0)

        for i in range(10):
          if i <= 8:
            self.play(
              FadeIn(array_dove[i])
            )
          else:
            self.play(
              FadeIn(array_hawk[i])
            )

        rect1 = Rectangle(color=PURPLE_D, height=2, width=9).set_fill(PURPLE_D, 1)
        rect2 = Rectangle(color=BLUE_C, height=2, width=1).set_fill(BLUE_C, 1)

        group = VGroup(rect1, rect2).arrange(RIGHT, buff=0).to_edge(LEFT).shift(1 * DOWN)
        group.set_x(0)
        group.set_y(-3)

        self.play(
            Create(rect1),
            Create(rect2)
        )

        self.wait(12)

        for i in range(5):
          array_dove[8-i].save_state()
          rect_aux1 = Rectangle(color=PURPLE_D, height=2, width=8-i).set_fill(PURPLE_D, 1)
          rect_aux2 = Rectangle(color=BLUE_C, height=2, width=2+i).set_fill(BLUE_C, 1)
          group_aux = VGroup(rect_aux1, rect_aux2).arrange(RIGHT,buff=0).to_edge(LEFT).shift(1*DOWN)
          group_aux.set_x(0)
          group_aux.set_y(-3)

          self.play(
            Transform(group, group_aux),
            Transform(array_dove[8-i], array_hawk[8-i])
          )

        self.wait(10)

        for i in range(4):
          rect_aux1 = Rectangle(color=PURPLE_D, height=2, width=5+i).set_fill(PURPLE_D, 1)
          rect_aux2 = Rectangle(color=BLUE_C, height=2, width=5-i).set_fill(BLUE_C, 1)
          group_aux = VGroup(rect_aux1, rect_aux2).arrange(RIGHT,buff=0).to_edge(LEFT).shift(1*DOWN)
          group_aux.set_x(0)
          group_aux.set_y(-3)

          self.play(
            Transform(group, group_aux),
            Restore(array_dove[4+i])
          )

        self.wait(2)


        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )
