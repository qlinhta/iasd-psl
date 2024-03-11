import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import community as community_louvain
import warnings

warnings.filterwarnings("ignore")

plt.style.use('default')
plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif')
plt.rc('font', size=14)
plt.rc('axes', titlesize=14)
plt.rc('axes', labelsize=14)
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.rc('legend', fontsize=14)
plt.rc('lines', markersize=10)


def label_propagation(G):
    labels = {node: i for i, node in enumerate(G.nodes())}
    while True:
        new_labels = labels.copy()
        nodes = list(G.nodes())
        np.random.shuffle(nodes)
        for node in nodes:
            neighbors = list(G.neighbors(node))
            if len(neighbors) == 0:
                continue
            neighbor_labels = [labels[neighbor] for neighbor in neighbors]
            new_labels[node] = max(set(neighbor_labels), key=neighbor_labels.count)
        if new_labels == labels:
            break
        labels = new_labels
    return labels


def modularity(G, labels):
    m = G.number_of_edges()
    A = nx.adjacency_matrix(G).toarray()
    Q = 0
    for i in range(len(G.nodes())):
        for j in range(len(G.nodes())):
            if labels[i] == labels[j]:
                Q += A[i, j] - G.degree(i) * G.degree(j) / (2 * m)
    return Q / (2 * m)


def louvain(G):
    partition = community_louvain.best_partition(G)
    return partition


if __name__ == '__main__':
    G = nx.karate_club_graph()
    labels = label_propagation(G)
    print(labels)

    print(f'Modularity: {modularity(G, labels)}')

    partition = louvain(G)
    print(partition)
    print(f'Modularity: {modularity(G, list(partition.values()))}')

    pos = nx.spring_layout(G)
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    nx.draw(G, with_labels=True, pos=pos, node_color=list(labels.values()), edge_color='grey', width=0.5, ax=ax[0],
            cmap=plt.cm.tab20, font_size=10)
    nx.draw(G, with_labels=True, pos=pos, node_color=list(partition.values()), edge_color='grey', width=0.5, ax=ax[1],
            cmap=plt.cm.tab20, font_size=10)
    ax[0].set_title('Label Propagation')
    ax[1].set_title('Louvain')

    plt.show()
