from manim import *
import math
listaPuntos = []
r = 0
prec = 0
it = 0
def listaResEq():
    global listaPuntos
    global r
    global prec
    global it
    y1 = r
    y2 = r
    listaPuntos = [(y1,y2)]
    for i in range(it):
        y1+=y1*(1+y1-2*y2)*prec
        y2+=y2*(-1+2*y1-y2)*prec
        listaPuntos.append((y1,y2))
    return listaPuntos
class EDScene(GraphScene):
    global r
    global listaPuntos
    global prec
    global it
    def func(self, t):
        global r
        global listaPuntos
        global prec
        global it
        t/=prec
        t = math.floor(t)
        return self.coords_to_point(listaPuntos[t][0],listaPuntos[t][1])
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=20,
            x_axis_label="$y_1$",
            y_axis_label="$y_2$",
            num_graph_anchor_points=100,
            y_min=0,
            y_max=12.5,
            graph_origin=np.array([- 4, - 3, 0.0]),
            exclude_zero_label=False,
            axes_color=GREEN,
            x_labeled_nums=range(0, 22, 2),
            y_labeled_nums=range(0, 14, 2),
            **kwargs
        )
        self.function_color = RED

    def construct(self):
        global r
        global listaPuntos
        global prec
        global it
        self.setup_axes(animate=True)
        self.wait(1)
        d3 = Dot(self.coords_to_point(0,0), color=ORANGE, radius=0.11)
        dC = Dot(self.coords_to_point(1,1), color="#8DD134", radius=0.11)
        l3 = MathTex("S", color=ORANGE).next_to(d3, LEFT+DOWN, buff=MED_SMALL_BUFF)
        lC = Tex("\\[N=(1,1)\\]", color="#8DD134").shift(4*RIGHT+2*UP)
        self.play(
            FadeIn(d3),
            FadeIn(dC),
            FadeIn(l3),
            FadeIn(lC),
        )
        self.wait(10)
        listaColores = ["#00FF69","#2AFF82","#55FF9B","#80FFB4","#AAFFCD","#D5FFE6","#FFFFFF"]
        listaPlots = []
        for i in range(1,6):
            r = 2*i
            prec = 0.0001
            it = 200000
            listaResEq()
            plot = ParametricFunction(self.func, t_max = 5, dt=5e-02, fill_opacity=0).set_color(listaColores[i])
            listaPlots.append(plot)
            texto = Tex("$H_"+str(i)+"="+str(round(r**2/(1+2*r)**3,6))+"$", color=listaColores[i]).shift(4*RIGHT+(3/2-1/2*i)*UP)
            
            self.play(ShowCreation(plot),FadeIn(texto),run_time=2)
        self.play(*[Uncreate(plot) for plot in listaPlots],run_time=3)
        self.wait(2)
        self.play(
            *[ FadeOut(mob) for mob in self.mobjects ]
        )