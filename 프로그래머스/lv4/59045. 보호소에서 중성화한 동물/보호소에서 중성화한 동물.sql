-- 코드를 입력하세요
SELECT
    i.animal_id as 'ANIMAL_ID',
    i.animal_type as 'ANIMAL_TYPE',
    i.name as 'NAME'
FROM animal_ins AS i INNER JOIN animal_outs AS o ON i.animal_id = o.animal_id
WHERE
    i.SEX_UPON_INTAKE LIKE "Intact%"
    AND (o.SEX_UPON_OUTCOME LIKE "Spayed%" OR o.SEX_UPON_OUTCOME LIKE "Neutered%")
