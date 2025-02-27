# FastAPI Stable Diffusion Service

This project provides a FastAPI backend for generating images using the Stable Diffusion pipeline from `diffusers`, along with a simple HTML/CSS/JS frontend.

## Introduction

This is a Hina Chono an AI chatbot that interacts with users and generates images using Stable Diffusion models. The project consists of a FastAPI backend and a Node.js-based frontend server, allowing users to chat and receive AI-generated anime-style images locally.

### Minimum System Requirements
This project is supported on Windows PCs with <b>NVIDIA GPUs only</b>.
Since Stable Diffusion XL (SDXL) models require significant computing power, ensure your system meets these minimum requirements.

<table>
   <tbody>
      <tr>
			<td>Component</td>
         <td>Specification</td>
		</tr>
      <tr>
			<td>OS</td>
         <td>Windows 10/11 (64-bit)</td>
		</tr>
      <tr>
			<td>GPU</td>
         <td>NVIDIA RTX 3060 (12GB VRAM)</td>
		</tr>
      <tr>
			<td>VRAM</td>
         <td>8GB minimum (12GB+ recommended)</td>
		</tr>
   </tbody>
</table>

### Models Used

<table>
	<tbody>
		<tr>
			<td>Model Name</td>
         <td>User</td>
         <td>Model Type</td>
			<td>CivitAI Link</td>
		</tr>
		<tr>
			<td>WAI-NSFW-illustrious-SDXL</td>
			<td>[WAI0731](https://civitai.com/user/WAI0731)</td>
         <td>SDXL Model</td>
         <td>[Link](https://civitai.com/models/827184/wai-nsfw-illustrious-sdxl?modelVersionId=1183765)</td>
		</tr>
      		<tr>
			<td>Chono Hina | Blue Box | アオのハコ</td>
			<td>[duongve13112002](https://civitai.com/user/duongve13112002)</td>
         <td>LORA</td>
         <td>[Link](https://civitai.com/models/975032/chono-hina-or-blue-box-or)</td>
		</tr>
      <tr>
			<td>EasyNegative</td>
			<td>[rqdwdw](https://civitai.com/user/rqdwdw)</td>
         <td>Embedding</td>
         <td>[Link](https://civitai.com/models/7808/easynegative?modelVersionId=9208)</td>
		</tr>
	</tbody>
</table>

## Installation

### Download Models
Since the model files are too large for GitHub, you need to download them manually.

1. **Download the models from Google Drive:**  
   [Google Drive Link](https://drive.google.com/drive/folders/17FU6A4sHU6uFlaOU6X1hiZMSibybHChi?usp=sharing)

Be sure to name the folder 'models' after downloading from Google Drive.

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
