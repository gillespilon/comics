#! /usr/bin/env python3
"""
2021-01-04
Data science pie chart
"""

from matplotlib import pyplot as plt


def main():
    labels = ['cleaning data', 'complaining about\ncleaning data']
    sizes = [90, 10]
    colours = ['#0077bb', '#cc3311']
    figsize = (8, 6)
    plt.xkcd()
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.pie(
        x=sizes,
        labels=labels,
        colors=colours,
        autopct='%1.f %%'
    )
    ax.set_title(label='data science')
    ax.text(
        x=2,
        y=-1.25,
        s='gilles pilon 2021-01-04',
        horizontalalignment='right'
    )
    fig.savefig(
        fname='20210104_data_science_pie_chart.svg',
        format='svg'
    )


if __name__ == '__main__':
    main()
