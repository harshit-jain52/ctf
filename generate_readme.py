import os

def generate_readme():
    readme_content = "# CTFLearn Solutions\n\n"

    # Traverse directories and collect files
    solutions = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                path = os.path.join(root, file)
                relative_path = os.path.relpath(path, ".")
                filename = file.split(".")[0]
                solutions.append((int(filename), relative_path))
    
    # Sort solutions by numeric ID
    solutions.sort()

    for solution_id, relative_path in solutions:
        readme_content += f"- [{solution_id}](./{relative_path})\n"
    
    # Add profile link
    profile_url = "https://ctflearn.com/user/harshit_jain52"
    readme_content += f"\n[Profile]({profile_url})\n"

     # Add Resources section
    resources_section = """
## Resources & Tools

- [CTFLearn](https://ctflearn.com)
- [CTF Handbook](https://ctf101.org/)
- [Intro to PWN](https://lnwatson.co.uk/posts/pwn-challenges/)
- [Intro to Forensics](https://infosecwriteups.com/beginners-ctf-guide-finding-hidden-data-in-images-e3be9e34ae0d)
- [Online decryption and decoding](https://cryptii.com/)
"""
    readme_content += resources_section
    
    # Write to README.md
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    generate_readme()
