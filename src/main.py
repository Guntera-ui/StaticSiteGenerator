
from pathlib import Path
import shutil
import sys

from gencontent import generate_page


ROOT = Path(__file__).resolve().parent.parent


def copy_directory(source, destination):
    if destination.exists():
        shutil.rmtree(destination)

    destination.mkdir(parents=True, exist_ok=True)

    for item in source.iterdir():
        target = destination / item.name

        if item.is_dir():
            copy_directory(item, target)
        else:
            shutil.copy2(item, target)
            print(f"Copied: {item} -> {target}")


def generate_pages_recursive(
    content_dir,
    template_path,
    destination_dir,
    basepath,
):
    for markdown_file in content_dir.rglob("*.md"):
        relative_path = markdown_file.relative_to(content_dir)
        destination = destination_dir / relative_path.with_suffix(".html")

        generate_page(
            markdown_file,
            template_path,
            destination,
            basepath,
        )


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    if not basepath.startswith("/"):
        basepath = "/" + basepath

    if not basepath.endswith("/"):
        basepath += "/"

    static_dir = ROOT / "static"
    docs_dir = ROOT / "docs"
    content_dir = ROOT / "content"
    template_path = ROOT / "template.html"

    if not static_dir.is_dir():
        raise FileNotFoundError(
            f"Static directory not found: {static_dir}"
        )

    print(f"Building site with basepath: {basepath}")

    copy_directory(static_dir, docs_dir)

    generate_pages_recursive(
        content_dir,
        template_path,
        docs_dir,
        basepath,
    )

    print("Site generated successfully!")


if __name__ == "__main__":
    main()

