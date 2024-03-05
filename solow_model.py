from manim import *

class Solow(Scene):

    def construct(self):

        #axes setting
        ax = Axes(
            x_range=[0, 6],
            y_range=[0, 1.4],
            x_length=9,
            y_length=4,
            axis_config={"include_tip": False, "include_ticks":False}).shift(LEFT*1.8)

        x_pos = [x for x in [1.5, 3, 4.5]]
        x_vals = MathTex("Ko","K^*","K1")
        x_dict = dict(zip(x_pos, x_vals))
        ax.add_coordinates(x_dict)

   
        special_ticks = [ax[0].get_tick(val, 0.1).set_color(YELLOW) for val in x_pos]

        labels = ax.get_axis_labels(
            x_label=Tex("Capital, K", font_size=33), y_label=Tex("Investment, Depreciation", font_size=33)
        )

        #end of axes setting


        #graphs config

        n=2.5


        inv_graph= ax.plot(
            lambda x: ((x+1)**(1-n) - 1)/(1.2-n) , color=BLUE_C,
            x_range=[0,5]
            )

        inv_graph_label= ax.get_graph_label(
            inv_graph, label= Tex("Investment", font_size=40)).next_to(inv_graph, UR + DOWN*0.95)


        dep_graph= ax.plot(
            lambda x: 0.225*x, x_range=[0,5], color=ORANGE
            )

        dep_graph_label= ax.get_graph_label(
            dep_graph, label= Tex("Depreciation", font_size=40)).next_to(inv_graph, UR + UP*2)

        graphs= VGroup()
        graphs.add(inv_graph, inv_graph_label, dep_graph, dep_graph_label)

        """con_graph= ax.plot(
            lambda x: ((x+1)**(1-n) - 1)/(1.8-n) , color=YELLOW,
            x_range=[0,5]
            )"""

        #end of graphs config


        #net loss and gain area and t_label

        initial_x= ValueTracker(1.5)

        t_label= always_redraw(lambda: ax.get_T_label(x_val=initial_x.get_value(), 
        graph=inv_graph, label=None, triangle_size=0.1))

        gain= always_redraw (lambda: ax.get_area(dep_graph, color=GREEN, x_range=(initial_x.get_value(),3),
        opacity=0.5,bounded_graph=inv_graph))

        loss= always_redraw (lambda: ax.get_area(dep_graph, color=RED, x_range=(initial_x.get_value(),3),
        opacity=0.5,bounded_graph=inv_graph))




      


        #animation stuff

        self.play(Create(ax),Create(graphs),run_time=2)
        self.add(*special_ticks, labels)
        self.wait(1)

        self.play(Create(t_label))
        self.wait(1)

        self.play(Create(gain))
        self.wait(2)
        self.play(initial_x.animate.set_value(3), run_time=2)
        self.wait(2)

        self.remove(gain)
        self.add(loss) 

        self.play(initial_x.animate.set_value(4.5))
        self.wait(2)
        self.play(initial_x.animate.set_value(3))
        self.wait()






