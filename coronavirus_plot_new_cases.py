import pandas as pd
import matplotlib.pyplot as plt

def main() -> None:
    '''Read Covid data and plot daily_lab-confirmed_cases'''
    fig, ax = plt.subplots()

    ax = pd.read_csv('coronavirus-cases_latest.csv', parse_dates=['Specimen date'])\
    .rename(columns=lambda x: x.replace(' ', '_'))\
    .query('Area_type == "Region"')\
    .pivot(index='Specimen_date', columns='Area_name', values='Daily_lab-confirmed_cases')\
    .plot(ax=ax, figsize=(12,6), style='.-', title='Covid-19 - UK daily lab confirmed cases')

    fig.savefig('daily_lab-confirmed_cases.png')

if __name__ == '__main__':
    main()
