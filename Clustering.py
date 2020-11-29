import numpy as np
import pandas as pd
from sklearn import preprocessing
from collections import defaultdict
from collections import defaultdict
import sys
import pylab as plt
import copy

plt.ion()

np.random.seed(200)
k = 3
centroids = {
    i+1: [np.random.uniform(low=0, high=0.7), np.random.uniform(low=0, high=0.7)]
    for i in range(k)
}

def assignment(df, centroids):
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['Rape'] - centroids[i][0]) ** 2
                + (df['Kidnapping and Abduction'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df


old_centroids = copy.deepcopy(centroids)
def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['Rape'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['Kidnapping and Abduction'])
    return k


#Clusters 4 rural places in tier 3, unlike 2011
#final cluster: [0.8664850564285879, 0.5157956362627378], 2: [0.04362950255514935, 0.032280685980397475], 3: [0.26458400959491757, 0.2111796753773657]}

df = pd.read_csv("processed_Clustering.csv")
df = df.loc[df['Year'] == 2011]

cols_to_norm = ['Rape', 'Kidnapping and Abduction']
df[cols_to_norm] = df[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
df = df.iloc[:, 1:]
#print(df)

colmap = {1: 'r', 2: 'g', 3: 'b'}
df = assignment(df, centroids)
old_centroids = copy.deepcopy(centroids)
centroids = update(centroids)
df = assignment(df, centroids)
while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assignment(df, centroids)
    if closest_centroids.equals(df['closest']):
        break
print(df)
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['Rape'], df['Kidnapping and Abduction'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
print(centroids)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()

x = [0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8]
x = np.array(x)
y = np.array(-0.647005*x + 0.1650021)
plt.plot(x, y)

y = np.array(-1.13005*x + 0.870034)
plt.plot(x, y)
plt.savefig('prediction.png')

