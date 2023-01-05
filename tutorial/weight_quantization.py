import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model('saved_model_dir')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant_model = converter.convert()
with open('weight_quantization .tflite', 'wb') as w:
    w.write(tflite_quant_model)