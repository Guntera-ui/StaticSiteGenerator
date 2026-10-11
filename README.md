# Static Site Generator

A simple static site generator built with Python as part of the [Boot.dev](https://www.boot.dev/) curriculum.

It converts Markdown files into HTML pages using a shared template and supports multiple pages, nested directories, images, and CSS.

## Features

- Converts Markdown into HTML
- Supports headings, links, images, lists, and text formatting
- Recursively generates pages from the `content/` directory
- Copies static assets such as images and CSS
- Supports configurable base paths for deployment
- Deploys to GitHub Pages

## Getting Started

**Requirements:** Python 3

Clone the repository:

```bash
git clone https://github.com/Guntera-ui/StaticSiteGenerator.git
cd StaticSiteGenerator
```

Run the website locally:

```bash
./main.sh
```

Open `http://localhost:8888/` in your browser.

## Creating New Pages

Add a Markdown file under `content/`:

```text
content/
└── blog/
    └── new-post/
        └── index.md
```

Run `./main.sh` to generate the corresponding HTML page.

## Building for Production

```bash
./build.sh
```

This generates the website in the `docs/` directory with the correct base path for GitHub Pages.

## Tests

```bash
./test.sh
```

## Live Website

[View the website](https://guntera-ui.github.io/StaticSiteGenerator/)

## Technologies

- Python
- Markdown
- HTML & CSS
- GitHub Pages

## Acknowledgments

Built as part of the [Boot.dev](https://www.boot.dev/) Backend Developer curriculum.
