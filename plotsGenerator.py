import matplotlib.pyplot as plt
import io
import base64
 
def simple_plot(x, y):
    img = io.BytesIO()
    plt.plot(x, y)
    plt.savefig(img, format='png')
    # img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

def line_Plot(x, y):
    plt.figure()
    img = io.BytesIO()
    plt.plot(x, y)
    plt.savefig(img, format='png')
    img.seek(0)
    linePlot = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(linePlot)




