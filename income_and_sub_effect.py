from manim import*


class Slide40Micro22W2(Scene):
	def construct(self):

		ax= Axes(x_range=[0,8], 
		y_range=[0,25],
		x_length=5,
		y_length=6.3,
       	axis_config={"include_tip": False, "include_ticks":False},
       	x_axis_config={"include_numbers":False}
       
        ).shift(UP*0.8)

		ax2= Axes(x_range=[0,8], 
		y_range=[0,25],
		x_length=5,
		y_length=6.3,
       	axis_config={"include_tip": False, "include_ticks":False},
       	x_axis_config={"include_numbers":False, "font_size":20}
       
        ).shift(UP*0.8)

		y_pos = [x for x in [4.5,6]]
		y_vals = MathTex("y_{2}","y_{1}")
		y_dict = dict(zip(y_pos, y_vals))
		x_labels =[0]
		test1= (ax2.add_coordinates(x_labels, y_dict))

		x_pos = [x for x in [1.25, 1.60, 3]]
		x_vals = MathTex("x_{2}","x_{c}","x_{1}")
		x_dict = dict(zip(x_pos, x_vals))
		y_labels =[0]
		test2= (ax2.add_coordinates(x_dict,y_labels))



        #budget lines

		def func(x):
			return(12-2*x)

		budget= ax.plot(func, x_range=[0,6], color=BLUE_D)
		budget_label= ax.get_graph_label(budget, MathTex('B_{1}',font_size=35),
		 x_val=5.1)
		bud1= VGroup(budget, budget_label)

		b2yint= ValueTracker(12)
		b2xint= ValueTracker(5)
		b2slope= ValueTracker(2)
	

		budget2= always_redraw( lambda: ax.plot(lambda x: b2yint.get_value()- b2slope.get_value()*x, 
		x_range=[0,b2xint.get_value()], color=YELLOW_D))

		budget2_label= ax.get_graph_label(budget2, MathTex('B_{2}',font_size=33), 
			x_val=1.8).shift(DOWN*1.9)
		bud2= VGroup(budget2,budget2_label)


		bcyint= ValueTracker(12)
		bcxint= ValueTracker(2)

		bccurve= always_redraw( lambda: ax.plot(lambda x: bcyint.get_value() - 6*x,
			x_range=[0,bcxint.get_value()],color=GREEN_D))
		bccurve_label= ax.get_graph_label(bccurve, MathTex('B_{c}',font_size=33), 
			x_val=3.42).shift(UP*1.2)



		#end of budget lines


		#equilibrium dots lines arrows and ics

		eq1_dot= Dot(ax.c2p (3,6))
		eq1_dotlab= MathTex('e_{1}',font_size=33).next_to(eq1_dot, RIGHT, buff=0.2)
		eq1dot= VGroup(eq1_dot,eq1_dotlab)

		ic1= ax.plot(lambda x: 18/x, x_range=[1.2,4.5])

		eq2_dot= Dot(ax.c2p (1.25,4.5))
		eq2_dotlab= MathTex('e_{2}',font_size=30).next_to(eq2_dot, LEFT, buff=0.2).shift(DOWN*0.3)
		eq2dot= VGroup(eq2_dot,eq2_dotlab)

		ic2= ax.plot(lambda x: 7.2/x-1, x_range=[0.8,2])

		eqc_dot= Dot (ax.c2p(1.60,11.05))
		eqc_dotlab= MathTex('e_{c}',font_size=30).next_to(eqc_dot, RIGHT, buff=0.2)
		eqcdot= VGroup(eqc_dot,eqc_dotlab)

		

		#end of equilibrium dots lines arrows and ics

		#sub and income effect

		subpoint1= ax.c2p(3,17)
		subpoint2= ax.c2p(1.60,17)
		subline1= ax.get_vertical_line(subpoint1)
		subline2= ax.get_vertical_line(subpoint2)
		subline= VGroup(subline1, subline2)

		subbrace= BraceBetweenPoints(subpoint1, subpoint2)
		subbrace_label= Tex("Substitution Effect", font_size=25).next_to(subbrace, UP, 
			buff=0.05).shift(RIGHT*1)
		subbrace_group= VGroup(subbrace,subbrace_label)

		incpoint= ax.c2p(1.25,17)
		incline= ax.get_vertical_line(incpoint)

		incbrace= BraceBetweenPoints(subpoint2, incpoint)
		incarrow= Arrow(ax.c2p(1.40,18), ax.c2p(1.40,22))
		incbrace_label= Tex("Income Effect", font_size=25).next_to(incarrow,UP, buff=0.1).shift(RIGHT*0.4)
		incbrace_group= VGroup(incbrace, incarrow, incbrace_label)

		obarrow= Arrow(ax.c2p(3.5,0),ax.c2p(1,0)).shift(DOWN*0.6)
		obbrace= BraceBetweenPoints(incpoint, subpoint1).next_to(obarrow,DOWN, buff=0.1)
		oblabel= Tex("Observed Response:", font_size=25).next_to(obbrace,DOWN, buff=0.1)
		oblabelx= MathTex("x_{1} - x_{2}", font_size=25).next_to(oblabel, RIGHT, buff=0.1)
		obresponse= VGroup(obarrow, obbrace, oblabel, oblabelx)

		compbrace= BraceBetweenPoints(ax.c2p(0,20.5), ax.c2p(0,12))
		compbracelab1= Tex("Compensating",font_size=30).next_to(compbrace,LEFT, buff=0.1)
		compbracelab2= Tex("Variation",font_size=30).next_to(compbracelab1,DOWN, buff=0.1)
		compvar= VGroup(compbrace, compbracelab1, compbracelab2)

		p1= ax.c2p(3,6)
		horline1= ax.get_horizontal_line(p1)

		p2= ax.c2p(1.25,4.5)
		horline2= ax.get_horizontal_line(p2)

		horlines= VGroup(horline1, horline2)
		
		#end of sub and income effect

		#animation

		self.add(ax)
		self.play(Create(bud1))
		self.wait(1)
		self.play(Create(ic1),Create(eq1dot))
		self.wait(1.5)

		self.add(budget2)
		self.play(b2xint.animate.set_value(2),b2slope.animate.set_value(6))
		self.play(Create(budget2_label))
		self.wait(1.5)

		self.play(Create(ic2), Create(eq2dot))
		self.wait(1.5)

		self.add(bccurve)
		self.play(Wiggle(bccurve))
		self.play(bcyint.animate.set_value(20.5), bcxint.animate.set_value(3.416),run_time=3.5)
		self.play(Create(bccurve_label))
		self.play(Create(eqcdot))
		self.wait(1.5)

		self.play(Create(subline))
		self.wait(1.5)
		self.play(Create(subbrace_group))
		self.wait(1.5)

		self.play(Create(incline))
		self.wait(1.5)
		self.play(Create(incbrace_group))
		self.wait(1.5)

		self.play(Create(compvar))
		self.wait(1.5)

		self.play(Create(ax2),Create(horlines))
		self.wait(1.5)
		self.play(Create(obresponse))
		self.wait(2)

		


		




		
