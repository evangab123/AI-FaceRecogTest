CREATE TABLE IF NOT EXISTS face_vectors (
    id SERIAL PRIMARY KEY,
    image_path TEXT NOT NULL,
    vector BYTEA NOT NULL
);