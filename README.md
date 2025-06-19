#  Fitness Class Booking System

A timezone-aware Django-based web application that allows clients to book Yoga, Zumba, and HIIT classes. Admins can manage slots, and users receive confirmation emails on successful bookings.

---

##  Features

- View available classes (Yoga, Zumba, HIIT)
- Timezone support (IST to client timezone)
- Admin dashboard for slot creation and vacancy management
- Color-coded slot availability (✅ Available / ❌ Full)
- One-click client booking with confirmation email
- User authentication (register, login, logout)

---

##  Tech Stack

- Python 3.x
- Django 4.x
- SQLite (default) or PostgreSQL
- Bootstrap 5
- Mailtrap (for email confirmation)
- Timezone-aware scheduling (using `pytz`)

---

## 📮 Sample API Requests (via cURL)

### 🔹 Get All Available Classes

```bash
curl http://127.0.0.1:8000/api/classes/



##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sahalcheruth/Fitness_Club
cd fitness_studio


