use pyo3::prelude::{pyfunction, PyResult};
use std::fs::{rename, File};
use std::io::{BufRead, BufReader, LineWriter, Write};
use std::path::PathBuf;

/// Truncate file to the desired size
#[pyfunction]
pub fn truncate_file_lines(in_file: PathBuf, lines_wanted: u64) -> PyResult<()> {
    let tmp_in_file = in_file.to_string_lossy();
    let tmp_filename = format!("{tmp_in_file}~"); // Create new filename with the tilde appended
    let mut g = LineWriter::new(File::create(&tmp_filename)?);

    for (idx, line) in BufReader::new(File::open(&in_file)?).lines().enumerate() {
        if idx >= lines_wanted.try_into()? {
            break;
        }
        writeln!(g, "{}", line?)?;
    }

    g.flush()?;
    rename(&tmp_filename, &in_file)?;

    Ok(())
}

#[cfg(test)]
mod mod_test_truncate_file_lines {
    use file_diff::diff_files;
    use std::fs::File;
    use testdir::testdir;

    use super::truncate_file_lines;

    #[test]
    fn test_truncate_file_lines() {
        let test_dir = testdir!();

        let test_path = test_dir.join("data.txt");
        std::fs::write(&test_path, "12345\n67\n890\n").ok().unwrap();
        assert!(&test_path.exists());

        let test_path_a = test_dir.join("expected_truncated_data_a.txt");
        std::fs::write(&test_path_a, "12345\n67\n").ok().unwrap();
        assert!(test_path_a.exists());
        truncate_file_lines(test_path.clone(), 2).unwrap();
        assert!(diff_files(
            &mut File::open(&test_path).unwrap(),
            &mut File::open(&test_path_a).unwrap()
        ));

        let test_path_b = test_dir.join("expected_truncated_data_b.txt");
        std::fs::write(&test_path_b, "12345\n").ok().unwrap();
        assert!(test_path_b.exists());
        truncate_file_lines(test_path.clone(), 1).unwrap();
        assert!(diff_files(
            &mut File::open(&test_path).unwrap(),
            &mut File::open(&test_path_b).unwrap()
        ));
    }
}
