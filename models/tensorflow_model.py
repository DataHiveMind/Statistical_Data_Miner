import tensorflow as tf

def build_tensorflow_model(input_shape):
    """
    Builds a basic TensorFlow model.
    
    Parameters:
    - input_shape (tuple): Shape of the input data.
    
    Returns:
    - model: Compiled TensorFlow model.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=input_shape),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='linear')  # Output layer
    ])
    
    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss='mse',
                  metrics=['mae'])
    return model

# Example usage
if __name__ == "__main__":
    sample_model = build_tensorflow_model((10,))
    sample_model.summary()
