import tensorflow as tf

def load_graph(frozen_graph_filename):
    # We load the protobuf file from the disk and parse it to retrieve the 
    # unserialized graph_def
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Then, we import the graph_def into a new Graph and returns it 
    with tf.Graph().as_default() as graph:
        # The name var will prefix every op/nodes in your graph
        # Since we load everything in a new graph, this is not needed
        tf.import_graph_def(graph_def, name="prefix")
    return graph

if __name__=='__main__':
    graph = load_graph('./Model/frozen_model.pb')
    for op in graph.get_operations():
        print(op.name)
    x = graph.get_tensor_by_name('prefix/v1:0')
    y = graph.get_tensor_by_name('prefix/v2:0')
    a = tf.add(x,y)
    with tf.Session(graph=graph) as sess :
        print(sess.run(a))