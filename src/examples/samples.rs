use pyo3::prelude::{pyfunction, PyResult, Python};
use std::env;

/// Formats the sum of two numbers as string.
#[pyfunction]
pub fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
pub fn print_something() -> PyResult<()> {
    println!("This is from Rust");
    Ok(())
}

#[cfg(not(tarpaulin_include))]
#[pyfunction]
pub fn print_cli_args(py: Python) -> PyResult<()> {
    // This one includes python and the name of the wrapper script itself, e.g.
    // `["/home/ferris/.venv/bin/python", "/home/ferris/.venv/bin/print_cli_args", "a",
    //   "b", "c"]`
    println!("{:?}", env::args().collect::<Vec<_>>());
    // This one includes only the name of the wrapper script itself, e.g.
    // `["/home/ferris/.venv/bin/print_cli_args", "a", "b", "c"])`
    println!(
        "{:?}",
        py.import("sys")?
            .getattr("argv")?
            .extract::<Vec<String>>()?
    );
    Ok(())
}

#[cfg(test)]
mod mod_test_sum_as_string {
    use super::sum_as_string;

    #[test]
    fn test_sum_as_string() -> Result<(), String> {
        let _expected_output = String::from("5");
        match sum_as_string(2, 3) {
            Ok(_expected_output) => Ok(()),
            _ => Err(String::from("Two plus three does not equal five")),
        }
    }
}

#[cfg(test)]
mod mod_test_print_something {
    use super::print_something;

    #[test]
    fn test_print_something() -> Result<(), String> {
        match print_something() {
            Ok(()) => Ok(()),
            _ => Err(String::from("Nothing was printed")),
        }
    }
}
