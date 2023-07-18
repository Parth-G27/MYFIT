
# Text generation code is here 

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

def generate_text(mean, median, std_dev, num_sentences=5):
    # Load pre-trained GPT-2 model and tokenizer
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # Set seed for reproducibility
    torch.manual_seed(42)

    # Generate text based on the provided statistics
    generated_text = []
    for _ in range(num_sentences):
        # Create an input string using the given statistics
        input_text = f"The mean is {mean:.2f}, the median is {median:.2f}, and the standard deviation is {std_dev:.2f}."

        # Tokenize the input text
        input_ids = tokenizer.encode(input_text, return_tensors="pt")

        # Generate text conditioned on the input
        with torch.no_grad():
            output = model.generate(
                input_ids,
                max_length=100,  # Maximum length of the generated text
                num_return_sequences=1,  # Number of generated sequences
                temperature=0.7,  # Controls the randomness of the output
            )

        # Decode the generated output and append it to the list
        generated_text.append(tokenizer.decode(output[0], skip_special_tokens=True))

    return "\n".join(generated_text)

if __name__ == "__main__":
    mean_input = float(input("Enter the mean: "))
    median_input = float(input("Enter the median: "))
    std_dev_input = float(input("Enter the standard deviation: "))

    generated_text = generate_text(mean_input, median_input, std_dev_input)
    print("\nGenerated Text:\n")
    print(generated_text)
