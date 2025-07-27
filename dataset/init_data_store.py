import os
import sqlite3
import h5py

# Paths to the data store files
DB_PATH = "matrix_metadata.db"
HDF5_PATH = "matrices.h5"

def create_sqlite_db(db_path):
    if os.path.exists(db_path):
        print(f"Database '{db_path}' already exists.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table for storing metadata
    cursor.execute("""
        CREATE TABLE matrices (
            hash TEXT PRIMARY KEY,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            other_metadata TEXT
        )
    """)

    conn.commit()
    conn.close()
    print(f"Created SQLite database at '{db_path}'.")

def create_hdf5_file(hdf5_path):
    if os.path.exists(hdf5_path):
        print(f"HDF5 file '{hdf5_path}' already exists.")
        return

    with h5py.File(hdf5_path, 'w') as f:
        # We don't need to add datasets yet; just create the empty file
        pass

    print(f"Created empty HDF5 file at '{hdf5_path}'.")

def main():
    create_sqlite_db(DB_PATH)
    create_hdf5_file(HDF5_PATH)

if __name__ == "__main__":
    main()
