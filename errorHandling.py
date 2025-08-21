# Ask user for the input file name
filename = input("Enter the filename to read: ")

try:
    # Open and read the input file
    with open(filename, "r") as file:
        content = file.read()

    # Count words
    words = content.split()
    word_count = len(words)

    # Convert content to uppercase
    content_upper = content.upper()

    # Write processed text and word count to output.txt
    with open("output.txt", "w") as file:
        file.write(content_upper)
        file.write("\n")
        file.write(f"Total number of words: {word_count}\n")

    print("✅ Successfully created output.txt with content in uppercase and word count.")

    # Show output file content
    with open("output.txt", "r") as file:
        output_content = file.read()
        print("\n📄 Output file content:\n")
        print(output_content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
