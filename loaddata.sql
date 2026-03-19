DROP TABLE IF EXISTS Posts;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS DemotionQueue;
DROP TABLE IF EXISTS Subscriptions;
DROP TABLE IF EXISTS Comments;
DROP TABLE IF EXISTS Reactions;
DROP TABLE IF EXISTS PostReactions;
DROP TABLE IF EXISTS Tags;
DROP TABLE IF EXISTS PostTags;
CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);
CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);
CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);
CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);
CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
INSERT INTO Categories ('label')
VALUES ('News');
INSERT INTO Categories ('label')
VALUES ('Lifestyle');
INSERT INTO Categories ('label')
VALUES ('Work');
INSERT INTO Categories ('label')
VALUES ('Food');
INSERT INTO Tags ('label')
VALUES ('JavaScript');
INSERT INTO Tags ('label')
VALUES ('React');
INSERT INTO Tags ('label')
VALUES ('Python');
INSERT INTO Tags ('label')
VALUES ('Django');
INSERT INTO Reactions ('label', 'image_url')
VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO Users (
'first_name', 
'last_name', 
'email', 
'bio', 
'username',
'password', 
'profile_image_url', 
'created_on', 
'active'
) 
VALUES (
'Spongebob',
'Squarepants',
'imready@thekrustykrab.oc',
'I''m SpongeBob SquarePants! I''m a fry cook at the Krusty Krab, the best fry cook in Bikini Bottom — just ask my boss Mr. Krabs, or don''t, he''ll probably charge you for the answer!',
'ready2fry',
'krabbypatty1',
'https://i.ebayimg.com/images/g/qc8AAOSw~Mdk8oWS/s-l1200.jpg',
'2003-14-12',
1
);

INSERT INTO Posts (
  'user_id', 
  'category_id', 
  'title', 
  'publication_date', 
  'image_url', 
  'content', 
  'approved'
)
VALUES (
  1, 
  2, 
  'UK''s Cosiest Thatched Cottages', 
  '2025-09-10', 
  'https://ichef.bbci.co.uk/images/ic/800xn/p0m7g4l8.jpg.webp', 
  'Thatched cottages trigger all sorts of signification, drawn from myth and literature," Matt Carey-Williams, founder of his eponymous London art gallery, who owns a thatched cottage in Wiltshire, tells the BBC. "They appear in Little Red Riding Hood and JRR Tolkien''s the Shire [in The Hobbit and The Lord of the Rings]." Also fitting this description is Anne Hathaway''s Cottage, a half-timbered building. Its construction began in 1463.', 
  1
);
INSERT INTO Posts (
  'user_id', 
  'category_id', 
  'title', 
  'publication_date', 
  'image_url', 
  'content', 
  'approved'
)
VALUES (
  1, 
  4, 
  'Does Eating Cheese Before Bed Cause Nightmares?', 
  '2026-03-18', 
  'https://food.fnr.sndimg.com/content/dam/images/food/fullset/2019/5/31/HE_cheese-board-Getty_4x3.jpg.rend.hgtvcom.616.462.85.suffix/1559329196445.webp',
  'We went right to the expert to determine the relationship between food and sleep. Karman Meyer RD, LDN, author of Eat To Sleep — What to Eat & When to Eat It for a Good Night''s Sleep isn''t sold on the link between cheese and nightmares. "There''s not any robust research that supports the claim that eating cheese before bed will cause nightmares,” says Meyer. “I''m a regular cheese-eater, at any time of day, and can''t recall the last time I awoke from sleep, stricken by fear from a nightmare. That''s anecdotal evidence, of course, but at least I know for me, there''s nothing to fear in eating cheese at night!” In fact, Karman includes cheese on the "Best Bedtime Snacks" list in her book.', 
  1
);
INSERT INTO Posts (
'user_id', 
'category_id', 
'title', 
'publication_date', 
'image_url', 
'content', 
'approved'
)
VALUES (
1,
3,
'Is Our Team the Best?',
'2026-02-14',
'https://static.wikia.nocookie.net/spongebob/images/7/79/The_Secret_Box_171.png/revision/latest/scale-to-width-down/1424?cb=20250725165834',
'Duh. Absolutely, no doubt. It''s not even a question',
1
);
