# Git & GitHub Notes

## Part 1: Git

### Version Control System (VCS)
A VCS tracks the history of changes as people and teams collaborate on a project together.

Developers can review a project's history to find out:
- **What** changes were made?
- **Who** made the changes?
- **When** were the changes made?
- **Why** were the changes needed?

VCSs give each contributor a unified and consistent view of a project, surfacing work that's already in progress. This helps team members stay aligned while working independently.

### Distributed Version Control (DVCS)
In a **distributed** version control system, every developer has a full copy of the project and its entire history.

Unlike centralized version control systems, DVCSs don't need a constant connection to a central repository.

### Git — the most popular DVCS
Git is the most widely used distributed version control system. Key benefits:

- **Full project history in one place** — Git lets developers see the entire timeline of changes, decisions, and progression of a project. From the moment they access the project's history, a developer has all the context needed to understand it and start contributing.
- **Asynchronous collaboration** — Developers work across every time zone. With a DVCS like Git, collaboration can happen at any time while maintaining source code integrity. Using branches, developers can safely propose changes to production code without affecting it directly.
- **Better cross-team collaboration** — Businesses using Git can break down communication barriers between teams and keep everyone focused on doing their best work. Git also makes it possible to align experts across a business to collaborate on major projects.

---

## Part 2: Core Git Commands

### `git init`
Initializes a brand new Git repository in the current directory. It creates a hidden `.git` folder that holds all the internal data Git needs — commit history, branches, settings, staging area. Nothing about your actual files changes; Git just starts tracking that directory.

```bash
mkdir project
cd project
git init
```

Used when starting a project from scratch, or when you have an existing folder of code that isn't tracked by Git yet. You only run it once.

### `git clone`
Downloads a full copy of a remote repository (GitHub, GitLab, etc.) to your machine — including all its files, history, and branches. It's effectively `git init` + connecting to the remote + downloading everything, in one command.

```bash
git clone https://github.com/owner/repo.git
cd repo
```

### `git add`
Stages a change. Git tracks changes to your files, but you have to explicitly stage them before they become part of the project's history. Anything staged with `git add` will be included in the next commit.

```bash
git add file1.md file2.md
git add .          # stage everything that changed
```

Staging and committing as two separate steps gives full control over exactly what goes into each snapshot.

### `git commit`
Saves the staged snapshot to the project's permanent history. Think of it like taking a photo: whatever was staged with `git add` becomes part of that photo.

```bash
git commit -m "add login form"
```

### `git status`
Shows the current state of your working directory — which files are untracked, modified, or staged. Safe to run anytime, has no side effects.

```bash
git status
```

### `git branch`
Lists local branches. If given a name, it creates a new branch (without switching to it).

```bash
git branch                # list branches
git branch new-feature    # create a branch
git checkout new-feature  # switch to it
git checkout -b new-feature  # create + switch in one command
```

Branches are independent, parallel lines of development off the main code (usually `main`). They let you experiment or build a feature without touching the working version. Each branch has its own commit history.

### `git merge`
Combines the history of two branches — typically used to bring a finished feature branch back into `main`. Git finds the common ancestor of both branches and merges the differences. If there's no conflict, it creates an automatic "merge commit."

```bash
git checkout main
git merge new-feature
```

If the same lines were changed differently in both branches, Git can't resolve it automatically — this is a **merge conflict**, and it has to be fixed by hand.

### `git pull`
Really two commands combined: `git fetch` (download new commits from the remote) + `git merge` (integrate them into your local branch).

```bash
git pull origin main
```

Used to catch up when a teammate has pushed new commits — keeps your local copy in sync before you keep working.

### `git push`
Sends your local commits to the remote repository (e.g. GitHub), updating it with your changes.

```bash
git push origin main
```

Commits only exist on your machine until you push them — nobody else can see them before that.

---

## Part 3: Typical Daily Workflow

```bash
git clone https://github.com/owner/repo.git   # get the project
cd repo
git branch                                    # check current branch
git checkout -b login-form                    # create + switch to a new branch
# ... write code ...
git status                                    # see what changed
git add .                                     # stage changes
git commit -m "add login form"                # save snapshot
git checkout main
git pull origin main                          # make sure main is up to date
git merge login-form                          # bring the feature into main
git push origin main                          # publish to GitHub
```

The core loop: **branch → change → stage → commit → merge → push.**

---

## Part 4: GitHub — Pull Requests

A pull request (PR) is how changes on a branch get proposed, reviewed, and merged into `main` — instead of merging locally and pushing directly.

1. Push your branch to GitHub first: `git push --set-upstream origin my-branch` (the `--set-upstream` part tells Git to link this local branch to a new branch on GitHub; after that, plain `git push` is enough on that branch).
2. On GitHub, go to the **Pull requests** tab → **New pull request**.
3. On the "Compare changes" page, set the **base** branch (usually `main`, the target) and the **compare** branch (your feature branch).
4. Review the diff — green lines are additions, red lines are deletions.
5. Click **Create pull request**, add a title and description.
6. Once reviewed (by yourself or teammates), merge it from the GitHub UI, or continue merging locally with `git merge`.

---

## Part 5: Secure Repo Hygiene

Two habits to set up **before** adding real files to a repo:

**`.gitignore`** — tells Git which files/folders to never track (so they never get committed, even accidentally):

```
venv/
.env
__pycache__/
*.pyc
.DS_Store
```

**`.env.example`** — a safe, empty template showing which environment variables the project needs, without real values:

```
API_KEY=
DATABASE_URL=
SECRET_TOKEN=
```

**Rule:** never commit real tokens, API keys, company data, or internal hostnames to a repo — public or private.

If a secret gets committed by accident:
```bash
git rm --cached .env
# add .env to .gitignore if not already there
git commit -m "remove accidentally committed .env"
```

---

## Part 6: Troubleshooting Notes

- **`Permission denied (publickey)`** → set up an SSH key, or use HTTPS with a personal access token instead.
- **Push rejected (non-fast-forward)** → someone else pushed first; run `git pull` (or `git pull --rebase`) to catch up, then push again.
- **Git asks for identity** → set it once with `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`.
