import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import seaborn as sns
import numpy as np
import squarify 

def area_chart(title, max_date, max_value, df, ylabel="Count of %-change in covid cases"):
    # Plot
    plt.figure(figsize=(16,10), dpi= 80)
    plt.fill_between(df["date"], df["PercentageChange-cases_Sum"], 0, where=df["PercentageChange-cases_Sum"] >= 0, facecolor='green', interpolate=True, alpha=0.7)
    plt.fill_between(df["date"], df["PercentageChange-cases_Sum"], 0, where=df["PercentageChange-cases_Sum"] <= 0, facecolor='red', interpolate=True, alpha=0.7)

    # Annotate
    plt.annotate('Peak day was\n' + max_date, xy=(94.0, 21.0), xytext=(88.0, 28),
                bbox=dict(boxstyle='square', fc='firebrick'),
                arrowprops=dict(facecolor='steelblue', shrink=0.05), fontsize=15, color='white')

    plt.xticks(df['date'].values[-1:])
    plt.title(title, fontsize=22)
    plt.ylabel(ylabel)
    plt.grid(alpha=0.5)
    plt.show()
    
def scatter_plot(plt_title, x_axis, y_axis, color):
    plt.scatter(x_axis, y_axis, c=color)
    plt.title(plt_title, fontsize=14)
    plt.rcParams["figure.figsize"] = (20,3)
    plt.show()
    
def diverging_text_visuals(title, df, column):
    df['colors'] = ['red' if x < 0 else 'green' for x in df[column]]
    df.sort_values(column, inplace=True)
    df.reset_index(inplace=True)

    # Draw plot
    plt.figure(figsize=(14,14), dpi= 80)
    plt.hlines(y=df.index, xmin=0, xmax=df[column])
    for x, y, tex in zip(df[column], df.index, df[column]):
        t = plt.text(x, y, round(tex, 2), horizontalalignment='right' if x < 0 else 'left', 
                    verticalalignment='center', fontdict={'color':'red' if x < 0 else 'green', 'size':14})

    # Decorations    
    plt.yticks(df.index, df.areaName, fontsize=12)
    plt.title(title, fontdict={'size':20})
    plt.grid(linestyle='--', alpha=0.5)
    plt.show()
    
def grouped_bar_chart_visual( title, data, x, ylabel, legend):
    fig, ax = plt.subplots(nrows=1, figsize=(10, 10), sharex=True)
    ax.set(title=title)
    data.plot.bar( x=x, stacked=False, ax=ax)
    for label in ax.get_xticklabels():
        label.set_rotation(0)

    ax.set(ylabel=ylabel)
    ax.legend(legend)
    
    plt.show()
    
def tree_map_visual(chart_title, data_size, labels ):
    plt.close()
    colors=['#264653','#fca311','#023e8a','#ffd166','#f07167','#590d22','#81b29a', '#780000', '#ffecd1', '#3c096c', '#fff3b0']
    fig = plt.gcf()
    fig.set_size_inches(13, 8)
    sns.set_style(style="whitegrid")
    squarify.plot(sizes=data_size, label=labels, alpha=0.6,color=colors).set(title=chart_title)
    plt.title(chart_title, fontsize=16, fontweight="bold")
    plt.axis('off')
    
    plt.show()

    
def donut_chart(title, values, labels):
    plt.close()
    colors = ['#00b4d8','#ffd166','#f07167','#264653','#81b29a']
    plt.pie(values, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.85)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')        #draw circle
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title(title, fontsize=16, fontweight="bold")
    plt.show()
    
def simple_bar_chart(title, value, label):
    x_pos = np.arange(len(label))

    # Create bars with different colors
    plt.bar(x_pos, value, color=['#f07167','#264653','#81b29a'])

    # Create names on the x-axis
    plt.xticks(x_pos, label)
    plt.title(title, fontsize=16, fontweight="bold")
    # Show graph
    plt.show()

def population_pyramid(title, df, label_1, label_2, city, x_label, y_label):
    # Draw Plot
    plt.figure(figsize=(13,10), dpi= 80)

    # for c, group in zip(colors, df[group_col].unique()):
    sns.barplot(x=label_1, y=city, data=df, order=city, color='#ffd166'
                # , label=group
            )
    sns.barplot(x=label_2, y=city, data=df, order=city, color='#81b29a'
                # , label=group
            )

    # Decorations    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.yticks(fontsize=12)
    plt.title(title, fontsize=16, fontweight="bold")
    plt.legend()
    plt.show()
    
def pie_chart(title, data, categories, explode, label_title):
    # Draw Plot
    fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi= 80)

    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}% ({:d} )".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(data, 
                                    autopct=lambda pct: func(pct, data),
                                    textprops=dict(color="w"), 
                                    colors=plt.cm.Dark2.colors,
                                    startangle=140,
                                    explode=explode)

    # Decoration
    ax.legend(wedges, categories, title=label_title, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=10, weight=700)
    ax.set_title(title)
    plt.show()