-- 코드를 입력하세요
SELECT 
    DISTINCT(p1.cart_id) as CART_ID
FROM
    (SELECT * FROM cart_products as c WHERE c.name = 'Milk') as p1 INNER JOIN 
    (SELECT * FROM cart_products as c WHERE c.name = 'Yogurt') as p2
    ON (p1.CART_ID = p2.CART_ID)
ORDER BY CART_ID ASC