import tensorflow as tf

sess = tf.Session()

filename_queue = tf.train.string_input_producer(
    tf.train.match_filenames_once("./*.csv"),
    shuffle=True)
reader = tf.TextLineReader(skip_header_lines=1)
key, value = reader.read(filename_queue)
record_defaults = [[0.], [0.], [0.], [0.], [""]]
col1, col2, col3, col4, col5 = tf.decode_csv(value,
                                             record_defaults=record_defaults)  # Convert CSV records to tensors. Each
features = tf.stack([col1, col2, col3, col4])
tf.global_variables_initializer().run(session=sess)
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(coord=coord, sess=sess)
for iteration in range(0, 5):
    example = sess.run([features])
    print(example)
coord.request_stop()
coord.join(threads)
