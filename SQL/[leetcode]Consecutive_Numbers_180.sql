# 1. self join 2회
SELECT DISTINCT l.num  AS ConsecutiveNums -- 연속하는 value가 두 번 있을 수 있다. disctinct
	FROM logs AS l
    		INNER JOIN logs AS l_next ON l.id + 1 = l_next.id -- 셀프조인을 할 때는 새로운 테이블에 이름을 붙여야함, 여기까지는 두번 연속 
    		INNER JOIN logs As l_next2 ON l_next.id +1 = l_next2.id -- 셀프조인 2번 가능함
WHERE l.num = l_next.num AND l_next.num = l_next2.num -- WHERE l.num = l_next.num = l_next2.num -- WHERE절에서 이런식으로 조건 쓸 면 RUN이 안됨


# 2. window 함수 LAG(),LEAD() 사용

-- 1. LEAD 함수로 풀기
SELECT DISTINCT l.num AS ConsecutiveNums -- 중복을 제거해야하기 때문에 DISTINCT
FROM (
    SELECT num
    , LEAD(num, 1) OVER (ORDER BY id) as next 
    , LEAD(num, 2) OVER (ORDER BY id) as afternext
    FROM logs
     ) l -- FROM절에 서브쿼리
WHERE l.num = l.next and l.num = l.afternext

-- 2. LAG 함수로 풀기
SELECT DISTINCT num AS ConsecutiveNums -- DISTINCT 빼놓지 말고 쓰기
FROM (
    SELECT num
    , LAG(num, 1) OVER (ORDER BY id) as next 
    , LAG(num, 2) OVER (ORDER BY id) as afternext
    FROM logs
     ) l -- FROM 절에 서브쿼리
WHERE l.num = l.next and l.num = l.afternext