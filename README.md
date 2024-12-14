# Quiz App Project  

## Overview  
The Quiz App is a dynamic, Django-based application that enables users to participate in quizzes, answer multiple questions, and conclude the quiz at their convenience. It also includes an administrative interface for managing quiz questions. The app uses a local SQLite database to store and retrieve quiz-related data and includes user authentication for the admin panel.

---

## Features  

### **User Functionality**
1. **Home Page**:  
   - The landing page allows users to start the quiz.  
   - Once the quiz starts, users can answer as many questions as they wish.  
   - The quiz concludes when the user chooses to end it.  

2. **Dynamic Questions**:  
   - Questions are fetched dynamically from the local SQLite database.  
   - A functional quiz requires questions to be pre-loaded into the database.

### **Admin Panel**  
1. Accessible by appending `/admin` to the project URL (e.g., `http://localhost:8000/admin`).  
2. Requires administrator authentication (superuser credentials).  
   - **Superuser ID**: `owais`  
   - **Password**: `owais123`  
3. Admins can add, edit, and delete questions in the database using the Django admin interface.  

---

## Requirements  
- **Python**: Version 3.10 or above  
- **Django**: Version 5.1.4  
- **Database**: SQLite (Local)  

---
