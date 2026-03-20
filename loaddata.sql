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
  "created_on" datetime,
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
  "created_on" datetime,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" datetime,
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
VALUES ('Sports');
INSERT INTO Categories ('label')
VALUES ('Lifestyle');
INSERT INTO Categories ('label')
VALUES ('Business');
INSERT INTO Categories ('label')
VALUES ('Food');
INSERT INTO Tags ('label')
VALUES ('Jellyfishing');
INSERT INTO Tags ('label')
VALUES ('BikiniBottom');
INSERT INTO Tags ('label')
VALUES ('BoatingSchool');
INSERT INTO Tags ('label')
VALUES ('TreedomeLife');
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
'https://i.scdn.co/image/ab6761610000e5eb877d4c061d08c040974224be',
'2003-14-12',
1
);
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
'Patrick',
'Star',
'patrick.star@bikinibottom.oc',
'This is Patrick, and I''m not a Krusty Krab!',
'patrickstar1',
'starpower2',
'https://static.wikia.nocookie.net/spongebob/images/1/17/Patrick_Star_Show_Patrick.png',
'2003-14-12',
1
);
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
'Gary',
'Squarepants',
'snail1@bikinibottom.oc',
'Meow',
'garythesnail',
'meow1',
'https://upload.wikimedia.org/wikipedia/commons/4/4a/Gary_%28SpongeBob%29_character.png',
'2003-14-12',
1
);
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
'Squilliam',
'Fancyson',
'squilliam@bikinibottom.oc',
'World-renowned artist, musician, and entrepreneur. I''ve achieved everything Squidward ever dreamed of, and I did it effortlessly. My unibrow alone has been featured in three galleries.',
'fancyson_elite',
'betterthansquid1',
'https://i1.sndcdn.com/avatars-000451991661-3mzpc2-t1080x1080.jpg',
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
  4, 
  'The Best Krabby Patty Secret Formula Theories',
  '2025-11-14 09:00:00',
  'https://static.wikia.nocookie.net/spongebob/images/4/48/Plankton%27s_Army_177.png',
  'Bikini Bottom''s most debated mystery isn''t the Bermuda Triangle — it''s the Krusty Krab''s secret formula. "I''ve dedicated years to uncovering the truth," says Sandy Cheeks, PhD. "My leading hypothesis involves a rare kelp extract native to the sea floor." Plankton, rival restaurateur and owner of the Chum Bucket, was unavailable for comment. Mr. Krabs, when pressed for details, simply replied "I smell money" and walked away.',
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
  2, 
  2, 
  'Is Living Under a Rock the New Minimalism?',
  '2025-12-01 10:15:00',
  'https://static.wikia.nocookie.net/spongebob/images/f/f0/Patrick%27s_house.png',
  'Patrick Star has been living under a rock for years — and interior design experts are taking notice. "There''s something deeply intentional about it," says renowned designer Pearl Krabs. "No clutter, no distractions, just pure simplicity." Patrick himself describes his design philosophy as "I didn''t know I had a philosophy." The rock currently has no windows, no furniture, and no electricity, which Patrick calls "cozy."',
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
3,
3,
'Boating School: Why Are Pass Rates So Low?',
'2026-01-22 11:30:00',
'https://static.wikia.nocookie.net/spongebob/images/7/76/MrsPuffBoatingSchoolStock.png',
'Mrs. Puff''s Boating School has reported a 2% pass rate for the third consecutive year, a statistic that instructor Mrs. Puff attributes to "one particular student." SpongeBob SquarePants, who has attempted the boating exam 1,258 times, remains optimistic. "This is definitely my year," he told reporters. "I''ve been practicing on a simulator made of cardboard and dreams." Mrs. Puff was later seen hyperventilating into a paper bag.',
0
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
  'Jellyfishing: Bikini Bottom''s Hottest New Hobby',
  '2026-02-10 08:45:00',
  'https://static.wikia.nocookie.net/spongebob/images/a/ab/Jellyfish_Hunter_004.png',
  'Move over pickleball — jellyfishing is taking Bikini Bottom by storm. Armed with nothing but a net and unbridled enthusiasm, locals are heading to Jellyfish Fields in record numbers. "It''s meditative," says SpongeBob SquarePants, widely regarded as the sport''s foremost expert. "You and the jellyfish, one with nature." Patrick Star, his frequent jellyfishing companion, adds: "I like the part where you catch them." Safety officials remind participants that jellyfish stings remain extremely painful.',
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
  4, 
  1, 
  'Sandy Cheeks'' Guide to Staying Fit Under the Sea',
  '2026-02-28 07:30:00',
  'https://www.randomgoofiness.com/wp-content/uploads/2012/02/sandy-doing-deadlifts.png',
  'Texas native and Bikini Bottom''s premier scientist-athlete Sandy Cheeks has built a reputation as the most physically fit resident of the sea floor. "Back in Texas we had a saying: if you ain''t sweatin'', you ain''t livin''," says Cheeks, who holds black belts in three martial arts and once wrestled a giant clam before breakfast. Her treedome gym, which she built herself, features a treadmill, a karate dojo, and what she describes as "the world''s only underwater lasso range." SpongeBob and Patrick have attempted her workout regimen twice, both times ending up in the hospital.',
  1
);


INSERT INTO Comments ('post_id', 'author_id', 'content') VALUES ( 1, 3, 'The things I would do to get my hands on that recipe!!!');
INSERT INTO Comments ('post_id', 'author_id', 'content') VALUES ( 1, 4, 'I know but I don''t care');
INSERT INTO Comments ('post_id', 'author_id', 'content') VALUES ( 2, 4, 'What''s wrong with you boy? ');
INSERT INTO Comments ('post_id', 'author_id', 'content') VALUES ( 5, 1, 'I''m getting snatched for the summer');