Docker-compose: move to project folder in your bash-terminal of Docker and run command:<br>
docker-compose up<br>
<br>
<br>
API Enpoints:<br>
<br>
For getting access to authorized only/author only use Postman/frontend client providing authorization bearer token<br>
<br>
/api/v1/signup    - Registration(via Postman/frontend client providing "name" "email" "password" in body)<br>
<br>
/api//token/    - Obtaining token for authorization(via Postman/frontend client providing "email" "password" in body)<br>
<br>
/api/v1/posts    - Post List for all<br>
<br>
/api/v1/posts/post/id     - Post retrive for all<br>
<br>
/api/v1/posts/create      - Create post for authorized only<br>
<br>
/api/v1/posts/update/id     - Update post only by its author<br>
<br>
/api/v1/posts/like_dislike/id     - Like/Dislike post for authorized only<br>
<br>
/api/v1/posts/comments      - Comment list for all<br>
<br>
/api/v1/posts/comments/create     - Comment create for authorized only<br>
<br>
/api/v1/posts/comments/update/id      - Update comment only by its author<br>
<br>
/api/v1/posts/comments/like_dislike/id      - Like/Dislike comment for authorized only<br>
<br>
/api/v1/accounts    - Account List for all<br>
<br>
/api/v1/accounts/id    - User Statistic for all<br>
