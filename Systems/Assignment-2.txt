Q1: Linux file system and windows file system.

a) Linux:

/
| -- etc
|   | -- e1.txt
|   | -- e2.txt
|   | -- e3.txt
| -- home
|   | -- h1.txt
|   | -- hf1
|   | -- hf2
| -- user
|   | -- u1.txt
|   | -- u2.mp3
|   | -- u3.jpg
|   | -- uf
|       | -- ufchild
| -- cos350
|   | -- assign1
|       | -- submission
|   | -- assign2

b) Windows:

C:\
| -- user
| -- doc
|   | -- d1.txt
|   | -- d2.txt
|   | -- d3.txt
| -- c.txt
| -- D:\
|   | -- d1.txt
|   | -- D1
|       | -- d2.txt
|       | -- d3.txt
|   | -- D2 
|   | -- D3
|       | -- d4.txt
|       | -- games
|           | -- BG3
|               | -- bg3.exe
| -- E:\


Q2: Relative path and absolute path. Consider the directory structure on a Unix-based file system (‘/’
is the root, and there are three folders (users, projects, archive) in the root).

a)/projects/shared/code/common/config/settings.ini

b)/dataset.txt

c)/../../user/alice/pictures/vacations/mountains/everest.jpg

d)/archive/backup/reports/reports1.pdf

Q3: Conversions between symbolic notation and numerical representation for Linux permissions. For
each part of the question, please present both the answers and the calculation processes. It's
essential to note that only the final answers will incur a deduction of half points.

a)rwxrwxrw- converts to 764

b)rw-r-xr-- converts to 654

c)764 converts to rwxrw-r--

d)640 converts to rw-r-----

Q4: You are responsible for managing a network utilizes IPv4 addressing. Consider the following
scenarios. For each part of the question, please present both the answers and how you arrived at the
solutions. It's essential to note that only the answers will incur a deduction of half points.

a) Number of hosts: 254, Valid range of host IP addresses: 192.168.100.1 to 192.168.100.254
Network address: 192.168.100.0, Broadcast address: 192.168.100.255

b) Number of hosts: 65,534, Valid range of host IP addresses: 192.168.0.1 to 192.168.255.254
Network address: 192.168.0.0, Broadcast address: 192.168.255.255

Q5: Identify any errors or suboptimal practices in the given commands. If the command is correct and
recommended, simply state 'it works well'. Please refrain from executing these commands on your
personal computer, as the potential consequences are unknown.

a) help ls works well

b) I would not recommended running chmod 777 /etc/passwd as it gives all access to the specific file
which seems to contain a password, possibly even the users password.

c) This command will work but it will search the root directory, a better practice would be to give a
a more specific file location to search.

d) This command will over write the file with random data so i would not run this command.