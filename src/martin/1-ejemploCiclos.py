from manim import *
import math
import requests
import numpy

listaPuntos = []
r = 0
prec = 0
it = 0
vert = []
def listaResEq():
    global listaPuntos
    global r
    global prec
    global it
    p = (1-r)/2
    s = (1-r)/2
    rN = r
    listaPuntos = [(rN,p,s)]
    for i in range(it):
        rN+=rN*(s-p)*prec
        p+=p*(rN-s)*prec
        s+=s*(p-rN)*prec
        listaPuntos.append((rN,p,s))
    return listaPuntos

class EDScene(Scene):
    global r
    global listaPuntos
    global prec
    global it
    global vert
    def func(self, t):
        global r
        global listaPuntos
        global prec
        global it
        global vert
        t/=prec
        t = math.floor(t)
        return vert[0]*listaPuntos[t][0]+vert[1]*listaPuntos[t][1]+vert[2]*listaPuntos[t][2]
        
    def construct(self):
        global r
        global listaPuntos
        global prec
        global it
        global vert
        title = Tex("Ejemplo. Más dimensiones. Ciclos")
        title.scale(1.4)

        self.play(
            Write(title)
        )
        self.wait(1)
        self.play(
            title.animate.to_edge(UP).scale(1/1.4)
        )
        aclaracion = Tex("Más dimensiones $\\Longrightarrow$ clasificación más complicada\n\nNo siempre se alcanza un equilibrio\n\nSolución periódica")
        aclaracion.set_color("#BBFFBB").shift(UP)
        self.play(
        	Write(aclaracion)
        )
        self.wait(5)
        
        aclPayoffMatrix = Tex("Juego de suma 0; $\\vec{x} \\cdot A \\vec{x} = -\\vec{x} \\cdot A \\vec{x} $").set_color(ORANGE).shift(DOWN*1/2)
        recordatorio = Tex("$x_i\'=x_i[(A\\vec{x})_i- \\vec{x} \\cdot A\\vec{x}]$").set_color(BLUE).shift(DOWN)
        consPayoffMatrix = Tex("$\\Longrightarrow x'_i=x_i(A \\vec{x})_i$").set_color(ORANGE).shift(DOWN*3/2)
        self.play(Write(aclPayoffMatrix))
        self.play(Write(recordatorio))
        self.wait(5)
        self.play(FadeInFrom(consPayoffMatrix,RIGHT))
        self.wait(5)
        self.play(
            FadeOut(aclaracion),
            FadeOut(aclPayoffMatrix),
            FadeOut(recordatorio),
            FadeOut(consPayoffMatrix)
        )
        title2 = Tex("Ejemplo: piedra, papel, tijera. Matriz de Payoff")
        title2.to_edge(UP)
        self.play(
            ReplacementTransform(title, title2)
        )
        R1 = SVGMobject("Rock.svg", height=.5, width=.5).set_color("#D0A67B")
        R2 = SVGMobject("Rock.svg", height=.5, width=.5).set_color("#D0A67B")
        P1 = SVGMobject("Paper.svg", height=.3, width=.3).set_color("#F0F0F0")
       	P2 = SVGMobject("Paper.svg", height=.3, width=.3).set_color("#F0F0F0")
        S1 = SVGMobject("Scissors.svg", height=.5, width=.5).set_color(ORANGE)
        S2 = SVGMobject("Scissors.svg", height=.5, width=.5).set_color(ORANGE)

        

        
        R1.init_colors(self)
        R1.set_x(-1.65)
        R1.set_y(.5)
        R2.init_colors(self)
        R2.set_x(-.5)
        R2.set_y(1.2)
        P1.init_colors(self)
        P1.set_x(-1.65)
        P1.set_y(-.5)
        P2.init_colors(self)
        P2.set_x(1)
        P2.set_y(1.2)
        S1.init_colors(self)
        S1.set_x(-1.65)
        S1.set_y(-1.5)
        S2.init_colors(self)
        S2.set_x(2.5)
        S2.set_y(1.2)
        
        payoffMat = Tex("{\\Large \\[A= ~~ \\begin{pmatrix}0&-1&1\\\\1&0&-1\\\\-1&1&0 \\end{pmatrix}\\]}").shift(DOWN*1/2)

        self.play(
          FadeInFrom(R1, RIGHT),
          FadeInFrom(R2, RIGHT),
          FadeInFrom(P1, RIGHT),
          FadeInFrom(P2, RIGHT),
          FadeInFrom(S1, RIGHT),
          FadeInFrom(S2, RIGHT),
          FadeInFrom(payoffMat, RIGHT)
        )
        self.wait(10)
        cAc = 3 * LEFT
        self.play(
            ApplyMethod(R1.shift,cAc),
            ApplyMethod(R2.shift,cAc),
            ApplyMethod(P1.shift,cAc),
            ApplyMethod(P2.shift,cAc),
            ApplyMethod(S1.shift,cAc),
            ApplyMethod(S2.shift,cAc),
            ApplyMethod(payoffMat.shift,cAc)
            )
        self.wait(1)
        sistEcEj = Tex("{\\large \\begin{align*} r\'&=r(s-p) \\\\p\'&=p(r-s) \\\\s\'&=s(p-r)  \\end{align*}}").shift(1*UP+4*RIGHT)
        self.play(Write(sistEcEj))
        self.wait(5)
        sistEcConc = Tex("{\\large\\[\\frac{r\'}{r}+\\frac{p\'}{p}+\\frac{s\'}{s}=0\\]}").shift(3/2*DOWN+4*RIGHT).set_color(PURPLE)
        self.play(Write(sistEcConc))
        self.wait(2)
        sistEcConf = Tex("{\\large\\[r \\cdot p \\cdot s = h \\]}").shift(5/2*DOWN+4*RIGHT).set_color(PURPLE)
        self.play(Write(sistEcConf))
        self.wait(5)
        title3 = Tex("Piedra, papel, tijera. Trayectorias en función de $h$")
        title3.to_edge(UP)
        self.play(
            ReplacementTransform(title2, title3),
            FadeOut(R1),
            FadeOut(R2),
            FadeOut(P1),
            FadeOut(P2),
            FadeOut(S1),
            FadeOut(S2),
            FadeOut(payoffMat),
            FadeOut(sistEcEj),
            FadeOut(sistEcConc),
            FadeOut(sistEcConf),
        )
        self.wait(1)
        triangle = Triangle().set_color(WHITE).scale(3).shift(1/2*DOWN)
        

        vert = triangle.get_vertices()
        print(vert)
        print(vert[0]+vert[1])
        print(type(vert))
        d1 = Dot(vert[0], color=GREY, radius=0.11)
        d2 = Dot(vert[1], color="#F0F0F0", radius=0.11)
        d3 = Dot(vert[2], color=ORANGE, radius=0.11)
        dC = Dot(1/3*(vert[0]+vert[1]+vert[2]), color="#8DD134", radius=0.11)
        l1 = MathTex("R", color=GREY).next_to(d1, UP, buff=MED_SMALL_BUFF)
        l2 = MathTex("P", color="#F0F0F0").next_to(d2, LEFT, buff=MED_SMALL_BUFF)
        l3 = MathTex("S", color=ORANGE).next_to(d3, RIGHT, buff=MED_SMALL_BUFF)
        lC = Tex("\\[N=\\frac{1}{3}(R+P+S)\\]", color="#8DD134").shift(4*RIGHT+2*UP)
        exp = Tex("$N$ es el equilibrio de Nash", color="#8DD134").shift(4*RIGHT+UP)
        self.play(
            FadeIn(triangle),
            FadeIn(d1),
            FadeIn(d2),
            FadeIn(d3),
            FadeIn(dC),
            FadeIn(l1),
            FadeIn(l2),
            FadeIn(l3),
            FadeIn(lC),
            FadeIn(exp)
        )
        self.wait(15)
        listaColores = ["#00FF69","#2AFF82","#55FF9B","#80FFB4","#AAFFCD","#D5FFE6","#FFFFFF"]
        listaPlots = []
        for i in range(1,6):
            r = (3+i)/9
            prec = 0.0001
            it = 200000
            listaResEq()
            plot = ParametricFunction(self.func, t_max = 14+i, dt=5e-02, fill_opacity=0).set_color(listaColores[i])
            listaPlots.append(plot)
            texto = Tex("$h_"+str(i)+"="+str(round(r*(1-r)**2/4,6))+"$", color=listaColores[i]).shift(4*LEFT+(3/2-1/2*i)*UP)
            self.play(ShowCreation(plot),FadeIn(texto),run_time=3)
        self.wait(15)
        self.play(*[Uncreate(plot) for plot in listaPlots],run_time=5)
        self.wait(2)
        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )
