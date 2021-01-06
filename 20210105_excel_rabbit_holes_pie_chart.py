#! /usr/bin/env python3
"""
2021-01-05
Excel rabbit holes pie chart
"""

from matplotlib import pyplot as plt


def main():
    labels = [
        'pivot table', 'sparklines', 'vlookup', '17 sheets',
        'pasting as values', 'not using external data',
        '542 764 rows x\n20 columns'
    ]
    sizes = [5, 5, 10, 10, 10, 10, 50]
    colours = [
        '#bbbbbb', '#0077bb', '#33bbee', '#009988', '#ee7733', '#ee3377',
        '#cc3311'
    ]
    figsize = (8, 6)
    plt.xkcd()
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.pie(
        x=sizes,
        labels=labels,
        colors=colours,
        autopct='%1.f %%',
        startangle=90
    )
    ax.set_title(label='excel rabbit holes')
    ax.text(
        x=2,
        y=-1.25,
        s='gilles pilon 2021-01-05',
        horizontalalignment='right'
    )
    fig.savefig(
        fname='20210105_excel_rabbit_holes_pie_chart.svg',
        format='svg'
    )


if __name__ == '__main__':
    main()
