# Brain-Model-Test
A very simplified, layered model of a human brain using Python, Tensorflow 2, and Keras.

## What is this?
This, as the description says, is an attempt to model brain function pathways in Python. It is much slower than direct data processing, however, and is not recommended to be used until a tagged release.

## A visualization of the target.
Sensor Input Layer                             Motor Layer
                  \                           /
                   \                         /
                    \                       /
                     Accepting Process Layer
                    /                       
                   /                         
                  /                           
      Memory State                             
     /            \
    /              \
   /                \
 DB                  True Processor
                    /              \
                   /                \  
                  /                  \
 Automatic Actions                    Predefined-Motion Controls

### Explanation
Each of the diagonal lines refers to a connection between the layers/structures. For example, the "True Processor" layer has connections to two structures: "Automatic Actions" and "Predefined-Motion Controls", the latter can be empty as this is being designed to be able to be implemented into robotics. "Memory State" is a router for, currently, a local SQLServer database (though at the moment of writing this code, it was a PostgreSQL state) which is being used to store "memories" so the the build will no longer need to reprocess if the input data is similar enough to an existing data point.

The "Accepting Processing Layer" mimics the role of the thalamus in a human brain which is typically seen as a routing network between the cerebrum and the inner brain. In both life and this project, inputs must be converted to a recognizable type of information in order to for a reaction to be generated and executed.

### Libraries Referenced/Used
..* Tensorflow 2 GPU
..* Numpy
..* pyodbc (SQLServer) or psycopg2 (PostgreSQL)
..* OpenCV 2
 
