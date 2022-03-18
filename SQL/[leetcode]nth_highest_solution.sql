# 함수 정의 : create function / 인수 정의 : (N INT) / 결과값 정의 : INT
# 함수 로직 시작 : BEGIN / 함수 로직 끝 : END


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      SELECT DISTINCT(salary) from Employee order by salary DESC
      LIMIT 1 OFFSET N
      
  );
END