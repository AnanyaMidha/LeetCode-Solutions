WITH CTE AS
(SELECT employee_id, manager_id
FROM Employees
WHERE salary < 30000)

select employee_id
from cte
where manager_id Not in (select employee_id
from employees ) order by employee_id