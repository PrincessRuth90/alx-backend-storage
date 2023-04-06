-- A script that creates a trigger that decreases the quantity of an item after adding a new order
CREATE TRIGGER DECREMENT
AFTER INSERT ON ORDERS FOR EACH ROW
UPDATE ITEMS SET QUANTITY = QUANTITY - NEW.NUMBER WHERE NAME = NEW.ITEM_NAME;
