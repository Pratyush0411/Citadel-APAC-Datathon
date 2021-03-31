import gtab
import pandas as pd
import multiprocessing as mp
from functools import partial

def processInput(df, t, i):
    # print(i)
    player_name = df.iloc[i]['player_name']
    try:
        res = t.new_query(player_name)
        return res['max_ratio'].mean()
    except Exception as e:
        return 0


def main():
    t = gtab.GTAB()
    t.set_active_gtab("google_anchorbank_geo=_timeframe=2019-01-01 2020-08-01.tsv")

    df = pd.read_csv('player.csv')

    inputs = range(df.shape[0])
    #  removing processes argument makes the code run on all available cores
    pool = mp.Pool(processes=2)
    func = partial(processInput, df, t)
    pops = pool.map(func, inputs)


    df['popularity_trends'] = pops
    df.to_csv('player_with_pop.csv', index=False)

if __name__ == "__main__":
    main()