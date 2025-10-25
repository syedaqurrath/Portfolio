# Syeda Qurrath UI Ain - Portfolio Website

A modern, responsive portfolio website built with Flask, showcasing professional skills, projects, and experience.

## 🚀 Features

- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern UI/UX**: Clean, professional design with smooth animations
- **Interactive Elements**: Dynamic project showcase and contact form
- **SEO Optimized**: Meta tags and structured content
- **Fast Loading**: Optimized assets and efficient code
- **Contact Form**: Functional contact form with email integration
- **Project Showcase**: Detailed project information with technology tags
- **Skills Display**: Organized skill categories with visual badges
- **Experience Timeline**: Professional experience and education history

## 📁 Project Structure

```
portfolio/
├── app.py                 # Main Flask application
├── portfolio_data.json    # Portfolio data (personal info, projects, etc.)
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Custom CSS styles
│   ├── js/
│   │   └── script.js     # JavaScript functionality
│   ├── images/           # Image assets
│   └── assets/           # Additional assets
└── templates/            # HTML templates
    ├── base.html         # Base template
    ├── index.html        # Home page
    ├── about.html        # About page
    ├── projects.html     # Projects page
    └── contact.html      # Contact page
```

## 🛠️ Technologies Used

### Backend

- **Flask**: Python web framework
- **Jinja2**: Template engine
- **JSON**: Data storage

### Frontend

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS Grid and Flexbox
- **JavaScript**: Interactive functionality
- **Bootstrap 5**: Responsive framework
- **Font Awesome**: Icons

### Features

- **Responsive Design**: Mobile-first approach
- **Smooth Animations**: CSS transitions and JavaScript effects
- **Form Validation**: Client-side and server-side validation
- **Email Integration**: Contact form with SMTP support

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📝 Configuration

### Email Settings

To enable email functionality, update the email configuration in `app.py`:

```python
def send_contact_email(name, email, message):
    # Configure your SMTP settings
    msg = MimeText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    msg['Subject'] = f"Portfolio Contact - {name}"
    msg['From'] = 'your-email@gmail.com'
    msg['To'] = 'qurrath2809@gmail.com'

    # Uncomment and configure SMTP
    # with smtplib.SMTP('smtp.gmail.com', 587) as server:
    #     server.starttls()
    #     server.login('your-email@gmail.com', 'your-app-password')
    #     server.send_message(msg)
```

### Portfolio Data

Update `portfolio_data.json` with your personal information:

```json
{
  "personal_info": {
    "name": "Your Name",
    "title": "Your Title",
    "email": "your-email@example.com",
    "phone": "+1234567890",
    "location": "Your Location",
    "linkedin": "your-linkedin-url",
    "github": "your-github-url",
    "summary": "Your professional summary"
  }
}
```

## 🎨 Customization

### Colors

Update CSS variables in `static/css/style.css`:

```css
:root {
  --primary-color: #2c3e50;
  --secondary-color: #3498db;
  --accent-color: #e74c3c;
  --text-color: #2c3e50;
  --bg-light: #ecf0f1;
}
```

### Styling

- **Typography**: Update font families in the CSS
- **Layout**: Modify grid systems and spacing
- **Animations**: Customize transition effects
- **Components**: Style individual elements

### Content

- **Projects**: Add/remove projects in `portfolio_data.json`
- **Skills**: Update skill categories and technologies
- **Experience**: Modify professional experience
- **Education**: Update academic background

## 📱 Responsive Design

The website is fully responsive with breakpoints:

- **Mobile**: < 576px
- **Tablet**: 576px - 768px
- **Desktop**: > 768px

## 🚀 Deployment

### Heroku

1. Create a `Procfile`:

   ```
   web: python app.py
   ```

2. Deploy to Heroku:
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

### Vercel

1. Install Vercel CLI:

   ```bash
   npm i -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

### Netlify

1. Build command: `python app.py`
2. Publish directory: `./`

## 🔧 Development

### Adding New Pages

1. Create route in `app.py`:

   ```python
   @app.route('/new-page')
   def new_page():
       return render_template('new-page.html', data=portfolio_data)
   ```

2. Create template in `templates/new-page.html`:
   ```html
   {% extends "base.html" %} {% block content %}
   <!-- Page content -->
   {% endblock %}
   ```

### Adding New Features

1. **Database Integration**: Replace JSON with SQLite/PostgreSQL
2. **Blog Section**: Add Flask-Admin for content management
3. **Dark Mode**: Implement theme switching
4. **Multi-language**: Add internationalization support
5. **PWA Features**: Add service worker for offline functionality

## 📊 Performance Optimization

- **Image Optimization**: Compress images and use WebP format
- **CSS/JS Minification**: Minify assets for production
- **Caching**: Implement browser caching
- **CDN**: Use Content Delivery Network for static assets

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**:

   ```bash
   # Change port in app.py
   app.run(debug=True, port=5001)
   ```

2. **Module not found**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Email not working**:
   - Check SMTP settings
   - Verify email credentials
   - Enable "Less secure app access" for Gmail

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Contact

**Syeda Qurrath UI Ain**

- Email: qurrath2809@gmail.com
- Phone: +91 9741940080
- Location: Bangalore, India

## 🙏 Acknowledgments

- Bootstrap for the responsive framework
- Font Awesome for the icons
- Flask community for the excellent documentation
- All contributors and supporters

---

**Built with ❤️ by Syeda Qurrath UI Ain**
