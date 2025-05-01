import tensorflow as tf

class build:
    @staticmethod
    def build_it():
        model = tf.keras.Sequential([
            tf.keras.Input(shape=(28, 28, 1)),  # Input layer explícita
            tf.keras.layers.Conv2D(16, (5, 5), activation='relu', input_shape=(28, 28, 1)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(32, (5, 5), activation='relu'),
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        return model
