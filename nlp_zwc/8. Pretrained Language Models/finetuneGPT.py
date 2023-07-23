import torch
import torch.nn as nn
from transformers import GPT2Model, GPT2Tokenizer
from datasets import load_dataset
import os
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'

# Load pre-trained GPT model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.add_special_tokens({'pad_token': '[PAD]'})  # Add padding token

gpt = GPT2Model.from_pretrained(model_name)

# Define your own task-specific classifier
class SentimentClassifier(nn.Module):
    def __init__(self, gpt):
        super(SentimentClassifier, self).__init__()
        self.gpt = gpt
        self.fc = nn.Linear(768, 2)  # Adjust output size for binary classification
        
    def forward(self, input_ids):
        outputs = self.gpt(input_ids)['last_hidden_state']
        outputs = self.fc(outputs[:, 0, :])  # Use the representation of the first token
        return outputs

# Load 'SST-2' dataset from Hugging Face's datasets library
dataset = load_dataset("glue", "sst2")
train_dataset = dataset["train"]
test_dataset = dataset["test"]

# Tokenize input and convert it to tensors
train_data = train_dataset["sentence"]
train_labels = torch.tensor(train_dataset["label"])

test_data = test_dataset["sentence"]
test_labels = torch.tensor(test_dataset["label"])

max_length = 512  # Define the maximum sequence length

input_ids_train = []
for data in train_data:
    encoded_data = tokenizer.encode(data, truncation=True, max_length=max_length)
    input_ids_train.append(encoded_data)

input_ids_test = []
for data in test_data:
    encoded_data = tokenizer.encode(data, truncation=True, max_length=max_length)
    input_ids_test.append(encoded_data)

# Pad input tensors to the same length
input_ids_train = torch.nn.utils.rnn.pad_sequence([torch.tensor(ids) for ids in input_ids_train], batch_first=True)
input_ids_test = torch.nn.utils.rnn.pad_sequence([torch.tensor(ids) for ids in input_ids_test], batch_first=True)

# Move model and tensors to the GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SentimentClassifier(gpt).to(device)
input_ids_train = input_ids_train.to(device)
input_ids_test = input_ids_test.to(device)
train_labels = train_labels.to(device)
test_labels = test_labels.to(device)

# Define the batch size
batch_size = 32

# Create data loaders for training and testing
train_data_loader = torch.utils.data.DataLoader(
    torch.utils.data.TensorDataset(input_ids_train, train_labels),
    batch_size=batch_size,
    shuffle=True
)

test_data_loader = torch.utils.data.DataLoader(
    torch.utils.data.TensorDataset(input_ids_test, test_labels),
    batch_size=batch_size,
    shuffle=False
)

# Example usage for sentiment classification
loss_func = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loop
try:
    for epoch in range(10):
        model.train()
        for batch_input_ids, batch_labels in train_data_loader:
            batch_input_ids = batch_input_ids.to(device)
            batch_labels = batch_labels.to(device)
            
            logits_train = model(batch_input_ids)
            loss = loss_func(logits_train, batch_labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print("Epoch:", epoch, "Training Loss:", loss.item())

        # Evaluation on the test set
        model.eval()
        test_loss = 0.0
        correct = 0
        total = 0
        with torch.no_grad():
            for batch_input_ids, batch_labels in test_data_loader:
                batch_input_ids = batch_input_ids.to(device)
                batch_labels = batch_labels.to(device)
                
                logits_test = model(batch_input_ids)
                batch_loss = loss_func(logits_test, batch_labels)
                test_loss += batch_loss.item()

                _, predicted_labels = torch.max(logits_test, 1)
                correct += (predicted_labels == batch_labels).sum().item()
                total += batch_labels.size(0)

        test_loss /= len(test_data_loader)
        accuracy = correct / total
        print("Test Loss:", test_loss)
        print("Accuracy:", accuracy)

except Exception as e:
    print("Error:", str(e))