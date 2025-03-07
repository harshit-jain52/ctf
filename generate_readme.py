import os
import urllib.parse

def generate_readme():
    readme_content = "# CTF Solutions\n"

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
    solutions = dict(sorted(solutions.items()))
    for site, site_solutions in solutions.items():
        site_solutions.sort()
        readme_content += "\n"
        readme_content += f"## {site}\n\n"
        for solution_id, relative_path in site_solutions:
            encoded_path = urllib.parse.quote(relative_path)
            readme_content += f"- [{solution_id}](./{encoded_path})\n"
     
    # Add Resources section
    resources_section = """
## Practice & Compete

- [CTFLearn](https://ctflearn.com)
- [picoCTF](https://play.picoctf.org/practice)
- [pwn.college](https://pwn.college)
- [pwnable.kr](https://pwnable.kr/) for Pwning
- [CTF.Hacker101](https://ctf.hacker101.com/) for Web Expoitation
- [Cryptohack](https://cryptohack.org/challenges/) for Cryptography
- [xss-game](https://xss-game.appspot.com/) for XSS
- [CTFTime](https://ctftime.org/) for Upcoming CTFs

## Concepts

- [CTF Handbook](https://ctf101.org/)
- [Intro to PWN](https://lnwatson.co.uk/posts/pwn-challenges/)
- [Intro to Forensics](https://infosecwriteups.com/beginners-ctf-guide-finding-hidden-data-in-images-e3be9e34ae0d)
- [RSA Attacks](https://www.ams.org/notices/199902/boneh.pdf)
- [XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
- [Prototype Pollution](https://learn.snyk.io/lesson/prototype-pollution/)
- [postMessage Vulnerabilities](https://docs.ioin.in/writeup/www.exploit-db.com/_docs_40287_pdf/index.pdf)
- [JS eval()](https://blog.brownplt.org/2012/10/21/js-eval.html)
- [File Upload Vulnerabilities](https://portswigger.net/web-security/file-upload)
- [Binary Exploitation](https://lettieri.iet.unipi.it/hacking/ch/part-2.pdf)

## Tools
- [Wireshark: TLS Decryption](https://wiki.wireshark.org/TLS)
- [curl Cheatsheet](https://devhints.io/curl)
- [nc Cheatsheet](https://quickref.me/nc)
- [nmap Cheatsheet](https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/)
- [BurpSuite docs](https://portswigger.net/burp/documentation)
- [Online decryption and decoding](https://cryptii.com/)
- [Online decompiler](https://dogbolt.org/)


[Other Useful Links](https://medium.com/technology-hits/capture-the-flag-ctf-resources-for-beginners-9394ee2ea07a#2e91)
"""
    readme_content += resources_section
    
    # Write to README.md
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    generate_readme()
