import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn.utils.rnn import pad_sequence

class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(Encoder, self).__init__()
        self.hidden_dim = hidden_dim
        self.rnn = nn.LSTM(input_dim, hidden_dim, bidirectional=True)

    def forward(self, inputs):
        outputs, (hidden, cell) = self.rnn(inputs)
        return outputs, hidden, cell

class Attention(nn.Module):
    def __init__(self, hidden_dim):
        super(Attention, self).__init__()
        self.hidden_dim = hidden_dim
        self.attn = nn.Linear(hidden_dim * 2, hidden_dim)
        self.v = nn.Parameter(torch.FloatTensor(hidden_dim))

    def forward(self, hidden, encoder_outputs):
        seq_len = encoder_outputs.shape[0]
        h = hidden.repeat(seq_len, 1, 1).transpose(0, 1)
        encoder_outputs = encoder_outputs.transpose(0, 1)
        attn_scores = torch.matmul(self.attn(torch.cat((h, encoder_outputs), dim=-1)), self.v)
        attn_weights = torch.softmax(attn_scores, dim=-1)
        context = torch.matmul(attn_weights.transpose(1, 2), encoder_outputs)
        return context

class Decoder(nn.Module):
    def __init__(self, output_dim, hidden_dim):
        super(Decoder, self).__init__()
        self.output_dim = output_dim
        self.hidden_dim = hidden_dim
        self.rnn = nn.LSTM(output_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.attention = Attention(hidden_dim)

    def forward(self, inputs, hidden, cell, encoder_outputs):
        inputs = inputs.unsqueeze(0)
        outputs, (hidden, cell) = self.rnn(inputs, (hidden, cell))
        context = self.attention(hidden[-1], encoder_outputs)
        outputs = self.fc(torch.cat((outputs.squeeze(0), context.squeeze(0)), dim=1))
        return outputs, hidden, cell

class Seq2Seq(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim):
        super(Seq2Seq, self).__init__()
        self.encoder = Encoder(input_dim, hidden_dim)
        self.decoder = Decoder(output_dim, hidden_dim)

    def forward(self, inputs, targets):
        encoder_outputs, hidden, cell = self.encoder(inputs)
        outputs = []
        for t in range(targets.shape[0]):
            output, hidden, cell = self.decoder(targets[t], hidden, cell, encoder_outputs)
            outputs.append(output)
        outputs = torch.stack(outputs, dim=0)
        return outputs

input_dim = 100  # Input vocabulary size
output_dim = 200  # Output vocabulary size
hidden_dim = 128  # Hidden layer size

model = Seq2Seq(input_dim, output_dim, hidden_dim)
print(model)