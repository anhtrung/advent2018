import os
from functools import reduce


def get_node(tree):
    num_child_nodes, num_metadata_entries = tree[0:2]
    data = tree[2:]

    node_values = []
    node_total_sum = 0
    for _ in range(num_child_nodes):
        data, md_sum, node_value = get_node(data)
        node_values.append(node_value)
        node_total_sum += md_sum
    metadata = (data[:num_metadata_entries])

    if num_child_nodes == 0:
        return data[num_metadata_entries:], sum(metadata), sum(metadata)
        
    value = sum([node_values[md-1] for md in metadata if md-1 < len(node_values)])
    return data[num_metadata_entries:], sum(metadata) + node_total_sum, value


dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()

tree = [int(i) for i in input_data.strip().split(' ')]

_, root_metadata, root_value = get_node(tree)

print("Part 1: " + str(root_metadata))
print("Part 2: " + str(root_value))
