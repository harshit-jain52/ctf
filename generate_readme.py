import os
import urllib.parse

def generate_readme():
    readme_content = "# CTF Solutions\n\n"

    # Traverse directories and collect files
    ctflearn_solutions = []
    pwnable_solutions = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                path = os.path.join(root, file)
                relative_path = os.path.relpath(path, ".")
                filename = file.split(".")[0]
                if root.startswith("./CTFLearn"):
                    ctflearn_solutions.append((int(filename), relative_path))
                elif root.startswith("./Pwnable.kr"):
                    pwnable_solutions.append((filename, relative_path))
    
    # Add CTFLearn solutions
    readme_content += "## CTFLearn\n\n"
    ctflearn_solutions.sort()
    for solution_id, relative_path in ctflearn_solutions:
        readme_content += f"- [{solution_id}](./{relative_path})\n"

    # Add Pwnable.kr solutions
    readme_content += "\n## Pwnable.kr\n\n"
    for solution_id, relative_path in pwnable_solutions:
        encoded_path = urllib.parse.quote(relative_path)
        readme_content += f"- [{solution_id}](./{encoded_path})\n"
    
     # Add Resources section
    resources_section = """
## Practice & Compete

- [CTFLearn](https://ctflearn.com)
- [Pwnable.kr](https://pwnable.kr/)
- [CTFTime](https://ctftime.org/)

## Resources & Tools
- [CTF Handbook](https://ctf101.org/)
- [Intro to PWN](https://lnwatson.co.uk/posts/pwn-challenges/)
- [Intro to Forensics](https://infosecwriteups.com/beginners-ctf-guide-finding-hidden-data-in-images-e3be9e34ae0d)
- [Online decryption and decoding](https://cryptii.com/)

[Other Useful Links](https://medium.com/technology-hits/capture-the-flag-ctf-resources-for-beginners-9394ee2ea07a#2e91)
"""
    readme_content += resources_section
    
    # Write to README.md
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    generate_readme()
