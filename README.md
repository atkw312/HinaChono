# FastAPI Stable Diffusion Service

This project provides a FastAPI backend for generating images using the Stable Diffusion pipeline from `diffusers`, along with a simple HTML/CSS/JS frontend.

## Installation

### Backend
1. Clone the repository:
   ```sh
   git clone https://github.com/atkw312/HinaChono.git
   cd HinaChono

   cd backend
   pip install -r requirements.txt
   python -m uvicorn api:app --reload
   
   cd ../frontend
   npm install -g serve
   serve -s . -l 5500
