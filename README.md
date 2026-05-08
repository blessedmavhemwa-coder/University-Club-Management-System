# University-Club-Management-System
This is a sample design of a system which interacts with the Database and stores the clubs of a university or school while also being able to perform simple tasks like add members and or activities

## Pages of the System
1. Home Page

   <img width="1365" height="717" alt="Screenshot 2026-05-08 071447" src="https://github.com/user-attachments/assets/403a91a5-dd70-452a-8461-6dde2f60833b" />

   This is the home page where you can see all the clubs available in the system, presented in a clear table with columns for ID, Name, Meeting Day, and Meeting Time. The current list
   includes Chess Club (Saturday 15:00), Debate Club (Wednesday 16:30), Robotics Club (Friday 14:00), Photography Club (Tuesday 13:00), and Moot (Monday 17:00). Above the table, the
   navigation menu provides quick access to other key sections: Students, Instructors, Activities, Memberships, Audit Log, Moderator Budget, and Club Details View. The top bar also shows
   the user’s logged‑in status and a Logout button. This central view serves as the main dashboard for managing all university clubs.

3. Students Page

   <img width="1365" height="720" alt="Screenshot 2026-05-08 071519" src="https://github.com/user-attachments/assets/315a31e7-d77c-47bb-a846-5ad168d722ef" />
   
   This is the students page where all the students in the system shows up, listing key details such as ID, Name, Email, Registration Number, Program, Year, and Faculty. The current
   table includes five students: Alice Brown (2024001, Computer Science, 3rd Year, Science), Bob White (2024002, Mathematics, 2nd Year, Science), Carol Green (2024003, Physics, 1st Year,
   Science), David Black (2024004, Computer Science, 4th Year, Science), and Eva Blue (2024005, Engineering, 2nd Year, Engineering). The same navigation menu from the home page is
   available at the bottom, allowing easy access to Home, Instructors, Activities, Memberships, Audit Log, Moderator Budget, and Club Details View. This page serves as the central
   directory for managing all student records within the university clubs system.

4. Instructors Page

   <img width="1365" height="715" alt="Screenshot 2026-05-08 071541" src="https://github.com/user-attachments/assets/74702c85-8e4b-4cec-9199-dcb001768756" />

   This is the Instructors Page where all faculty advisors and club moderators are listed, including their professional details such as ID, Name, Email, Staff Number, Department,
   Position, and Salary. The current table shows three instructors: Dr. John Smith (Computer Science, Senior Lecturer, 80000), Prof.Jane Doe (Mathematics, Professor, 80,000),
   Prof.JaneDoe (Mathematics,Professor,95,000) and Dr. Robert Johnson (Physics, Associate Professor, $85,000). The left-hand menu provides navigation to other core sections, while the
   top bar indicates the logged‑in user and logout option. A footer with the copyright notice appears at the bottom. This page helps administrators track instructor information and
   assign club supervision responsibilities within the university clubs system.

6. Activities Page

   <img width="1365" height="717" alt="Screenshot 2026-05-08 071628" src="https://github.com/user-attachments/assets/5662e113-f6e9-4844-83f9-0df57e7450bb" />

   This is the activities page where the details about the activities of each club are displayed, including the club name, type of activity, date, time, and location. The current table
   shows seven upcoming events: Chess Club has a Meet & Greet (2024-03-15 at 14:00 in Student Union) and a Practice session (2024-03-08 at 15:00 in Room 101); Debate Club features a
   Competition (2024-03-20 at 10:00 in Auditorium) and a Workshop (2024-03-10 at 16:00 in Room 205); Robotics Club lists a Workshop (2024-03-12 at 14:30 in Engineering Lab) and a
   Competition (2024-03-25 at 9:00 in Main Hall); Photography Club has an Exhibition (2024-03-18 at 11:00 in Art Gallery). Above the table, an “Add New Activity” button allows users to
   create additional entries. The side menu and top bar provide consistent navigation and logout access. This page serves as the central calendar and event log for all club‑related
   activities.

7. Memberships Page
   
   <img width="1365" height="717" alt="Screenshot 2026-05-08 071656" src="https://github.com/user-attachments/assets/dd5d73a9-0681-41ba-84d2-0e6caf187097" />

   The memberships page is where the members are displayed in relation to the clubs they have joined, showing each student’s name, the club, their join date, and their role within that
   club. The current table lists several entries: Alice Brown is a member of Chess Club (joined 2024-01-15) and appears multiple times in Debate Club (2024-01-25, 2026-03-06,
   2026-03-08); David Black is President of Chess Club (2024-01-10); Eva Blue is Treasurer of Photography Club (2024-02-15); Bob White is Secretary of Debate Club (2024-01-20) and a
   member of Robotics Club (2024-02-05); Carol Green is Vice President of Photography Club (2024-02-20). An “Add New Membership” button allows administrators to enroll students into
   clubs. The standard navigation menu (Home, Students, Instructors, Activities, etc.) and logout option are present. This page acts as the enrollment and roles registry for all
   club‑student relationships.

8. Audit Log Page
   <img width="1365" height="720" alt="Screenshot 2026-05-08 071724" src="https://github.com/user-attachments/assets/97212509-a067-4d25-898c-e4135576b0a3" />

   This is the audit log page where all salary change records for instructors are tracked, including the audit ID, instructor ID, old salary, new salary, who made the change, and the
   timestamp of the change. The current table shows one entry: Instructor ID 1 had a salary updated from 75,000 to 80,000 by root@localhost on 2026-03-06 at 20:34:51. The standard side
   menu and logout bar are present, along with a copyright footer. This page ensures transparency and accountability for budget‑related modifications within the university clubs
   management system.

9. Moderator Budget

   <img width="1365" height="720" alt="Screenshot 2026-05-08 071749" src="https://github.com/user-attachments/assets/460a0a43-7077-44e0-beb5-7f7eb02c905c" />

   This is the Moderator Budget page where information regarding the clubs moderator’s allocated budget is displayed, showing each instructor’s ID, name, and the total budget of the
   clubs they moderate. The current table lists three moderators: Dr. John Smith (Instructor ID 1) with a total budget of 900.0, Prof.JaneDoe (ID2) with 900.0, Prof.JaneDoe(ID2) with
   1250.0 and Dr. Robert Johnson (ID 3) with $1500.0. The standard side menu and logout bar provide navigation to other sections. This page helps administrators monitor and manage
   financial resources assigned to each club moderator across the university clubs system.

10. Club Details Page

    <img width="1361" height="719" alt="Screenshot 2026-05-08 071812" src="https://github.com/user-attachments/assets/5ad4f129-1148-41f1-9aee-191faa760370" />

    This is the Club Details page where the comprehensive information for each club is shown, including Club ID, Club Name, Budget, Meeting Day, Meeting Time, Moderator, and Member
    Count. The current table lists five clubs: Chess Club (ID 1, Budget 600.0, Saturday 15:00, moderated by Dr.JohnSmith with 2 members), Photography Club (ID4, Budget 600.0, Saturday
    15:00, moderated by Dr.JohnSmith with 2 members), Photography Club (ID4, Budget 300.0, Tuesday 13:00, also moderated by Dr. John Smith with 2 members), Debate Club (ID 2, Budget
    750.0, Wednesday 16:30, moderated by Prof.JaneDoe with 4 members), Moot (ID5, Budget 750.0, Wednesday 16:30, moderated by Prof.JaneDoe with 4members), Moot (ID5, Budget 500.0,
    Monday 17:00, moderated by Prof. Jane Doe with 0 members), and Robotics Club (ID 3, Budget $1500.0, Friday 14:00, moderated by Dr. Robert Johnson with 1 member). An “Add New Club”
    button allows creation of additional clubs. This page serves as the master record for all club configurations, budgets, and moderator assignments within the university clubs
    management system.
