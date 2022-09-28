-- 코드를 입력하세요
SELECT
    i.animal_id as 'ANIMAL_ID',
    i.name as 'NAME'
FROM animal_ins as i INNER JOIN animal_outs as o ON i.animal_id = o.animal_id
WHERE i.datetime > o.datetime
ORDER BY i.datetime
