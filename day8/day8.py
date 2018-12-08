import os



def get_node(tree, start_idx):
    num_child_nodes = tree[start_idx]
    num_metadata_entries = tree[start_idx + 1]
    metadata = []
    idx = start_idx + 2
    for i in range(num_child_nodes):
        idx, node_metadata = get_node(tree, idx)
        metadata.extend(node_metadata)
    for i in range(num_metadata_entries):
        metadata.append(tree[idx + i])
    return idx + num_metadata_entries, metadata

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()

tree = input_data.strip().split(' ')
tree = [int(i) for i in tree]

i, metadata = get_node(tree, 0)

print("Part 1: " + str(sum(metadata)))