# 🏠 Orphanage Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/AdityaKumar00007/Orphanage-Management-System.svg)](https://github.com/AdityaKumar00007/Orphanage-Management-System/stargazers)

A comprehensive **Django-based web application** designed to streamline orphanage operations, including child care management, adoption processes, and donation tracking. This system provides an intuitive interface for administrators to manage daily operations efficiently while ensuring the welfare of children in care.

## 🌟 Features

### 👶 Child Management
- **Child Registration**: Complete profiles with personal information, admission dates, and guardian contacts
- **Adoption Tracking**: Monitor adoption status and availability
- **Age & Gender Filtering**: Easy categorization and search functionality
- **Care History**: Track important dates and milestones

### 🤝 Adoption System
- **Adoption Portal**: Browse available children for adoption
- **Secure Authentication**: Login required for adoption processes
- **Real-time Status Updates**: Automatic status changes upon adoption
- **Adoption Confirmation**: Streamlined adoption workflow

### 💝 Donation Management
- **Multiple Donation Types**: Support for money, clothes, toys, school supplies, food, and blankets
- **Donor Information**: Complete donor profiles with contact details
- **Donation Tracking**: Timestamp and categorize all donations
- **Success Notifications**: Confirmation system for successful donations

### 🔐 User Authentication
- **Secure Login/Signup**: User registration and authentication system
- **Access Control**: Protected routes for sensitive operations
- **Session Management**: Secure user sessions

### 📊 Administrative Features
- **Dashboard Overview**: Quick insights into system status
- **Data Management**: Easy CRUD operations for all entities
- **Reports Generation**: Track donations and adoptions over time

## 🛠️ Technology Stack

- **Backend**: Django 4.x (Python Web Framework)
- **Database**: SQLite (Development) / PostgreSQL (Production Ready)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design
- **Authentication**: Django's built-in authentication system
- **Deployment**: Ready for cloud deployment (Heroku, AWS, etc.)

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AdityaKumar00007/Orphanage-Management-System.git
cd Orphanage-Management-System
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
pip install pillow  # For image handling
```

### 4. Database Setup
```bash
cd orphanage_management
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access the application.

## 📱 Usage Guide

### For Administrators:
1. **Access Admin Panel**: `/admin/` (requires superuser account)
2. **Manage Children**: Add, edit, or view child profiles
3. **Monitor Donations**: Track all incoming donations
4. **Oversee Adoptions**: Manage adoption processes

### For Public Users:
1. **Browse Children**: View available children for adoption
2. **Make Donations**: Contribute money or items
3. **Adoption Requests**: Submit adoption applications (requires login)

## 🗄️ Database Models

### Child Model
- Name, Age, Gender
- Date of Birth & Admission
- Guardian Contact Information
- Adoption Status

### Donation Model
- Donor Information
- Donation Type & Amount
- Timestamp & Contact Details

## 🎨 User Interface

The application features a clean, responsive design optimized for:
- **Desktop Browsers**: Full functionality with optimal layout
- **Tablet Devices**: Responsive design adapts to medium screens
- **Mobile Phones**: Mobile-friendly interface for on-the-go access

## 🔧 Configuration

### Settings Configuration
Edit `orphanage_management/settings.py` for:
- Database configuration
- Static files setup
- Security settings
- Email configuration (for notifications)

### Environment Variables
For production deployment, configure:
```bash
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

## 🤝 Contributing

We welcome contributions to improve the Orphanage Management System! Here's how you can help:

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Write clear commit messages
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors & Acknowledgments

- **Aditya Kumar** - *Initial Development* - [@AdityaKumar00007](https://github.com/AdityaKumar00007)

### Special Thanks
- Django Community for the excellent framework
- Contributors who help improve this project
- Orphanages and NGOs for inspiration and feedback

## 📞 Support & Contact

If you have any questions, suggestions, or need help with the system:

- **GitHub Issues**: [Create an Issue](https://github.com/AdityaKumar00007/Orphanage-Management-System/issues)
- **Email**: Contact through GitHub profile
- **Documentation**: Check the Wiki section for detailed guides

## 🔄 Changelog

### Version 1.0.0 (Current)
- Initial release with core functionality
- Child management system
- Donation tracking
- Basic adoption workflow
- User authentication
- Responsive UI design

## 🚀 Future Enhancements

- [ ] Email notification system
- [ ] Advanced reporting and analytics
- [ ] Document management for legal papers
- [ ] Multi-language support
- [ ] Mobile application
- [ ] Payment gateway integration
- [ ] Automated backup system
- [ ] Role-based access control

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ for orphanages and child welfare organizations worldwide.

</div>
