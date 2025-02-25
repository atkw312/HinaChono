Write-Output "🔄 Installing dependencies..."

if (-Not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Output "⚠️ Node.js is not installed. Please install it from https://nodejs.org/"
    exit
}

if (-Not (Get-Command serve -ErrorAction SilentlyContinue)) {
    Write-Output "📦 Installing 'serve' for frontend..."
    npm install -g serve
}

Write-Output "🐍 Installing Python dependencies..."
cd backend
pip install -r requirements.txt

Write-Output "✅ Setup complete! Run './start.ps1' or './start.sh' to start the service."