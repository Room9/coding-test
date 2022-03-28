# 함수 정의 : create function / 인수 정의 : (N INT) / 결과값 정의 : INT
# 함수 로직 시작 : BEGIN / 함수 로직 끝 : END

## 1. RETURN(query) 방식으로 리턴하기
# OFFSET 이용 : N까지 다 상쇄하고 select 하겠다

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      SELECT DISTINCT(salary) from Employee order by salary DESC
      LIMIT 1 OFFSET N
  );
END


## 2. RETURN 할 변수를 decalre 하고, 
# SELECT ~ INTO 변수 FROM(서브쿼리) 형식으로 변수에 쿼리결과값 넣어주고
# RETURN 변수 설정

CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN INT;
BEGIN
    /* Write your PL/SQL query statement below */
    DECLARE result INT

    Begin
    Select Salary into result
    From (Select Salary, dense_rank() over(order by salary desc) rn From Employee where salary is not null) where rn = N;
    Exception
         When NO_DATA_FOUND Then
            result := NULL;
    End;
    
    RETURN result;
END;
