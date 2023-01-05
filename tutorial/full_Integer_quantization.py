import tensorflow as tf
import numpy as np

def representative_dataset_gen():
    for image in raw_test_data:
        image = tf.image.resize(image, (640, 640))
        image = image[np.newaxis,:,:,:]
        yield [image]

raw_test_data = np.load('calibration.npy', allow_pickle=True)

# Full Integer Quantization - Input/Output=float32
converter = tf.lite.TFLiteConverter.from_saved_model('saved_model_dir')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8
converter.representative_dataset = representative_dataset_gen
tflite_quant_model = converter.convert()
with open('full_integer_quantization.tflite', 'wb') as w:
    w.write(tflite_quant_model)