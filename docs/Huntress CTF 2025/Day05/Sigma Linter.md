# Sigma Linter

> Web

```text
Oh wow, another web app interface for command-line tools that already exist!
This one seems a little busted, though...
```

![image](./images/sigma0.png)

A YAML-linter is provided, with a few examples:

![image](./images/sigma1.png)
![image](./images/sigma2.png)
![image](./images/sigma3.png)
![image](./images/sigma4.png)

After a bit of searching, I came across [this blog](https://trevorsaudi.medium.com/yaml-2-json-hackpack-ctf-7de28ef0ecff)

Upon trying the approach in the blog:

![image](./images/sigma5.png)

The displayed error indicates that the command was indeed executed! Now we try with valid commands to get the flag

![image](./images/sigma6.png)

To resolve the errors shown:

![image](./images/sigma7.png)

Executed successfully, but not displayed. Since `title` is a mandatory field, try to inject the command there:

![image](./images/sigma8.png)

Yep it worked! We can see the output of the shell command in the error message. We now know there's a `flag.txt`:

![image](./images/sigma9.png)
