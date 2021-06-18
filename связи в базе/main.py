import pandas as pd


if __name__ in '__main__':
    print('1')
    columns = ['det', 'ind', 'count']
    data = [['1', '1', 15], ['2', '3', 21], ['1', '1', 52], ['2', '2', 33]]
    df = pd.DataFrame(data=data, columns=columns)
    df = df[(df['count'] > 0) & (df['count'] < 1000)]
    df = df.groupby('det', 'ind').size().reset_index('count')
    print(df)

