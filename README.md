# 🦃 Thanksgiving Recipe Generator

A beautiful FastAPI application that generates personalized Thanksgiving recipes based on your dietary preferences using GPT-4.

## ✨ Features

- **Beautiful UI**: Modern, responsive design with gradient backgrounds and smooth animations
- **Dietary Options**: Support for Vegetarian, Vegan, and Traditional (no restrictions) diets
- **GPT-4 Integration**: Uses OpenAI's GPT-4 to generate personalized recipes
- **Secure**: API keys are only used for the session and not stored
- **Print Friendly**: Easy to print your generated recipes

## 🚀 Quick Start

### Prerequisites

- Python 3.13
- OpenAI API key

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <your-repo-url>
   cd thanksgiving-recipe1
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

4. **Open your browser** and go to:
   ```
   http://localhost:8000
   ```

## 🎯 How to Use

1. **Enter your OpenAI API key** in the form
2. **Select your dietary preference**:
   - 🥬 **Vegetarian**: No meat, but includes dairy and eggs
   - 🌱 **Vegan**: No animal products at all
   - 🍗 **No Restrictions**: Traditional Thanksgiving with all foods
3. **Click "Generate My Thanksgiving Recipe"**
4. **Get your personalized recipe** with ingredients and cooking instructions!

## 🛠️ Technical Details

### Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **Jinja2**: Template engine for HTML rendering
- **OpenAI**: Official OpenAI Python client (v1.51.0)
- **Bootstrap 5**: For responsive UI components
- **Font Awesome**: For beautiful icons

### Project Structure

```
thanksgiving-recipe1/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
│   ├── index.html       # Main form page
│   ├── recipe.html      # Recipe display page
│   └── error.html       # Error handling page
├── static/              # Static files (CSS, JS, images)
└── README.md           # This file
```

### API Endpoints

- `GET /`: Main form page
- `POST /generate-recipe`: Generate recipe based on dietary preferences

## 🔧 Configuration

The application uses the following environment variables (optional):
- No environment variables required - API key is entered through the UI

## 🎨 UI Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Gradient Backgrounds**: Beautiful purple gradient background
- **Interactive Elements**: Hover effects and smooth transitions
- **Form Validation**: Client-side validation for better UX
- **Error Handling**: User-friendly error messages
- **Print Support**: Easy recipe printing

## 🚨 Security Notes

- API keys are only used for the current session
- No data is stored on the server
- All communication with OpenAI is done securely

## 🐛 Troubleshooting

### Common Issues

1. **"Invalid API Key" Error**:
   - Verify your OpenAI API key is correct
   - Ensure you have sufficient credits in your OpenAI account

2. **"Connection Error"**:
   - Check your internet connection
   - Verify OpenAI services are available

3. **"Rate Limit Exceeded"**:
   - Wait a few minutes before trying again
   - Consider upgrading your OpenAI plan

### Getting Help

If you encounter issues:
1. Check the error message in the UI
2. Verify your OpenAI API key and account status
3. Ensure all dependencies are installed correctly

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Happy Thanksgiving! 🦃🍽️**
