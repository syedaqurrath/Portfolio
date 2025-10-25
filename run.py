#!/usr/bin/env python3
"""
Portfolio Application Startup Script
Run this script to start the portfolio application
"""

import os
import sys
from app import app

if __name__ == '__main__':
    # Set default environment if not set
    if not os.environ.get('FLASK_ENV'):
        os.environ['FLASK_ENV'] = 'development'
    
    print("Starting Portfolio Application...")
    print("Open your browser and go to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=app.config.get('DEBUG', True)
        )
    except KeyboardInterrupt:
        print("\nServer stopped. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)
