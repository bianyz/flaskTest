import polars
import flask

import flasktest

if __name__ == '__main__':
    df = polars.read_parquet("data_test.parquet")
    print(df.head)
    flasktest.app.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
