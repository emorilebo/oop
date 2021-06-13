from user import User
from post import Post

app_user_one = User("emory@gmail.com", "Emori", "Crux", "Software Enginner")
app_user_one.get_user_info()
app_user_one.change_password("Denny")

new_post = Post("On a secret mission today", app_user_one.name)
new_post.get_post_info()