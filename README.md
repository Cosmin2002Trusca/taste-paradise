# Taste Paradise Restaurant

Welcome to Taste Paradise, where every bite is a journey to culinary bliss! Nestled in the heart of Graz, Taste Paradise offers an unforgettable dining experience, blending bold flavors, fresh ingredients, and exceptional service. Our menu is a vibrant celebration of global cuisine, with each dish crafted to excite your senses and transport you to a world of tantalizing tastes. Whether you're craving a comforting classic or exploring something new, our diverse selection promises something for everyone.

At Taste Paradise, we believe in creating a welcoming atmosphere where friends and family can gather, savor, and enjoy. From our elegant ambiance to our attentive staff, every detail is designed to ensure your visit is truly special. Come experience a paradise of flavors—your perfect escape from the ordinary.

[View Taste Paradise live website here](https://taste-paradise-e2f6c6cf02fa.herokuapp.com/)
- - -

## User Experience (UX)

From the moment you land on our website, we’ve crafted an intuitive, user-friendly experience that makes exploring Taste Paradise a delight. With a sleek, modern design, our website is easy to navigate, whether you're on your desktop or mobile device. Everything is just a click away, so you can quickly find what you’re looking for.

### Project Goals

The main goal of the Taste Paradise website project is to create a user-friendly, seamless platform that enhances the overall customer experience by providing easy navigation, streamlined online ordering, and reservation systems. The website will showcase the brand's identity, menu, and values while being fully optimized for mobile devices and search engines to increase visibility and engagement. It will feature interactive elements like live chat and social media integration, promote special offers and events, and ensure secure transactions and privacy. Ultimately, the website will serve as a dynamic hub for both customer interaction and business growth, offering convenience and a connection to the Taste Paradise experience.

### Agile Methodology

Agile Methodology was used to help prioritize and organize tasks, writting the user stories and using Project Boards on Github. Template was created to help write User Stories.

* Project Board is set to public.
* Project Board was used to track progression of the task through the Todo, In progress and Done columns

### Target Audience

The target audience for the Taste Paradise website is diverse, focusing on food enthusiasts, busy professionals, families, and individuals looking for a high-quality dining experience. Our audience includes locals seeking a unique dining destination, as well as tourists and foodies eager to explore new flavors and cuisines. We also aim to attract tech-savvy customers who prefer the convenience of online ordering and reservations. Families and groups are a key demographic, drawn to the welcoming atmosphere and variety of menu options suitable for all tastes. Additionally, we target individuals who value sustainability, quality ingredients, and exceptional service, ensuring they feel connected to the Taste Paradise brand both online and in-person.

### First time user

For first-time users visiting the Taste Paradise website, we aim to provide a smooth and welcoming experience that introduces them to our brand and offerings. Upon landing on the site, they’ll be greeted with an easy-to-navigate layout, showcasing our diverse menu, unique dishes, and commitment to quality. We want first-time visitors to quickly find essential information like our location, hours, and online ordering options, with clear calls-to-action to guide them through their journey. Whether they are browsing the menu, making a reservation, or exploring our sustainability efforts, we ensure the site feels intuitive and user-friendly. First-time users will be encouraged to connect with us through simple features like social media links or the option to subscribe to our newsletter, allowing them to stay updated on special offers and new dishes. Ultimately, our goal is to make a lasting impression, turning first-time visitors into loyal customers.

### Registered user

For registered users, the Taste Paradise website offers a personalized and streamlined experience. Once logged in, they’ll have quick access to their previous orders, making reordering favorites or customizing meals faster and more convenient. Registered users can also enjoy exclusive perks, such as special promotions, discounts, and early access to events or new menu items. Their account allows them to easily track reservations, manage payment methods, and save their favorite dishes for future visits, creating a more tailored experience every time they interact with the website. Additionally, registered users can receive personalized recommendations based on their past choices, ensuring a unique, efficient, and enjoyable experience every time they visit Taste Paradise online.

### Admin user

For admin users, the Taste Paradise website provides a straightforward backend system focused on managing tables, bookings, and user accounts. Admins can easily view, update, and manage table availability, ensuring smooth reservation processes and optimizing seating arrangements. They can also access and manage booking details, including customer preferences, party sizes, and special requests, ensuring a personalized experience for each guest. Additionally, admins have the ability to manage user accounts, viewing and updating customer information, monitoring booking history, and assisting with account-related inquiries. This system helps streamline operations, improve customer service, and maintain an efficient flow of reservations, all while offering a seamless and organized management experience.

## Wireframing

 [link to website wireframe](https://www.figma.com/design/x4ywdTnt13jvvjGzlT6Ffx/Booking-website-for-Restaurant?m=auto&t=RQqwpBgkSICD3LS6-6)

## Database diagram


Tables and Relationships

Table

Fields:
number (Primary Key): A unique identifier for the table (positive integer).

capacity: The number of people the table can seat (positive integer).

Relationship:
This table is related to the Booking table via a ForeignKey relationship. A single table can have multiple bookings (one-to-many relationship).
Booking

Fields:

user (ForeignKey to User): A reference to the User model, indicating which user made the booking. A single user can make multiple bookings (one-to-many relationship).

customer_name: The name of the customer who made the booking (string, max length 50).

customer_email: The email of the customer (email field).

customer_phone: The phone number of the customer (optional, string with a regex validator ensuring numeric values).

table (ForeignKey to Table): A reference to the Table model, specifying which table is reserved. A single table can have many bookings, but only one booking can be made per table at a specific date and time (one-to-many relationship).

booking_date: The date of the reservation (date field).

booking_time: The time of the reservation (time field).

number_of_guests: The number of guests for the reservation (positive integer).

special_request: Any special requests or comments from the customer (optional text field).

created_at: The timestamp when the booking was created (auto-generated datetime).

updated_at: The timestamp when the booking was last updated (auto-generated datetime).

Relationships:

This table is related to the User table (one-to-many) via the user ForeignKey. A user can make multiple bookings.

This table is also related to the Table table (one-to-many) via the table ForeignKey. A table can have multiple bookings, but only one booking can be made for a table at a specific date and time.

Constraints and Indexes

Booking Model Constraints:

Unique Constraint (unique_together): Ensures that a table cannot be booked for the same time and date more than once. This prevents double bookings of a table.

Validation:

Ensures the number of guests does not exceed the table's capacity.

Ensures the booking time is between 09:00 and 22:00.

Ensures the booking time is not in the past.

Table Model:

Primary Key: The number field is unique and serves as the primary identifier for each table.

Relationships Summary

One-to-Many Relationship:

User to Booking: A user can make multiple bookings (one user, many bookings).

Table to Booking: A table can have multiple bookings, but only one booking can exist for the same table at a specific time and date (one table, many bookings).

Unique Booking per Table per Time:

The combination of table, booking_date, and booking_time is enforced to be unique in the Booking model, ensuring no double-booking for the same table at the same time.

## Testing

### Validators

- HTML validator: [link to HTML validator](https://validator.w3.org/)
![HTML validator image](./static/images/Htmlcheckscreenshot.png)

- CSS validator: [link to CSS validator](https://jigsaw.w3.org/css-validator/)
![CSS validator image](./static/images/csscheckscreenshot.png)
- Python validator: [link to Python validator](https://pep8ci.herokuapp.com/)

- Accessibility: [link to Accessibility tester](https://wave.webaim.org/)
![Accessibility tester image](./static/images/accesibilitycheckscreenshot.png)

### Browser Testing

- To ensure cross-browser compatibility, I tested my website on multiple popular browsers including Google Chrome, Mozilla Firefox, Microsoft Edge, and Safari. I checked the layout, responsiveness, and key functionalities such as navigation, forms, and interactive elements across each browser.

### Responsiveness

- To make sure the website was fully responsive, I tested it on a variety of screen sizes, including desktops, tablets, and mobile devices. I used browser developer tools (like Chrome DevTools) to simulate different screen resolutions and orientations. Additionally, I viewed the site on physical devices when possible to confirm real-world performance and usability.

- Phone : ![phone screenshot](./static/images/screenshotphone.png)

- Tablet : ![tablet screenshot](./static/images/tabletscreenshot.png)

- Desktop : ![desktop screenshot](./static/images/desktopscreenshot.png)

### Manual testing

![manual testing](./static/images/manualtestingscreenshot.png)

## Features 
 
 - Homepage: The homepage has an excellent layout, offering smooth navigation and a clear, engaging presentation.
 - log in / sign up  form: The login and sign-up forms are seamlessly integrated, providing a smooth and user-friendly experience.
 - Menu: The menu with food and drinks is well-organized, offering a visually appealing and easy-to-navigate selection.
 - My bookings: The bookings page is efficiently designed, offering a seamless and user-friendly experience for looking at reservations.
 - Book table page: The "Book Table" page is intuitively designed, making the reservation process quick and effortless.
 - Edit booking: The "Edit Booking" page is user-friendly, allowing easy and efficient updates to existing reservations.

 ### Heroku Deployment
* Log into [Heroku](https://www.heroku.com/) account or create an account.
* Click the "New" button at the top right corner and select "Create New App".
* Enter a unique application name
* Select your region
* Click "Create App"

#### Deploy

1. Make sure DEBUG = False in the settings.py
2. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
3. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
4. Click 'Open App' to view the deployed live site.

# Live Website
[link](https://taste-paradise-e2f6c6cf02fa.herokuapp.com/)

### Acknowledgments

* I would like to thank my mentor for support and feedback throughout this project, Mitko Bachvarov.
* I would also like to extend my appreciation to the Slack community for their continuous engagement and willingness to share knowledge. The collaborative environment provided a platform for learning, troubleshooting, and gaining inspiration from fellow developers.