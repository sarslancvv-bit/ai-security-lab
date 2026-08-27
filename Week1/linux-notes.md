# Linux / Bash Notes

Bash — one of the most common Linux shells.

## Directory Tree in Linux (filesystem)

```
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

It often shows username, hostname, current directory.

**Structure:** `command options arguments`

Example: `echo` (command) `Hello World` (argument)

**Is the shell the same as the terminal?**
Not exactly. The terminal is the window or app you type into. The shell is the program running inside it.

---

## `pwd`

`pwd` — prints your current working directory.

```
example --> /home/samim/ai-security-lab
```

`ls` — tells me `fundamentals` and `notes.txt` are located in `/home/samim/ai-security-lab`.

---

## `cd`

`cd` — changes the directory.

- **Absolute path:** The full path starting from the root directory (`/`). For example: `/home/pete/Desktop`
- **Relative path:** A path based on your current location. If you are in `/home/pete/Documents` and want to access a subdirectory named `taxes`, you can use `taxes/`.

```bash
cd /home/pete/Pictures   # moves directly to Pictures directory
```

| Symbol | Meaning |
|---|---|
| `.` | represents the directory you're currently in |
| `..` | moves you one level up to the directory containing your current one |
| `~` | a shortcut to your personal home directory |
| `-` | takes you back to the last directory you were in |

**Does `cd` work on files?** No. `cd` changes into directories, not regular files.

---

## `ls`

List the directories and files in the current directory.

| Option | Meaning |
|---|---|
| `-a` | Show all files, including hidden files (filenames starting with a dot `.`). |
| `-l` | Long format — shows file permissions, number of links, owner, group, size, modification time, and name. |
| `-h` | Human-readable sizes (used with `-l`). |
| `-t` | Sort by modification time. |
| `-r` | Reverse the sort order. |
| `-S` | Sort by file size. |
| `-d` | List the directory itself instead of its contents. |

Common combos:
```bash
ls -lh
ls -la
ls -ltr   # sort by time, then reverse
```

---

## `touch`

Its primary purpose is to change file timestamps; it is also commonly used to create new, empty files.

```bash
touch mysuperduperfile          # if the file does not exist, touch creates it
touch file1.txt file2.txt file3.log   # can create multiple files at once
```

```bash
# Check the original timestamp
$ ls -l mysuperduperfile
-rw-r--r-- 1 samim samim 0 Aug 14 14:20 mysuperduperfile

# Update the timestamp
$ touch mysuperduperfile

# Check the new timestamp
$ ls -l mysuperduperfile
-rw-r--r-- 1 samim samim 0 Aug 14 14:21 mysuperduperfile
```

Updates the timestamp to the current time if the file already exists.

| Option | Meaning |
|---|---|
| `-a` | Change only the access time. |
| `-m` | Change only the modification time. |
| `-c` | Do not create the file if it does not exist. |
| `-d "DATE"` | Use a specific date string. |
| `-r FILE` | Use another file's timestamp as a reference. |
| `-t STAMP` | Use a timestamp in a compact numeric format. |

---

## `file`

To find out what kind of file a file is, you can use the `file` command.

```bash
file fundamentals
fundamentals: directory

file fundamentals notes.txt file1.txt   # can use multiple files

file *   # show every item's properties
file1.txt:        empty
file2.txt:        empty
file3.log:        empty
fundamentals:     directory
mysuperduperfile: empty
notes.txt:        ASCII text
```

`-i` shows the MIME-style information, useful when working with web files or scripts:
```bash
file -i index.html
```

| Option | Meaning |
|---|---|
| `-i` | Show MIME type information. |
| `-b` | Brief mode, omit the filename in output. |
| `-L` | Follow symbolic links. |
| `-z` | Try to inspect compressed files. |

---

## `cat`

View the content of files, and link files together.

```bash
cat file.txt                  # not ideal for large files, but its main purpose is viewing
cat dogfile birdfile > animals   # linking example
cat > newfile.txt             # creates a new file
cat >> notes.txt              # append new information into an existing file
```

| Option | Meaning |
|---|---|
| `-n` | Number all output lines, starting from 1. |
| `-b` | Number only non-empty output lines. |
| `-s` | Squeeze multiple blank lines into one blank line. |
| `-A` | Show non-printing characters, tabs, and line endings. |

`cat` is for short files. For long files, use `less` so you can scroll, search, and quit without flooding the terminal.

---

## `less`

```bash
less /home/samim/ai-security-lab/newfile.txt   # enters the long text
```

**Inside `less`:**
1. Page Up, Page Down, Up, and Down to navigate line by line or page by page.
2. Press `g` to move directly to the beginning of the text file.
3. Press `G` (Shift + g) to jump to the end of the text file.
4. Press `u` to move up and `d` to move down.
5. If you forget the commands while inside `less`, just press `h` to display a helpful summary.

| Command | Meaning |
|---|---|
| `/search_term` | Searches forward for "search_term". |
| `?search_term` | Searches backward for "search_term". |
| `n` | Jumps to the next occurrence of the search term. |
| `N` | Jumps to the previous occurrence. |

| Option | Meaning |
|---|---|
| `-N` | Show line numbers. |
| `+G` | Open at the end of the file. |
| `+F` | Follow new content as it is added, similar to `tail -f` — dosyayı aç ve yeni eklenen içerikleri takip et. |

---

## `history`

`history` — can see the list of commands you have used.

- **Up Arrow:** Want to run the same command you just did? Just press the up arrow key to cycle backward through your history.
- **The `!!` Shortcut:** To execute the most recent command again, use `!!`. For example, if you just ran `cat file1`, typing `!!` and pressing Enter will run `cat file1` again.
- **Run by number:** Use `!102` to run command number 102 from your history.
- **Run by prefix:** Use `!cat` to run the most recent command that started with `cat`.
- With **Ctrl-R**, you can search any command in history and bash will match the most similar; pressing Enter executes the matched one.

```bash
history -c   # Clear current history list — removes all entries from the history list in memory
history -w   # Write history to file — saves the current session's history to ~/.bash_history
less ~/.bash_history   # view the bash_history
history -d <offset>    # Delete a specific entry by its history number
```

---

## `cp`

```bash
cp [OPTIONS] SOURCE DESTINATION
```

Can copy one file to another file, one or more files into a directory, or an entire directory tree with the right option.

```bash
cp file1.txt file2.txt file3.log /home/samim/ai-security-lab/newfile_backup
# can copy several files into the same directory
```

**Wildcards:**

| Symbol | Meaning |
|---|---|
| `*` | Matches any sequence of characters. |
| `?` | Matches any single character. |
| `[]` | Matches any one of the characters enclosed in the brackets. |

```bash
cp file[A-B].txt /home/samim/ai-security-lab/my_directory
# fileA.txt ve fileB.txt'yi my_directory'ye basar ama fileC.txt'yi basmaz

cp file?.txt /home/samim/ai-security-lab/my_directory
# file10.txt'yi basmaz ama file1'den file9'a kadar hepsini basabilir (one single character)
```

**Copying Directories Recursively:**

```bash
cp -r Pumpkin/ /home/samim/Documents
# copies Pumpkin and everything inside it to Documents directory

cp -r previous_directory/ my_directory/
```

**Easy way to remember:**

| Command | Destination exists? | What happens? |
|---|---|---|
| `cp file dir/` | Yes | Overwrites |
| `cp -i file dir/` | Yes | Asks you |
| `cp -f file dir/` | Yes | Forces overwrite |
| `cp -n file dir/` | Yes | Doesn't overwrite |

**Purpose of `-p`:** tries to make the copied file keep the same metadata as the original.

```bash
ls -l --time-style=long-iso notes.txt
-rw-r--r-- 1 samim samim 48 2026-08-14 19:37 notes.txt
```

If you do a normal copy:
```bash
cp myfile.txt backup/
```
the copied file generally gets a new modification timestamp corresponding to when you copied it.

But:
```bash
cp -p myfile.txt backup/
```
preserves important attributes, especially:
- Modification/access timestamps
- Permissions (mode), such as `rw-r--r--`
- Ownership, when you have permission to preserve it

So if the original was last modified on August 10:
```
myfile.txt          → modified Aug 10
backup/myfile.txt   → modified Aug 10
```
instead of appearing as newly modified today.

> Bu dosyayı mesela ben 22:13'te modify ettim, ama `-p` fonksiyonu sayesinde notes.txt'nin ilk ne zaman modify olduğu bu sayede korunmuş oldu.

**Archive Copies with `-a`:**

The `-a` option means archive. It is commonly used for backup-style directory copies because it preserves many attributes and copies recursively. It copies directories recursively and preserves things such as permissions, timestamps, symbolic links, and ownership where possible.

```bash
cp -a /home/samim/ai-security-lab/my_directory /home/samim/ai-security-lab/backup
# backup'a my_directory'deki tüm dosyalar kaydoldu
```

**Copy Only Newer Files with `-u`:**

```
source/
├── file1.txt    ← modified today
├── file2.txt    ← modified Monday
└── file3.txt    ← modified today

backup/
├── file1.txt    ← modified yesterday
├── file2.txt    ← modified today
```

```bash
cp -u source/*.txt backup/
```

What happens?
```
file1.txt → COPIED      source is newer
file2.txt → NOT COPIED  destination is newer
file3.txt → COPIED      doesn't exist in backup
```

**All options:**

| Option | Meaning |
|---|---|
| `-r` / `-R` | Copy directories recursively. |
| `-i` | Ask before overwriting a file. |
| `-f` | Force overwriting by removing the destination first if needed. |
| `-n` | Do not overwrite existing files. |
| `-p` | Preserve mode, ownership where possible, and timestamps. |
| `-a` | Archive mode, useful for preserving directory trees. |
| `-u` | Copy only when the source is newer than the destination. |
| `-v` | Show each file as it is copied. |

```bash
cp -rv /home/samim/ai-security-lab/my_directory /home/samim/ai-security-lab/backup

'/home/samim/ai-security-lab/my_directory/newfile.txt' -> '/home/samim/ai-security-lab/backup/my_directory/newfile.txt'
'/home/samim/ai-security-lab/my_directory/notes.txt' -> '/home/samim/ai-security-lab/backup/my_directory/notes.txt'
'/home/samim/ai-security-lab/my_directory/file1.txt' -> '/home/samim/ai-security-lab/backup/my_directory/file1.txt'
'/home/samim/ai-security-lab/my_directory/file2.txt' -> '/home/samim/ai-security-lab/backup/my_directory/file2.txt'
'/home/samim/ai-security-lab/my_directory/file3.log' -> '/home/samim/ai-security-lab/backup/my_directory/file3.log'
'/home/samim/ai-security-lab/my_directory/file10.txt' -> '/home/samim/ai-security-lab/backup/my_directory/file10.txt'
'/home/samim/ai-security-lab/my_directory/fileA.txt' -> '/home/samim/ai-security-lab/backup/my_directory/fileA.txt'
'/home/samim/ai-security-lab/my_directory/fileB.txt' -> '/home/samim/ai-security-lab/backup/my_directory/fileB.txt'
'/home/samim/ai-security-lab/my_directory/previous_directory/old_directory.txt' -> '/home/samim/ai-security-lab/backup/my_directory/previous_directory/old_directory.txt'
```

---

## `mv`

Two primary purposes: renaming files or directories, and moving them to a different location.

**Renaming Files and Directories:**

```bash
mv oldfile newfile
mv notes.txt notlar.txt          # kendi yaptığım

mv old_directory_name new_directory_name
mv my_directory my_first_example  # kendi yaptığım
```

**Moving Files and Directories:**

To move a single file into a different directory:
```bash
mv file2 /home/pete/Documents
mv move_deneme.txt /home/samim/ai-security-lab/backup   # kendi yaptığım
```

Moving multiple files at once:
```bash
mv file_1 file_2 somedirectory/
mv pha.txt oha2.txt /home/samim/ai-security-lab/backup   # kendi yaptığım
```

On GNU/Linux systems, a useful option is `-t`, which allows you to specify the target directory first. This can be clearer when moving many files.

```bash
mv -t somedirectory/ file_1 file_2   # tek olay ilk directory'yi yazabilmek
```

> Unlike the `cp` command, you do not need a recursive option to move a directory. `mv` handles directories by default.

**Important Options:**

By default, if you move a file to a destination where a file with the same name already exists, `mv` will overwrite it without warning. To prevent accidental data loss:

- **`-i` (interactive):** A crucial safety feature. It will prompt you for confirmation before overwriting any existing file.
```bash
mv -i source_file destination_directory

mv -i oha2.txt /home/samim/ai-security-lab/backup   # kendi yaptığım
mv: overwrite '/home/samim/ai-security-lab/backup/oha2.txt'? y
```

- **`-b` (backup):** If you intend to overwrite a file but want to keep the old version, this option creates a backup of the destination file. The backup is typically renamed with a tilde (`~`) suffix.
```bash
mv -b file1 directory_with_file1
mv -b notes.txt /home/samim/ai-security-lab/backup/notes.txt   # kendi yaptığım
```

- **`-v` (verbose):** Prints out what it is doing, showing each file being moved or renamed.
```bash
mv -v fileC.txt file10.txt /home/samim/ai-security-lab/my_first_example
renamed 'fileC.txt' -> '/home/samim/ai-security-lab/my_first_example/fileC.txt'
renamed 'file10.txt' -> '/home/samim/ai-security-lab/my_first_example/file10.txt'
```

- **`-n`:** Move source_file into destination_directory, but do NOT overwrite it if a file with the same name already exists there.
```bash
mv -n mysuperduperfile /home/samim/ai-security-lab/previous_directory
mv: not replacing '/home/samim/ai-security-lab/previous_directory/mysuperduperfile'
```

---

## `mkdir`

As you work with files, you will need to organize them into directories. The primary tool for this task is `mkdir`, which stands for "make directory."

```bash
mkdir documents                       # Creating a Single Directory
mkdir books paintings                 # Creating Multiple Directories
mkdir -p books/hemingway/favorites    # Creating Nested Directories
mkdir -m 755 public                   # Setting Directory Permissions
```

The `-m 755` example creates a directory that the owner can write to and others can read and enter (permissions covered later).

`-v`: Print a message for each created directory.
```bash
mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

**How do I create nested directories?** Use `mkdir -p parent/child/grandchild`.

---

## `rm`

To delete files, you use the `rm` (remove) command. `rm` removes directory entries from the filesystem — in normal terms, it deletes files. Unlike many desktop environments, command-line deletion usually does not move files to a trash folder, so you should check your command before pressing Enter.

**Remove a Single File:**
```bash
rm file1
```

**Remove Files with Wildcards:**
```bash
rm *.tmp   # removes every .tmp file in the current directory
```

Before using `rm` with a wildcard, it is safer to preview the match with `ls`:
```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

**Interactive Deletion with `-i`:**
```bash
rm -i important.txt
rm: remove regular file 'important.txt'? y
```

**Forceful Deletion with `-f`:**
```bash
rm -f old-cache.txt
```
Be careful: `-f` also suppresses some safety prompts, so it can hide mistakes.

**Removing Directories with `-r`:**

By default, `rm` cannot delete a directory.
```bash
rm projects
rm: cannot remove 'projects': Is a directory
```

To remove a directory and everything inside it, use `-r` or `-R` for recursive removal:
```bash
rm -r old-project
```

**The Dangers of `rm -rf`:**

This command can be appropriate for removing generated folders such as build outputs, but it is dangerous because it removes a whole tree without asking questions. Always check:
- Are you in the directory you think you are in? Use `pwd`.
- Did your wildcard expand correctly? Preview with `ls`.
- Is the path absolute or relative? `/tmp/cache` and `tmp/cache` are very different.
- Is there an accidental space? `"rm -rf old-project"` and `"rm -rf old project"` target different paths.

**Using `rmdir` for Empty Directories:**
```bash
rmdir empty-directory
```
The `rmdir` command will only succeed if the directory is completely empty.

```bash
rm -rv previous_directory
# removes and outputs what it removed:
removed 'previous_directory/old_directory.txt'
removed 'previous_directory/mysuperduperfile'
removed directory 'previous_directory'
```

---

## `find`

The `find` command searches directory trees using criteria such as name, type, size, and modification time.

**Using `find`:**

You specify the directory to search in and the criteria for what you are looking for.

```bash
find /home -name puppies.jpg
# find /home looks inside /home and its subdirectories
```

**Searching by Name and Type:**
```bash
find . -name "*.txt"   # "." represents current directory
find /home -type d -name MyFolder   # -type d looks for a directory instead of a file
```

**Searching by Size and Time:**
```bash
find . -type f -size +10M
find . -type f -size -1k
```
- `-mtime -7` means modified within the last 7 days.
- `-mtime +30` means modified more than 30 days ago.

**Running Actions on Results:**
```bash
find . -name "*.log" -print

find . -name "*.log" -exec ls -l {} \;   # runs ls -l on each match
```
The `{}` placeholder is replaced by each matching path. The escaped semicolon marks the end of the command.

> Be careful with destructive actions such as `-delete`. First run the same search without `-delete` to confirm the matches.

| Option | Meaning |
|---|---|
| `-name PATTERN` | Match by filename. |
| `-iname PATTERN` | Match by filename, ignoring case. |
| `-type f` | Match regular files. |
| `-type d` | Match directories. |
| `-size +10M` | Match files larger than 10 megabytes. |
| `-mtime -7` | Match files modified within the last 7 days. |
| `-maxdepth N` | Limit how deep find searches. |

---

## `man`

**Inside a man page:**
- Press `/` and type a search term to search forward.
- Press `n` to jump to the next match.
- Press `N` to jump to the previous match.
- Press `q` to quit.

**Understanding Man Page Sections:**

| Section | Meaning |
|---|---|
| 1 | User commands. |
| 2 | System calls. |
| 3 | Library functions. |
| 5 | File formats. |
| 8 | System administration commands. |

---

# Permissions

## 1. Introduction to File Permissions

```bash
ls -l "/mnt/c/Users/samim/OneDrive/Masaüstü"
```

```
-rwxrwxrwx 1 samim samim        24 Jun 10 15:22  ACCOUNT.txt
-rwxrwxrwx 1 samim samim    590915 Aug  9 15:24  AI-Security-Hafta1-4-Detay-v3.pdf
-rwxrwxrwx 1 samim samim    101070 Jul  3 14:23 'Academic Records Summary.html'
drwxrwxrwx 1 samim samim       512 Jul  3 14:23 'Academic Records Summary_files'
drwxrwxrwx 1 samim samim       512 Jun 13 14:55 'Autmation Explore'
-rwxrwxrwx 1 samim samim     30178 Jul 16 15:16  Burgan_BI_Mulakat_Hazirlik_Plani.docx
-rwxrwxrwx 1 samim samim    346583 Apr  6 22:29 'CLAUDE _PROJECT.pdf'
-rwxrwxrwx 1 samim samim       802 Oct 12  2025 'DSA GELECEK DERSLER.txt'
-rwxrwxrwx 1 samim samim      1304 Sep 19  2023 'Display Driver Uninstaller.lnk'
-rwxrwxrwx 1 samim samim       736 Apr  9 16:39 'Git Notepad.txt'
-rwxrwxrwx 1 samim samim        66 Feb 18 18:55 'META MASK WALLET ID.txt'
-rwxrwxrwx 1 samim samim       505 Apr  2 13:30 'MIDTERM TARİHLERİ.txt'
-rwxrwxrwx 1 samim samim      1421 Jul 13  2024 'Opera GX Browser.lnk'
-rwxrwxrwx 1 samim samim      1949 Mar 15 19:32 'PROJECT STAGE A.txt'
drwxrwxrwx 1 samim samim       512 Jul  9 11:55  Project
-rwxrwxrwx 1 samim samim      2402 Oct 27  2023 'SU COURSE.lnk'
-rwxrwxrwx 1 samim samim      1976 Aug 14 12:39 'UiPath Assistant.lnk'
-rwxrwxrwx 1 samim samim      1825 Aug 14 12:39 'UiPath Diagnostic Tool.lnk'
-rwxrwxrwx 1 samim samim      1778 Aug 14 12:39 'UiPath Studio.lnk'
-rwxrwxrwx 1 samim samim      1412 Jan  1  2026 'Visual Studio Code.lnk'
-rwxrwxrwx 1 samim samim   1833023 Jul 17 13:12 'WHAT IS SQL.png'
-rwxrwxrwx 1 samim samim      1959 Aug  4 15:03 'Zoom Workplace.lnk'
drwxrwxrwx 1 samim samim       512 Apr 28  2025  __pycache__
-rwxrwxrwx 1 samim samim       520 Jul 17 13:13  desktop.ini
-rwxrwxrwx 1 samim samim       227 Jul  9 12:10  entry-points.json
-rwxrwxrwx 1 samim samim     18715 Aug 14 23:58  linux-notes.md
-rwxrwxrwx 1 samim samim        88 Feb 18 18:47 'meta mask password.txt'
-rwxrwxrwx 1 samim samim      1452 Jul  9 12:10  project.json
-rwxrwxrwx 1 samim samim       120 Jul  9 12:10  project.uiproj
```

The first column is important — it represents the file type and its permissions.

**Decoding the Permission String:**

In this example, the `d` signifies that Desktop is a directory. For a regular file, you would see a hyphen (`-`).

```
d |rwx | rwx| rwx
```

| Symbol | Meaning |
|---|---|
| `r` | Read permission |
| `w` | Write permission |
| `x` | Execute permission |
| `-` | No permission granted |

The meaning of these permissions can change slightly depending on whether it's a file or a directory. For example, execute (`x`) permission on a directory allows you to enter it, while on a file, it allows you to run it as a program.

```
d | rwx | r-x | r-x
```

- **User (Owner):** The first set (`rwx`) applies to the owner of the file, which is `pete` in our example. The owner has read, write, and execute permissions.
- **Group:** The second set (`r-x`) applies to the group associated with the file, which is `penguins`. Members of this group have read and execute permissions but cannot write to the file.
- **Other:** The final set (`r-x`) applies to all other users on the system. They have read and execute permissions.

---

## 2. Modifying Permissions

When you need to modify file or directory access rights, the primary tool you'll use is the `chmod` (change mode) command. `chmod` offers two main methods: **symbolic** and **numerical** mode.

**Using Symbolic Mode:**

It uses letters to represent users and permissions. You first specify which permission set you want to change (user, group, or other), then use `+` to add a permission or `-` to remove it.

| Symbol | Meaning |
|---|---|
| `u` | user/owner |
| `g` | group |
| `o` | others |
| `a` | all: user, group, and others |

```bash
chmod u+x myfile   # adds (+) the executable (x) permission for the user (u) on myfile
chmod g-w myfile   # removes the write permission for the group
chmod ug+w myfile  # users and group have permission to write in myfile (multiple permissions)
```

**Using Numerical Mode:**

| Value | Permission |
|---|---|
| 4 | read (r) |
| 2 | write (w) |
| 1 | execute (x) |

To grant read, write, and execute permissions: `4 + 2 + 1 = 7`.

```bash
chmod 755 myfile
```
- 7 (User): 4 + 2 + 1 → The user gets read, write, and execute permissions (rwx)
- 5 (Group): 4 + 0 + 1 → The group gets read and execute permissions (r-x)
- 5 (Others): 4 + 0 + 1 → All other users get read and execute permissions (r-x)

---

## 3. Ownership Permissions

**Changing User Ownership:**

To transfer the ownership of a file to a different user, you use the `chown` (change owner) command. You typically need superuser privileges (`sudo`) to change the owner of a file you don't own.

```bash
sudo chown patty myfile   # changes the user owner of myfile to the user (patty)
```

**Changing Group Ownership:**
```bash
sudo chgrp whales myfile   # sets the group ownership of myfile to the group (whales)
```

**Changing Both User and Group:**
```bash
sudo chown patty:whales myfile
# assigns user ownership to (patty) and group ownership to (whales) for the file (myfile)
```

---

## 4. Umask

Every file that gets created comes with a default set of permissions. If you ever want to change that default set of permissions, you can do so with the `umask` command. This command uses the 3-bit permission set we see in numerical permissions.

Instead of adding these permissions, `umask` takes away these permissions.

```bash
umask 021
```
We are stating that we want the default permissions of new files to allow users access to everything, but for groups, we want to take away their write permission, and for others, we want to take away their executable permission.

The default umask on most distributions is `022`, meaning full user access, but no write access for group and other users.

When you run the `umask` command, it will apply that default set of permissions to any new file you create.

> **umask:** Yeni oluşturulan dosya ve klasörlerin varsayılan izinlerinden hangi izinlerin çıkarılacağını belirler.
> Örnek: `umask 022` → group ve others için write (w) iznini kaldırır.
> Yeni dosya: `644` (rw-r--r--), yeni klasör: `755` (rwxr-xr-x).

---

## 5. Setuid

There are many cases in which normal users need elevated access to do stuff. The system administrator can't always be there to enter a root password every time a user needs access to a protected file, so there are special file permission bits to allow this behavior. The **Set User ID (SUID)** allows a user to run a program as the owner of the program file rather than as themselves.

**Example:**

Let's say I want to change my password — simple, right? I just use the `passwd` command:
```bash
passwd
```

What is the `passwd` command doing? It's modifying a couple of files, but most importantly it's modifying the `/etc/shadow` file:

```bash
ls -l /etc/shadow
```
`/etc/shadow` → a protected Linux file that stores password hashes and password-related account information.

This file is owned by root — how is it possible that we are able to modify a file owned by root?

```bash
ls -l /usr/bin/passwd
```
Shows detailed information about the `passwd` executable file, which is the program used to change user passwords.

The important part is `-rwsr-xr-x`:
- `rwx` → the owner (root) can read, write, and execute.
- `s` → SUID (Set User ID) is enabled. When a normal user runs `passwd`, the program temporarily runs with the file owner's (root) privileges.
- `r-x` → group and other users can read and execute it.

That's why we are able to access a protected file like `/etc/shadow` when we run the `passwd` command. If you removed that bit, you would not be able to modify `/etc/shadow` and therefore not change your password.

> **SUID (Set User ID) — Kısa Özet**
> SUID, bir programı çalıştıran kişinin değil, program dosyasının sahibinin yetkileriyle çalışmasını sağlar.
> Örnek: Normal kullanıcı `/etc/shadow` dosyasını değiştiremez çünkü dosya root'a aittir. Ancak `passwd` komutunda SUID vardır:
> ```
> -rwsr-xr-x root root /usr/bin/passwd
>    ↑
>    s = SUID
> ```
> Bu yüzden `passwd` çalışırken geçici olarak root yetkisiyle `/etc/shadow` dosyasını güncelleyebilir.
>
> **SUID verme:**
> ```
> chmod u+s file
> chmod 4755 file
> ```
> - `4` → SUID
> - `s` → SUID + execute izni var
> - `S` → SUID var ama execute izni yok
>
> **Mantık:** Kullanıcıya tamamen root yetkisi vermeden, belirli bir programın gerekli yüksek yetkiyle çalışmasını sağlamak.

---

## SGID (Set Group ID) — Kısa Özet

SGID, SUID'nin group versiyonudur. Bir program çalıştırıldığında, kullanıcının kendi grubuyla değil, program dosyasının grubunun yetkileriyle çalışmasını sağlar.

**Örnek:**
```
-rwxr-sr-x root tty /usr/bin/wall
      ↑
      s = SGID
```
Burada `wall` programının grubu `tty`. SGID sayesinde program çalışırken `tty` grubunun yetkilerini kullanabilir.

**SGID verme:**
```
chmod g+s myfile
chmod 2555 myfile
```
- `2` → SGID
- Group kısmındaki `s` → SGID aktif

**Mantık:**
- SUID → dosya sahibinin (user) yetkisiyle çalıştırır.
- SGID → dosyanın grubunun yetkisiyle çalıştırır.

Ek olarak, SGID bir klasöre verilirse, o klasörde oluşturulan yeni dosyalar klasörün grubunu miras alır. Bu özellikle ortak proje klasörlerinde çok kullanışlıdır.

---

## Process Permission

**1. Önce process nedir?**

Bir programı çalıştırdığında Linux o program için bir process (süreç) oluşturur.

Örneğin kullanıcı bob:
```bash
touch test.txt
```
çalıştırırsa: Bob → `touch` programını çalıştırır → `touch` process'i oluşur. Linux bu process'in hangi kullanıcıya ait olduğunu ve hangi yetkilere sahip olduğunu UID'lerle takip eder.

**2. Real UID (RUID) — "Bunu kim başlattı?"**

Real UID, process'i gerçekten hangi kullanıcının başlattığını gösterir.

Örneğin: Bob UID = 500. Bob `touch test.txt` çalıştırırsa process'in Real UID = 500 (Bob) olur.

Yani RUID = process'i başlatan gerçek kullanıcı.

**3. Effective UID (EUID) — "Şu anda kimin yetkilerini kullanıyorum?"**

Bu en önemli olanı. Effective UID, process'in dosyalara erişirken hangi kullanıcının yetkilerini kullandığını belirler.

Normal durumda:
```
Bob UID = 500
Bob → touch çalıştırıyor
RUID = 500
EUID = 500
```
Dolayısıyla `touch`, Bob'un yetkileriyle çalışır.

Örneğin Bob'un `/root/secret.txt` dosyasına erişim izni yoksa:
```bash
touch /root/secret.txt
```
başarısız olur. Çünkü Linux permission kontrolünde process'in EUID'sine bakar:
```
EUID = 500 (Bob)
→ Bob'un izni yok
→ Access Denied
```

**4. SUID olunca ne değişiyor?**

`passwd` programına bakalım:
```
-rwsr-xr-x root root /usr/bin/passwd
   ↑
  SUID
```

Dosyanın sahibi: root → UID 0. Bob'un UID'si: Bob → UID 500.

Bob `passwd` çalıştırdığında SUID nedeniyle:
```
RUID = 500 → Bob
EUID = 0   → root
```

Yani:
- RUID bize "Bob başlattı" der.
- EUID bize "Şu anda root yetkisi kullanılıyor" der.

Bu nedenle `passwd`, normalde Bob'un değiştiremeyeceği `/etc/shadow` dosyasına erişebilir.

**5. Peki Bob artık root mu?**

Hayır. Bu çok önemli. Bob'un kendisi root olmadı. Sadece `passwd` process'i belirli işlemleri yaparken root yetkisine sahip.

```
Bob
UID = 500
     ↓
passwd çalıştırır
     ↓
RUID = 500  ← hâlâ Bob'un başlattığı biliniyor
EUID = 0    ← process root yetkisi kullanabiliyor
```
`passwd` bittiğinde bu durum da biter.

**6. Bob neden Sally'nin şifresini değiştiremiyor?**

Diyelim:
```
Bob   UID = 500
Sally UID = 600
root  UID = 0
```

Bob `passwd` çalıştırınca:
```
RUID = 500
EUID = 0
```

Program root yetkisi sayesinde `/etc/shadow` dosyasına teknik olarak erişebilir. Ama program aynı zamanda `RUID = 500` bilgisinden programı Bob'un başlattığını bilir. Bu nedenle `passwd` programının kendi güvenlik kontrolleri Bob'un yalnızca kendi şifresini değiştirmesine izin verir.

Yani kabaca:
```
Bob: "Sally'nin şifresini değiştireyim."

passwd:
"Dosyaya root olarak erişebilirim ama
senin gerçekten Bob olduğunu RUID'den biliyorum.
Sally'nin şifresini değiştirmene izin vermiyorum."
```

Gerçek root kullanıcısı çalıştırırsa:
```
RUID = 0
EUID = 0
```
olduğu için `passwd sally` yapabilir.

Burada önemli ayrım: Linux'un dosya izinleri EUID üzerinden kontrol edilir; Bob'un hangi hesabın şifresini değiştirebileceği gibi ek kısıtlamaları ise `passwd` programının kendisi uygulayabilir.

**7. Saved UID (SUID / Saved User ID) nedir?**

Buradaki isim biraz kafa karıştırıcı çünkü SUID permission ile saved UID aynı şey değil.

Saved UID'nin amacı process'in gerektiğinde yüksek yetkiyi bırakıp daha sonra tekrar geri alabilmesini sağlamaktır.

Örneğin `passwd` gibi bir process düşün:
```
RUID = 500 → Bob
EUID = 0   → şu anda root
Saved UID = 0 → root yetkisini sakla
```

Program her işlemi root olarak yapmak istemeyebilir. Sadece `/etc/shadow` erişimi gerektiğinde:
```
EUID = 0
→ root yetkisi kullan
```

Normal bir işlem yaparken:
```
EUID = 500
→ Bob'un yetkilerine dön
```

Tekrar root gerektiğinde saved UID sayesinde:
```
EUID = 0
→ root yetkisine geri dön
```

Bu güvenlik açısından önemlidir. **Mantık:** "Root yetkim var ama ihtiyacım olmadığı zaman kullanmayayım."

**Üçünü yan yana koyarsak:**

| UID | Anlamı | Sorduğu soru |
|---|---|---|
| Real UID (RUID) | Process'i başlatan kullanıcı | Kim başlattı? |
| Effective UID (EUID) | Process'in aktif yetkisi | Kimin yetkisini kullanıyorum? |
| Saved UID | Sonradan geri dönülebilecek UID | Hangi yetkiyi sakladım? |

**Normal program** — Bob `touch` çalıştırıyor:
```
RUID  = 500 (Bob)
EUID  = 500 (Bob)
Saved = 500
```
Her şey Bob olarak çalışıyor.

**SUID program** — Bob SUID-root bir program çalıştırıyor:
```
RUID  = 500 (Bob)   → Kim başlattı?
EUID  = 0   (root)  → Şu an hangi yetki?
Saved = 0   (root)  → Gerektiğinde hangi yetkiye dönebilirim?
```

> **Notlarına yazmalık özet:**
> Process Permissions: Linux her process için farklı UID'ler tutar. Real UID (RUID) process'i gerçekten kimin başlattığını, Effective UID (EUID) process'in şu anda hangi kullanıcının yetkilerini kullandığını, Saved UID ise process'in gerektiğinde geri dönebileceği yetkili UID'yi tutar. Normalde RUID ve EUID aynıdır; SUID programlarda farklı olabilir.
> Örnek: Bob (UID 500) SUID'li `passwd` programını çalıştırırsa RUID=500 kalırken EUID=0 (root) olabilir. Böylece `passwd` `/etc/shadow`'a erişebilir, ancak program hâlâ işlemi Bob'un başlattığını bilir.

---

## Sticky Bit

Sticky Bit, özellikle birden fazla kullanıcının yazma iznine sahip olduğu ortak klasörleri korumak için kullanılan özel bir izindir.

Normalde bir klasörde herkesin write izni varsa, kullanıcılar birbirlerinin dosyalarını silebilir veya yeniden adlandırabilir. Sticky Bit bunu engeller.

Sticky Bit aktif olduğunda bir dosyayı sadece:
- Dosyanın sahibi
- Klasörün sahibi
- root

silebilir veya yeniden adlandırabilir.

Örneğin `/tmp`:
```
drwxrwxrwt /tmp
         ↑
         t = Sticky Bit
```
Herkes `/tmp` içinde dosya oluşturabilir, ancak Ali, Mehmet'in dosyasını silemez.

**Sticky Bit ekleme:**
```bash
chmod +t klasor
chmod 1777 klasor   # numeric olarak, burada 1 = Sticky Bit
```

Kısaca: **Sticky Bit = "Ortak klasörü herkes kullanabilir ama herkes sadece kendi dosyasını yönetebilir."**

---

# Services (systemd / systemctl)

## Checking the Status of Services

**Önce service nedir?**

Service, arka planda çalışan ve sisteme bir hizmet sağlayan programdır. Örneğin:
- `nginx` → web server
- `ssh` → uzaktan bağlantı servisi
- `mysql` → database servisi

Linux'ta `systemd` bu servisleri yönetir. Biz de `systemctl` komutuyla systemd'ye ne yapacağını söyleriz.

### 1. `systemctl status` — Genel duruma bak

```bash
systemctl status nginx.service
```

```
Loaded: loaded (...; enabled)
Active: active (running)
Main PID: 495
```

- **Loaded** → Servis sisteme yüklenmiş/tanınmış mı?
- **enabled** → Bilgisayar açıldığında otomatik başlatılacak mı?
- **Active: active (running)** → Servis şu anda çalışıyor mu?
- **Main PID** → Servisin ana process'inin ID'si.

Alttaki satırlar ise servisin son loglarını gösterir. Bir hata varsa buraya bakmak faydalıdır.

### 2. `systemctl is-active` — Şu anda çalışıyor mu?

```bash
systemctl is-active nginx
```
Sonuç: `active` veya `inactive`.

`is-active` = Şu anda çalışıyor musun?

### 3. `systemctl is-enabled` — Açılışta otomatik başlayacak mı?

```bash
systemctl is-enabled nginx
```
Sonuç: `enabled` veya `disabled`.

Burada önemli bir ayrım var: **active ≠ enabled**. Bir servis şu anda çalışıyor olabilir ama bilgisayar yeniden başlatıldığında otomatik başlamayabilir.

| Durum | Anlamı |
|---|---|
| active + enabled | Şu anda çalışıyor ve açılışta otomatik başlayacak. |
| active + disabled | Şu anda çalışıyor ama restart sonrası otomatik başlamayacak. |
| inactive + enabled | Şu anda çalışmıyor ama sonraki açılışta başlatılması ayarlanmış. |

### 4. `systemctl is-failed` — Servis hata vermiş mi?

```bash
systemctl is-failed nginx
```
Servis başlatılırken çökmüşse `failed` görebilirsin.

`is-failed` = Servis çalışırken/başlatılırken problem oluşmuş mu?

### Gerçek bir senaryo

Bir web sitesine erişilemiyor ve Nginx'ten şüpheleniyorsun.

```bash
systemctl status nginx
```
Bakıyorsun: `Active: inactive`. Demek ki Nginx çalışmıyor.

```bash
sudo systemctl start nginx
systemctl is-active nginx
# active
```

Ayrıca bilgisayar yeniden başladığında Nginx'in otomatik başlamasını istiyorsan:
```bash
sudo systemctl enable nginx
systemctl is-enabled nginx
# enabled
```

**Bilmen gereken kısa özet:**
- `systemctl status nginx` → Servis hakkında genel detaylı bilgi
- `systemctl is-active nginx` → Şu anda çalışıyor mu?
- `systemctl is-enabled nginx` → Bilgisayar açılınca otomatik başlayacak mı?
- `systemctl is-failed nginx` → Servis hata durumunda mı?

> En önemli ayrım active vs enabled: Active = şu an çalışıyor, Enabled = sistem açılışında otomatik başlatılacak.

---

## Reading `systemctl status` Output in Detail

Bu kısım aslında öncekinin devamı. Burada amaç `systemctl status` çıktısını okuyabilmek.

```bash
sudo systemctl status httpd
```

Apache web server'ın durumunu gösterir. Çıktıda önemli yerler şunlar:

```
httpd.service - The Apache HTTP Server

Loaded: loaded (...; enabled)
Active: active (running) since ...
Process: 12345 ExecStart=... (status=0/SUCCESS)
Main PID: 12346 (httpd)
Status: "Running, listening on ports 80 and 443."
CGroup: ...
```

**1. Loaded**
```
Loaded: loaded (...; enabled)
```
Servisin systemd tarafından tanındığını gösterir. Buradaki `enabled` ise: sistem açıldığında servis otomatik başlatılacak. `disabled` olsaydı otomatik başlamazdı.

**2. Active ⭐**

İlk bakacağın yerlerden biri:
```
Active: active (running)
```
→ Servis şu anda çalışıyor.

Başka sonuçlar da görebilirsin:
```
active (running) → çalışıyor ✅
inactive (dead)  → çalışmıyor
failed           → hata vererek durmuş ❌
```
Ayrıca ne zamandır çalıştığını da gösterir: `since Wed ...; 1min 23s ago`

**3. Process**
```
Process: 12345 ExecStart=/usr/sbin/httpd ... (status=0/SUCCESS)
```
Servisi başlatmak için hangi komutun çalıştırıldığını ve sonucunu gösterir. `status=0/SUCCESS` → Başlatma işlemi başarılı. Linux'ta genel olarak exit code 0 = başarı anlamına gelir.

**4. Main PID**
```
Main PID: 12346 (httpd)
```
Servisin ana process'inin Process ID'si.
```
Apache çalışıyor
      ↓
Process ID = 12346
```
`ps` gibi komutlarla bu process'i ayrıca görebilirsin.

**5. Status**
```
Status: "Running, listening on ports 80 and 443."
```
Servisin kendi verdiği ek durum bilgisidir. Burada Apache: "Çalışıyorum ve 80 ile 443 portlarını dinliyorum." diyor.

**6. CGroup**
```
CGroup: /system.slice/httpd.service
 ├─12346 httpd
 ├─12347 httpd
 ├─12348 httpd
```
Bu servise ait process'leri gösterir. Bir servisin tek bir process'ten oluşması gerekmez. Apache örneğinde bir ana process ve birden fazla worker process olabilir.

Çok detayına girmen gerekmiyorsa: **CGroup = servise ait process'lerin grubu** diye bilmen yeterli.

**7. En alttaki loglar ⭐**
```
Starting The Apache HTTP Server...
...
Started The Apache HTTP Server.
```
Servisin yakın zamanda ne yaptığını gösterir. Özellikle servis çalışmıyorsa burası çok önemlidir:
```
Active: failed
```
gördüğünde aşağıdaki loglarda neden başarısız olduğunu bulabilirsin. Örneğin:
```
Failed to start...
Address already in use
```
→ Kullanmak istediği port başka program tarafından kullanılıyor olabilir.

**Sınav/not için bilmen gerekenler:**

| Alan | Anlamı |
|---|---|
| Loaded | Servis systemd tarafından tanınmış mı, enabled mı? |
| Active | Servis şu anda çalışıyor mu? ⭐ |
| Process | Başlatma komutu ve sonucu |
| Main PID | Ana process'in ID'si |
| Status | Servisin kendi durum açıklaması |
| CGroup | Servise bağlı process'ler |
| Logs | Son olaylar ve hata mesajları ⭐ |

> En önemli mantık: Bir servisle problem olduğunda `systemctl status servis` çalıştır → önce `Active` durumuna bak → sorun varsa alttaki logları kontrol et.

---

## `sudo -l`

```bash
sudo -l
```
Kullanıcıya verilen sudo yetkilerini gösterir.

`(ALL : ALL) ALL` — kullanıcının herhangi bir kullanıcı/grup kimliğiyle tüm komutları çalıştırabileceği anlamına gelir. Güvenli sistemlerde bunun yerine yalnızca gerekli komutlara izin verilmesi tercih edilir.
