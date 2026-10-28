#!/usr/bin/env python3
"""Erzeugt einen URL-encoded nbgitpuller-Link für den JupyterHub.

Aufruf:
    python3 nbgitpuller_link.py <repo-url> [pfad/zum/notebook.ipynb] [hub-url]

Beispiel:
    python3 nbgitpuller_link.py https://github.com/nsteudtner/biw3-10-uebung03.git
    python3 nbgitpuller_link.py https://github.com/nsteudtner/biw3-10-uebung03.git InstationaereBehaelterleerung_Nummerik.ipynb
    python3 nbgitpuller_link.py https://gitlab.hrz.tu-chemnitz.de/nick/biw3-10-uebung03.git "" https://jupyterhub.hpc.tu-dresden.de
"""
import sys
from urllib.parse import quote

HUB_DEFAULT = "https://jupyterhub.hpc.tu-dresden.de"
BRANCH = "main"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    repo = sys.argv[1].rstrip("/")
    notebook = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else ""
    hub = (sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else HUB_DEFAULT).rstrip("/")

    urlpath = f"tree/{notebook}" if notebook else "tree"
    link = (
        f"{hub}/hub/user-redirect/git-pull"
        f"?repo={quote(repo, safe='')}"
        f"&branch={quote(BRANCH, safe='')}"
        f"&urlpath={quote(urlpath, safe='')}"
    )
    print(link)


if __name__ == "__main__":
    main()
