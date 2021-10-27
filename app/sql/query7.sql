/* CREATE VIEW p (Document, Sum) AS
SELECT payment_document_id, sum(payed_sum) FROM payment_document
JOIN order_row ON payment_document.payment_document_id = order_row.payment_document
GROUP BY payment_document_id; */
SELECT * FROM payment_document
LEFT JOIN p ON payment_document.payment_document_id = p.Document
WHERE Sum = (Select MAX(Sum) FROM p);