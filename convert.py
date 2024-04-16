import tensorflow as tf

# 加载 .h5 格式的模型
model = tf.keras.models.load_model("model.h5")

# 保存为 .keras 格式
model.save("model2.keras")
