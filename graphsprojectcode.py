import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Wiki-Vote.txt', sep='\t', skiprows=4, names=['fromN', 'toN'])
df = df.iloc[:10000, :]
df.to_csv('Wiki-Vote.csv')

G = nx.Graph()
G.add_edges_from(zip(df.fromN, df.toN))
rich_club=nx.rich_club_coefficient(G)
degrees=list(rich_club.keys())
values=list(rich_club.values())
print("rich-club values:")
print(values)

degree_assortativity=nx.degree_assortativity_coefficient(G)
print("degree assortativity:")
print(degree_assortativity)