from textgenrnn import textgenrnn

textgen_2 = textgenrnn('textgenrnn_weights.hdf5')
textgen_2.generate(30, temperature=1.0)