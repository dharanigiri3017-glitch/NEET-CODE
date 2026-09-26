SELECT student_id, exam_id, score
FROM exam_results e
WHERE NOT EXISTS (
    SELECT 1
    FROM exam_results e2
    WHERE e2.student_id = e.student_id
      AND (
          e2.score > e.score
          OR (e2.score = e.score AND e2.exam_id < e.exam_id)
      )
)
ORDER BY student_id;
