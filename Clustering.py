import pylab as plt
import copy
import numpy as numpy
import pandas as pd

numpy.random.seed(200)
k = 3

cluster_centroid = {}
for i in range(k):
    cluster_centroid[i+1] = [numpy.random.uniform(low=0, high=0.7), numpy.random.uniform(low=0, high=0.7)]
colors = {1: 'red', 2: 'green', 3: 'blue'}


def cluster_centroid_assign(df, cluster_centroid):
    for i in cluster_centroid.keys():
        df['distance from {}'.format(i)] = (numpy.sqrt((df['Rape'] - cluster_centroid[i][0]) ** 2 + (df['Kidnapping and Abduction'] - cluster_centroid[i][1]) ** 2))
    distance_from_centroid = ['distance from {}'.format(i) for i in cluster_centroid.keys()]
    df['closest_centroid'] = df.loc[:, distance_from_centroid].idxmin(axis=1)
    df['closest_centroid'] = df['closest_centroid'].map(lambda x: int(x.lstrip('distance from ')))
    df['color'] = df['closest_centroid'].map(lambda x: colors[x])
    return df

def update_cluster_centroid(k):
    for i in cluster_centroid.keys():
        cluster_centroid[i][0] = numpy.mean(df[df['closest_centroid'] == i]['Rape'])
        cluster_centroid[i][1] = numpy.mean(df[df['closest_centroid'] == i]['Kidnapping and Abduction'])
    return k

def k_means(cluster_centroid, df):
    df = cluster_centroid_assign(df, cluster_centroid)
    old_cluster_centroid = copy.deepcopy(cluster_centroid)
    cluster_centroid = update_cluster_centroid(cluster_centroid)
    df = cluster_centroid_assign(df, cluster_centroid)

    while True:
        closest_centroid_cluster_centroid = df['closest_centroid'].copy(deep=True)
        cluster_centroid = update_cluster_centroid(cluster_centroid)
        df = cluster_centroid_assign(df, cluster_centroid)
        if closest_centroid_cluster_centroid.equals(df['closest_centroid']):
            break
    return cluster_centroid, df

#Clusters 4 rural places in tier 3, unlike 2011
#final cluster: [0.8664850564285879, 0.5157956362627378], 2: [0.04362950255514935, 0.032280685980397475], 3: [0.26458400959491757, 0.2111796753773657]}

df = pd.read_csv("processed_Clustering.csv")
df = df.loc[df['Year'] == 2011]

cols_to_norm = ['Rape', 'Kidnapping and Abduction']
df[cols_to_norm] = df[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
df = df.iloc[:, 1:]

cluster_centroid, df = k_means(cluster_centroid, df)

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['Rape'], df['Kidnapping and Abduction'], color=df['color'], alpha=0.5, edgecolor='k')
for i in cluster_centroid.keys():
    plt.scatter(*cluster_centroid[i], color = colors[i])
print(cluster_centroid)

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()

x = [0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8]
x = numpy.array(x)
y = numpy.array(-0.647005*x + 0.1650021)
plt.plot(x, y)

y = numpy.array(-1.13005*x + 0.870034)
plt.plot(x, y)
