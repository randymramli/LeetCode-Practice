-- 175 Combine 2 tables

select firstName,lastName,city,state
from Person left JOIN Address
ON Person.personId = Address.personId

-- 176 Second Highest Salary

select(
    select distinct
    salary
    from Employee
    order by salary desc
    Limit 1 offsett 1)  as secondhighestsalary

-- 177 Nth Highest Salary

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
Declare M INT;
Set M = N -1;
  RETURN (
    select distinct Salary from Employee
    Order By Salary desc
    Limit M,1
  );
END

-- 178 Rank Scores
Select score, dense_rank()
over(order by Score desc) as 'Rank'
from Scores


-- 181 Employees Earning More Than Their Managers

Select 
    X.name as 'Employee'
From 
    Employee as X,
    Employee as Y
Where X.managerId = Y.Id
And X.Salary > Y.Salary

-- 182 Duplicate Emails

Select email

from Person

Group By email
Having count(email) > 1;

--185 Department Top Three Salaries

Select D.Name as 'Department', E.Name as 'Employee', E.Salary
from Employee as E Inner join Department as D
On E.departmentId = D.Id
where 
3 > (select count(distinct E2.Salary)
        from Employee as E2
        Where E2.Salary > E.Salary
        And E.departmentId = E2.departmentId
    )