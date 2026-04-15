# randhasher

[![Python package](https://github.com/mhamzaib/libplayground-randhasher/actions/workflows/python-package.yml/badge.svg)](https://github.com/mhamzaib/libplayground-randhasher/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**randhasher** is a Python utility designed for developers and security researchers who need to quickly audit or compare string transformations across multiple hashing algorithms. 

Instead of writing boilerplate loops around `hashlib`, **randhasher** performs the heavy lifting and returns structured data via Pandas DataFrames. It is built to be extensible, supporting everything from standard SHA-256 to variable-length SHAKE digests and legacy algorithms.

## Why use this?
* **Quick Audits:** Instantly see how different algorithms (SHA-2, SHA-3, BLAKE2) represent the same input.
* **Database Planning:** Compare raw byte sizes (`digest`) vs string lengths (`hexdigest`) for schema optimization.
* **Extensible:** Supports dynamic discovery of all algorithms available on your specific OpenSSL build.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/mhamzaib/libplayground-randhasher.git
cd libplayground-randhasher

# Install in editable mode (recommended)
pip install -e .
```
---

## Quick Start

### As a Library
```python
from randhasher.functions import HashTypes

# Initialize (unsafe=True allows access to non-guaranteed platform hashes)
hasher = HashTypes(unsafe=False)

# Generate all SHA-3 variants for a string
df = hasher.generateSha3("your-secure-string")

print(df)
```

### As a CLI Tool
Once installed, you can run `randhasher` directly from your terminal:
```bash
# Get all available hashes for a string
randhasher "hello world" --type all

# Get only SHA-2 variants without hex columns
randhasher "secret-key" --type sha --no-hex
```

---

## Core Features
* **Family Grouping:** Specialized methods for `SHA`, `SHA-3`, `BLAKE`, and `SHAKE`.
* **The "Other" Catch-all:** Easily find legacy or platform-specific hashes like `md5` or `ripemd160` that don't fit the main families.
* **Pandas Integration:** Every result is returned as a DataFrame, making it trivial to export to CSV, JSON, or SQL.

---

## Development & Testing

This project uses `pytest` for unit testing and GitHub Actions for CI/CD.

```bash
# Run tests locally
pytest tests/
```

### Future Roadmap
- [ ] Add support for HMAC (keyed-hashing).
- [ ] Performance benchmarking (time-to-hash column).
- [ ] Export directly to `.csv` via CLI.

## Author
**Hamza** - [mhamzaib](https://github.com/mhamzaib)