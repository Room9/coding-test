# Inner join + 서브쿼리
SELECT a.name AS Department,
    e.name AS Employee,
    a.salary AS Salary
FROM (SELECT d.id, d.name, max(e.salary) AS salary
    FROM Employee e JOIN Department d
    ON e.departmentId = d.id
    group by d.id, d.name) a
INNER JOIN Employee e ON a.salary = e.salary and a.id = e.departmentId


# rank() over (parition by ~) 사용 + 서브쿼리 대신 with 절로 t1, t2 선언 

With t1 as(
            Select *,dense_rank() over (partition by departmentId order by salary desc) as rnk
            from Employee
        ), 
    t2 as (select * from t1 where rnk = 1)
Select d.name as Department, t2.name as Employee,t2.salary as Salary
from Department d inner join t2
on d.id = t2.departmentId

