## 2.1.1 (2023-08-30)

1. Make sure `sphinx` tries to generate docs first, then fail on CI when docs contain sphinx errors
1. Run GitHub Actions CI on all major operating systems

## 2.1.0 (2023-08-30)

1. Switch `ruff` to select all rules automatically to run, instead of manually specifying each category
1. Revert `python_files` setting to the default and add `--strict-markers` to `addopts`
1. Switch back to `pytest-instafail` and add `--instafail` to `pytest` run command
1. Bump `pyright` to 1.1.324, `ruff` to 0.0.286, `semgrep` to 1.37.0, `sphinx` to 7.2.4 and `vulture` to 2.9.1

## 2.0.6 (2023-08-20)

1. Exclude build/lib/\* subdirectory when searching for known ignore lines on CI

## 2.0.5 (2023-08-20)

1. Exclude tests in directory adjacent to package directory by default
1. Bump `vulture` to 2.9

## 2.0.4 (2023-08-19)

1. We no longer use `pytest-vulture` since it uses a different config file than `vulture` itself
1. Tweak bashate command on CI to ignore the `E006` (line too long) issue

## 2.0.3 (2023-08-18)

1. Ship the `py.typed` file with the package properly

## 2.0.2 (2023-08-18)

1. README updates

## 2.0.1 (2023-08-18)

1. Test Python 3.11 on CI
1. Remove old licensing boilerplate
1. Stop using `pytype`, as its development has slowed immensely, also `mypy` and `pyright` seem sufficient
1. Fix all outstanding CI issues

## 2.0.0 (2023-08-18)

1. Use the MIT License
1. Rename to `rustpy01`
1. General Python package structure updated
1. Switch entirely to `pyproject.toml` and use `setuptools-scm`
1. Switch entirely to `ruff` from `flake8`
1. `.gitignore` template updated

## 1.2.0 (2023-08-17)

Checkpoint release prior to upcoming 2.x release.

1. Bump to Python 3.10 as a minimum version for new projects
1. More tools and linters added, versions bumped
1. GitHub Actions workflow tweaks
1. Do not propagate logger message to root logger, if it is present
1. Set `mypy` strict flag to true
1. Ensure generating Sphinx documentation always works, especially via GitHub Actions
1. Continue even though codecov errors out primarily because codecov limits the number of uploads allowed for each commit, even if scheduled

## 1.1.0 (2021-05-22)

1. Bump to Python 3.9 as a minimum version for new projects
1. Support more tools, such as pyupgrade and vulture for finding dead code
1. Turn on code coverage integration via GitHub Actions
1. Support Windows, Ubuntu Linux and macOS on GitHub Actions
1. Dependency version bumps

## 1.0.1 (2020-08-31)

1. Add CHANGELOG.md
1. Add Sphinx documentation generation
1. Add notes for codecov submission

## 1.0.0 (2020-08-13)

First version. To adapt this to something desirable:

1. Remember to rename everything away from `bstrap`, including `.coveragerc` and the `bstrap/` folder.
1. Update the `py38bootstrap` name, and update the README.md file.
1. `devices/` folder demonstrates how inherited objects can be placed in a subfolder, while `util` folder demonstrates regular functions.
1. `tests/` folder demonstrates an example `pytest` test structure.
