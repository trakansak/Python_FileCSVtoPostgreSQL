SELECT first_name,last_name,subjectname,grade FROM students

INNER JOIN student_records ON
students.student_id = student_records.student_id
    
WHERE student_records.subjectid='010123112'

ORDER BY grade ASC;