# info
Research on methods of unambiguous forms of information delivery

# Git Worktree Layout for Source and Published Site

The project uses two Git worktrees:

```text
myproject/
├── .repo/        # shared bare Git repository
├── workspace/    # main branch: Sphinx sources
└── site/         # publishing branch: generated HTML
```

The purpose of this arrangement is to keep the project directory tidy while maintaining a strict separation between source files and generated publication files.

## Initial setup

Create the project directory:

```bash
mkdir myproject
cd myproject
```

Clone the GitHub repository as a bare repository:

```bash
git clone --bare git@github.com:USER/REPOSITORY.git .repo
```

Create the source worktree from `main`:

```bash
git --git-dir=.repo worktree add workspace main
```

Create an empty orphan `publishing` branch and its worktree:

```bash
git --git-dir=.repo worktree add --orphan -b publishing site
```

The resulting structure is:

```text
myproject/
├── .repo/
├── workspace/
└── site/
```

## Normal source workflow

Work inside `workspace/`:

```bash
cd workspace
```

Edit the Sphinx sources, then commit and push normally:

```bash
git add -A
git commit -m "Update articles"
git push
```

`workspace/` is checked out on the `main` branch.

## Building the site

Generate the Sphinx HTML output directly into the `site/` worktree.

For example, from `workspace/`:

```bash
sphinx-build -b html . ../site
```

Adjust the source path if the Sphinx source files are stored in a subdirectory.

Conceptually:

```text
workspace/                    site/
   main                     publishing
     │                          ▲
     │      sphinx-build        │
     └──────────────────────────┘
```

## Publishing

After generating the HTML:

```bash
cd ../site

git add -A
git commit -m "Publish site"
git push -u origin publishing
```

The `-u` option is required only on the first push. Subsequent publications can use:

```bash
git push
```

Configure GitHub Pages to publish from the root of the `publishing` branch.

## Important points

* `main` contains the Sphinx source material.
* `publishing` contains only generated website files.
* Do **not** merge `main` into `publishing`.
* The two branches have independent purposes and may have independent histories.
* `myproject/` itself is not a worktree. It is only a container for `.repo/`, `workspace/`, and `site/`.
* Commands using `--git-dir=.repo` are normally needed only when operating from `myproject/`.
* Inside `workspace/` or `site/`, ordinary Git commands work normally.
* Use `git add -A` when publishing so that deleted generated pages are also removed from the `publishing` branch.

## Day-to-day workflow

```text
1. cd myproject/workspace
2. Edit source material.
3. Commit and push changes to main.
4. Build Sphinx HTML into ../site.
5. cd ../site
6. Commit generated changes.
7. Push publishing.
```

In short:

```text
edit source
    ↓
commit main
    ↓
build
    ↓
commit publishing
    ↓
publish
```
