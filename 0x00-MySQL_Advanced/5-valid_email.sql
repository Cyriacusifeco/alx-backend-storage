-- This SQL script creates a trigger that performs email validation when the email is updated.
-- The trigger sets the valid_email attribute based on the validity of the updated email.

DELIMITER //

CREATE TRIGGER update_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    DECLARE is_valid_email INT DEFAULT 0;
    
    IF NEW.email <> OLD.email THEN
        -- Perform email validation logic here
        -- Set is_valid_email to 1 if the email is valid
        
        -- Example email validation logic using a simple regular expression
        IF NEW.email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' THEN
            SET is_valid_email = 1;
        END IF;
    ELSE
        -- If the email is not changed, retain the existing valid_email value
        SET is_valid_email = OLD.valid_email;
    END IF;
    
    SET NEW.valid_email = is_valid_email;
END //

DELIMITER ;
