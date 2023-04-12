from collections import defaultdict
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers import Dense
import numpy as np

from collections import deque
from random import sample

x_data = np.linspace(0, 15, 16)

class ReplayBuffer:
    """Replay buffer.

    Stores and samples gameplay experiences
    """

    def __init__(self, max_size: int = 2000) -> None:
        self.buffer = deque(maxlen=max_size)

    def store(self, experience) -> None:
        """Store a gameplay experience in the buffer.

        Args:
            experience: gameplay experience to store

        Returns:
            None
        """
        self.buffer.append(experience)

    def sample(self, batch_size: int = 32) -> list:
        """Samples a list of gameplay experiences of (max) size batch_size.

        Args:
            batch_size: maximum size of the batch to sample

        Returns:
            Sampled batch of gameplay experiences
        """
        batch_size = min(batch_size, len(self.buffer))
        return sample(self.buffer, batch_size)

class Agent:
    def __init__(
        self,
        env,
        learning_rate=0.1,
        initial_epsilon=1.0,
        epsilon_decay=10**(-100),
        final_epsilon=0.1,
        discount_factor=0.95,
    ):
        """Initialize a Reinforcement Learning agent with an empty dictionary
        of state-action values (model), a learning rate and an epsilon.

        Args:
            learning_rate: The learning rate
            initial_epsilon: The initial epsilon value
            epsilon_decay: The decay for epsilon
            final_epsilon: The final epsilon value
            discount_factor: The discount factor for computing the Q-value
        """
        
        normalizer = keras.layers.Normalization(input_shape=[1,], axis=None)  
        normalizer.adapt(np.array(x_data))
        self.model = keras.Sequential([  
	        normalizer,  
	        Dense(64, activation='relu'),  
	        Dense(64, activation='relu'),  
	        Dense(4)  
        ])
        self.model.compile(  
            optimizer=tf.optimizers.Adam(learning_rate=0.001),  
	          loss='mse'  
        )

        self.buffer = ReplayBuffer()

        self.env = env

        self.lr = learning_rate
        self.gamma = discount_factor

        self.epsilon = initial_epsilon
        self.epsilon_decay = epsilon_decay
        self.final_epsilon = final_epsilon

        self.training_error = []

    def get_action(self, obs: int) -> int:

        if np.random.random() < self.epsilon:
            return self.env.action_space.sample()

        else:
            state = obs
            qvals = self.model( tf.convert_to_tensor( s ) )
            return int(np.argmax( qvals ))

    def update(
        self,
        obs: int,
        action: int,
        reward: float,
        terminated: bool,
        next_obs: int,
    ):

        self.buffer.store( (obs, action, reward, next_obs, terminated) )

        if len(self.buffer.buffer) > 255:

           batch = self.buffer.sample(256)

           # Model predictions 
           batch_states = [ x[0] for x in batch]
           states = tf.convert_to_tensor(batch_states, dtype=tf.float32)
           qvalues = self.model.predict(states)

           # We want to calculate the error over the q-values, so we make a copy to use as a target
           qtargets = np.copy(qvalues)

           # We then repeat for all utilities of the next states in the batch:
           batch_ns = [ x[3] for x in batch]
           newstates = tf.convert_to_tensor(batch_ns, dtype=tf.float32)
           utilities = self.model.predict(newstates)
           utilities = [np.amax(utility) for utility in utilities]

           for i in range(len(batch)):
               experience = batch[i]
               target = experience[2]
               if not experience[4]:
                   # Error is similar to q-learning
                   target = target + self.gamma * utilities[i]

               qtargets[i][experience[1]] = target
           qtargets = tf.convert_to_tensor(qtargets, dtype=tf.float32)
           training_history = self.model.fit(x=states, y=qtargets, verbose=0)
           loss = training_history.history['loss']
           return loss

        pass

    def decay_epsilon(self):
        self.epsilon = max(self.final_epsilon, self.epsilon - self.epsilon_decay)
