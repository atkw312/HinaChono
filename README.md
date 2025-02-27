# FastAPI Stable Diffusion Service

This project provides a FastAPI backend for generating images using the Stable Diffusion pipeline from `diffusers`, along with a simple HTML/CSS/JS frontend.

## Installation

### Download Models
Since the model files are too large for GitHub, you need to download them manually.

1. **Download the models from Google Drive:**  
   [Google Drive Link](https://drive.google.com/drive/folders/17FU6A4sHU6uFlaOU6X1hiZMSibybHChi?usp=sharing)
   

### Backend
1. Clone the repository:
   ```sh
   git clone https://github.com/atkw312/HinaChono.git
   cd HinaChono

2. Extract and place the downloaded models in the `models/` folder inside `backend/`     
   ```sh
   cd backend
   mkdir -p models
   mv ~/Downloads/models/* models/

3. Start backend server:
   ```sh
   pip install -r requirements.txt
   python -m uvicorn api:app --reload
   
### Frontend
1. Start frontend server in another Terminal tab:
   ```sh
   cd HinaChono
   cd frontend

   npm install -g serve
   serve -s . -l 5500
