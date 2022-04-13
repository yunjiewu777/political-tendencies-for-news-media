import tensorflow as tf

model = tf.keras.Model(...)
checkpoint = tf.train.Checkpoint(model)

# Save a checkpoint to /tmp/training_checkpoints-{save_counter}. Every time
# checkpoint.save is called, the save counter is increased.
save_path = checkpoint.save('/checkpoints')

# Restore the checkpointed values to the `model` object.
checkpoint.restore(save_path)