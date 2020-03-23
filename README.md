# Brain-Model-Test
A very simplified, layered model of a human brain using Python, Tensorflow 2, and Keras.

## What is this?
This, as the description says, is an attempt to model brain function pathways in Python. It is much slower than direct data processing, however, and is not recommended to be used until a tagged release.

## A visualization of the target.
![Brain Model Flowchart-esque Diagram](https://i.ibb.co/rpwVFV3/Python-Brain-Diagram.png)

### Explanation
The process initiates with a data input which is pushed through multiple layers until either it hits a related existing memory point in a database (SQLServer or PostgreSQL) or needs a generated data point which is then forwarded out to a motor control/action layer. The Accepting Processing Layer serves similar to the human thalamus in terms routing information between the cerebrum and spinal cord and processes the incoming data.

### Libraries Referenced/Used
* Tensorflow 2 GPU
* Numpy
* pyodbc (SQLServer) or psycopg2 (PostgreSQL)
* OpenCV 2
 
