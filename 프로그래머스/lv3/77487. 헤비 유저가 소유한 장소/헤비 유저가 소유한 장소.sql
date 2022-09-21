-- 코드를 입력하세요
SELECT places.id, places.name, places.host_id 
FROM places, (SELECT host_id, COUNT(host_id) AS count FROM places GROUP BY host_id HAVING count > 1) as grp 
WHERE places.host_id = grp.host_id 

