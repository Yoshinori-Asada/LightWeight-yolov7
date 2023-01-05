import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model('saved_model_dir')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]
tflite_quant_model = converter.convert()
with open('float16_quantization.tflite', 'wb') as w:
    w.write(tflite_quant_model)