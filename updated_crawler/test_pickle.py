import pickle

config_dictionary = {'remote_hostname': 'google.com', 'remote_port': 80}

# Step 2
with open('config.dictionary', 'wb') as config_dictionary_file:
    # Step 3
    pickle.dump(config_dictionary, config_dictionary_file)

with open('config.dictionary', 'rb') as config_dictionary_file:
    # Step 3
    config_dictionary = pickle.load(config_dictionary_file)

    # After config_dictionary is read from file
    print(config_dictionary)