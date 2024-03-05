from manim import*


class Slide14Micro22W2(Scene):
	def construct(self):

		ax= Axes(x_range=[0,7], 
		y_range=[0,12],
		x_length=6,
		y_length=3.5,
       	axis_config={"include_tip": False, "include_ticks":False,"font_size":25},
       
        ).shift(UP*2.2)

		x1_pos = [x for x in [1,1.5,2,2.3]]
		x1_vals = [MathTex("x_{4}",font_size=2),MathTex("x_{3}",font_size=2),
		MathTex("x_{2}",font_size=2),MathTex("x_{1}",font_size=2)]
		x1_dict = dict(zip(x1_pos, x1_vals))
		ax.add_coordinates(x1_dict)

		ax2= Axes(x_range=[0,7],
		x_length=6,
		y_length=3.5, 
		y_range=[0,12],
       	axis_config={"include_tip": False, "include_ticks":False,"font_size":20},
       
        ).shift(DOWN*1.8)

		x2_pos = [x for x in [1,1.5,2,2.3]]
		x2_vals = [MathTex("x_{4}",font_size=2),MathTex("x_{3}",font_size=2),
		MathTex("x_{2}",font_size=2),MathTex("x_{1}",font_size=2)]
		x2_dict = dict(zip(x2_pos, x2_vals))

		y2_pos = [x for x in [9,8,7,6.4]]
		y2_vals = [MathTex("P_{4}",font_size=2),MathTex("P_{3}",font_size=2),
		MathTex("P_{2}",font_size=2),MathTex("P_{1}",font_size=2)]
		y2_dict = dict(zip(y2_pos, y2_vals))


		ax2.add_coordinates(x2_dict,y2_dict)

        #budget line 1

		def func(x):
			return(10-5*x)

		budget= ax.plot(func, x_range=[0,2], color=BLUE_D)
		budget_label= ax.get_graph_label(budget, MathTex('B_{1}(Slope= -2)',font_size=0.00001), x_val=0)
		bud1= VGroup(budget, budget_label)

		eq_dot1= Dot(ax.c2p(1.5,2.5))
		eq_dot1lab= MathTex("e_{1}",font_size=25).next_to(eq_dot1,RIGHT,buff=0.1)
		eqdot1= VGroup(eq_dot1,eq_dot1lab)

		ic1= ax.plot(lambda x: (11.25/x-5), x_range=[1,2])

		#end of budget line 1


		#budget line 2

		def func2(x):
			return 10-3*x
		budget2= ax.plot(func2,x_range=[0,3.33], color=GREEN_D)
		budget2_label= ax.get_graph_label(budget2, MathTex('B_{2}(Slope= -4)',font_size=30), x_val=0.5)
		bud2= VGroup(budget2)

		eq_dot2= Dot(ax.c2p(2,4))
		eq_dot2lab= MathTex("e_{2}",font_size=25).next_to(eq_dot2,RIGHT,buff=0.1)
		eqdot2= VGroup(eq_dot2,eq_dot2lab)

		ic2= ax.plot(lambda x: (12/x-2), x_range=[1.3,3])

		#end of budget line 2


		#budget line 3

		def func3(x):
			return 10-2*x
		budget3= ax.plot(func3,x_range=[0,5], color=GREEN_D)

		eq_dot3= Dot(ax.c2p(2.3,5.4))
		eq_dot3lab= MathTex("e_{3}",font_size=25).next_to(eq_dot3,RIGHT,buff=0.1)
		eqdot3= VGroup(eq_dot3,eq_dot3lab)

		ic3= ax.plot(lambda x: 10.58/x+0.9, x_range=[1.2,3])


		#end of budget line 3

		#budget line 4

		def func4(x):
			return 10-9*x
		budget4= ax.plot(func4,x_range=[0,1.11], color=GREEN_D)

		eq_dot4= Dot(ax.c2p(1,1))
		eq_dot4lab= MathTex("e_{4}",font_size=25).next_to(eq_dot4,RIGHT,buff=0.1)
		eqdot4= VGroup(eq_dot4, eq_dot4lab)

		eqdots= VGroup(eqdot2,eqdot3,eqdot4)

		ic4= ax.plot(lambda x: 9/x-8, x_range=[0.8,1.1] )


		#end of budget line 4

		#price consumption line

		line1= ax.plot_line_graph(x_values=[1,1.5], y_values=[1,2.5],add_vertex_dots =False)
		line2= ax.plot_line_graph(x_values=[1.5,2], y_values=[2.5,4],add_vertex_dots =False)
		line3= ax.plot_line_graph(x_values=[2,2.3], y_values=[4,5.4],add_vertex_dots =False)
		pcline= VGroup(line1, line2, line3)

		arrowline= Arrow(ax.c2p(2.3,5.4),ax.c2p(2.8,6.3), color=YELLOW)
		arrow_lab= Tex("Price Consumption Curve", color=YELLOW, font_size=30).next_to(arrowline, RIGHT, buff=0.3)
		arrow= VGroup(arrowline, arrow_lab)


		#end of price consumption line

		#lines to equilibrium points plane 1


		eqline1= ax.get_lines_to_point(ax.c2p(1,1))
		eqline2= ax.get_lines_to_point(ax.c2p(1.5,2.5))
		eqline3= ax.get_lines_to_point(ax.c2p(2,4))
		eqline4= ax.get_lines_to_point(ax.c2p(2.3,5.4))
		eqline= VGroup(eqline1, eqline2, eqline3, eqline4)


		#end lines to equilibrium points plane 1



		#dashed lines from plane 2 to plane 1

		dline1= DashedLine(ax2.c2p(1,12),ax2.c2p(1,9))
		dline2= DashedLine(ax2.c2p(1.5,12),ax2.c2p(1.5,8))
		dline3= DashedLine(ax2.c2p(2,12),ax2.c2p(2,7))
		dline4= DashedLine(ax2.c2p(2.3,12),ax2.c2p(2.3,6.4))
		dline= VGroup(dline1, dline2, dline3, dline4)


		#end of dashed lines from plane 2 to plane 1

		#demand curve plane 2

		d_curve=ax2.plot(lambda x: 11-2*x, x_range=[0.5,4])
		d_curvelab=Tex("Demand Curve", font_size=30).next_to(d_curve).shift(DOWN*1)
		dcurve= VGroup(d_curve,d_curvelab)

		#eq points and line to x axis

		eqline12= ax2.get_lines_to_point(ax2.c2p(1,9))
		eqline22= ax2.get_lines_to_point(ax2.c2p(1.5,8))
		eqline32= ax2.get_lines_to_point(ax2.c2p(2,7))
		eqline42= ax2.get_lines_to_point(ax2.c2p(2.3,6.4))
		eqline_2= VGroup(eqline12,eqline22,eqline32,eqline42)

		p2eqdot1= Dot(ax2.c2p(1,9))
		p2eqdot1lab= MathTex("e'_{1}",font_size=25).next_to(p2eqdot1,RIGHT,buff=0.1)

		p2eqdot2= Dot(ax2.c2p(1.5,8))
		p2eqdot2lab= MathTex("e'_{2}",font_size=25).next_to(p2eqdot2,RIGHT,buff=0.1)

		p2eqdot3= Dot(ax2.c2p(2,7))
		p2eqdot3lab= MathTex("e'_{3}",font_size=25).next_to(p2eqdot3,RIGHT,buff=0.1)

		p2eqdot4= Dot(ax2.c2p(2.3,6.4))
		p2eqdot4lab= MathTex("e'_{4}",font_size=25).next_to(p2eqdot4,RIGHT,buff=0.1)

		p2eqdot= VGroup(p2eqdot1,p2eqdot1lab, p2eqdot2,p2eqdot2lab,
		p2eqdot3,p2eqdot3lab, p2eqdot4,p2eqdot4lab)


		#end of line from eq to x axis


		#animation
		self.add(ax)
		self.play(Create(bud1))
		self.play(Create(ic1))
		self.wait()
		self.play(Create(eqdot1))
		self.wait()
		self.play(Create(bud2), Create(budget3),Create(budget4))
		self.wait(1.5)

		self.play(Create(ic2), Create(ic3), Create(ic4))
		self.wait(1.5)

		self.play(Create(eqdots))
		self.wait(1.5)

		self.play(Create(pcline),Create(arrow))
		self.wait(1.5)
		self.remove(pcline,arrow)

		self.play(Create(ax2))
		self.wait(1.5)

		self.play(Create(eqline))
		self.wait(1.5)

		self.play(Create(dline),Create(p2eqdot))
		self.wait(1.5)

		self.play(Create(dcurve),Create(eqline_2))
		self.wait(3)


		"""self.add(ax, bud1, bud2,ax2, budget3, budget4,
			eqdots,ic1,ic2,ic3,ic4,pcline,arrow,
			dline1,eqline,dcurve,dline,eqline_2,p2eqdot
			)


		self.play(z.animate.set_value(5),a.animate.set_value(2))
		self.wait(2)"""


		
