CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    upload_datetime DATETIME,
    file_path TEXT NOT NULL,
    thumbnail_path TEXT,
    uploaded_by INTEGER,
    like_counter INTEGER DEFAULT 0,
    dislike_counter INTEGER DEFAULT 0,
    FOREIGN KEY (uploaded_by) REFERENCES users (id)
);
CREATE TABLE IF NOT EXISTS playlists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
CREATE TABLE IF NOT EXISTS playlist_videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    playlist_id INTEGER,
    video_id INTEGER,
    FOREIGN KEY (playlist_id) REFERENCES playlists (id),
    FOREIGN KEY (video_id) REFERENCES videos (id)
);
CREATE TABLE IF NOT EXISTS reactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    video_id INTEGER,
    reaction INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(video_id) REFERENCES videos(id)
);
