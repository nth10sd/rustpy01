[![codecov](https://codecov.io/gh/nth10sd/rustpy01/graph/badge.svg?token=ABPPKT6D0W)](https://codecov.io/gh/nth10sd/rustpy01)

# README

This demo was tested with Python 3.10 - 3.12.

## Prerequisites

Ensure Python is installed, especially on Windows.

Install Rust by following the [instructions on their website](https://www.rust-lang.org/).

After Rust installation,
```
rustup --version
```

You should have at least the following output:
```
rustup 1.26.0 (5af9b9484 2023-04-05)
info: This is the version for the rustup toolchain manager, not the rustc compiler.
info: The currently active `rustc` version is `rustc 1.74.0 (79e9716c9 2023-11-13)`
```

Ensure you do not have any existing `venv` at `~/venv-rustpy01`.

Create a new Python 3.10 (install it beforehand) virtual environment using `venv` and switch to it.

Linux or macOS:
```
python3.10 -u -m venv --upgrade-deps ~/venv-rustpy01 ; . ~/venv-rustpy01/bin/activate ;
```

Windows:
```
pushd ~ ; python -u -m venv --upgrade-deps venv-rustpy01 ; popd ; Set-ExecutionPolicy Unrestricted -Scope Process; ~/venv-rustpy01/Scripts/Activate.ps1 ; ~/venv-rustpy01/Scripts/Activate.ps1 ;
```

Install [cargo-binstall](https://github.com/cargo-bins/cargo-binstall).

Make sure Cargo is usable and use `cargo-binstall` to install `cargo-tarpaulin` (code coverage).
```
cargo binstall -y cargo-tarpaulin
```

Clone the repository and cd into it (replace `<repo>` with desired location):
```
$ git clone <repo> ; cd <repo> ;
```

## maturin-related (Rust)

Development command for Linux and Windows:
```
cargo clippy --all-targets -- -D warnings ; python -u -m pip install --upgrade pip ; pip install --upgrade -r requirements.txt ; cargo tarpaulin --all-targets --count --exclude-files=target/* --engine=llvm --fail-under=80 --ignored --no-dead-code --out=stdout --skip-clean --target-dir=target/tarpaulin-target/ ; maturin develop --release --strip ;
```

Development command for macOS (which uses `zsh`):
```
cargo clippy --all-targets -- -D warnings ; python -u -m pip install --upgrade pip ; pip install --upgrade -r requirements.txt ; setopt +o nomatch ; cargo tarpaulin --all-targets --count --exclude-files=target/* --engine=llvm --fail-under=80 --ignored --no-dead-code --out=stdout --skip-clean --target-dir=target/tarpaulin-target/ ; setopt -o nomatch ; maturin develop --release ;
```

Switch `maturin develop` for debug Rust code with symbols if needed.

## Run tools on your package

(All commands here must be run within the `venv`, in the main repository directory - not any subfolders)

For comprehensive tests and all linters:
```
python -u -m pytest --cov --mypy --pylint --ruff --ruff-format
```

## Prepare text data for truncation

Download [enwik9.zip](http://mattmahoney.net/dc/enwik9.zip) test data for the [Large Text Compression Benchmark](http://mattmahoney.net/dc/textdata.html). Extract it and move the extracted file to the root folder of this `git` repository, renaming it to `enwik9.txt`. Verify its SHA-1 hash.

It is the first 109 bytes of the English Wikipedia dump on Mar. 3, 2006.

Check the SHA1 hash of the test data file:

Linux or macOS:
```
shasum ~/backup-enwik9.txt ;
```

Windows:
```
Get-FileHash -algorithm sha1 ~/backup-enwik9.txt ;
```

## Running

Run the module using:
```
python -u -m rustpy01
```

Ensure any file is present in the root folder of the `git` repository with the hardcoded filename `enwik9.txt`, it will then be truncated to 100k lines. Here is a sample command (Remember to update on CI if this command gets updated):

Linux or macOS:
```
cp ~/backup-enwik9.txt enwik9.txt ; date ; time python -u -m rustpy01.truncate ; date ; rm enwik9.txt ;
```

Windows:
```
cp ~/backup-enwik9.txt enwik9.txt ; date ; Measure-Command { python -u -m rustpy01.truncate | Out-Default } ; date ; rm enwik9.txt ;
```

## Documentation generation via Sphinx (Linux-only)

* Change into `docs/` folder: `cd docs/`
* Run generation command - you **must** first be in the `docs/` directory: `./gen-sphinx-html.sh`
* Your generated HTML files are now in `docs/build/html/` directory
* Open `index.html` to start
