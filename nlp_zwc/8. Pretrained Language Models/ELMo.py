import torch
import torch.nn as nn
from allennlp.modules.elmo import Elmo, batch_to_ids

# Load pre-trained ELMo model
options_file = 'https://allennlp.s3.amazonaws.com/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_options.json'
weight_file = 'https://allennlp.s3.amazonaws.com/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5'
elmo = Elmo(options_file, weight_file, num_output_representations=1, dropout=0)

# Define your own PyTorch model
class ELMoModel(nn.Module):
    def __init__(self, elmo, num_classes):
        super(ELMoModel, self).__init__()
        self.elmo = elmo
        self.fc = nn.Linear(1024, num_classes)  # Adjust input size if needed
        
    def forward(self, inputs):
        character_ids = batch_to_ids(inputs).cuda()  # Convert input sentences to character ids
        embeddings = self.elmo(character_ids)['elmo_representations'][0]  # Get ELMo embeddings
        outputs = self.fc(embeddings)
        return outputs

# Example usage
input_sentences = ["This is sentence 1.", "This is sentence 2."]
num_classes = 2  # Number of classes for binary classification

model = ELMoModel(elmo, num_classes).cuda()
outputs = model(input_sentences)
print(outputs)