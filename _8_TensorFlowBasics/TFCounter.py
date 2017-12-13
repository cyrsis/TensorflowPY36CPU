import tensorflow as  tf

value = tf.Variable(0, name="value")
one = tf.constant(1)
new_value = tf.add(value,one)
update_value =tf.assign(value,new_value)


sess = tf.Session()

sess.run(tf.global_variables_initializer())

print("init Value of value "+str(sess.run(value)))

for _ in range(100) :
    sess.run(update_value)
    print("Value in the loop "+ str(sess.run(value)))


sess.close()