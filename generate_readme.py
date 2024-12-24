import os

def generate_readme():
    readme_content = "# CTFLearn Solutions\n\n"
    profile_url = "https://ctflearn.com/user/harshit_jain52"  # Update your profile link as needed

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

    # Add solutions to README
    for solution_id, relative_path in solutions:
        readme_content += f"- [{solution_id}](./{relative_path})\n"
    
    # Add profile link
    readme_content += f"\n[Profile]({profile_url})\n"

    # Write to README.md
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    generate_readme()
