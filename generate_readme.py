import os
import urllib.parse

def generate_readme():
    readme_content = "# CTF Writeups\n"
    index_content = "# Index\n"

    # Traverse directories and collect files
    solutions :dict[str, list[int]] = {}
    for root, _, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md") and file != "index.md":
                path = os.path.join(root, file)
                relative_path = os.path.relpath(path, "docs")
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
- [GoogleCTF Beginner's Quest](https://capturetheflag.withgoogle.com/beginners-quest)
- [CTFTime](https://ctftime.org/) for Upcoming CTFs

## Concepts

- [CTF Handbook](https://ctf101.org/)
- [Intro to PWN](https://lnwatson.co.uk/posts/pwn-challenges/)
- [Intro to Forensics](https://infosecwriteups.com/beginners-ctf-guide-finding-hidden-data-in-images-e3be9e34ae0d)
- [Guide to Web Security](https://portswigger.net/web-security/)
- [PCAP Challenges](https://www.packetsafari.com/blog/2023/01/13/ctf-pcap-challenges/)
- [RSA Attacks](https://www.ams.org/notices/199902/boneh.pdf)
- [Prototype Pollution](https://learn.snyk.io/lesson/prototype-pollution/)
- [postMessage Vulnerabilities](https://docs.ioin.in/writeup/www.exploit-db.com/_docs_40287_pdf/index.pdf)
- [JS eval()](https://blog.brownplt.org/2012/10/21/js-eval.html)
- [Smashing the Stack for Fun and Profit](https://inst.eecs.berkeley.edu/~cs161/fa08/papers/stack_smashing.pdf)
- [Format Strings](https://axcheron.github.io/exploit-101-format-strings/)
- [Server Side Template Injection](https://medium.com/@bdemir/a-pentesters-guide-to-server-side-template-injection-ssti-c5e3998eae68)

## Tools

- [CyberChef](https://gchq.github.io/CyberChef/)
- [Wireshark: TLS Decryption](https://wiki.wireshark.org/TLS)
- [curl Cheatsheet](https://devhints.io/curl)
- [nc Cheatsheet](https://quickref.me/nc)
- [nmap Cheatsheet](https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/)
- [BurpSuite docs](https://portswigger.net/burp/documentation)
- [Online decryption and decoding](https://cryptii.com/)
- [Online decompiler](https://dogbolt.org/)


[Other Useful Links](https://medium.com/technology-hits/capture-the-flag-ctf-resources-for-beginners-9394ee2ea07a#2e91)

[CTF Repos](https://github.com/stars/harshit-jain52/lists/ctf-black-flag)
"""
    readme_content += resources_section
    index_content += resources_section

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
    
    with open("docs/index.md", "w") as index_file:
        index_file.write(index_content)

if __name__ == "__main__":
    generate_readme()
