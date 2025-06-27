SELECT 
    P.product_name, 
    SUM(O.unit) AS unit
FROM 
    Orders O
JOIN 
    Products P 
    ON O.product_id = P.product_id
WHERE 
    O.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY 
    P.product_id, P.product_name
HAVING 
    SUM(O.unit) >= 100;

