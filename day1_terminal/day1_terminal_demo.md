# Day 1: Terminal Basics — Instructor Demo Script

**Companion to [day1_terminal.md](day1_terminal.md).** That file is the outline of *what* we cover; this file is the crib sheet for *what to type live*, in order, with talking points, the mistakes students reliably make, and rough timings.

This is a teaching script, not a student handout. Students who want a reference should keep `day1_terminal.md` open.

**Total class time: 120 min (9–11 AM).** Timings below sum to ~115 min, leaving no slack — see [Pacing and what to cut](#pacing-and-what-to-cut) before you start. Remember the course promise: *we move at the pace of the student who finishes last.* Friday 09/11 is a buffer day, so it is fine to end the day mid-section 6.

---

## Pre-class checklist

- [ ] Projector mirrored, terminal font bumped to ~18–20 pt (Terminal → Settings → Profiles → Font, or `Cmd +` a few times).
- [ ] Your demo shell starts in a **clean, empty** directory — not your real home directory. Students copy what they see, and they should not see your grant drafts.
  ```bash
  mkdir -p ~/day1_demo && cd ~/day1_demo
  ```
- [ ] Reset your prompt to something short so the projected line does not wrap. In zsh:
  ```bash
  PS1='%1~ %# '
  ```
  In bash: `PS1='\W \$ '`
- [ ] Turn off any shell theme that auto-suggests or colorizes heavily — it confuses students about what they actually typed.
- [ ] Know who is on Windows. If anyone is, decide now: WSL, Git Bash, or pair them with a neighbor. Do not discover this at minute 40.
- [ ] Have the CoreHPC bastion hostname on the board for section 7.

---

## 0. Course intro (~10 min)

Keep it short — the point of today is hands on keyboards.

- One slide of the schedule from [README.md](../README.md): 3 days of terminal/onboarding, 4 days of Python, 1 day of data science.
- The framing that makes this course work: **you already understand algorithms.** The genetic code is a dictionary. Transcription is a for loop. The hard part is not the concept, it is the syntax that a computer will accept. Say this out loud today, and again on Day 2 when you introduce loops.
- Ground rules: no grades, interrupt constantly, and if your screen does not look like mine, say so immediately rather than falling behind silently.
- The AI point (from the syllabus): LLMs will write most of this code for you. That is exactly why you need to be able to read it and tell when it is wrong.

**Talking point that lands:** ask how many people have used the Finder or a file explorer to move a file. Everyone. Then: "the terminal is the same filesystem, same files, same folders — just a different window onto it. Nothing you learn today is a separate world."

---

## 1. Introduction to the Terminal (~10 min)

### Open it together

- **macOS:** `Cmd + Space`, type "Terminal", Enter. (Mention iTerm2 exists; do not install it today.)
- **Linux:** `Ctrl + Alt + T` on most desktops, or search "Terminal".
- Have everyone confirm they see a prompt and a cursor before you type anything else.

### Talking points

- Point at the prompt and name its parts: `username@hostname current_directory %`. The prompt is the shell telling you *who* you are and *where* you are.
- **The `%` vs `$` gotcha — address it now, unprompted.** macOS defaults to `zsh` (prompt ends in `%`); most Linux machines and CoreHPC default to `bash` (prompt ends in `$`). Everything today works identically in both.
  ```bash
  echo $SHELL
  ```
  Expected: `/bin/zsh` on a modern Mac, `/bin/bash` on CoreHPC.
- Tell them **never to type the `$` or `%`** they see in tutorials. This is the single most common copy-paste error for the rest of the week.

### Basic command syntax

Write the shape on the board and leave it there all day:

```
command  --option  argument
```

Type these, in this order, and narrate that each one is the same shape:

```bash
ls
ls -l
ls -l -a
ls -la
```

Then the outline's example, so they see the shape on a command that does real work:

```bash
cp -r old_folder new_folder
```

**What to point out:**
- `ls` alone is a bare command. `-l` is an option (a.k.a. flag) that changes *how* it behaves. `old_folder` and `new_folder` are arguments — *what* it acts on.
- Single-dash short flags can be stacked: `-la` is `-l -a`. Double-dash flags are long names, `--all`, and cannot be stacked.
- Order of options usually does not matter; order of arguments almost always does. `cp A B` is very different from `cp B A`.

### The two lifesavers

Demo both, deliberately and slowly, because students will need them 200 times this week:

```bash
man ls
```
Point out: arrow keys or space to scroll, `/` to search, **`q` to quit**. Someone will get stuck in `man` today; pre-empt it. (On CoreHPC, `ls --help` is often faster.)

```bash
Control + c
```
Type an unfinished command like `ls -l "` and press Enter so the shell hangs waiting for a closing quote, then `Ctrl + c` out of it. Frame it: **`Ctrl + c` is your emergency exit.** Then note the two lookalikes so they do not conflate them: `Ctrl + c` cancels, `Ctrl + d` says "no more input", `Ctrl + z` suspends (and needs `fg` to resume).

**Common student mistakes:**
- Typing the prompt character along with the command.
- Assuming the terminal is frozen when a command produced no output. Say it explicitly: **silence means success.** Unix commands that work usually say nothing.
- Using the mouse to move the cursor within a line. Show `Ctrl + a` (start of line), `Ctrl + e` (end), and the up-arrow for history.

---

## 2. Navigating the File System (~20 min)

This is the section to slow down on. Everything else today depends on students having a mental model of *where they are*.

### pwd

```bash
pwd
```
Expected: `/Users/jdoe/day1_demo` on macOS, `/home/jdoe/day1_demo` on Linux.

**Talking point:** "Where am I?" The terminal has exactly one current directory at a time, and every relative command you type is interpreted from there. Note that macOS uses `/Users`, Linux uses `/home` — same idea, different name.

### ls

```bash
ls
ls -l
ls -lh
ls -a
ls -lt
```

**What to point out:**
- `-l` = long format. Walk the columns once, briefly: permissions, links, owner, group, size, date, name. Promise them the permission column comes back in section 6 when we `chmod` a script.
- `-h` = human-readable sizes. `4096` becomes `4.0K`. Only meaningful with `-l`.
- `-a` = all, including dotfiles. Reveal that `.` and `..` are real entries, and that files starting with `.` are hidden by convention, not by magic. Mention `.DS_Store` — every Mac user in the room has thousands and has never seen one.
- `-t` = sort by time, newest first. Add `-r` to reverse. This is the flag they will actually use daily on real data.

Then, so they connect it to the GUI:

```bash
open .          # macOS — opens the current directory in Finder
```
(`xdg-open .` on Linux.) **Do this.** Watching the Finder window open on the exact directory their prompt names is the moment the terminal stops feeling like a separate universe.

### cd

```bash
cd ~
pwd
cd Documents
pwd
cd ..
pwd
cd -
pwd
cd
pwd
```

**What to point out:**
- `~` is shorthand for your home directory. `cd` with no argument goes home too.
- `..` is the parent directory. `.` is the current directory — useless-looking now, essential in section 6 when we run `./hello.sh`.
- `cd -` jumps back to the previous directory. Cheap trick, huge quality-of-life win.
- **Teach tab completion here, not later.** Type `cd Doc` and hit Tab. Then type `cd D` and hit Tab twice to show the list of candidates. Tell them: if Tab does not complete, the thing you are typing does not exist — Tab is a spell-checker for filenames.

### mkdir

```bash
mkdir practice
cd practice
mkdir -p analysis/round1/plots
ls
ls analysis
```

**What to point out:**
- Plain `mkdir a/b/c` fails if `a` does not exist yet; `-p` creates the whole chain and does not complain if it already exists.
- `-p` is what you will use in scripts, because it is safe to re-run.

### Relative vs absolute paths

The conceptual core of the section. Run the outline's examples for real:

```bash
cd ~/day1_demo/practice
ls analysis            # relative — "analysis, starting from here"
ls ./analysis          # identical; the ./ is explicit but optional
ls ~/day1_demo/practice/analysis   # ~ expands to your home
ls /Users/jdoe/day1_demo/practice/analysis   # absolute — works from anywhere
```

Then prove the difference instead of asserting it:

```bash
cd /
ls analysis                                   # fails — no such directory here
ls /Users/jdoe/day1_demo/practice/analysis    # works
cd ~/day1_demo/practice
```

**Talking point:** an absolute path starts with `/` and is unambiguous from anywhere on the machine — it is a street address. A relative path is directions from where you are standing. Both are correct; absolute paths are what you want in scripts and in emails to your PI, relative paths are what you want while working.

**Common student mistakes:**
- Typing a path with a space in it: `cd My Folder` fails because the shell sees two arguments. Show both fixes: `cd "My Folder"` and `cd My\ Folder`. Then advise: **never put spaces in filenames you will touch from the terminal.** Use `_` or `-`. This advice will save them hours in Python later.
- Case. `cd documents` fails when the folder is `Documents`. macOS filesystems are usually case-*insensitive* and Linux/CoreHPC is case-*sensitive*, so code that works on their laptop can break on the cluster. Worth 20 seconds.
- `cd` into a file rather than a directory: `cd notes.txt` → "Not a directory."
- Losing track of location. Prescribe the fix: **when confused, `pwd` then `ls`.** Say it as a mantra.

**Checkpoint (ask the room, wait for everyone):** "Starting from your home directory, get into `analysis/round1/plots` in one command using a relative path. Now get back to home using an absolute path. Now do it again with `cd -`."

---

## 3. File Operations (~20 min)

### touch

```bash
touch notes.txt
ls -l notes.txt
touch notes.txt
ls -l notes.txt
```

**What to point out:** on a file that does not exist, `touch` creates it empty (size `0`). On a file that does exist, it does *not* wipe it — it just updates the timestamp. That is actually its original purpose; creating empty files is the side effect we exploit.

Give yourself something to read in the next demo:

```bash
printf 'line one\nline two\nline three\nline four\nline five\n' > notes.txt
```
(Do not explain `>` yet — say "we will unpack this arrow in section 5" and move on. Foreshadowing is fine; detouring is not.)

### cat, head, tail

```bash
cat notes.txt
head notes.txt
tail notes.txt
head -n 2 notes.txt
tail -n 1 notes.txt
```

**What to point out:**
- `cat` dumps the whole file to the screen. Fine for 5 lines. Ask what happens with a 40 GB FASTQ file — then tell them: you will fill your scrollback and wish you had not. This is *why* `head` and `tail` exist.
- `head`/`tail` default to 10 lines; `-n` sets the count.
- `tail -f logfile` follows a file as it grows. Show it only if the room is ahead of schedule — it is the right tool for watching a cluster job's output on Day 0's material, but it needs `Ctrl + c` to escape and that costs time.
- For long files, `less notes.txt` is the humane option: same navigation as `man`, `q` to quit.

**Common student mistakes:**
- `cat` on a binary file, which garbles the terminal. If it happens, the fix is `reset` (or close the tab). Worth mentioning so nobody panics.
- Reading `-n 20` as "twenty files."

### cp, mv, rm

```bash
cp notes.txt notes_backup.txt
ls

mv notes_backup.txt notes_old.txt      # same directory = rename
ls

mkdir archive
mv notes_old.txt archive/              # different directory = move
ls
ls archive

cp -r archive archive_copy             # -r for directories
ls

rm notes.txt
ls

rm -r archive_copy
ls
```

**What to point out:**
- `mv` is both "move" and "rename" — there is no separate rename command, because renaming *is* moving within a directory. Students find this genuinely surprising.
- `cp` and `rm` need `-r` (recursive) to handle directories. Without it: "omitting directory" / "is a directory."
- **The `rm` talk. Do not skip it, do not rush it.** There is no Trash. There is no undo. `rm` unlinks the file and it is gone.
  - Prescribe `rm -i` (prompts per file) while they are learning: `rm -i notes_old.txt`.
  - Show `ls` *before* `rm` as a habit: look at what the pattern matches before you delete it.
  - Name the two catastrophes explicitly so they recognize them: `rm -rf *` in the wrong directory, and the space typo in `rm -rf ~ /old_stuff`, which deletes your home directory instead of `~/old_stuff`.
  - **Do not** live-demo a destructive `rm -rf` "as a joke." Someone will remember the keystrokes and not the punchline.
- Overwriting is silent: `cp a.txt b.txt` destroys the old `b.txt` without asking. `cp -i` prompts.

**Checkpoint:** "Make a file, copy it, rename the copy, move it into a new folder, then delete the folder and its contents. Use `ls` after every step."

---

## 4. Text Editing (~20 min)

### Framing (30 seconds, but say it)

You need to edit text on a machine with no GUI — a cluster node, a server over SSH. That is the entire reason terminal editors exist. On your laptop you will use VSCode; on CoreHPC you will use one of these.

### vim (~8 min)

Teach vim primarily so that **nobody is ever trapped in it.** Assume they will meet it by accident, because `git` and other tools open it by default.

```bash
vim scratch.txt
```

Then, narrating every keystroke because there is no visual feedback:

1. You are in **normal mode**. Keys are commands, not text. Typing `dd` here deletes a line — it does not type "dd".
2. Press `i` → **insert mode**. Note `-- INSERT --` at the bottom. Now type: `hello from vim`.
3. Press `ESC` → back to normal mode. The indicator disappears.
4. `:w` + Enter — write (save). Point at the confirmation line.
5. `:q` + Enter — quit.
6. Reopen, change something, and demo `:wq` (write and quit) and `:q!` (quit, discarding changes).

**What to point out:**
- The mode concept is the whole ballgame. Every vim horror story is someone typing in normal mode.
- **`ESC` then `:q!` is the universal escape hatch.** Have the whole room do it together twice. This is the most valuable 60 seconds of the section.
- `!` means "force, I know what I am doing." It appears again in `rm -f` and `git push --force`. Same energy, same danger.
- Navigation in normal mode: arrow keys work fine. `h j k l` exist and you can mention them, but do not drill them today.

**Common student mistakes:**
- Typing `:wq` while still in insert mode, which literally inserts the text `:wq`. Do this on purpose, show the mess, then `ESC` and fix it.
- Trying to save with `Cmd + S`.
- Discovering vim through `git commit` next week with no idea what happened. Naming this now pays off later.

### nano (~8 min)

Your stated preference in the outline — so tell them why: the shortcuts are printed at the bottom of the screen, so nano teaches itself.

```bash
nano hello.txt
```

- Type freely — there are no modes. This is the whole advantage.
- Arrow keys move the cursor; `Ctrl + a` / `Ctrl + e` jump to line start/end.
- `Ctrl + O` → **write Out** (save). It prompts for the filename; press Enter to accept.
- `Ctrl + X` → exit. If there are unsaved changes it asks Y/N first.
- `Ctrl + C` inside nano shows the cursor position; it does *not* quit. Flag this — it contradicts the "Ctrl+C cancels" rule they learned in section 1.
- Point at the two-line help menu at the bottom and decode the notation: **`^` means Control.** `^X` is `Ctrl + x`. Students stare at `^X` without realizing it is telling them exactly what to press.

**Checkpoint:** "Create a file in nano, type your name, save it, exit, and prove it worked with `cat`."

```bash
cat hello.txt
```

### If you have a fast room (~2 min)

`echo` writes one line without any editor at all:

```bash
echo "quick note" > quick.txt
cat quick.txt
```
This also sets up section 5 nicely.

---

## 5. Piping and Redirection (~15 min)

**Framing:** every command reads from an input and writes to an output. Normally the output is your screen. Pipes and redirects re-aim it. This is the idea that makes the terminal more powerful than a GUI: small tools, composed.

Draw it on the board:

```
command1  |  command2      # output of 1 becomes input of 2
command   >  file          # output goes into file (overwrite)
command   >> file          # output appends to end of file
```

### Set up something worth filtering

```bash
cd ~/day1_demo
mkdir -p pipes && cd pipes
touch a.txt b.txt c.txt structure1.pdb structure2.pdb structure3.pdb readme.md
ls
```

### Piping

```bash
ls | wc -l
ls | grep "txt"
ls | grep "pdb" | wc -l
```

**What to point out:**
- `wc -l` counts lines. Since `ls` piped into another command prints one name per line, this counts files.
- `grep "pattern"` keeps only matching lines. It is the single most useful command in bioinformatics; they will meet it again constantly.
- Pipes chain arbitrarily. Build the third command up one stage at a time — run `ls`, then `ls | grep "pdb"`, then add `| wc -l` — so they see the stream narrowing at each step.

A second example that shows pipes working on file *contents* rather than filenames:

```bash
cat ../practice/notes.txt | grep "line" | wc -l
```
Then immediately show the better version, because someone will ask:
```bash
grep -c "line" ../practice/notes.txt
```
**Talking point:** pipes are for composing tools, not for showing off. If one command already does the job, use it.

### Redirection

```bash
ls *.pdb > pdb_list.txt
cat pdb_list.txt

readlink -f *.pdb > pdb_list.txt     # the outline's example: full absolute paths
cat pdb_list.txt

echo "# analysis notes" > log.txt
cat log.txt
echo "ran step 1" >> log.txt
echo "ran step 2" >> log.txt
cat log.txt
```

**What to point out:**
- `>` **destroys** the existing contents of the target file, without warning, before the command even runs. Demo it deliberately: `echo "first" > log2.txt`, `cat log2.txt`, `echo "second" > log2.txt`, `cat log2.txt` — "first" is gone.
- `>>` appends. Rule of thumb for their own work: **`>>` for logs, `>` only when you mean to start fresh.**
- `readlink -f` prints absolute paths. (Verified working on current macOS and on Linux. On macOS older than 12.3 the BSD `readlink` has no `-f`; the portable fallback is `ls -d "$PWD"/*.pdb`.) This is genuinely how you build a file list to hand to a batch job or a Python script — connect it forward to `pdb_list.txt` being read line-by-line in Day 2's file handling, and to job submission from Day 0.
- The `*` wildcard: `*.pdb` means "anything ending in .pdb". The **shell** expands it before the command ever sees it. Prove it:
  ```bash
  echo *.pdb
  ```
  Point out that `echo` never knew about files — the shell had already substituted the names. This is why `ls` before `rm *` tells you the truth about what will be deleted.

**Common student mistakes:**
- Redirecting a file into itself: `sort notes.txt > notes.txt` empties it. Mention it; do not demo it on anything they care about.
- Expecting `>` to print to the screen *and* save. It does not. (`tee` does, if someone asks.)
- Confusing `|` with `>`. The mnemonic: pipe goes to a *command*, arrow goes to a *file*.

---

## 6. Scripting Basics (~20 min)

**Framing:** a script is just the commands you already typed today, saved in a file so you can re-run them tomorrow, or 500 times, or on the cluster at 3 AM. Nothing new — the same commands, written down. Also: it is a record of what you actually did, which matters when a reviewer asks how you processed your data.

### Write it

```bash
cd ~/day1_demo
nano hello.sh
```

Type this in, live, explaining line by line:

```bash
#!/bin/bash

# A first script: report where we are and what is here.
echo "Hello, world!"
echo "You are here:"
pwd
echo "This directory contains:"
ls
echo "Done."
```

Save with `Ctrl + O`, Enter; exit with `Ctrl + X`.

**Line-by-line talking points:**
- `#!/bin/bash` — the **shebang**. It tells the system which interpreter runs this file. It must be the very first line, with no blank line above it. On Day 2 the Python equivalent shows up as `#!/usr/bin/env python3`.
- `#` starts a comment. Same as Python's `#`, which is a nice bridge to next class.
- Everything else is exactly what they typed by hand in sections 2–3.

### Make it executable

```bash
ls -l hello.sh
chmod +x hello.sh
ls -l hello.sh
```

**What to point out:** run `ls -l` before and after and have them read the permission column out loud. `-rw-r--r--` becomes `-rwxr-xr-x`. **This is the callback you promised in section 2** — the `x` is the "may be executed" bit, and without it the shell refuses. Do not go deeper into octal permissions today; `chmod +x` is enough. (On macOS you may see a trailing `@`, as in `-rwxr-xr-x@` — that just means the file carries extended attributes. Wave it off; it is not part of today's lesson.)

### Run it

```bash
./hello.sh
```

**What to point out:**
- **The `./` is the part that confuses everyone.** The shell only searches directories on your `PATH` for commands, and the current directory is deliberately not on it (for security). `./hello.sh` says "the `hello.sh` right here." This is where `.` from section 2 finally earns its keep.
- Show the error first if you want it to stick: `hello.sh` → `command not found`. Then `./hello.sh` works.
- The alternative, which skips `chmod` entirely: `bash hello.sh`. Here you are running `bash` and handing it the file as an argument, so the executable bit is irrelevant. Both are correct; `./` is what you will see in documentation.

### Make it slightly real

Show that a script is worth writing when it does something tedious:

```bash
nano count_files.sh
```

```bash
#!/bin/bash

# Count the .pdb files in a directory given as an argument.
echo "Counting .pdb files in: $1"
ls "$1"/*.pdb | wc -l
```

```bash
chmod +x count_files.sh
./count_files.sh pipes
```

**What to point out:** `$1` is the first argument passed to the script — the same "command, option, argument" shape from section 1, now on the receiving end. Quoting `"$1"` protects against spaces in the path. Do not teach loops or `if` in bash; that budget belongs to Python starting tomorrow.

### Interrupting

```bash
nano forever.sh
```

```bash
#!/bin/bash
while true; do
  echo "still running..."
  sleep 1
done
```

```bash
chmod +x forever.sh
./forever.sh
```

Let it scroll for a few seconds, then `Ctrl + c`.

**Talking point:** this closes the loop from section 1. Any runaway command — a script, a Python program with an infinite loop, a `tail -f` — ends with `Ctrl + c`. Also mention `clear` (or `Cmd + K`) to tidy the screen afterward. And to be transparent: yes, that `while` loop is a for-loop-shaped thing in bash, and yes, it is the concept we build the whole Python week on. Do not teach its syntax now.

**Common student mistakes:**
- Naming the script `hello.sh` and then running `hello.sh` without `./`.
- Forgetting `chmod +x` — the error is "permission denied," which sounds like a filesystem problem and is really a missing `x` bit.
- Editing the script and expecting the running one to change.
- Windows line endings, if anyone edited the file in a Windows GUI editor: `bad interpreter: /bin/bash^M`. The fix is `dos2unix hello.sh`. Only mention this if it actually happens.

---

## 7. Connecting to Remote Servers (~5–10 min)

Keep this short — Day 0 covered CoreHPC in depth, and this is a callback, not a re-teach.

### Talking points

- Everything you learned today works unchanged on a machine 30 miles away. That is the payoff: the terminal is location-independent in a way the Finder is not.
- Syntax, in the same command/argument shape:
  ```bash
  ssh username@hostname
  ```
- The real one:
  ```bash
  ssh jdoe@chpc-ucsf-bastion-vm1.corehpc.ucsf.edu
  ```
- Point them to [day0_corehpc.md](../day0_corehpc/day0_corehpc.md#accessing-corehpc) for MFA, VPN requirements, and the details.

### If you demo it live

Log in on the projector and run the exact same three commands from section 2:

```bash
pwd
ls
hostname
```

**Talking point:** `pwd` and `ls` behave identically; only `hostname` and the prompt reveal you are somewhere else. Then `exit` to come back, and note that the prompt is how you tell — students will absolutely run commands on the wrong machine at some point this year.

**Common student mistakes:**
- Typing the literal word `username` or the example `jdoe`.
- Panicking at the first-connection host key prompt. You must type the whole word `yes`, not `y`.
- The password not echoing as you type. Nothing is broken — SSH deliberately prints nothing, not even asterisks. Say this before they ask.

---

## Pacing and what to cut

The timings above total ~115 of 120 minutes with no buffer, and this room will have wildly heterogeneous prior experience. Decide cuts in this order:

**Cut first (lowest cost):**
- Section 6's `count_files.sh` and `forever.sh` — keep `hello.sh` and `Ctrl + c` only.
- The live SSH demo in section 7; talk through the syntax instead.
- `tail -f`, `less`, `tee`, `cd -`.

**Cut second:**
- vim down to the bare minimum: open, `i`, `ESC`, `:wq`, `:q!`. Nothing else.
- The `readlink -f` example in section 5.

**Never cut:**
- Relative vs absolute paths (section 2). Everything downstream depends on it.
- Tab completion (section 2).
- The `rm` safety talk (section 3).
- `ESC` `:q!` to escape vim (section 4).
- `Ctrl + c` (sections 1 and 6).

**If you finish early**, spend the time on the end-of-class items below rather than adding material — getting VSCode and Miniconda installed on 12 laptops always takes longer than you think, and Day 2 assumes both.

---

## End-of-class items

From the outline, as time allows — otherwise these open Day 2:

- Install [VSCode](https://code.visualstudio.com) if it is not already there.
- Sign up for [GitHub](https://github.com) and the [Student Developer Pack](https://education.github.com/pack).
- Miniconda install, if the room is far enough ahead. Budget 15 minutes and expect at least one PATH problem.

**Closing line worth using:** everything today was one machine talking to itself. Tomorrow we start writing programs — and the first one is a Python script you run with exactly the command shape you learned in the first ten minutes: `python greeter.py`.
