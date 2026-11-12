"""cutest-picture-01 entry (Python 3.13, stdlib only).

Copies the picture in cute.png beside this file to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
The picture is a 3D-rendered baby otter pup hugging a baby
duckling: huge sparkling eyes, head tilt, tiny pink bow.
This file never edits the picture; it only copies it and checks
the copy matches byte for byte, so the output is deterministic.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "cute.png"
OUT.mkdir(parents=True, exist_ok=True)
if SRC.stat().st_size == 0:
    raise SystemExit("cute.png is empty")
if SRC.read_bytes()[:3] != b"\xff\xd8\xff":
    raise SystemExit("cute.png is not a JPEG image")
dest = OUT / "entry.png"
shutil.copyfile(SRC, dest)
if dest.stat().st_size != SRC.stat().st_size:
    raise SystemExit("entry copy size mismatch")
if dest.read_bytes() != SRC.read_bytes():
    raise SystemExit("entry copy differs from cute.png")
