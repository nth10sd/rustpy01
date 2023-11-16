(Insert GitHub Actions/codecov status badges here)

# README

## Prerequisites

Install Rust by following the [instructions on their website](https://www.rust-lang.org/).

This demo was tested with Python 3.10 and the following rustup/Rust versions:

```
$ rustup --version
rustup 1.26.0 (5af9b9484 2023-04-05)
info: This is the version for the rustup toolchain manager, not the rustc compiler.
info: The currently active `rustc` version is `rustc 1.74.0 (79e9716c9 2023-11-13)`
```

Create a new Python 3.10 (install it beforehand) virtual environment using `venv` and switch to it.

```
python3.10 -u -m venv ~/venv-rustpy01 ;
```

```
source ~/venv-rustpy01/bin/activate && pip install --upgrade pip ;
```

Install [cargo-binstall](https://github.com/cargo-bins/cargo-binstall).

Make sure Cargo is usable and use `cargo-binstall` to install `cargo-tarpaulin` (code coverage).

```
cargo binstall -y cargo-tarpaulin
```

Clone the repository and cd into it.

## maturin-related (Rust)

Development command:

```
cargo clippy --all-targets -- -D warnings && python -u -m pip install --upgrade pip ; pip install --upgrade -r requirements.txt && cargo tarpaulin --all-targets --count --exclude-files=target/* --engine=llvm --fail-under=80 --ignored --no-dead-code --out=stdout --skip-clean --target-dir=target/tarpaulin-target/ && maturin develop --release
```

Switch `maturin develop` for debug Rust code.

## Run tools on your package

(All commands here must be run within the `venv`, in the main repository directory - not any subfolders)

For comprehensive tests and all linters:
```
python -u -m pytest --cov --mypy --pylint --ruff --ruff-format
```

## Prepare text data for truncation

Download [enwik9.zip](http://mattmahoney.net/dc/enwik9.zip) test data for the [Large Text Compression Benchmark](http://mattmahoney.net/dc/textdata.html). Extract it and move the extracted file to the root folder of this `git` repository, renaming it to `enwik9.txt`. Verify its SHA-1 hash.

It is the first 109 bytes of the English Wikipedia dump on Mar. 3, 2006.

## Running

Run the module using:

```
(venv-rustpy01) $ python -u -m rustpy01
```

Ensure any file is present in the root folder of the `git` repository with the hardcoded filename `enwik9.txt`, it will then be truncated to 1 million lines after running the following command:

```
(venv-rustpy01) $ python -u -m rustpy01.truncate
```

This command may also be useful:
```
(venv-rustpy01) $ date ; cp ~/backup-enwik9.txt enwik9.txt ; time python -u -m rustpy01.truncate ; date
```

## Documentation generation via Sphinx

* Change into `docs/` folder: `cd docs/`
* Run generation command - you **must** first be in the `docs/` directory: `./gen-sphinx-html.sh`
* Your generated HTML files are now in `docs/build/html/` directory
* Open `index.html` to start
