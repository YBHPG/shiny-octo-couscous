CREATE VIEW max_cost AS
SELECT *
FROM reserved_product_payment.order
WHERE month(order_date) = 03
    AND year(order_date) = 2013;
SELECT *
FROM max_cost
WHERE total_cost = (
        SELECT max(total_cost)
        FROM max_cost
    );
DROP VIEW max_cost;
select payment_document_id
from payment_document
    join order_row on payment_document.payment_document_id = order_row.payment_document
group by payment_document_id