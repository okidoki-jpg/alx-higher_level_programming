-- List all records with a non-empty name value of the
-- table "second_table" from the database hbtn_0c_0".
-- Results are sorted in descending order by score

SELECT score, name FROM second_table
WHERE name != ''
ORDER BY score DESC;
