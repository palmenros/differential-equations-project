from manim import *


class EDScene(Scene):

    def construct(self):
        
        title = Tex("Cambio de variables Lotka-Volterra / replicador").to_edge(UP)
        LV0 = MathTex("y'_i=y_i\\left( r_i+\\sum_{j=1}^{n} b_{ij}y_j \\right)").shift(2*UP).set_color(BLUE)
        Repl = Tex("$x_i\'=x_i[(A\\vec{x})_i- \\vec{x} \\cdot A\\vec{x}]$").shift(1/2*UP).set_color(BLUE)
        self.add(title);self.add(LV0);
        self.wait(1)
        self.play(Write(Repl))
        self.wait(2)
        constX = Tex("$x_i >0,\\sum_{i=1}^px_i=1$").shift(1/2*UP+3*RIGHT).set_color(BLUE)
        constY = Tex("$y_i >0$").shift(2*UP+3*RIGHT).set_color(BLUE)
        self.play(
            ApplyMethod(LV0.shift,2*LEFT),
            ApplyMethod(Repl.shift,2*LEFT)
        )
        self.wait(1)
        self.play(
            Write(constX),
            Write(constY)
            )
        self.wait(5)
        #Header teorema "#C92FFC"
        #Introducción teorema "#EAB5FC"
        #Demostraciones "#8F79FC"
        headerCD = Tex("Teorema (fórmula del cambio $REPL \\to L-V$)").set_color("#C92FFC").shift(0.4*DOWN)
        bodyCD = Tex("{ \\footnotesize La ecuación del replicador en $p$ variables es equivalente a un sistema de\\\\Lotka-Volterra de $p-1$ variables tomando el siguiente cambio de variables\\\\invertible, que lleva órbitas de una ecuación en órbitas de la otra.\\[y_i = x_i/x_n \\iff x_i = y_i/\\sum_{j=1}^n y_j, \\text{ donde }y_n=1\\text{. Geometría proyectiva}\\]}").set_color("#EAB5FC").shift(2.3*DOWN)
        self.play(Write(headerCD),Write(bodyCD))
        self.wait(40)
        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )
