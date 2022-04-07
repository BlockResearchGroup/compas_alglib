import compas
from compas.datastructures import Network
from compas_alglib.matrices import connectivity_matrix

network = Network.from_obj(compas.get_data("lines.obj"))

key_index = network.key_index()
edges = [(key_index[u], key_index[v]) for u, v in network.edges()]

n = network.number_of_vertices()

C = connectivity_matrix(edges, n)

print(C)
