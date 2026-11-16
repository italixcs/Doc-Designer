SELECT b.label, o.object_id, o.title, i.issue_text
FROM issue AS i
JOIN object_record AS o ON o.object_id = i.object_id
JOIN batch AS b ON b.batch_id = o.batch_id
WHERE i.resolved = 0
ORDER BY b.label, o.object_id;
