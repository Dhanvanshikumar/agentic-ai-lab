def log(input_text, tool, output):
    with open("logs.txt", "a") as f:
        f.write(f"Input: {input_text}\n")
        f.write(f"Tool: {tool}\n")
        f.write(f"Output: {output}\n")
        f.write("-"*30 + "\n")