select employee_id, department_id from Employee
where primary_flag = 'Y'
union select employee_id, department_id from Employee
where employee_id in (select employee_id from Employee
group by employee_id having count(employee_id)=1)
/* First table created is all cases where the primary_flag is Y
Second table created is all cases where there is exists only one employee_id regardless of if the flag is Y or N'
Combining these tables together by union will generate our distinct output even if both cases are met */
