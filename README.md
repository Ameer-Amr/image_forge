# ImageForge

A Django web application for batch downloading images from URLs and packaging them into a convenient ZIP file.

## Features

- **Batch Image Download**: Submit multiple image URLs (comma-separated) and download them all at once
- **Concurrent Processing**: Uses ThreadPoolExecutor for efficient parallel downloading
- **ZIP Packaging**: Automatically packages all images into a single ZIP file
- **Simple Interface**: Clean, minimal web interface for easy URL submission
- **Error Handling**: Gracefully handles failed downloads without interrupting the process

## Requirements

- Python 3.8+
- Django 5.2.7
- See `requirements.txt` for full dependencies

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd image_forge
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

## Usage

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:8000/core/process/`

3. **Download images**
   - Enter comma-separated image URLs in the text area
   - Click the "Download" button
   - Your browser will download a ZIP file containing all successfully fetched images

### Example URLs Format
```
https://example.com/image1.jpg, https://example.com/image2.png, https://example.com/image3.jpg
```

## Project Structure

```
image_forge/
├── core/                   # Main application
│   ├── views.py           # Image processing logic
│   ├── urls.py            # App URL routing
│   └── ...
├── image_forge/           # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── ...
├── templates/             # HTML templates
│   └── index.html         # Main interface
├── staticfiles/           # Collected static files
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Configuration

- **Database**: SQLite (default) - configured in `image_forge/settings.py`
- **Allowed Hosts**: localhost, 127.0.0.1, testserver
- **Max Workers**: Up to 10 concurrent downloads (configurable in `core/views.py`)
- **Download Timeout**: 10 seconds per image


### Creating a Superuser (for admin access)
```bash
python manage.py createsuperuser
```

### Admin Interface
Access the Django admin at: `http://127.0.0.1:8000/admin/`


## How It Works

1. User submits comma-separated image URLs via the web form
2. Backend receives URLs and validates the request
3. ThreadPoolExecutor fetches images concurrently (up to 10 at a time)
4. Each downloaded image is given a unique UUID filename
5. All images are packaged into a ZIP file in memory
6. ZIP file is returned as an HTTP response for download


## License

This project is available for personal and educational use.

