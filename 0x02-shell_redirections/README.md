# Tasks on Shell Permissions

## Task 0: Hello world

Write a script that prints "Hello, World", followed by a new line to the standard output.

## Task 1: Confused smiley

Write a script that displays a confused smiley "(Ôo)'.

## Task 2: Let's display a file

Display the content of the /etc/passwd file.

## Task 3: What about 2?

Display the content of /etc/passwd and /etc/hosts

## Task 4: Last lines of a file

Display the last 10 lines of /etc/passwd

## Task 5: I'd prefer the first ones actually

Display the first 10 lines of /etc/passwd

## Task 6: Line #2

Write a script that displays the third line of the file iacta.

The file iacta will be in the working directory

- You’re not allowed to use sed

## Task 7: It is a good file that cuts iron without making a noise

Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.

## Task 8: Save current state of directory

Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

## Task 9: Duplicate last line

Write a script that duplicates the last line of the file iacta

- The file iacta will be in the working directory

## Task 10:

Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

## Task 11:

Write a script that counts the number of directories and sub-directories in the current directory.

- The current and parent directories should not be taken into account
- Hidden directories should be counted

## Task 12:

Create a script that displays the 10 newest files in the current directory.

Requirements:

- One file per line
- Sorted from the newest to the oldest


## Task 13:

Create a script that takes a list of words as input and prints only words that appear exactly once.

- Input format: One line, one word
- Output format: One line, one word
- Words should be sorted


## Task 14:

Display lines containing the pattern “root” from the file /etc/passwd

## Task 15:

Display the number of lines that contain the pattern “bin” in the file /etc/passwd

## Task 16:

Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.

## Task 17:

Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.

## Task 18:

Display all lines of the file /etc/ssh/sshd_config starting with a letter.

- include capital letters as well


## Task 19:

Replace all characters A and c from input to Z and e respectively.

## Task 20:

Create a script that removes all letters c and C from input.

## Task 21:

Write a script that reverse its input.

## Task 22:

Write a script that displays all users and their home directories, sorted by users.

- Based on the the /etc/passwd file


## Task 23:

Write a command that finds all empty files and directories in the current directory and all sub-directories.

- Only the names of the files and directories should be displayed (not the entire path)
- Hidden files should be listed
- One file name per line
- The listing should end with a new line
- You are not allowed to use basename, grep, egrep, fgrep or rgrep


## Task 24:

Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

- Hidden files should be listed
- Only regular files (not directories) should be listed
- The names of the files should be displayed without their extensions
- The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
- One file name per line
- The listing should end with a new line
- You are not allowed to use basename, grep, egrep, fgrep or rgrep


## Task 25:

An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more.

Create a script that decodes acrostics that use the first letter of each line.

- The ‘decoded’ message has to end with a new line
- You are not allowed to use grep, egrep, fgrep or rgrep


## Task 26:

Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

    Order by number of requests, most active host or IP at the top
    You are not allowed to use grep, egrep, fgrep or rgrep

Format:

```
host    When possible, the hostname making the request. Uses the IP address if the hostname was unavailable.
logname Unused, always -
time    In seconds, since 1970
method  HTTP method: GET, HEAD, or POST
url Requested path
response    HTTP response code
bytes   Number of bytes in the reply
```

Here is an example with one day of logs of the NASA website (1995).

```
julien@ubuntu:/tmp/0x02$ wget https://s3.amazonaws.com/alx-intranet.hbtn.io/public/nasa_19950801.tsv
--2022-03-08 11:08:26--  https://s3.amazonaws.com/alx-intranet.hbtn.io/public/nasa_19950801.tsv
Resolving s3.amazonaws.com (s3.amazonaws.com)... 52.217.171.144
Connecting to s3.amazonaws.com (s3.amazonaws.com)|52.217.171.144|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 782913 (765K) [binary/octet-stream]
Saving to: ‘nasa_19950801.tsv’

nasa_19950801.tsv   100%[===================>] 764.56K  --.-KB/s    in 0.008s

2022-03-08 11:08:26 (98.4 MB/s) - ‘nasa_19950801.tsv’ saved [782913/782913]

julien@ubuntu:/tmp/0x02$ head nasa_19950801.tsv
host    logname time    method  url     response        bytes
in24.inetnebr.com       -       807249601       GET     /shuttle/missions/sts-68/news/sts-68-mcc-05.txt 200     1839
uplherc.upl.com -       807249607       GET     /       304     0
uplherc.upl.com -       807249608       GET     /images/ksclogo-medium.gif      304     0
uplherc.upl.com -       807249608       GET     /images/MOSAIC-logosmall.gif    304     0
uplherc.upl.com -       807249608       GET     /images/USA-logosmall.gif       304     0
ix-esc-ca2-07.ix.netcom.com     -       807249609       GET     /images/launch-logo.gif 200     1713
uplherc.upl.com -       807249610       GET     /images/WORLD-logosmall.gif     304     0
slppp6.intermind.net    -       807249610       GET     /history/skylab/skylab.html     200     1687
piweba4y.prodigy.com    -       807249610       GET     /images/launchmedium.gif        200     11853
julien@ubuntu:/tmp/0x02$ ./103-the_biggest_fan < nasa_19950801.tsv
www-relay.pa-x.dec.com
piweba3y.prodigy.com
www.thyssen.com
130.110.74.81
ix-min1-02.ix.netcom.com
uplherc.upl.com
reggae.iinet.net.au
seigate.sumiden.co.jp
ircgate1.rcc-irc.si
s150.phxslip4.indirect.com
torben.dou.dk
julien@ubuntu:/tmp/0x02$
```
