PRAGMA foreign_keys = ON;
CREATE TABLE batch (
  batch_id TEXT PRIMARY KEY,
  label TEXT NOT NULL
);
CREATE TABLE object_record (
  object_id TEXT PRIMARY KEY,
  batch_id TEXT NOT NULL REFERENCES batch(batch_id),
  title TEXT NOT NULL,
  object_type TEXT NOT NULL CHECK (object_type IN ('postcard','poster','pamphlet')),
  status TEXT NOT NULL CHECK (status IN ('pending','captured','checked','published')),
  image_filename TEXT
);
CREATE TABLE issue (
  issue_id INTEGER PRIMARY KEY,
  object_id TEXT NOT NULL REFERENCES object_record(object_id),
  issue_text TEXT NOT NULL,
  owner_role TEXT NOT NULL,
  resolved INTEGER NOT NULL CHECK (resolved IN (0,1))
);
INSERT INTO batch VALUES ('B01','Postcards A'),('B02','Mixed paper B'),('B03','Mixed paper C');
INSERT INTO object_record VALUES
 ('OBJ001','B01','Harbor postcard','postcard','captured','OBJ001.jpg'),
 ('OBJ002','B02','Exhibition poster','poster','checked','OBJ002.jpg'),
 ('OBJ003','B03','Gallery pamphlet','pamphlet','published','OBJ003.jpg');
INSERT INTO issue VALUES
 (1,'OBJ001','Confirm short title','metadata volunteer',0),
 (2,'OBJ003','Correct filename','capture volunteer',1);
