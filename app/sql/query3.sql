drop view max_cost;
CREATE VIEW max_cost AS
SELECT * FROM reserved_product_payment.product;
 SELECT * FROM max_cost WHERE unit_cost = (SELECT max(unit_cost) FROM max_cost);