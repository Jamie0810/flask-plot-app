from flask import Flask, render_template, Blueprint
import matplotlib.pyplot as plt
import numpy as np
from plotsGenerator import simple_plot, line_Plot
import io
import base64


plots = Blueprint('plots', __name__)

@plots.route('/test', methods=['GET']) 
def test():
    return "test"

@plots.route('/simplePlots')
def simplePlot():
	simple_plot_url = simplePlot()
	linePlot_url = linePlot()
	return render_template('plots.html', simpleGraph=simple_plot_url, linePlot=linePlot_url)

def simplePlot():
	x1 = [0, 1, 2, 3, 4]
	y1 = [10, 30, 40, 5, 50]
	simple_plot_url = simple_plot(x1,y1);
	return simple_plot_url
	
def linePlot():
	x = np.linspace(-1, 1, 50)
	y = 2*x + 1
	linePlot_url = line_Plot(x, y);
	return linePlot_url





