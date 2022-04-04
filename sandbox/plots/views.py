import plotly.graph_objects as go
from django.shortcuts import render
from plots.models import Pessoa
from plotly.offline import plot




def demo_plot_view(request):
    """ 
    View demonstrating how to display a graph object
    on a web page with Plotly. 
    """
    
    # Generating some data for plots.
    x = [i for i in range(-10, 11)]
    y1 = [3*i for i in x]
    y2 = [i**2 for i in x]
    y3 = [10*abs(i) for i in x]

    # List of graph objects for figure.
    # Each object will contain on series of data.
    graphs = []

    # Adding linear plot of y1 vs. x.
    graphs.append(
        go.Scatter(x=x, y=y1, mode='lines', name='Line y1')
    )

    # Adding scatter plot of y2 vs. x. 
    # Size of markers defined by y2 value.
    graphs.append(
        go.Scatter(x=x, y=y2, mode='markers', opacity=0.8, 
                   marker_size=y2, name='Scatter y2')
    )

    # Adding bar plot of y3 vs x.
    graphs.append(
        go.Bar(x=x, y=y3, name='Bar y3')
    )

    # Setting layout of the figure.
    layout = {
        'title': 'Title of the figure',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 420,
        'width': 560,
    }

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')

    return render(request, 'demo-plot.html', 
                  context={'plot_div': plot_div})
    
def plot_from_models(request):
    #pegando os dados
    nomes = list(Pessoa.objects.values_list("nome", flat=True))
    altura = list(Pessoa.objects.values_list("altura", flat=True))
    peso = list(Pessoa.objects.values_list("peso", flat=True))
    #obtendo a lista de objetos graphs
    graphs = []

    # Gerando os gráficos
    graphs.append(
        go.Bar(x=altura, y=peso, name='Altura por Peso')
    )
    graphs.append(
        go.Scatter(x=altura, y=peso, name='Altura por Peso')
    )
    # Definindo o layout do gráfico.
    layout = {
        'title': 'Gráficos da models Pessoa',
        'xaxis_title': 'Altura',
        'yaxis_title': 'Peso',
        'height': 420,
        'width': 560,
    }
    
    # O objeto que será renderizado no html
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')
    
    return render(request, 'pessoa.html', context={"plot_div": plot_div})

def pie_chart_from_models(request):
    nomes = list(Pessoa.objects.values_list("nome", flat=True))
    peso = list(Pessoa.objects.values_list("peso", flat=True))
    graphs = []
    
    graphs.append(
        go.Pie(labels=nomes, values=peso)
    )
    # Definindo o layout do gráfico.
    layout = {
        'title': 'Gráficos da models Pessoa',
        'xaxis_title': 'Peso',
        'yaxis_title': 'Peso',
        'height': 420,
        'width': 560,
    }
    
    # O objeto que será renderizado no html
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')
    return render(request, 'pessoa.html', context={"plot_div": plot_div})
    
