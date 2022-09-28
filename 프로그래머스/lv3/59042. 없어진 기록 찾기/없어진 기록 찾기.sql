-- 코드를 입력하세요
SELECT
    o.animal_id as 'ANIMAL_ID',
    o.name  as 'NAME'
FROM animal_ins AS i RIGHT JOIN animal_outs AS o ON i.animal_id = o.animal_id
WHERE i.animal_id IS NULL