#!/usr/bin/env python3
"""news-image-20261127: publish the bundled 27 November 2026 news image.

The repository ships entry.png, a 1024x1024 picture that sums up the
world news of Friday 27 November 2026. This program checks the bundled
file (PNG signature, exact dimensions, size limit) and writes those
exact bytes to /output/entry.png, then confirms the copy by comparing
SHA-256 digests. It uses no network, no clock and no randomness, so
every run produces the same output bytes.
"""

import hashlib
import struct
import sys
from pathlib import Path

BUNDLED_NAME = "entry.png"
MAX_BYTES = 1024 * 1024
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
OUTPUT_DIR = Path("/output")
OUTPUT_NAME = "entry.png"

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def png_dimensions(data: bytes) -> tuple:
    """Read width and height from the PNG IHDR chunk."""
    if data[:8] != PNG_SIGNATURE:
        raise ValueError("bundled file is not a PNG image")
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError("bundled PNG has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def load_bundled_image() -> bytes:
    here = Path(__file__).resolve().parent
    path = here / BUNDLED_NAME
    if not path.is_file():
        raise FileNotFoundError(f"bundled image missing: {path}")
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise ValueError(
            f"bundled image is {len(data)} bytes, over the 1 MiB limit"
        )
    width, height = png_dimensions(data)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            f"bundled image is {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )
    return data


def write_output(data: bytes) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / OUTPUT_NAME
    target.write_bytes(data)
    written = target.read_bytes()
    if sha256_hex(written) != sha256_hex(data):
        raise ValueError("output copy failed digest verification")
    return target


def main() -> int:
    try:
        data = load_bundled_image()
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    try:
        target = write_output(data)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(data)} bytes, "
          f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT} PNG)")
    print(f"sha256: {sha256_hex(data)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
