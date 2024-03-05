from manim import*

class Slide44Micro22W3(Scene):
	def construct(self):

		#edgeworth box
		ax1= Axes(x_range=[0,12], 
		y_range=[0,25],
		x_length=8,
		y_length=5,
       	axis_config={"include_tip": False, "include_ticks":False},
       	x_axis_config={"include_numbers":False}).shift(UP*0.5)

		x_label = ax1.get_x_axis_label(
            Tex("Loaves of Bread per Year").scale(0.65), edge=DOWN, direction=DOWN, buff=1
        )

		y_label = ax1.get_y_axis_label(
            Tex("Litres of Wine per Year").scale(0.65).rotate(90 * DEGREES),
            edge=LEFT,
            direction=LEFT,
            buff=1,
        )

		keeslab= Tex("Kees",font_size=30).next_to(ax1, LEFT).shift(DOWN*3.5)
		botleft= MathTex("O", font_size=30).next_to(keeslab,UP).shift(RIGHT*0.4)
		aaronlab= Tex("Aaron", font_size=30).next_to(botleft,UP).shift(UP*5.5+RIGHT*9.5)
		topright= MathTex("O'", font_size=30).next_to(aaronlab,DL)


		ax_1= VGroup(ax1, x_label, y_label,keeslab,botleft,aaronlab,topright)

		ax2= Axes(x_range=[0,12], 
		y_range=[0,25],
		x_length=-8,
		y_length=-5,
       	axis_config={"include_tip": False, "include_ticks":False},
       	x_axis_config={"include_numbers":False}).shift(UP*0.5)

		edgeworth= VGroup(ax_1, ax2)

		#ic lines
		k_3= ax1.plot(lambda x: 40/x, x_range=[2,9], color=BLUE_D)
		k3= VGroup(k_3)

		k_4= ax1.plot(lambda x: 60/x, x_range=[3,9], color=BLUE_E)
		k4= VGroup(k_4)

		k1= ax1.plot(lambda x: 220/x, x_range=[9.5,11.5], color=BLUE_E)

		k2= ax1.plot(lambda x: 160/x ,x_range=[7.5,10.5], color=BLUE_E)

		k5= ax1.plot(lambda x: 12/x, x_range=[1.5,4], color=BLUE_E)

		k6= ax1.plot(lambda x: 5/x, x_range=[0.7,3],color=BLUE_E)
		

		a1= ax2.plot( lambda x: 6.5/x, x_range= [1,3], color=YELLOW_E)

		a2= ax2.plot(lambda x: 22.5/x, x_range=[2,5], color=YELLOW_E)

		a_3= ax2.plot(lambda x: 73/x, x_range=[3.3,10], color=YELLOW_E)
		a3= VGroup(a_3)

		a_4= ax2.plot(lambda x: 92/x ,x_range=[4,10], color=YELLOW_E)
		a4= VGroup(a_4) 

		a5= ax2.plot(lambda x: 194/x, x_range=[8.5,11])

		a6= ax2.plot(lambda x: 230/x ,x_range=[9.5,11.8])

		
		dot_g= Dot(ax1.c2p(2.3,17.4))
		dot_glab= MathTex("g", font_size=30).next_to(dot_g, UR, buff=0.1)
		dotg= VGroup(dot_g, dot_glab)

		dot_d2= Dot(ax1.c2p(4.5,9))
		dot_d2lab=MathTex("d_{2}", font_size=30).next_to(dot_d2, DL, buff=0.01)
		dotd2= VGroup(dot_d2, dot_d2lab)

		dot_d1= Dot(ax1.c2p(5.9,13))
		dot_d1lab= MathTex("d_{1}", font_size=30).next_to(dot_d1, UR, buff=0.1)
		dotd1= VGroup(dot_d1, dot_d1lab)

		dot_d3= Dot(ax1.c2p(5.4,11.25))
		dot_d3lab= MathTex("d_{3}", font_size=30).next_to(dot_d3, DL, buff=0.01)
		dotd3= VGroup(dot_d3, dot_d3lab)

		dot_d4= Dot(ax1.c2p(10.3,21.3))
		dot_d4lab= MathTex("d_{4}", font_size=30).next_to(dot_d4, DOWN, buff=0.1)
		dotd4= VGroup(dot_d4, dot_d4lab)


		dot_d5= Dot(ax1.c2p(8.8,18))
		dot_d5lab= MathTex("d_{5}", font_size=30).next_to(dot_d5, DOWN, buff=0.1)
		dotd5= VGroup(dot_d5, dot_d5lab)


		dotd6= Dot(ax1.c2p(2.35,5))


		dotd7= Dot(ax1.c2p(1.4,3.3))

		dot_r= Dot(ax1.c2p(2.3,13))
		dot_rlab= MathTex("r", font_size=30).next_to(dot_r, LEFT, buff=0.1)
		dotr= VGroup(dot_r, dot_rlab)


		dashedline1= DashedLine(ax1.c2p(2.3,17.4), ax1.c2p(2.3,13))
		dashedline2= DashedLine(ax1.c2p(2.3,13), ax1.c2p(5.9,13))
		dline= VGroup(dashedline1, dashedline2)
		x_vals = [0, 1.4, 2.35, 4.5, 5.3, 5.9, 7.5, 8.8, 10.3, 12 ]
		y_vals = [0, 3.3, 5, 9, 11.25, 13, 13, 18, 21.3, 25]

		contactcurve = ax1.plot_line_graph(x_values=x_vals, y_values=y_vals, add_vertex_dots=False)
		ccarrow= Arrow(ax1.c2p(7.5,13), ax1.c2p(9.5,10))
		ccarrowlab= Tex("Contact Curve", font_size=20).next_to(ccarrow, DR, buff=0.1)
		contactcurvelab= VGroup(ccarrow, ccarrowlab)

		#end of ic lines


		#animations

		self.add(edgeworth)

		self.play(Create(a1), Create(k1), Create(a2), Create(k2))
		self.play(Create(dotd4), Create(dotd5))
		self.wait(1)

		self.play(Create(a5), Create(a6), Create(k5), Create(k6))
		self.play(Create(dotd6), Create(dotd7))
		self.wait(1)

		self.play(Create(a4), Create(k4))
		self.play(Create(dotd3))
		self.wait(2)
		self.play(Create(contactcurve), Create(contactcurvelab))
		self.wait(2)

		self.play(Create(k3), Create(a3))
		self.play(Create(dotg), Create(dotd1), Create(dotd2))
		self.wait(2)

		self.play(Create(dotr), Create(dline))
		self.wait(4)


		"""self.add(edgeworth, k3, k4 ,a3, dotd1, dotg, a4, dotd2, dotd3, k1, a1, k2, a2,
			k5, a6, k6, a5, dotd4, dotd5, dotd6, dotd7, contactcurve)"""




