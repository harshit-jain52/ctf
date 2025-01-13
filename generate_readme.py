import os
import urllib.parse

def generate_readme():
    readme_content = "# CTF Solutions\n\n"

    # Traverse directories and collect files
    solutions :dict[str, list[int]] = {}
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                path = os.path.join(root, file)
                relative_path = os.path.relpath(path, ".")
                filename = file.split(".")[0]
                site = root.split("/")[1]
                if site not in solutions:
                    solutions[site] = []
                solutions[site].append((filename, relative_path))
                
    # Sort solutions by site and solution_id
    for site, site_solutions in solutions.items():
        site_solutions.sort()
        readme_content += f"## {site}\n\n"
        for solution_id, relative_path in site_solutions:
            encoded_path = urllib.parse.quote(relative_path)
            readme_content += f"- [{solution_id}](./{encoded_path})\n"
     
    # Add Resources section
    resources_section = """
## Practice & Compete

- [CTFLearn](https://ctflearn.com)
- [picoCTF](https://play.picoctf.org/practice)
- [Pwnable.kr](https://pwnable.kr/) for Pwning
- [CTF.Hacker101](https://ctf.hacker101.com/) for Web Expoitation
- [Cryptohack](https://cryptohack.org/challenges/) for Cryptography
- [CTFTime](https://ctftime.org/) for Upcoming CTFs

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
