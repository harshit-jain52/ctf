.global _start
_start:
.intel_syntax noprefix
    mov rax, 59		        # this is the syscall number of execve
    lea rdi, [rip+binsh]	# points the first argument of execve at the /bin/sh string below
    mov rsi, 0		        # this makes the second argument, argv, NULL
    mov rdx, 0		        # this makes the third argument, envp, NULL
    syscall			        # this triggers the system call
binsh:				        # a label marking where the /bin/sh string is
    .string "/bin/sh"
