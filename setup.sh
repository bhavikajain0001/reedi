mkdir -p ~/.streamlit
echo "[theme]
primaryColor = '#162c47'
backgroundColor = '#00a79e'
secondaryBackgroundColor = '#162c47'
textColor = '#ffffff'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
