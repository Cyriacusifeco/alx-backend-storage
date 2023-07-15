-- SQL script to create a stored procedure ComputeAverageScoreForUser
-- This procedure computes and stores the average score for a student based on their user_id

DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Calculate the average score for the user
    UPDATE users
    SET average_score = (
        SELECT AVG(score)
        FROM corrections
        WHERE user_id = users.id
    )

    WHERE id = user_id;
    
    -- Optionally, you can return the calculated average score
    SELECT id, name, average_score FROM users;
END //

DELIMITER ;
