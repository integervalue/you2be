from utils.db import get_db

def insert_reaction(user_id, video_id, reaction):
    db = get_db()

    # Insert the video reaction into the table
    db.execute("""
    INSERT INTO reactions (user_id, video_id, reaction)
    VALUES (?, ?, ?);
    """, (user_id, video_id, reaction))

    # Update video like and dislike counter
    db.execute("""
    UPDATE videos 
    SET like_counter = like_counter + CASE WHEN ? = 1 THEN 1 ELSE 0 END,
    dislike_counter = dislike_counter + CASE WHEN ? = -1 THEN 1 ELSE 0 END
    WHERE id = ?;
    """, (reaction, reaction, video_id))


    db.commit()
    db.close()

def remove_reaction(user_id, video_id, current_reaction):
    db = get_db()

    db.execute("""
    DELETE FROM reactions WHERE user_id = ? AND video_id = ?;
    """, (user_id, video_id))

    db.execute("""
    UPDATE videos 
    SET like_counter = like_counter - CASE WHEN ? = 1 THEN 1 ELSE 0 END,
    dislike_counter = dislike_counter - CASE WHEN ? = -1 THEN 1 ELSE 0 END
    WHERE id = ?;
    """, (current_reaction, current_reaction, video_id))

    db.commit()
    db.close()

def toggle_reaction(user_id, video_id, current_reaction):
    db = get_db()

    db.execute("""
    UPDATE reactions
    SET reaction = CASE WHEN ? = 1 THEN -1 ELSE 1 END
    WHERE user_id = ? AND video_id = ?;
    """, (current_reaction, user_id, video_id))

    db.execute("""
    UPDATE videos 
    SET like_counter = like_counter + CASE WHEN ? = 1 THEN -1 ELSE 1 END,
    dislike_counter = dislike_counter + CASE WHEN ? = -1 THEN -1 ELSE 1 END
    WHERE id = ?;
    """, (current_reaction, current_reaction, video_id))

    db.commit()
    db.close()