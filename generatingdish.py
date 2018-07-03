from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.train_from_file('input.txt', num_epochs=1)
textgen.generate()
textgen.save('weights.hdf5')