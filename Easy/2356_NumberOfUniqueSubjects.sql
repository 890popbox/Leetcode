select teacher_id, count( distinct subject_id) as cnt from Teacher
group by teacher_id
/* select the teachers_id, cnt of distinct subjects, group this by the teachers_id
the query must group all by unique teacher_ids from Teachers,
then the query counts all distinct subjects in that teacher_id only
*/
