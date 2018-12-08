import os



def get_node(tree, start_idx):
    num_child_nodes = tree[start_idx]
    num_metadata_entries = tree[start_idx + 1]

    metadata = []
    own_metadata = []
    nodes = []

    idx = start_idx + 2
    for i in range(num_child_nodes):
        idx, node_metadata, node_value = get_node(tree, idx)
        metadata.extend(node_metadata)
        nodes.append((idx, node_metadata, node_value))
    for i in range(num_metadata_entries):
        own_metadata.append(tree[idx + i])
    metadata.extend(own_metadata)
    if num_child_nodes == 0:
        value = sum(metadata)
    else:
        value = 0
        for i in own_metadata:
            if i - 1 < len(nodes):
                value += nodes[i-1][2]
    
    return idx + num_metadata_entries, metadata, value

dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir, 'input')) as f:
    input_data = f.read()

tree = input_data.strip().split(' ')
tree = [int(i) for i in tree]

_, root_metadata, root_value = get_node(tree, 0)

print("Part 1: " + str(sum(root_metadata)))

print("Part 2: " + str(root_value))
