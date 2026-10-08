import os
import subprocess
import sys
import webbrowser


def main() -> int:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(base_dir, "index.html")

    if not os.path.exists(index_path):
        print(f"Report not found: {index_path}", file=sys.stderr)
        return 1

    url = "file://" + index_path.replace("\\", "/")
    webbrowser.open(url, new=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
