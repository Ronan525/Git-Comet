# Git Comet

Git Comet is a web forum built for coders to ask questions, make connections, or to simply chat.

## Entity Relationship Diagram

![Entity Relationship Diagram](static/images/git-comet-erd.png)

## Project Structure

The project is organized into several key directories and files:

- `account/`: Manages user accounts, including models, views, and admin configurations.
- `forum/`: Handles forum-related functionalities such as forms, views, and templates.
- `git_comet/`: The main Django application configuration, including settings and URLs.
- `static/` and `staticfiles/`: Contains static assets like CSS and JavaScript files.
- `templates/`: Stores HTML templates for rendering views.
- `manage.py`: A command-line utility for administrative tasks.
- `requirements.txt`: Lists the Python dependencies for the project.
- `Procfile`: Specifies the commands to run the application on Heroku.
- `README.md`: You're reading this right now. Hello! 👋

## Technologies Used

- **Django**
- **Heroku**
- **Gitpod**
- **Code Institute Template**
- **Code Institute Database**
- **Visual Studio Code**
- **Copilot**

## Features Implemented

1. **User Authentication**: Not done quite yet. Hopefully on the next commit.
2. **Forum**: Created a forum where users can post topics and will eventually be able to comment on posts.
3. **Admin Interface**: Customized the Django admin interface to manage user accounts and forum posts.
4. **Static Files Management**: Configured the handling of static files.
5. **Deployment**: Set up deployment configurations for Heroku, such as the `Procfile`, `runtime.txt`, and numerous Heroku config vars that I will detail on a later commit as I can't sign into Heroku, reason being, Google Authenticator decided it's going to feed me incorrect codes. Thanks Google.
6. **Ratings**: Implemented a rating system that allows users to rate posts. This feature strengthens community engagement and encourages users to create accounts.
7. **Draft and Update Posts**: Added the ability for users to save drafts and update their posts. This feature allows users to refine their content before publishing and keep their posts up-to-date.
8. **Profile Picture**: Enabled users to choose from a selection of three profile pictures. This feature provides users with an extra bit of customization.
9. **Bio**: Added a bio feature that allows users to create and update a personal biography on their profile. This adds a personal touch to user profiles and helps build a sense of community.
10. **Contact Us**: Created a Contact Us page that provides users with a way to reach out to the site administrators for support, feedback, or inquiries. This feature is essential for maintaining open communication with the user base.

### Purpose Behind Features

- **User Authentication**: The purpose of adding user authentication is to ensure that users can securely log in and manage their accounts. It was essential that users were given the option to change their username, email address, and password. This feature also lays the groundwork for future enhancements, such as personalized content and user-specific settings.
- **Forum**: The main forum allows users to create and participate in discussions. This is the core functionality of Git Comet, enabling coders to ask questions, share knowledge, and connect with others in the community. The forum allows for signed-in users to make posts of their own, or rate and comment on other users' posts. This interaction fosters a collaborative environment where users can learn from each other and build professional relationships.
- **Ratings**: Ratings synergize extremely well with the main forum page. When this site was just an idea, a rating system was my favorite feature. The reason behind this, not only to strengthen community engagement and further encourage users to create accounts, but also because it was the first time I had ever attempted something of the sort. Ratings help highlight valuable content and give users a sense of accomplishment when their posts are well-received.
- **Admin Interface**: Customizing the Django admin interface helps administrators manage user accounts and forum posts more efficiently. It provides a user-friendly way to oversee the site's content and user interactions. This is required for any social platform to ensure that the community guidelines are followed and to manage any inappropriate content or user behavior.
- **Profile Picture**: A signed-in user can choose from a selection of three profile pictures. Profile pictures provide users with that extra bit of customization that was my goal for Git Comet. This feature helps users express their individuality and makes the platform feel more personalized.
- **Draft and Update Posts**: The ability to save drafts and update posts allows users to work on their posts over time and make changes as needed. This feature ensures that users can refine their content before publishing and keep their posts up-to-date with new information. It also reduces the pressure on users to finalize their posts in one sitting, leading to higher quality content.
- **Contact Us**: The Contact Us page provides users with a way to reach out to the site administrators for support, feedback, or inquiries. This feature is essential for maintaining open communication with the user base and addressing any issues or suggestions they may have. It helps build trust and shows that the administrators are approachable and responsive to user needs.
- **Bio**: The Bio feature allows users to create and update a personal biography on their profile. This adds a personal touch to user profiles and helps build a sense of community by allowing users to share more about themselves. It encourages users to connect on a more personal level and fosters a sense of belonging within the community.

### Issues Faced

- **User Authentication**: Implementing user authentication has been challenging due to the need for secure password handling and session management. Additionally, integrating third-party authentication providers has introduced complexity.
- **Forum**: Ensuring that the forum is user-friendly and supports features like post creation, editing, and commenting has required careful planning and testing. Handling user-generated content securely is also a concern.
- **Admin Interface**: Customizing the admin interface to meet the specific needs of the site has involved learning and applying Django's admin customization capabilities. Ensuring that the interface is intuitive for administrators has been a priority.
- **Static Files Management**: Configuring static files correctly has been crucial for the site's performance. Issues with file paths and caching have required troubleshooting.
- **Deployment**: Deploying the application to Heroku has presented challenges, such as configuring environment variables and ensuring that the application runs smoothly in a production environment. Issues with Google Authenticator have also hindered the deployment process.

## How I've Used Copilot

GitHub Copilot has been an invaluable tool throughout the development of Git Comet. However, on many occassions, Copilot has provided me with incorrect code, used techniques I'm not familiar with, and many more small issues. Despite this, I've used Copilot to great effect. Here are some of the ways Copilot has assisted me in building this project.

1. **Code Suggestions**: Copilot has provided code suggestions, helping me write code faster. It has been particularly useful for generating boilerplate code, repetitive tasks, and project wide changes (such as renaming a file).
2. **Documentation**: Copilot has assisted in writing this readme file. I wrote the content, whilst Copilot formatted it so that it doesn't look like a lunatics notepad document. Copilot has also provided me with very useful and surprisingly accurate commit messages. If only it was this accurate with its code.
3. **Debugging**: By suggesting potential fixes and improvements, Copilot has helped me debug issues more efficiently. It has provided insights into best practices and alternative approaches to solving problems.
4. **Learning**: Copilot has served as a learning tool, offering explanations and examples for various coding concepts and libraries. This has been especially helpful when working with new technologies or unfamiliar code it would often try to use.

Overall, GitHub Copilot has significantly enhanced my productivity and in some cases, the quality of my code. It has been like having an exceptionally smart (but also arrogant) person to talk to. Although it has been adamant I add code which clearly will not work, it's tried its best.

## Heroku Config Vars

- **DATABSE_URL**: The link to my postgresql database generated by Code Institute.
- **SECRET_KEY**: The secret key for the site.