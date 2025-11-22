from os import WCONTINUED

import pandas as pd
import numpy as np
from icecream import ic as ic
import matplotlib.pyplot as plt



data = pd.read_csv('cumulative.csv')
head = data.head()
df = pd.DataFrame(data)

id_name = {}
x_set = []
y_set = []
columns = df.columns
ic(columns)

for key, value in df.iterrows():
    id_name[df.loc[key, "KEPID"]] = df.loc[key, "KEPOI_NAME"]

for key, value in id_name.items():
    x_set.append(key)
    y_set.append(value)

score = []

for value in df["KOI_SCORE"]:
    if value == "KOI_SCORE":
        continue
    else:
        score.append(value)

score_analysis = []

for x in score:
    x = float(x)
    score_analysis.append(x)


max_prad = []

for value in df["KOI_PRAD"]:
    if value == "KOI_PRAD":
        continue
    else:
        max_prad.append(value)

prad = []

for x in max_prad:
    x = float(x)
    prad.append(x)


# max_prod_min = np.min(prad)
max_prod_max = np.max(prad)
max_prod_mean = np.mean(prad)
max_prod_std = np.std(prad)

# score_analysis_min = np.min(score_analysis)
score_analysis_max = np.max(score_analysis)
score_analysis_mean = np.mean(score_analysis)
score_analysis_std = np.std(score_analysis)

# # ic(score_analysis_min)
# ic(score_analysis_max)
# ic(score_analysis_mean)
# ic(score_analysis_std)
#
# ic(max_prod_mean)
# ic(max_prod_min)
# ic(max_prod_mean)
# ic(max_prod_std)
# ic(max_prod_max)


x_set = set(x_set)
y_set = set(y_set)

conf = []
cand = []
false_p = []

for key, disp in df["KOI_PDISPOSITION"].items():
    conf.append(disp)

for x in conf:
    if x == "CANDIDATE":
        cand.append(x)
    elif x == "FALSE POSITIVE":
        false_p.append(x)

cand_avg = len(cand)
false_p_avg = len(false_p)

c = -1

for i in range(26):
    key = {}
    ic(columns)
    for k, value in enumerate(columns):
        key[k] = value

    for u, v in enumerate(columns):


        set_x = []
        set_y = []
        floats_x = []
        floats_y = []

        if v in ["KEP_ID", "KEPOI_NAME", "KEPLER_NAME", "KOI_DISPOSITION", "KOI_PDISPOSITION"]:
            continue
        else:
            length = len(columns)

            for value in range(length):
                c = c + 1

                curr_index = df.columns.get_loc(v)
                ic(curr_index)
                current = df[v].iloc[curr_index]


                if v == v:
                    v = columns[curr_index + 1]
                set_x = [x for x in df[v]]

                index_ = df.columns.get_loc(v)
                ic(index_)
                index_ = index_ + 1
                # if index_ ==
                set_y = [x for x in df[v]]
                ic(set_x[0:10], set_y[0:10])

                for x in set_x:
                    if x == v:
                        continue
                    try:
                        x = float(x)
                        floats_x.append(x)

                    except ValueError as e:
                        pass

                for x in set_y:
                    if x == v:
                        continue
                    try:
                        x = float(x)
                        floats_y.append(x)

                    except ValueError as e:
                        pass

                plt.set_cmap(plt.get_cmap("Pastel1"))
                labels = []
                ic(floats_x[0:10], floats_y[0:10])
                plt.scatter(floats_x, floats_y)
                file_name = "scatter_"
                plt.savefig(f"{file_name}" + str(c + 1) + ".png")
                plt.close()

                # except ValueError as e:
                #     continue
