use examples::samples::{print_cli_args, print_something, sum_as_string};
use file_helpers::truncate::truncate_file_lines;
use pyo3::prelude::{pymodule, wrap_pyfunction, PyModule, PyResult, Python};

mod examples {
    pub mod samples;
}
mod file_helpers {
    pub mod truncate;
}

/// A Python module implemented in Rust.
#[cfg(not(tarpaulin_include))]
#[pymodule]
fn _rustpy01(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(truncate_file_lines, m)?)?;

    // Examples
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_wrapped(wrap_pyfunction!(print_cli_args))?;
    m.add_wrapped(wrap_pyfunction!(print_something))?;
    Ok(())
}
