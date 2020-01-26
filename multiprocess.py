import pandas as pd
import time
import itertools
from multiprocessing import Pool
import multiprocessing as multi


def create_df(tuple_input):
    print(tuple_input)
    ret_name = tuple_input[0]
    row_idx = tuple_input[1]
    df_input = pd.read_csv("data/" + ret_name + ".csv", index_col=0)
    time.sleep(10)
    df_new = df_input.iloc[: row_idx]
    df_new.to_csv("data/" + ret_name + str(row_idx) + "_new.csv")
    return


if __name__ == "__main__":
    t1 = time.time()
    ret_list = ["top_btm", "top_mkt", "mkt_btm"]
    row_idx_list = [3, 4]
    p = Pool(multi.cpu_count())
    p.map(create_df, [*itertools.product(ret_list, row_idx_list)])
    t2 = time.time()
    print(t2 - t1)

    # t1 = time.time()
    # for ret_type in ["top_btm", "top_mkt", "mkt_btm"]:
    #     create_df(ret_type)
    # t2 = time.time()
    # print(t2 - t1)
