

# Example function to process text file
def process_text_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        # Remove trailing newline characters and concatenate all lines into a single string
        full_text = "  ".join(line.replace("\n", " ").replace("\t", " ").strip() for line in lines)
        #print(f"Full text from file '{filepath}':")
        #print(full_text)
    return full_text 
